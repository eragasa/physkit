from __future__ import annotations

import numpy as np

from physkit.periodic.lattice.base import Lattice3D
from physkit.periodic.lattice.lattice3d import (
    DirectLattice3D,
    ReciprocalLattice3D,
)


def test_reports_right_handed_direct_basis() -> None:
    lattice = DirectLattice3D(
        a1=np.array([1.0, 0.0, 0.0]),
        a2=np.array([0.0, 2.0, 0.0]),
        a3=np.array([0.0, 0.0, 3.0]),
    )

    assert isinstance(lattice, Lattice3D)
    assert lattice.is_right_handed is True


def test_reports_left_handed_direct_basis() -> None:
    lattice = DirectLattice3D(
        a1=np.array([1.0, 0.0, 0.0]),
        a2=np.array([0.0, 0.0, 3.0]),
        a3=np.array([0.0, 2.0, 0.0]),
    )

    assert lattice.is_right_handed is False


def test_reports_reciprocal_basis_handedness() -> None:
    direct_lattice = DirectLattice3D(
        a1=np.array([1.0, 0.0, 0.0]),
        a2=np.array([0.0, 0.0, 3.0]),
        a3=np.array([0.0, 2.0, 0.0]),
    )
    reciprocal_lattice = ReciprocalLattice3D.from_direct_lattice(direct_lattice)

    assert isinstance(reciprocal_lattice, Lattice3D)
    assert reciprocal_lattice.is_right_handed is False
