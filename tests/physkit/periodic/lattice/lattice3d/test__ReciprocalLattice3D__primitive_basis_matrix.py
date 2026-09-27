from __future__ import annotations

import numpy as np

from physkit.periodic.lattice.lattice3d import ReciprocalLattice3D


def test_returns_the_ordered_reciprocal_basis_columns() -> None:
    lattice = ReciprocalLattice3D(
        b1=np.array([1.0, 2.0, 3.0]),
        b2=np.array([4.0, 5.0, 6.0]),
        b3=np.array([7.0, 8.0, 10.0]),
    )

    np.testing.assert_array_equal(lattice.primitive_basis_matrix, lattice.B)
    assert lattice.B.flags.writeable is False
