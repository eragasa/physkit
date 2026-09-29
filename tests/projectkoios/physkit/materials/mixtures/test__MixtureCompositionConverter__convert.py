"""Software verification for molar and mass composition conversion."""

import numpy as np

from projectkoios.physkit.materials.mixtures.molar import (
    MassToMolarMixtureConversionRequest,
    MixtureCompositionConverter,
    MolarMixture,
    MolarToMassMixtureConversionRequest,
)
from projectkoios.physkit.units import PhysicalUnit, VectorQuantity


class TestMixtureCompositionConverter:
    """Verify bidirectional finite-mixture conversion."""

    def test_conversion_round_trip_preserves_amounts_and_mean_molar_mass(
        self,
    ) -> None:
        """Explicit target units survive molar-to-mass-to-molar conversion."""
        source = MolarMixture(
            species=("Al", "Cu"),
            mole_amounts=VectorQuantity(
                magnitude=np.asarray([1.0, 3.0], dtype=np.float64),
                unit=PhysicalUnit(expression="mole"),
            ),
            molar_masses=VectorQuantity(
                magnitude=np.asarray([26.9815385, 63.546], dtype=np.float64),
                unit=PhysicalUnit(expression="gram / mole"),
            ),
        )
        converter = MixtureCompositionConverter()

        mass_result = converter.convert_to_mass(
            request=MolarToMassMixtureConversionRequest(
                mixture=source,
                target_mass_unit=PhysicalUnit(expression="gram"),
            )
        )
        round_trip = converter.convert_to_molar(
            request=MassToMolarMixtureConversionRequest(
                mixture=mass_result.mixture,
                target_amount_unit=PhysicalUnit(expression="millimole"),
            )
        )

        assert np.allclose(
            mass_result.mixture.mass_amounts.magnitude,
            np.asarray([26.9815385, 190.638], dtype=np.float64),
            rtol=1.0e-14,
            atol=0.0,
        )
        assert np.allclose(
            round_trip.mixture.mole_amounts.magnitude,
            np.asarray([1000.0, 3000.0], dtype=np.float64),
            rtol=1.0e-14,
            atol=0.0,
        )
        assert np.isclose(
            mass_result.mixture.mean_molar_mass.magnitude,
            source.mean_molar_mass.magnitude,
            rtol=1.0e-14,
            atol=0.0,
        )
        assert round_trip.mixture.species == source.species
        assert mass_result.request.mixture is source
