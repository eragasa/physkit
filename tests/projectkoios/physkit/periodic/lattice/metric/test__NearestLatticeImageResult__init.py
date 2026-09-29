"""Tests for direct nearest-image result consistency validation."""

import numpy as np
import pytest

from projectkoios.physkit.periodic.lattice.lattice2d import DirectLattice2D
from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D
from projectkoios.physkit.periodic.lattice.metric import (
    DirectLatticeMetric,
    NearestLatticeImageResult,
)


def test__NearestLatticeImageResult__init__checks_large_2d_mapping_scale() -> None:
    scale = 1.0e150
    metric = DirectLatticeMetric(
        DirectLattice2D(
            a1=np.array([scale, 0.0]),
            a2=np.array([scale, 1.0e146]),
        )
    )
    image_fractional = np.array([1.0, -1.0])
    image_cartesian = metric.to_cartesian(image_fractional)

    result = NearestLatticeImageResult(
        metric=metric,
        displacement_fractional=image_fractional,
        translation_indices=np.zeros(2, dtype=np.int64),
        image_fractional=image_fractional,
        image_cartesian=image_cartesian,
    )

    np.testing.assert_array_equal(result.image_cartesian, image_cartesian)

    inconsistent_cartesian = image_cartesian.copy()
    inconsistent_cartesian[0] = 1.0e140
    with pytest.raises(ValueError, match="mapped fractional image"):
        NearestLatticeImageResult(
            metric=metric,
            displacement_fractional=image_fractional,
            translation_indices=np.zeros(2, dtype=np.int64),
            image_fractional=image_fractional,
            image_cartesian=inconsistent_cartesian,
        )


def test__NearestLatticeImageResult__init__checks_tiny_3d_mapping_scale() -> None:
    scale = 1.0e-100
    metric = DirectLatticeMetric(
        DirectLattice3D(
            a1=np.array([scale, 0.0, 0.0]),
            a2=np.array([0.0, 2.0 * scale, 0.0]),
            a3=np.array([0.0, 0.0, 3.0 * scale]),
        )
    )
    image_fractional = np.array([0.25, -0.5, 0.75])
    image_cartesian = metric.to_cartesian(image_fractional)

    result = NearestLatticeImageResult(
        metric=metric,
        displacement_fractional=image_fractional,
        translation_indices=np.zeros(3, dtype=np.int64),
        image_fractional=image_fractional,
        image_cartesian=image_cartesian,
    )

    np.testing.assert_array_equal(result.image_cartesian, image_cartesian)

    inconsistent_cartesian = image_cartesian.copy()
    inconsistent_cartesian[0] += 1.0e-110
    with pytest.raises(ValueError, match="mapped fractional image"):
        NearestLatticeImageResult(
            metric=metric,
            displacement_fractional=image_fractional,
            translation_indices=np.zeros(3, dtype=np.int64),
            image_fractional=image_fractional,
            image_cartesian=inconsistent_cartesian,
        )
