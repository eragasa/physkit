"""Construction tests for ``AntoineVaporPressureModel``."""

import pytest

from projectkoios.physkit.thermal.thermo.vaporpressure.antoine import (
    AntoineTemperatureRange,
    AntoineVaporPressureModel,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, Unitless


class TestAntoineVaporPressureModelInit:
    """Verify explicit coefficient, unit, range, and provenance contracts."""

    @staticmethod
    def _model() -> AntoineVaporPressureModel:
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

    def test__init_retains_unit_aware_coefficients_and_provenance(self) -> None:
        model = self._model()

        assert isinstance(model.A.unit, Unitless)
        assert model.B.unit == model.coefficient_temperature_unit
        assert model.C.unit == model.coefficient_temperature_unit
        assert model.coefficient_pressure_unit == PhysicalUnit(expression="bar")
        assert model.valid_temperature_range is not None
        assert model.source == "synthetic instructional coefficients"

    def test__init_rejects_physical_A_units(self) -> None:
        model = self._model()

        with pytest.raises(ValueError, match="A must be unitless"):
            AntoineVaporPressureModel(
                A=ScalarQuantity(
                    magnitude=model.A.magnitude,
                    unit=PhysicalUnit(expression="kelvin"),
                ),
                B=model.B,
                C=model.C,
                coefficient_temperature_unit=model.coefficient_temperature_unit,
                coefficient_pressure_unit=model.coefficient_pressure_unit,
                valid_temperature_range=model.valid_temperature_range,
                source=model.source,
            )

    def test__init_rejects_B_in_a_different_temperature_unit(self) -> None:
        model = self._model()

        with pytest.raises(ValueError, match="B must use"):
            AntoineVaporPressureModel(
                A=model.A,
                B=ScalarQuantity(
                    magnitude=model.B.magnitude,
                    unit=PhysicalUnit(expression="degree_Celsius"),
                ),
                C=model.C,
                coefficient_temperature_unit=model.coefficient_temperature_unit,
                coefficient_pressure_unit=model.coefficient_pressure_unit,
                valid_temperature_range=model.valid_temperature_range,
                source=model.source,
            )

    def test__init_rejects_nonpressure_coefficient_output_unit(self) -> None:
        model = self._model()

        with pytest.raises(ValueError, match="compatible with pressure"):
            AntoineVaporPressureModel(
                A=model.A,
                B=model.B,
                C=model.C,
                coefficient_temperature_unit=model.coefficient_temperature_unit,
                coefficient_pressure_unit=PhysicalUnit(expression="meter"),
                valid_temperature_range=model.valid_temperature_range,
                source=model.source,
            )

    def test__init_rejects_empty_source(self) -> None:
        model = self._model()

        with pytest.raises(ValueError, match="source must be nonempty"):
            AntoineVaporPressureModel(
                A=model.A,
                B=model.B,
                C=model.C,
                coefficient_temperature_unit=model.coefficient_temperature_unit,
                coefficient_pressure_unit=model.coefficient_pressure_unit,
                valid_temperature_range=model.valid_temperature_range,
                source="",
            )
