from __future__ import annotations

import numpy as np

from physkit.periodic.lattice.lattice2d import (
    DirectLattice2D,
    ReciprocalLattice2D,
)


def test_constructs_immutable_dual_reciprocal_basis() -> None:
    direct = DirectLattice2D(
        a1=np.array([2.0, 1.0]),
        a2=np.array([1.0, 3.0]),
    )

    reciprocal = ReciprocalLattice2D.from_direct_lattice(direct)

    np.testing.assert_allclose(
        direct.A.T @ reciprocal.primitive_basis,
        2.0 * np.pi * np.eye(2),
        atol=1.0e-14,
    )
    assert reciprocal.B.flags.writeable is False
