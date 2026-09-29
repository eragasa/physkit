"""Tests for direct-lattice metric construction and immutable ownership."""

import numpy as np
import pytest

from projectkoios.physkit.periodic.lattice.lattice1d import DirectLattice1D
from projectkoios.physkit.periodic.lattice.lattice2d import DirectLattice2D
from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D
from projectkoios.physkit.periodic.lattice.metric import DirectLatticeMetric


def test__DirectLatticeMetric__init__derives_two_dimensional_geometry() -> None:
    lattice = DirectLattice2D(
        a1=np.array([1.0, 0.0]),
        a2=np.array([0.35, 0.90]),
    )

    metric = DirectLatticeMetric(lattice)

    expected_tensor = lattice.A.T @ lattice.A
    np.testing.assert_allclose(metric.metric_tensor, expected_tensor)
    np.testing.assert_allclose(
        metric.inverse_metric_tensor,
        np.linalg.inv(expected_tensor),
    )
    np.testing.assert_allclose(
        metric.primitive_basis.T @ metric.reciprocal_basis,
        2.0 * np.pi * np.eye(2),
        rtol=0.0,
        atol=3.0e-15,
    )
    np.testing.assert_allclose(
        metric.reciprocal_metric_tensor,
        (2.0 * np.pi) ** 2 * metric.inverse_metric_tensor,
    )
    assert metric.dimension == 2
    assert metric.measure == pytest.approx(abs(np.linalg.det(lattice.A)))


def test__DirectLatticeMetric__init__derives_three_dimensional_geometry() -> None:
    lattice = DirectLattice3D(
        a1=np.array([1.0, 0.0, 0.0]),
        a2=np.array([0.20, 0.90, 0.0]),
        a3=np.array([0.10, 0.25, 0.80]),
    )

    metric = DirectLatticeMetric(lattice)

    np.testing.assert_allclose(
        metric.metric_tensor,
        lattice.A.T @ lattice.A,
    )
    np.testing.assert_allclose(
        metric.primitive_basis.T @ metric.reciprocal_basis,
        2.0 * np.pi * np.eye(3),
        rtol=0.0,
        atol=3.0e-15,
    )
    assert metric.dimension == 3
    assert metric.measure == pytest.approx(abs(np.linalg.det(lattice.A)))


def test__DirectLatticeMetric__init__owns_immutable_storage() -> None:
    first_vector = np.array([1.0, 0.0])
    second_vector = np.array([0.25, 0.75])
    metric = DirectLatticeMetric(DirectLattice2D(first_vector, second_vector))

    first_vector[0] = 3.0
    second_vector[1] = 4.0

    np.testing.assert_allclose(
        metric.primitive_basis,
        np.array([[1.0, 0.25], [0.0, 0.75]]),
    )
    for array in (
        metric.primitive_basis,
        metric.reciprocal_basis,
        metric.metric_tensor,
        metric.inverse_metric_tensor,
        metric.reciprocal_metric_tensor,
    ):
        assert array.flags.writeable is False
    with pytest.raises(ValueError, match="read-only"):
        metric.metric_tensor[0, 0] = 2.0


def test__DirectLatticeMetric__init__rejects_unrepresentable_metric() -> None:
    tiny = 1.0e-200
    lattice = DirectLattice3D(
        a1=np.array([tiny, 0.0, 0.0]),
        a2=np.array([0.0, tiny, 0.0]),
        a3=np.array([0.0, 0.0, tiny]),
    )

    with pytest.raises(ValueError, match="invertible in float64"):
        DirectLatticeMetric(lattice)


def test__DirectLatticeMetric__init__rejects_unsupported_dimension() -> None:
    with pytest.raises(TypeError, match="DirectLattice2D or DirectLattice3D"):
        DirectLatticeMetric(DirectLattice1D(1.0))  # type: ignore[arg-type]
