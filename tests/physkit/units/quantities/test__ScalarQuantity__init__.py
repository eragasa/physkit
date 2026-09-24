"""Verification of ``ScalarQuantity`` construction."""

import pytest

from physkit.units.quantities import PhysicalUnit, ScalarQuantity, Unitless


def test_requires_finite_builtin_float() -> None:
    quantity = ScalarQuantity(1.0, PhysicalUnit("meter"))
    assert quantity.magnitude == 1.0
    assert quantity.unit == PhysicalUnit("meter")
    with pytest.raises(TypeError):
        ScalarQuantity(1, Unitless())  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        ScalarQuantity(float("nan"), Unitless())
