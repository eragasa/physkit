"""Characteristic-speed tests for ``MaxwellBoltzmannGasState``."""

import math

import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.kinetic_theory import (
    MaxwellBoltzmannGasState,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity


class TestMaxwellBoltzmannGasStateCharacteristicSpeeds:
    """Verify unit-aware analytic speed properties of the modeled gas state."""

    @staticmethod
    def _state(*, temperature_kelvin: float, molar_mass_kg_per_mol: float):
        return MaxwellBoltzmannGasState(
            temperature=ScalarQuantity(
                magnitude=temperature_kelvin,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            molar_mass=ScalarQuantity(
                magnitude=molar_mass_kg_per_mol,
                unit=PhysicalUnit(expression="kilogram / mole"),
            ),
        )

    def test__characteristic_speeds_match_closed_form_values(self) -> None:
        temperature_kelvin = 300.0
        molar_mass_kg_per_mol = 0.0280134
        state = self._state(
            temperature_kelvin=temperature_kelvin,
            molar_mass_kg_per_mol=molar_mass_kg_per_mol,
        )
        scale = SI.R_g * temperature_kelvin / molar_mass_kg_per_mol

        assert state.most_probable_speed.magnitude == pytest.approx(
            math.sqrt(2.0 * scale), rel=5e-16, abs=0.0
        )
        assert state.mean_speed.magnitude == pytest.approx(
            math.sqrt(8.0 * scale / math.pi), rel=5e-16, abs=0.0
        )
        assert state.root_mean_square_speed.magnitude == pytest.approx(
            math.sqrt(3.0 * scale), rel=5e-16, abs=0.0
        )
        expected_unit = PhysicalUnit(expression="meter / second")
        assert state.most_probable_speed.unit == expected_unit
        assert state.mean_speed.unit == expected_unit
        assert state.root_mean_square_speed.unit == expected_unit

    def test__characteristic_speeds_have_expected_order(self) -> None:
        state = self._state(
            temperature_kelvin=1200.0,
            molar_mass_kg_per_mol=0.004002602,
        )

        assert (
            state.most_probable_speed.magnitude
            < state.mean_speed.magnitude
            < state.root_mean_square_speed.magnitude
        )
