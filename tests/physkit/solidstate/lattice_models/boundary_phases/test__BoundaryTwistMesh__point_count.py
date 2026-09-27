"""Tests for ``BoundaryTwistMesh.point_count``."""

from physkit.solidstate.lattice_models.boundary_phases import BoundaryTwistMesh
from physkit.solidstate.lattice_models.geometry import LatticeDimension


def test_multiplies_all_axis_counts() -> None:
    assert BoundaryTwistMesh(LatticeDimension.ONE, (4,)).point_count == 4
    assert BoundaryTwistMesh(LatticeDimension.TWO, (2, 3)).point_count == 6
    assert BoundaryTwistMesh(LatticeDimension.THREE, (2, 3, 4)).point_count == 24
