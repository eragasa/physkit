"""Evaluation tests for ``BoltzmannExponentialEnergyDistribution``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.statmech.distributions.boltzmann_energy import (
    BoltzmannExponentialEnergyDistribution,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestBoltzmannExponentialEnergyDistributionEvaluate:
    """Verify normalized unit-aware exponential energy density."""

    def test__evaluate_matches_formula_and_reciprocal_energy_unit(self) -> None:
        thermal_energy_electron_volts = 0.05
        distribution = BoltzmannExponentialEnergyDistribution(
            thermal_energy=ScalarQuantity(
                magnitude=thermal_energy_electron_volts,
                unit=PhysicalUnit(expression="electron_volt"),
            )
        )
        energies = VectorQuantity(
            magnitude=np.array([0.0, 0.05, 0.1], dtype=np.float64),
            unit=PhysicalUnit(expression="electron_volt"),
        )

        evaluation = distribution.evaluate(energies=energies)

        expected = (
            np.exp(-energies.magnitude / thermal_energy_electron_volts)
            / thermal_energy_electron_volts
        )
        assert evaluation.request.distribution is distribution
        assert evaluation.request.energies is energies
        np.testing.assert_allclose(
            evaluation.probability_density.magnitude,
            expected,
            rtol=2.0e-16,
            atol=0.0,
        )
        assert evaluation.probability_density.unit == PhysicalUnit(
            expression="(electron_volt) ** -1"
        )

    def test__evaluate_converts_thermal_energy_to_requested_energy_unit(self) -> None:
        distribution = BoltzmannExponentialEnergyDistribution(
            thermal_energy=ScalarQuantity(
                magnitude=1.602176634e-20,
                unit=PhysicalUnit(expression="joule"),
            )
        )
        energies = VectorQuantity(
            magnitude=np.array([0.0, 0.1], dtype=np.float64),
            unit=PhysicalUnit(expression="electron_volt"),
        )

        evaluation = distribution.evaluate(energies=energies)

        expected_thermal_energy_electron_volts = 0.1
        expected = (
            np.exp(-energies.magnitude / expected_thermal_energy_electron_volts)
            / expected_thermal_energy_electron_volts
        )
        np.testing.assert_allclose(
            evaluation.probability_density.magnitude,
            expected,
            rtol=3.0e-16,
            atol=0.0,
        )

    def test__evaluate_rejects_negative_energy(self) -> None:
        distribution = BoltzmannExponentialEnergyDistribution(
            thermal_energy=ScalarQuantity(
                magnitude=0.05,
                unit=PhysicalUnit(expression="electron_volt"),
            )
        )

        with pytest.raises(ValueError, match="energies must be nonnegative"):
            distribution.evaluate(
                energies=VectorQuantity(
                    magnitude=np.array([-0.01], dtype=np.float64),
                    unit=PhysicalUnit(expression="electron_volt"),
                )
            )
