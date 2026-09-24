"""Verification of ``UnitSystem.energy_unit``."""

from physkit.units import PhysicalUnit, UnitSystem, Unitless


def test_returns_selected_energy_scale() -> None:
    assert isinstance(UnitSystem.NONDIMENSIONAL.energy_unit, Unitless)
    assert UnitSystem.SI.energy_unit == PhysicalUnit("joule")
    assert UnitSystem.METAL.energy_unit == PhysicalUnit("electron_volt")
