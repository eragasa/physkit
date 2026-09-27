"""Tests for ``BoundaryTwistMesh`` construction."""

import pytest

from physkit.solidstate.lattice_models.boundary_phases import BoundaryTwistMesh
from physkit.solidstate.lattice_models.geometry import LatticeDimension


def test_retains_positive_integer_axis_counts() -> None:
    mesh = BoundaryTwistMesh(LatticeDimension.THREE, (2, 3, 4))

    assert mesh.counts == (2, 3, 4)


def test_rejects_invalid_axis_counts() -> None:
    with pytest.raises(ValueError, match="length must match dimension"):
        BoundaryTwistMesh(LatticeDimension.TWO, (2,))
    with pytest.raises(TypeError, match="built-in integers"):
        BoundaryTwistMesh(LatticeDimension.ONE, (True,))
    with pytest.raises(ValueError, match="must be positive"):
        BoundaryTwistMesh(LatticeDimension.TWO, (2, 0))
