"""Tests for fractional-to-Cartesian direct-basis mapping."""

import numpy as np
import pytest

from projectkoios.physkit.periodic.lattice.lattice2d import DirectLattice2D
from projectkoios.physkit.periodic.lattice.metric import DirectLatticeMetric


def test__DirectLatticeMetric__to_cartesian__maps_vectors_and_batches() -> None:
    lattice = DirectLattice2D(
        a1=np.array([1.0, 0.0]),
        a2=np.array([0.5, 1.0]),
    )
    metric = DirectLatticeMetric(lattice)
    fractional = np.array([[1.0, 0.0], [0.0, 1.0], [0.25, -0.5]])

    cartesian = metric.to_cartesian(fractional)

    np.testing.assert_allclose(cartesian, fractional @ lattice.A.T)
    assert cartesian.dtype == np.float64


@pytest.mark.parametrize(
    "coordinates",
    [np.array(1.0), np.array([1.0]), np.ones((2, 3))],
)
def test__DirectLatticeMetric__to_cartesian__rejects_wrong_dimension(
    coordinates: np.ndarray,
) -> None:
    metric = DirectLatticeMetric(
        DirectLattice2D(np.array([1.0, 0.0]), np.array([0.5, 1.0]))
    )

    with pytest.raises(ValueError, match="final dimension 2"):
        metric.to_cartesian(coordinates)


def test__DirectLatticeMetric__to_cartesian__rejects_nonfinite_values() -> None:
    metric = DirectLatticeMetric(
        DirectLattice2D(np.array([1.0, 0.0]), np.array([0.5, 1.0]))
    )

    with pytest.raises(ValueError, match="finite values"):
        metric.to_cartesian(np.array([np.nan, 0.0]))
