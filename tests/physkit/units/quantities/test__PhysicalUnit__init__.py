"""Verification of ``PhysicalUnit`` construction."""

import pytest

from physkit.units.quantities import PhysicalUnit, Unitless


def test_distinguishes_valid_physical_units_from_unitless() -> None:
    assert PhysicalUnit("centimeter") != PhysicalUnit("meter")
    assert Unitless().expression == "dimensionless"
    with pytest.raises(ValueError):
        PhysicalUnit("dimensionless")
    with pytest.raises(ValueError):
        PhysicalUnit("not_a_real_unit")
