from __future__ import annotations

from physkit.periodic.lattice.lattice1d import DirectLattice1D


def test_returns_primitive_cell_length() -> None:
    assert DirectLattice1D(2.5).measure == 2.5
