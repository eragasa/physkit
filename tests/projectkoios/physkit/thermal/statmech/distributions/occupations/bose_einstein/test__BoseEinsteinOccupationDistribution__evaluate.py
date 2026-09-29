"""Evaluation tests for ``BoseEinsteinOccupationDistribution``."""

import numpy as np
import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.distributions.occupations.bose_einstein.distribution import (  # noqa: E501
    BoseEinsteinOccupationDistribution,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestBoseEinsteinOccupationDistributionEvaluate:
    """Verify unit-aware Bose--Einstein factors and their physical domain."""

    @staticmethod
    def _temperature() -> ScalarQuantity:
        return ScalarQuantity(
            magnitude=float(SI.q / SI.k_B),
            unit=PhysicalUnit(expression="kelvin"),
        )

    def test__evaluate_matches_bose_einstein_formula(self) -> None:
        energies = VectorQuantity(
            magnitude=np.array([0.5, 2.0, 5.0], dtype=np.float64),
            unit=PhysicalUnit(expression="electron_volt"),
        )

        evaluation = BoseEinsteinOccupationDistribution().evaluate(
            energies=energies,
            chemical_potential=ScalarQuantity(
                magnitude=0.0,
                unit=PhysicalUnit(expression="electron_volt"),
            ),
            temperature=self._temperature(),
        )

        expected = 1.0 / np.expm1(energies.magnitude)
        np.testing.assert_allclose(
            evaluation.occupation_factors.magnitude,
            expected,
            rtol=6.0e-16,
            atol=0.0,
        )
        assert isinstance(evaluation.occupation_factors.unit, Unitless)

    def test__evaluate_rejects_energy_not_above_chemical_potential(self) -> None:
        distribution = BoseEinsteinOccupationDistribution()

        with pytest.raises(ValueError, match="must exceed"):
            distribution.evaluate(
                energies=VectorQuantity(
                    magnitude=np.array([0.0, 1.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="electron_volt"),
                ),
                chemical_potential=ScalarQuantity(
                    magnitude=0.0,
                    unit=PhysicalUnit(expression="electron_volt"),
                ),
                temperature=self._temperature(),
            )
