"""Verification of ``UniformCartesianGrid1D`` construction."""

import pytest

from physkit.discretization.cartesian_grids import UniformCartesianGrid1D
from physkit.units import PhysicalUnit, ScalarQuantity, Unitless


def test_rejects_incompatible_and_invalid_geometry() -> None:
    with pytest.raises(ValueError, match="must not mix"):
        UniformCartesianGrid1D(
            ScalarQuantity(0.0, Unitless()),
            ScalarQuantity(1.0, PhysicalUnit("meter")),
            ScalarQuantity(0.25, Unitless()),
        )
    with pytest.raises(ValueError, match="incompatible"):
        UniformCartesianGrid1D(
            ScalarQuantity(0.0, PhysicalUnit("meter")),
            ScalarQuantity(1.0, PhysicalUnit("kilogram")),
            ScalarQuantity(0.25, PhysicalUnit("meter")),
        )
    with pytest.raises(ValueError, match="must divide"):
        UniformCartesianGrid1D(
            ScalarQuantity(-1.0, Unitless()),
            ScalarQuantity(1.0, Unitless()),
            ScalarQuantity(0.3, Unitless()),
        )
    with pytest.raises(ValueError, match="greater than"):
        UniformCartesianGrid1D(
            ScalarQuantity(1.0, Unitless()),
            ScalarQuantity(0.0, Unitless()),
            ScalarQuantity(0.25, Unitless()),
        )
