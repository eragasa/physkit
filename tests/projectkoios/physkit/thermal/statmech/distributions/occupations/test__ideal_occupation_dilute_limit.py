"""Cross-statistic dilute-limit verification."""

import numpy as np
import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.distributions.occupations.bose_einstein.distribution import (  # noqa: E501
    BoseEinsteinOccupationDistribution,
)
from projectkoios.physkit.thermal.statmech.distributions.occupations.fermi_dirac.distribution import (  # noqa: E501
    FermiDiracOccupationDistribution,
)
from projectkoios.physkit.thermal.statmech.distributions.occupations.maxwell_boltzmann.distribution import (  # noqa: E501
    MaxwellBoltzmannOccupationDistribution,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestIdealOccupationDiluteLimit:
    """Verify quantum occupations approach the classical factor."""

    @pytest.mark.parametrize(
        "quantum_distribution",
        [FermiDiracOccupationDistribution(), BoseEinsteinOccupationDistribution()],
        ids=["fermi-dirac", "bose-einstein"],
    )
    def test__quantum_factor_converges_to_maxwell_boltzmann(
        self,
        quantum_distribution: (
            FermiDiracOccupationDistribution | BoseEinsteinOccupationDistribution
        ),
    ) -> None:
        energies = VectorQuantity(
            magnitude=np.array([8.0, 10.0, 12.0], dtype=np.float64),
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
        quantum = quantum_distribution.evaluate(
            energies=energies,
            chemical_potential=chemical_potential,
            temperature=temperature,
        )
        classical = MaxwellBoltzmannOccupationDistribution().evaluate(
            energies=energies,
            chemical_potential=chemical_potential,
            temperature=temperature,
        )

        np.testing.assert_allclose(
            quantum.occupation_factors.magnitude,
            classical.occupation_factors.magnitude,
            rtol=3.4e-4,
            atol=0.0,
        )
