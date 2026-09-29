"""Speed-distribution evaluation tests for ``MaxwellBoltzmannGasState``."""

import math

import numpy as np
import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.kinetic_theory import (
    MaxwellBoltzmannGasState,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestMaxwellBoltzmannGasStateEvaluateSpeedDistribution:
    """Verify unit-aware Maxwell--Boltzmann speed probability density."""

    TEMPERATURE_KELVIN = 300.0
    MOLAR_MASS_KG_PER_MOL = 0.0280134

    @classmethod
    def _state(cls) -> MaxwellBoltzmannGasState:
        """Return the nitrogen-at-300-K synthetic test configuration."""
        return MaxwellBoltzmannGasState(
            temperature=ScalarQuantity(
                magnitude=cls.TEMPERATURE_KELVIN,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            molar_mass=ScalarQuantity(
                magnitude=cls.MOLAR_MASS_KG_PER_MOL,
                unit=PhysicalUnit(expression="kilogram / mole"),
            ),
        )

    @staticmethod
    def _speeds(*, magnitudes: np.ndarray, unit: str) -> VectorQuantity:
        return VectorQuantity(
            magnitude=magnitudes,
            unit=PhysicalUnit(expression=unit),
        )

    def test__evaluate_speed_distribution_matches_selected_formula_values(
        self,
    ) -> None:
        speed_values = np.array([0.0, 250.0, 500.0, 1000.0], dtype=np.float64)
        speeds = self._speeds(magnitudes=speed_values, unit="meter / second")
        state = self._state()

        evaluation = state.evaluate_speed_distribution(speeds=speeds)

        factor = self.MOLAR_MASS_KG_PER_MOL / (2.0 * SI.R_g * self.TEMPERATURE_KELVIN)
        expected = np.array(
            [
                (4.0 / math.sqrt(math.pi))
                * factor**1.5
                * speed**2
                * math.exp(-factor * speed**2)
                for speed in speed_values
            ],
            dtype=np.float64,
        )
        assert evaluation.request.state is state
        assert evaluation.request.speeds is speeds
        np.testing.assert_allclose(
            evaluation.probability_density.magnitude,
            expected,
            rtol=5e-15,
            atol=0.0,
        )
        assert evaluation.probability_density.unit == PhysicalUnit(
            expression="(meter / second) ** -1"
        )

    def test__evaluate_speed_distribution_converts_compatible_speed_units(
        self,
    ) -> None:
        speed_values_km_per_hour = np.array([0.0, 900.0, 1800.0], dtype=np.float64)
        speeds = self._speeds(
            magnitudes=speed_values_km_per_hour,
            unit="kilometer / hour",
        )

        evaluation = self._state().evaluate_speed_distribution(speeds=speeds)

        assert evaluation.probability_density.unit == PhysicalUnit(
            expression="(kilometer / hour) ** -1"
        )
        represented_probability = np.trapezoid(
            evaluation.probability_density.magnitude,
            x=speed_values_km_per_hour,
        )
        assert 0.0 < represented_probability < 1.0

    def test__evaluate_speed_distribution_density_integrates_to_one(self) -> None:
        speed_values = np.linspace(0.0, 5000.0, 50001, dtype=np.float64)
        speeds = self._speeds(
            magnitudes=speed_values,
            unit="meter / second",
        )

        density = (
            self._state().evaluate_speed_distribution(speeds=speeds).probability_density
        )
        represented_probability = np.trapezoid(density.magnitude, x=speed_values)

        assert represented_probability == pytest.approx(1.0, rel=0.0, abs=2e-14)

    def test__evaluate_speed_distribution_peaks_at_most_probable_speed(self) -> None:
        state = self._state()
        most_probable_speed = state.most_probable_speed.magnitude
        speeds = self._speeds(
            magnitudes=np.array(
                [
                    most_probable_speed - 1.0,
                    most_probable_speed,
                    most_probable_speed + 1.0,
                ],
                dtype=np.float64,
            ),
            unit="meter / second",
        )

        density = state.evaluate_speed_distribution(speeds=speeds).probability_density

        assert density.magnitude[1] > density.magnitude[0]
        assert density.magnitude[1] > density.magnitude[2]

    def test__evaluate_speed_distribution_rejects_negative_speed(self) -> None:
        speeds = self._speeds(
            magnitudes=np.array([-1.0], dtype=np.float64),
            unit="meter / second",
        )

        with pytest.raises(ValueError, match="speeds must be nonnegative"):
            self._state().evaluate_speed_distribution(speeds=speeds)

    def test__evaluate_speed_distribution_rejects_incompatible_unit(self) -> None:
        with pytest.raises(ValueError, match="compatible with speed"):
            self._state().evaluate_speed_distribution(
                speeds=VectorQuantity(
                    magnitude=np.array([1.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="joule"),
                )
            )

    def test__evaluate_speed_distribution_rejects_unitless_speeds(self) -> None:
        with pytest.raises(TypeError, match="physical speed unit"):
            self._state().evaluate_speed_distribution(
                speeds=VectorQuantity(
                    magnitude=np.array([1.0], dtype=np.float64),
                    unit=Unitless(),
                )
            )
