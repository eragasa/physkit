"""Tests for finite-periodic-domain site orderings."""

from projectkoios.physkit.periodic.lattice.finite_domain import LatticeSiteOrdering


def test_declares_only_last_axis_fastest() -> None:
    assert tuple(LatticeSiteOrdering) == (LatticeSiteOrdering.LAST_AXIS_FASTEST,)
    assert LatticeSiteOrdering.LAST_AXIS_FASTEST.value == "last_axis_fastest"
