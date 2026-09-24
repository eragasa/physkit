"""Verification of ``UnitSystem.mass_unit``."""

from physkit.units import PhysicalUnit, UnitSystem, Unitless


def test_returns_selected_particle_mass_scale() -> None:
    assert isinstance(UnitSystem.NONDIMENSIONAL.mass_unit, Unitless)
    assert UnitSystem.SI.mass_unit == PhysicalUnit("kilogram")
    assert UnitSystem.METAL.mass_unit == PhysicalUnit("dalton")
