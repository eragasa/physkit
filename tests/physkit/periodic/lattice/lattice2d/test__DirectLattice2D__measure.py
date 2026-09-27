from __future__ import annotations

import numpy as np

from physkit.periodic.lattice.lattice2d import DirectLattice2D


def test_returns_unsigned_primitive_cell_area() -> None:
    lattice = DirectLattice2D(
        a1=np.array([0.0, 1.0]),
        a2=np.array([1.0, 0.0]),
    )

    assert np.linalg.det(lattice.A) < 0.0
    assert lattice.measure == 1.0
