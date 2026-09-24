"""Verification of Pint dimensional compatibility."""

from physkit.units.quantities import MODEL_SYSTEM_UNIT_CONVERTER, PhysicalUnit


def test_reports_dimensional_compatibility() -> None:
    assert MODEL_SYSTEM_UNIT_CONVERTER.compatible(
        PhysicalUnit("joule * second"),
        PhysicalUnit("kilogram * meter ** 2 / second"),
    )
    assert not MODEL_SYSTEM_UNIT_CONVERTER.compatible(
        PhysicalUnit("meter"),
        PhysicalUnit("kilogram"),
    )
