from __future__ import annotations

import numpy as np

from projectkoios.physkit.periodic.lattice.lattice3d import DirectLattice3D


def test_preserves_the_ordered_basis_orientation() -> None:
    lattice = DirectLattice3D(
        a1=np.array([1.0, 0.0, 0.0]),
        a2=np.array([0.0, 0.0, 3.0]),
        a3=np.array([0.0, 2.0, 0.0]),
    )

    assert lattice.signed_measure == -6.0
    assert lattice.measure == 6.0
