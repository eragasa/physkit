from __future__ import annotations

import numpy as np

from physkit.periodic.lattice.lattice2d import DirectLattice2D


def test_constructs_vectors_from_integer_indices() -> None:
    lattice = DirectLattice2D(
        a1=np.array([2.0, 1.0]),
        a2=np.array([1.0, 3.0]),
    )
    indices = np.array([[4, -2], [1, 3]])

    vectors = lattice.vector(indices)

    np.testing.assert_array_equal(vectors, indices @ lattice.A.T)
