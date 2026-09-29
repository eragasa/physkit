"""Isotherm-family tests for ``IdealGasEquationOfState``."""

import numpy as np

from projectkoios.physkit.thermal.thermo.eos.ideal_gas import (
    IdealGasEquationOfState,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestIdealGasEquationOfStateEvaluateIsotherms:
    """Verify ordered package-owned ideal-gas isotherm construction."""

    def test__evaluate_isotherms_retains_inputs_and_temperature_order(self) -> None:
        model = IdealGasEquationOfState(
            amount=ScalarQuantity(
                magnitude=1.0,
                unit=PhysicalUnit(expression="mole"),
            )
        )
        volumes = VectorQuantity(
            magnitude=np.array([0.5, 1.0, 2.0], dtype=np.float64),
            unit=PhysicalUnit(expression="liter"),
        )
        temperatures = VectorQuantity(
            magnitude=np.array([200.0, 250.0, 300.0], dtype=np.float64),
            unit=PhysicalUnit(expression="kelvin"),
        )
        pressure_unit = PhysicalUnit(expression="bar")

        isotherms = model.evaluate_isotherms(
            volumes=volumes,
            temperatures=temperatures,
            pressure_unit=pressure_unit,
        )

        assert isotherms.request.model is model
        assert isotherms.request.volumes is volumes
        assert isotherms.request.temperatures is temperatures
        assert len(isotherms) == temperatures.magnitude.size
        for index, isotherm in enumerate(isotherms):
            assert isotherm.volumes is volumes
            assert isotherm.temperature.magnitude == temperatures.magnitude[index]
            assert isotherm.temperature.unit == temperatures.unit
            assert isotherm.pressures.unit == pressure_unit
        assert np.all(
            isotherms.isotherms[0].pressures.magnitude
            < isotherms.isotherms[-1].pressures.magnitude
        )
