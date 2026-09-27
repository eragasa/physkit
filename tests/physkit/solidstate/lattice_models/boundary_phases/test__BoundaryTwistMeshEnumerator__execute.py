"""Tests for deterministic boundary-twist mesh enumeration."""

from physkit.solidstate.lattice_models.boundary_phases import (
    BoundaryTwistMesh,
    BoundaryTwistMeshEnumerator,
)
from physkit.solidstate.lattice_models.geometry import LatticeDimension


def test_varies_the_last_axis_fastest() -> None:
    mesh = BoundaryTwistMesh(LatticeDimension.TWO, (2, 3))
    points = BoundaryTwistMeshEnumerator().execute(mesh)

    assert len(points) == mesh.point_count
    assert tuple(point.turns for point in points) == (
        (0.0, 0.0),
        (0.0, 1.0 / 3.0),
        (0.0, 2.0 / 3.0),
        (0.5, 0.0),
        (0.5, 1.0 / 3.0),
        (0.5, 2.0 / 3.0),
    )
