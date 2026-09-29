"""Tests for exact nearest-image resolution in nonorthogonal lattices."""

from itertools import product

import numpy as np
import pytest

from projectkoios.physkit.periodic.lattice.lattice2d import DirectLattice2D
from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D
from projectkoios.physkit.periodic.lattice.metric import (
    DirectLatticeMetric,
    NearestLatticeImageResolver,
)


def test__NearestLatticeImageResolver__execute__beats_componentwise_rounding() -> None:
    metric = DirectLatticeMetric(
        DirectLattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array([0.35, 0.90]),
        )
    )
    displacement = np.array([0.62, 0.57])
    naive_fractional = displacement - np.rint(displacement)
    naive_cartesian = metric.to_cartesian(naive_fractional)

    result = NearestLatticeImageResolver().execute(metric, displacement)

    np.testing.assert_array_equal(result.translation_indices, np.array([1, 0]))
    np.testing.assert_allclose(result.image_fractional, np.array([-0.38, 0.57]))
    assert result.distance < np.linalg.norm(naive_cartesian)
    assert result.displacement_fractional.flags.writeable is False
    assert result.translation_indices.flags.writeable is False
    assert result.image_fractional.flags.writeable is False
    assert result.image_cartesian.flags.writeable is False


def test__NearestLatticeImageResolver__execute__searches_beyond_neighbor_shell() -> (
    None
):
    metric = DirectLatticeMetric(
        DirectLattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array([0.99, 0.01]),
        )
    )
    displacement = np.array([0.54784675, -0.92085314])

    result = NearestLatticeImageResolver().execute(metric, displacement)

    np.testing.assert_array_equal(result.translation_indices, np.array([-18, 18]))
    assert np.max(np.abs(result.translation_indices - np.rint(displacement))) > 1.0


def test__NearestLatticeImageResolver__execute__matches_bounded_3d_reference() -> None:
    metric = DirectLatticeMetric(
        DirectLattice3D(
            a1=np.array([1.0, 0.0, 0.0]),
            a2=np.array([0.20, 0.90, 0.0]),
            a3=np.array([0.10, 0.25, 0.80]),
        )
    )
    displacement = np.array([1.58, -0.44, 0.48])
    candidates = np.asarray(
        tuple(product(range(-2, 4), repeat=3)),
        dtype=np.int64,
    )
    candidate_fractional = displacement[None, :] - candidates
    candidate_cartesian = metric.to_cartesian(candidate_fractional)
    distances = np.linalg.norm(candidate_cartesian, axis=1)

    result = NearestLatticeImageResolver().execute(metric, displacement)

    assert result.distance == pytest.approx(float(np.min(distances)))
    np.testing.assert_allclose(
        result.image_cartesian,
        metric.to_cartesian(result.image_fractional),
    )


def test__NearestLatticeImageResolver__execute__retains_integer_zero_image() -> None:
    metric = DirectLatticeMetric(
        DirectLattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array([0.5, 1.0]),
        )
    )

    result = NearestLatticeImageResolver().execute(
        metric,
        np.array([3.0, -2.0]),
    )

    np.testing.assert_array_equal(result.translation_indices, np.array([3, -2]))
    np.testing.assert_array_equal(result.image_fractional, np.zeros(2))
    assert result.distance == 0.0


def test__NearestLatticeImageResolver__execute__rejects_invalid_input() -> None:
    metric = DirectLatticeMetric(
        DirectLattice2D(
            a1=np.array([1.0, 0.0]),
            a2=np.array([0.5, 1.0]),
        )
    )
    resolver = NearestLatticeImageResolver()

    with pytest.raises(TypeError, match="DirectLatticeMetric"):
        resolver.execute(metric.direct_lattice, np.zeros(2))  # type: ignore[arg-type]
    with pytest.raises(ValueError, match=r"shape \(2,\)"):
        resolver.execute(metric, np.zeros(3))
    with pytest.raises(ValueError, match="finite values"):
        resolver.execute(metric, np.array([np.inf, 0.0]))
    with pytest.raises(ValueError, match="int64 translation"):
        resolver.execute(metric, np.array([float(2**63), 0.0]))
