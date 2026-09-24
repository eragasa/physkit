"""Verification of ``UniformCartesianGrid1D.coordinates``."""

import numpy as np

from physkit.discretization.cartesian_grids import UniformCartesianGrid1D
from physkit.units import PhysicalUnit, ScalarQuantity, Unitless


def test_preserves_order_spacing_and_interior_coordinates() -> None:
    grid = UniformCartesianGrid1D(
        ScalarQuantity(-1.0, Unitless()),
        ScalarQuantity(1.0, Unitless()),
        ScalarQuantity(0.5, Unitless()),
    )

    assert grid.interval_count == 4
    assert grid.point_count == 5
    assert grid.interior_point_count == 3
    np.testing.assert_array_equal(
        grid.coordinates().magnitude,
        [-1.0, -0.5, 0.0, 0.5, 1.0],
    )
    np.testing.assert_array_equal(
        grid.interior_coordinates().magnitude,
        [-0.5, 0.0, 0.5],
    )


def test_converts_compatible_units_to_lower_bound_unit() -> None:
    grid = UniformCartesianGrid1D(
        ScalarQuantity(0.0, PhysicalUnit("meter")),
        ScalarQuantity(100.0, PhysicalUnit("centimeter")),
        ScalarQuantity(250.0, PhysicalUnit("millimeter")),
    )

    assert grid.coordinate_unit == PhysicalUnit("meter")
    assert grid.spacing == ScalarQuantity(0.25, PhysicalUnit("meter"))
    np.testing.assert_allclose(
        grid.coordinates().magnitude,
        [0.0, 0.25, 0.5, 0.75, 1.0],
        rtol=0.0,
        atol=2.0e-16,
    )
