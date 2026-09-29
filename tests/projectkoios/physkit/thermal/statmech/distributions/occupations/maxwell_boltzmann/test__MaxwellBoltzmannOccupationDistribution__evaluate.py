"""Evaluation tests for ``MaxwellBoltzmannOccupationDistribution``."""

import numpy as np

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.distributions.occupations.maxwell_boltzmann.distribution import (  # noqa: E501
    MaxwellBoltzmannOccupationDistribution,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestMaxwellBoltzmannOccupationDistributionEvaluate:
    """Verify the unit-aware classical ideal occupation factor."""

    def test__evaluate_matches_maxwell_boltzmann_formula(self) -> None:
        energies = VectorQuantity(
            magnitude=np.array([-0.5, 1.0, 3.0], dtype=np.float64),
            unit=PhysicalUnit(expression="electron_volt"),
        )

        evaluation = MaxwellBoltzmannOccupationDistribution().evaluate(
            energies=energies,
            chemical_potential=ScalarQuantity(
                magnitude=0.0,
                unit=PhysicalUnit(expression="electron_volt"),
            ),
            temperature=ScalarQuantity(
                magnitude=float(SI.q / SI.k_B),
                unit=PhysicalUnit(expression="kelvin"),
            ),
        )

        expected = np.exp(-energies.magnitude)
        np.testing.assert_allclose(
            evaluation.occupation_factors.magnitude,
            expected,
            rtol=6.0e-16,
            atol=0.0,
        )
        assert isinstance(evaluation.occupation_factors.unit, Unitless)
