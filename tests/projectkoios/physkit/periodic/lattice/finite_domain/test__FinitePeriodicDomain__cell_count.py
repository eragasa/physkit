"""Tests for ``FinitePeriodicDomain.cell_count``."""

from projectkoios.physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
)


def test_multiplies_all_axis_extents() -> None:
    assert FinitePeriodicDomain(LatticeDimension.ONE, (4,)).cell_count == 4
    assert FinitePeriodicDomain(LatticeDimension.TWO, (2, 3)).cell_count == 6
    assert FinitePeriodicDomain(LatticeDimension.THREE, (2, 3, 4)).cell_count == 24
