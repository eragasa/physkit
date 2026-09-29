"""Tests for supported PIAB3D Cartesian plane normals."""

from projectkoios.physkit.qm.piab3d.tise.analytical.eigenfunctions import (
    Piab3DPlaneNormal,
)


class TestPiab3DPlaneNormalMembers:
    """Verify the closed Cartesian plane-normal vocabulary."""

    def test__members__use_uppercase_names_and_lowercase_axis_values(self) -> None:
        assert tuple(Piab3DPlaneNormal) == (
            Piab3DPlaneNormal.X,
            Piab3DPlaneNormal.Y,
            Piab3DPlaneNormal.Z,
        )
        assert tuple(member.name for member in Piab3DPlaneNormal) == (
            "X",
            "Y",
            "Z",
        )
        assert tuple(member.value for member in Piab3DPlaneNormal) == (
            "x",
            "y",
            "z",
        )
