"""Pressure-evaluation tests for ``IdealGasEquationOfState``."""

import numpy as np
import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.thermo.eos.ideal_gas import (
    IdealGasEquationOfState,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestIdealGasEquationOfStateEvaluatePressure:
    """Verify unit-aware ideal-gas pressure evaluation."""

    @staticmethod
    def _model() -> IdealGasEquationOfState:
        return IdealGasEquationOfState(
            amount=ScalarQuantity(
                magnitude=1.0,
                unit=PhysicalUnit(expression="mole"),
            )
        )

    def test__evaluate_pressure_matches_closed_form_isotherm(self) -> None:
        model = self._model()
        volume_values_cubic_metres = np.array(
            [1.0e-4, 5.0e-4, 1.0e-3],
            dtype=np.float64,
        )
        volumes = VectorQuantity(
            magnitude=volume_values_cubic_metres,
            unit=PhysicalUnit(expression="meter ** 3"),
        )
        temperature = ScalarQuantity(
            magnitude=300.0,
            unit=PhysicalUnit(expression="kelvin"),
        )

        evaluation = model.evaluate_pressure(
            volumes=volumes,
            temperature=temperature,
            pressure_unit=PhysicalUnit(expression="kilopascal"),
        )

        expected_kilopascal = (
            SI.R_g * temperature.magnitude / volume_values_cubic_metres / 1000.0
        )
        assert evaluation.request.model is model
        assert evaluation.volumes is volumes
        assert evaluation.temperature is temperature
        np.testing.assert_allclose(
            evaluation.pressures.magnitude,
            expected_kilopascal,
            rtol=2.0e-16,
            atol=0.0,
        )
        assert evaluation.pressures.unit == PhysicalUnit(expression="kilopascal")

    def test__evaluate_pressure_converts_compatible_input_units(self) -> None:
        model = IdealGasEquationOfState(
            amount=ScalarQuantity(
                magnitude=1000.0,
                unit=PhysicalUnit(expression="millimole"),
            )
        )

        evaluation = model.evaluate_pressure(
            volumes=VectorQuantity(
                magnitude=np.array([1.0], dtype=np.float64),
                unit=PhysicalUnit(expression="liter"),
            ),
            temperature=ScalarQuantity(
                magnitude=26.85,
                unit=PhysicalUnit(expression="degree_Celsius"),
            ),
            pressure_unit=PhysicalUnit(expression="bar"),
        )

        expected_bar = SI.R_g * 300.0 / 1.0e-3 / 1.0e5
        assert evaluation.pressures.magnitude[0] == pytest.approx(expected_bar)

    def test__evaluate_pressure_rejects_nonpositive_volume(self) -> None:
        with pytest.raises(ValueError, match="volumes must be positive"):
            self._model().evaluate_pressure(
                volumes=VectorQuantity(
                    magnitude=np.array([0.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="meter ** 3"),
                ),
                temperature=ScalarQuantity(
                    magnitude=300.0,
                    unit=PhysicalUnit(expression="kelvin"),
                ),
                pressure_unit=PhysicalUnit(expression="pascal"),
            )
