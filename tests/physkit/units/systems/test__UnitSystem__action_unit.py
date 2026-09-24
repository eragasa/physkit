"""Verification of ``UnitSystem.action_unit``."""

from physkit.units import PhysicalUnit, UnitSystem, Unitless


def test_returns_selected_action_scale() -> None:
    assert isinstance(UnitSystem.NONDIMENSIONAL.action_unit, Unitless)
    assert UnitSystem.SI.action_unit == PhysicalUnit("joule * second")
    assert UnitSystem.METAL.action_unit == PhysicalUnit(
        "electron_volt * picosecond"
    )
