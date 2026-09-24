"""Verification of ``UniformCartesianGrid2D.coordinate_axes``."""

import numpy as np

from physkit.discretization.cartesian_grids import (
    UniformCartesianGrid1D,
    UniformCartesianGrid2D,
)
from physkit.units import PhysicalUnit, ScalarQuantity, Unitless


def axis(lower: float, upper: float, spacing: float, unit):
    return UniformCartesianGrid1D(
        ScalarQuantity(lower, unit),
        ScalarQuantity(upper, unit),
        ScalarQuantity(spacing, unit),
    )


def test_preserves_tensor_product_conventions() -> None:
    first = axis(-1.0, 1.0, 0.5, Unitless())
    second = axis(0.0, 1.0, 0.5, Unitless())
    grid = UniformCartesianGrid2D(first, second)

    assert grid.shape == (5, 3)
    assert grid.interior_shape == (3, 1)
    assert grid.indexing == "ij"
    assert grid.flattening_order == "C"
    axes = grid.coordinate_axes()
    np.testing.assert_array_equal(axes[0].magnitude, first.coordinates().magnitude)
    np.testing.assert_array_equal(axes[1].magnitude, second.coordinates().magnitude)


def test_retains_each_compatible_physical_axis_unit() -> None:
    first = axis(0.0, 1.0, 0.5, PhysicalUnit("meter"))
    second = axis(0.0, 100.0, 25.0, PhysicalUnit("centimeter"))
    grid = UniformCartesianGrid2D(first, second)

    assert grid.coordinate_axes()[0].unit == PhysicalUnit("meter")
    assert grid.coordinate_axes()[1].unit == PhysicalUnit("centimeter")
