"""Verification of nominal model-system unit ownership."""

from physkit.units.quantities import ModelSystemUnit, PhysicalUnit, Unitless


def test_concrete_units_inherit_model_system_unit() -> None:
    assert PhysicalUnit.__bases__ == (ModelSystemUnit,)
    assert Unitless.__bases__ == (ModelSystemUnit,)
