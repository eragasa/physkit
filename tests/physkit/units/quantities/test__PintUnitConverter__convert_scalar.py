"""Verification of scalar Pint conversion."""

import pytest

from physkit.units.quantities import (
    MODEL_SYSTEM_UNIT_CONVERTER,
    PhysicalUnit,
    ScalarQuantity,
)


def test_converts_compatible_scalar_value() -> None:
    result = MODEL_SYSTEM_UNIT_CONVERTER.convert_scalar(
        ScalarQuantity(100.0, PhysicalUnit("centimeter")),
        PhysicalUnit("meter"),
    )
    assert result == ScalarQuantity(1.0, PhysicalUnit("meter"))


def test_rejects_incompatible_dimensions() -> None:
    with pytest.raises(ValueError):
        MODEL_SYSTEM_UNIT_CONVERTER.convert_scalar(
            ScalarQuantity(1.0, PhysicalUnit("meter")),
            PhysicalUnit("kilogram"),
        )
