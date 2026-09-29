"""Software verification for multiplicity-weighted site fractions."""

import numpy as np

from projectkoios.physkit.materials.mixtures.sublattice import (
    SiteFractionMixture,
    SublatticeSiteFractions,
    SublatticeSpecification,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


class TestSiteFractionMixture:
    """Verify site access and overall-composition evaluation."""

    @staticmethod
    def _sublattice(
        *,
        name: str,
        species: tuple[str, ...],
        multiplicity: float,
        fractions: np.ndarray,
    ) -> SublatticeSiteFractions:
        """Construct one immutable sublattice record for this evidence owner."""
        return SublatticeSiteFractions(
            specification=SublatticeSpecification(
                name=name,
                species=species,
                multiplicity=ScalarQuantity(
                    magnitude=multiplicity,
                    unit=Unitless(),
                ),
            ),
            fractions=VectorQuantity(magnitude=fractions, unit=Unitless()),
        )

    def test_evaluate_overall_composition_uses_multiplicity_and_exclusions(
        self,
    ) -> None:
        """Vacancy exclusion is explicit and retained in the result request."""
        mixture = SiteFractionMixture(
            sublattices=(
                self._sublattice(
                    name="substitutional",
                    species=("A", "B"),
                    multiplicity=1.0,
                    fractions=np.asarray([0.75, 0.25], dtype=np.float64),
                ),
                self._sublattice(
                    name="interstitial",
                    species=("B", "Va"),
                    multiplicity=2.0,
                    fractions=np.asarray([0.25, 0.75], dtype=np.float64),
                ),
            )
        )

        result = mixture.evaluate_overall_composition(excluded_species=("Va",))

        assert result.included_species == ("A", "B")
        assert np.allclose(
            result.amounts_per_formula_unit.magnitude,
            np.asarray([0.75, 0.75], dtype=np.float64),
        )
        assert np.allclose(
            result.mole_fractions.magnitude,
            np.asarray([0.5, 0.5], dtype=np.float64),
        )
        assert result.request.excluded_species == ("Va",)
        assert (
            mixture.sublattice(name="interstitial")
            .fraction_for(species_name="Va")
            .magnitude
            == 0.75
        )
