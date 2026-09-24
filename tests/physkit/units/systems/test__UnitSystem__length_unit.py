"""Verification of ``UnitSystem.length_unit``."""

from physkit.units import PhysicalUnit, UnitSystem, Unitless


def test_returns_selected_length_scale() -> None:
    assert isinstance(UnitSystem.NONDIMENSIONAL.length_unit, Unitless)
    assert UnitSystem.SI.length_unit == PhysicalUnit("meter")
    assert UnitSystem.METAL.length_unit == PhysicalUnit("angstrom")
