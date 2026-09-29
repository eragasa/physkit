"""Construction tests for ``AntoineVaporPressureEvaluation``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.thermo.vaporpressure.antoine import (
    AntoineVaporPressureEvaluation,
    AntoineVaporPressureEvaluationRequest,
    AntoineVaporPressureModel,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestAntoineVaporPressureEvaluationInit:
    """Verify request, pressure-unit, and vector-shape correlation."""

    @staticmethod
    def _request() -> AntoineVaporPressureEvaluationRequest:
        temperature_unit = PhysicalUnit(expression="kelvin")
        model = AntoineVaporPressureModel(
            A=ScalarQuantity(magnitude=5.0, unit=Unitless()),
            B=ScalarQuantity(magnitude=1200.0, unit=temperature_unit),
            C=ScalarQuantity(magnitude=-30.0, unit=temperature_unit),
            coefficient_temperature_unit=temperature_unit,
            coefficient_pressure_unit=PhysicalUnit(expression="bar"),
            valid_temperature_range=None,
            source="synthetic",
        )
        return AntoineVaporPressureEvaluationRequest(
            model=model,
            temperatures=VectorQuantity(
                magnitude=np.array([400.0, 500.0], dtype=np.float64),
                unit=temperature_unit,
            ),
            pressure_unit=PhysicalUnit(expression="pascal"),
            enforce_valid_range=True,
        )

    def test__init_retains_correlated_request_and_pressures(self) -> None:
        request = self._request()
        pressures = VectorQuantity(
            magnitude=np.array([1.0, 2.0], dtype=np.float64),
            unit=request.pressure_unit,
        )

        evaluation = AntoineVaporPressureEvaluation(
            request=request,
            pressures=pressures,
        )

        assert evaluation.request is request
        assert evaluation.pressures is pressures
        assert evaluation.temperatures is request.temperatures

    def test__init_rejects_pressure_shape_mismatch(self) -> None:
        request = self._request()

        with pytest.raises(ValueError, match="pressures must match temperatures"):
            AntoineVaporPressureEvaluation(
                request=request,
                pressures=VectorQuantity(
                    magnitude=np.array([1.0], dtype=np.float64),
                    unit=request.pressure_unit,
                ),
            )
