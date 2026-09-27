from __future__ import annotations

from physkit.periodic.lattice.lattice1d import ReciprocalLattice1D


def test_returns_unsigned_reciprocal_cell_length() -> None:
    assert ReciprocalLattice1D(-2.5).measure == 2.5
