from __future__ import annotations

import numpy as np

from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D


def test_returns_the_ordered_direct_basis_columns() -> None:
    lattice = DirectLattice3D(
        a1=np.array([1.0, 2.0, 3.0]),
        a2=np.array([4.0, 5.0, 6.0]),
        a3=np.array([7.0, 8.0, 10.0]),
    )

    np.testing.assert_array_equal(lattice.primitive_basis_matrix, lattice.A)
    assert lattice.A.flags.writeable is False
