from __future__ import annotations

import numpy as np

from physkit.periodic.lattice.lattice3d import (
    DirectLattice3D,
    ReciprocalLattice3D,
)


def test_constructs_immutable_dual_reciprocal_basis() -> None:
    direct = DirectLattice3D(
        a1=np.array([2.0, 0.0, 0.0]),
        a2=np.array([0.5, 3.0, 0.0]),
        a3=np.array([1.0, 0.25, 4.0]),
    )

    reciprocal = ReciprocalLattice3D.from_direct_lattice(direct)

    np.testing.assert_allclose(
        direct.A.T @ reciprocal.B,
        2.0 * np.pi * np.eye(3),
        atol=1.0e-14,
    )
    assert reciprocal.B.flags.writeable is False
