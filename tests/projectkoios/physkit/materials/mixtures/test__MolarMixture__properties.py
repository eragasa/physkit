"""Software verification for unit-aware molar-mixture properties."""

import numpy as np
import pytest

from projectkoios.physkit.materials.mixtures.molar import MolarMixture
from projectkoios.physkit.units import PhysicalUnit, VectorQuantity


class TestMolarMixture:
    """Verify intrinsic ordered molar-mixture behavior."""

    def test_properties_preserve_species_order_and_explicit_units(self) -> None:
        """Totals, fractions, and mean molar mass follow their definitions."""
        mixture = MolarMixture(
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

        assert mixture.species == ("Al", "Cu")
        assert mixture.total_mole_amount.magnitude == 4.0
        assert np.array_equal(
            mixture.mole_fractions.magnitude,
            np.asarray([0.25, 0.75], dtype=np.float64),
        )
        assert np.isclose(mixture.mean_molar_mass.magnitude, 54.404884625)
        assert mixture.mean_molar_mass.unit == PhysicalUnit(expression="gram / mole")

    def test_duplicate_species_are_rejected(self) -> None:
        """Species identity cannot be ambiguous within the ordered record."""
        with pytest.raises(ValueError, match="unique"):
            MolarMixture(
                species=("Al", "Al"),
                mole_amounts=VectorQuantity(
                    magnitude=np.asarray([1.0, 1.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="mole"),
                ),
                molar_masses=VectorQuantity(
                    magnitude=np.asarray([26.9815385, 26.9815385]),
                    unit=PhysicalUnit(expression="gram / mole"),
                ),
            )
