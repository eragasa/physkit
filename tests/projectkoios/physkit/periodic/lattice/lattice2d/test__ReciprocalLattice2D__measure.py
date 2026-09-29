from __future__ import annotations

import numpy as np

from projectkoios.physkit.periodic.lattice.lattice2d import ReciprocalLattice2D


def test_returns_unsigned_reciprocal_cell_area() -> None:
    lattice = ReciprocalLattice2D(
        b1=np.array([0.0, 2.0]),
        b2=np.array([3.0, 0.0]),
    )

    assert lattice.measure == 6.0
