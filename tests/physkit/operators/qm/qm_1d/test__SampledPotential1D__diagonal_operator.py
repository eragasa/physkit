"""Verification of represented sampled potential energy."""

import numpy as np
import pytest

from physkit.discretization.cartesian_grids import UniformCartesianGrid1D
from physkit.operators.qm import SampledPotential1D
from physkit.units import ScalarQuantity, Unitless, VectorQuantity


def grid() -> UniformCartesianGrid1D:
    return UniformCartesianGrid1D(
        ScalarQuantity(-1.0, Unitless()),
        ScalarQuantity(1.0, Unitless()),
        ScalarQuantity(0.5, Unitless()),
    )


def test_preserves_grid_order_and_diagonal_values() -> None:
    potential = SampledPotential1D(
        grid(),
        VectorQuantity(np.array([0.125, 0.0, 0.125]), Unitless()),
    )

    np.testing.assert_array_equal(
        potential.diagonal_operator().to_dense().magnitude,
        np.diag([0.125, 0.0, 0.125]),
    )
    np.testing.assert_array_equal(
        potential.matrix().to_dense().magnitude,
        potential.diagonal_operator().to_dense().magnitude,
    )


def test_rejects_value_count_different_from_grid() -> None:
    with pytest.raises(ValueError, match="interior-point count"):
        SampledPotential1D(
            grid(),
            VectorQuantity(np.array([0.0, 0.0]), Unitless()),
        )
