from __future__ import annotations

import numpy as np

from physkit.periodic.lattice.lattice3d import ReciprocalLattice3D


def test_constructs_vectors_from_integer_indices() -> None:
    lattice = ReciprocalLattice3D(
        b1=np.array([2.0, 0.0, 0.0]),
        b2=np.array([0.5, 3.0, 0.0]),
        b3=np.array([1.0, 0.25, 4.0]),
    )
    indices = np.array([[2, -1, 3], [0, 1, -2]])

    vectors = lattice.vector(indices)

    np.testing.assert_array_equal(vectors, indices @ lattice.B.T)
