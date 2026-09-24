"""Verification of ``UniformCartesianGrid2D`` construction."""

import pytest

from physkit.discretization.cartesian_grids import (
    UniformCartesianGrid1D,
    UniformCartesianGrid2D,
)
from physkit.units import PhysicalUnit, ScalarQuantity, Unitless


def axis(unit: PhysicalUnit | Unitless) -> UniformCartesianGrid1D:
    return UniformCartesianGrid1D(
        ScalarQuantity(0.0, unit),
        ScalarQuantity(1.0, unit),
        ScalarQuantity(0.5, unit),
    )


def test_requires_nominal_compatible_axes() -> None:
    unitless = axis(Unitless())
    with pytest.raises(TypeError):
        UniformCartesianGrid2D(object(), unitless)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="compatible"):
        UniformCartesianGrid2D(
            axis(PhysicalUnit("meter")),
            axis(PhysicalUnit("kilogram")),
        )
    with pytest.raises(ValueError, match="compatible"):
        UniformCartesianGrid2D(unitless, axis(PhysicalUnit("meter")))
