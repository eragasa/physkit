"""Evaluation tests for ``FermiDiracOccupationDistribution``."""

import numpy as np

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.distributions.occupations.base import (
    IdealOccupationStatistic,
)
from projectkoios.physkit.thermal.statmech.distributions.occupations.fermi_dirac.distribution import (  # noqa: E501
    FermiDiracOccupationDistribution,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestFermiDiracOccupationDistributionEvaluate:
    """Verify unit-aware stable Fermi--Dirac occupation factors."""

    def test__evaluate_matches_fermi_dirac_formula(self) -> None:
        energies = VectorQuantity(
            magnitude=np.array([-2.0, 0.0, 2.0], dtype=np.float64),
            unit=PhysicalUnit(expression="electron_volt"),
        )
        chemical_potential = ScalarQuantity(
            magnitude=0.0,
            unit=PhysicalUnit(expression="electron_volt"),
        )
        temperature = ScalarQuantity(
            magnitude=float(SI.q / SI.k_B),
            unit=PhysicalUnit(expression="kelvin"),
        )

        evaluation = FermiDiracOccupationDistribution().evaluate(
            energies=energies,
            chemical_potential=chemical_potential,
            temperature=temperature,
        )

        expected = 1.0 / (np.exp(energies.magnitude) + 1.0)
        assert evaluation.request.statistic is IdealOccupationStatistic.FERMI_DIRAC
        assert evaluation.request.energies is energies
        assert evaluation.request.chemical_potential is chemical_potential
        assert evaluation.request.temperature is temperature
        np.testing.assert_allclose(
            evaluation.occupation_factors.magnitude,
            expected,
            rtol=5.0e-16,
            atol=0.0,
        )
        assert isinstance(evaluation.occupation_factors.unit, Unitless)
