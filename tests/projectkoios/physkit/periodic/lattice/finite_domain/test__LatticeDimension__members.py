"""Tests for supported finite-periodic-domain dimensions."""

from projectkoios.physkit.periodic.lattice.finite_domain import LatticeDimension


def test_declares_exact_supported_dimensions() -> None:
    assert tuple(LatticeDimension) == (
        LatticeDimension.ONE,
        LatticeDimension.TWO,
        LatticeDimension.THREE,
    )
    assert tuple(member.value for member in LatticeDimension) == (1, 2, 3)
