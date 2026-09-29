"""Evaluation tests for ``AntoineVaporPressureModel``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.thermo.vaporpressure.antoine import (
    AntoineTemperatureRange,
    AntoineVaporPressureModel,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestAntoineVaporPressureModelEvaluate:
    """Verify formula, unit conversion, range, singularity, and overflow."""

    @staticmethod
    def _kelvin_bar_model() -> AntoineVaporPressureModel:
        temperature_unit = PhysicalUnit(expression="kelvin")
        return AntoineVaporPressureModel(
            A=ScalarQuantity(magnitude=5.0, unit=Unitless()),
            B=ScalarQuantity(magnitude=1200.0, unit=temperature_unit),
            C=ScalarQuantity(magnitude=-30.0, unit=temperature_unit),
            coefficient_temperature_unit=temperature_unit,
            coefficient_pressure_unit=PhysicalUnit(expression="bar"),
            valid_temperature_range=AntoineTemperatureRange(
                lower=ScalarQuantity(magnitude=400.0, unit=temperature_unit),
                upper=ScalarQuantity(magnitude=800.0, unit=temperature_unit),
            ),
            source="synthetic instructional coefficients",
        )

    @staticmethod
    def _temperatures(*, values: list[float], unit: str) -> VectorQuantity:
        return VectorQuantity(
            magnitude=np.array(values, dtype=np.float64),
            unit=PhysicalUnit(expression=unit),
        )

    def test__evaluate_computes_kelvin_bar_coefficients_in_requested_unit(
        self,
    ) -> None:
        model = self._kelvin_bar_model()
        temperatures = self._temperatures(
            values=[400.0, 500.0, 800.0],
            unit="kelvin",
        )
        expected_bar = 10.0 ** (
            model.A.magnitude
            - model.B.magnitude / (temperatures.magnitude + model.C.magnitude)
        )

        evaluation = model.evaluate(
            temperatures=temperatures,
            pressure_unit=PhysicalUnit(expression="kilopascal"),
        )

        assert evaluation.request.model is model
        assert evaluation.request.temperatures is temperatures
        np.testing.assert_allclose(
            evaluation.pressures.magnitude,
            expected_bar * 100.0,
            rtol=2.0e-15,
            atol=0.0,
        )
        assert evaluation.pressures.unit == PhysicalUnit(expression="kilopascal")

    def test__evaluate_converts_input_celsius_and_native_torr(self) -> None:
        coefficient_temperature_unit = PhysicalUnit(expression="degree_Celsius")
        model = AntoineVaporPressureModel(
            A=ScalarQuantity(magnitude=3.0, unit=Unitless()),
            B=ScalarQuantity(
                magnitude=100.0,
                unit=coefficient_temperature_unit,
            ),
            C=ScalarQuantity(
                magnitude=10.0,
                unit=coefficient_temperature_unit,
            ),
            coefficient_temperature_unit=coefficient_temperature_unit,
            coefficient_pressure_unit=PhysicalUnit(expression="torr"),
            valid_temperature_range=None,
            source="synthetic Celsius and Torr coefficients",
        )
        expected_pascal = 10.0 ** (3.0 - 100.0 / (26.85 + 10.0)) * 101_325.0 / 760.0

        evaluation = model.evaluate(
            temperatures=self._temperatures(
                values=[26.85],
                unit="degree_Celsius",
            ),
            pressure_unit=PhysicalUnit(expression="pascal"),
        )

        assert evaluation.pressures.magnitude[0] == pytest.approx(
            expected_pascal,
            rel=8.0e-15,
        )

    def test__evaluate_rejects_temperature_outside_validity_range(self) -> None:
        with pytest.raises(ValueError, match="outside the model validity range"):
            self._kelvin_bar_model().evaluate(
                temperatures=self._temperatures(
                    values=[399.0],
                    unit="kelvin",
                ),
                pressure_unit=PhysicalUnit(expression="pascal"),
            )

    def test__evaluate_can_disable_validity_range_enforcement(self) -> None:
        evaluation = self._kelvin_bar_model().evaluate(
            temperatures=self._temperatures(values=[399.0], unit="kelvin"),
            pressure_unit=PhysicalUnit(expression="pascal"),
            enforce_valid_range=False,
        )

        assert evaluation.temperatures.magnitude[0] == 399.0

    def test__evaluate_rejects_antoine_singularity(self) -> None:
        model = self._kelvin_bar_model()
        singular_model = AntoineVaporPressureModel(
            A=model.A,
            B=model.B,
            C=ScalarQuantity(
                magnitude=-300.0,
                unit=model.coefficient_temperature_unit,
            ),
            coefficient_temperature_unit=model.coefficient_temperature_unit,
            coefficient_pressure_unit=model.coefficient_pressure_unit,
            valid_temperature_range=None,
            source="synthetic singularity case",
        )

        with pytest.raises(ValueError, match="denominator singularity"):
            singular_model.evaluate(
                temperatures=self._temperatures(values=[300.0], unit="kelvin"),
                pressure_unit=PhysicalUnit(expression="pascal"),
            )

    def test__evaluate_rejects_pressure_overflow(self) -> None:
        temperature_unit = PhysicalUnit(expression="kelvin")
        model = AntoineVaporPressureModel(
            A=ScalarQuantity(magnitude=400.0, unit=Unitless()),
            B=ScalarQuantity(magnitude=0.0, unit=temperature_unit),
            C=ScalarQuantity(magnitude=0.0, unit=temperature_unit),
            coefficient_temperature_unit=temperature_unit,
            coefficient_pressure_unit=PhysicalUnit(expression="pascal"),
            valid_temperature_range=None,
            source="synthetic overflow case",
        )

        with pytest.raises(ValueError, match="pressures must be finite"):
            model.evaluate(
                temperatures=self._temperatures(values=[300.0], unit="kelvin"),
                pressure_unit=PhysicalUnit(expression="pascal"),
            )
