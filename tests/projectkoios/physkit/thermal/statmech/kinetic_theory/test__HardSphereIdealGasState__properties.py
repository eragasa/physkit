"""Property tests for ``HardSphereIdealGasState``."""

import math

import pytest

from projectkoios.physkit.constants import SI
from projectkoios.physkit.thermal.statmech.kinetic_theory import (
    HardSphereIdealGasState,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity


class TestHardSphereIdealGasStateProperties:
    """Verify unit-aware hard-sphere gas invariants and derived quantities."""

    ARGON_COLLISION_DIAMETER_METRES = 3.4e-10
    PRESSURE_PASCAL = 1.0
    TEMPERATURE_KELVIN = 300.0

    @classmethod
    def _state(cls) -> HardSphereIdealGasState:
        return HardSphereIdealGasState(
            pressure=ScalarQuantity(
                magnitude=cls.PRESSURE_PASCAL,
                unit=PhysicalUnit(expression="pascal"),
            ),
            temperature=ScalarQuantity(
                magnitude=cls.TEMPERATURE_KELVIN,
                unit=PhysicalUnit(expression="kelvin"),
            ),
            collision_diameter=ScalarQuantity(
                magnitude=cls.ARGON_COLLISION_DIAMETER_METRES,
                unit=PhysicalUnit(expression="meter"),
            ),
        )

    def test__properties_match_hard_sphere_closed_forms(self) -> None:
        state = self._state()
        expected_cross_section = math.pi * self.ARGON_COLLISION_DIAMETER_METRES**2
        expected_number_density = self.PRESSURE_PASCAL / (
            SI.k_B * self.TEMPERATURE_KELVIN
        )
        expected_mean_free_path = 1.0 / (
            math.sqrt(2.0) * expected_number_density * expected_cross_section
        )

        assert state.collision_cross_section.magnitude == pytest.approx(
            expected_cross_section,
            rel=1.0e-15,
        )
        assert state.collision_cross_section.unit == PhysicalUnit(
            expression="meter ** 2"
        )
        assert state.number_density.magnitude == pytest.approx(
            expected_number_density,
            rel=1.0e-15,
        )
        assert state.number_density.unit == PhysicalUnit(expression="meter ** -3")
        assert state.mean_free_path.magnitude == pytest.approx(
            expected_mean_free_path,
            rel=1.0e-15,
        )
        assert state.mean_free_path.unit == PhysicalUnit(expression="meter")

    def test__properties_convert_compatible_input_units(self) -> None:
        state = HardSphereIdealGasState(
            pressure=ScalarQuantity(
                magnitude=1.0e-5,
                unit=PhysicalUnit(expression="bar"),
            ),
            temperature=ScalarQuantity(
                magnitude=26.85,
                unit=PhysicalUnit(expression="degree_Celsius"),
            ),
            collision_diameter=ScalarQuantity(
                magnitude=0.34,
                unit=PhysicalUnit(expression="nanometer"),
            ),
        )

        assert state.pressure_in_pascal.magnitude == pytest.approx(1.0)
        assert state.temperature_in_kelvin.magnitude == pytest.approx(300.0)
        assert state.collision_diameter_in_metres.magnitude == pytest.approx(
            self.ARGON_COLLISION_DIAMETER_METRES
        )
        assert state.mean_free_path.magnitude == pytest.approx(
            self._state().mean_free_path.magnitude
        )

    def test__init_rejects_nonpositive_pressure(self) -> None:
        with pytest.raises(ValueError, match="pressure must be positive"):
            HardSphereIdealGasState(
                pressure=ScalarQuantity(
                    magnitude=0.0,
                    unit=PhysicalUnit(expression="pascal"),
                ),
                temperature=self._state().temperature,
                collision_diameter=self._state().collision_diameter,
            )

    def test__init_rejects_incompatible_collision_diameter_unit(self) -> None:
        with pytest.raises(ValueError, match="compatible with length"):
            HardSphereIdealGasState(
                pressure=self._state().pressure,
                temperature=self._state().temperature,
                collision_diameter=ScalarQuantity(
                    magnitude=1.0,
                    unit=PhysicalUnit(expression="second"),
                ),
            )
