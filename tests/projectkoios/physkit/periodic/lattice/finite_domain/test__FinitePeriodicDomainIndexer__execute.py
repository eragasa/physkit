"""Tests for last-axis-fastest finite-periodic-domain indexing."""

import pytest

from projectkoios.physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    FinitePeriodicDomainIndexer,
    LatticeCoordinate,
    LatticeDimension,
)


def test_uses_last_axis_fastest_in_all_supported_dimensions() -> None:
    indexer = FinitePeriodicDomainIndexer()

    assert (
        indexer.execute(
            FinitePeriodicDomain(LatticeDimension.ONE, (4,)),
            LatticeCoordinate(LatticeDimension.ONE, (3,)),
        )
        == 3
    )
    assert (
        indexer.execute(
            FinitePeriodicDomain(LatticeDimension.TWO, (2, 3)),
            LatticeCoordinate(LatticeDimension.TWO, (1, 2)),
        )
        == 5
    )
    assert (
        indexer.execute(
            FinitePeriodicDomain(LatticeDimension.THREE, (2, 3, 4)),
            LatticeCoordinate(LatticeDimension.THREE, (1, 2, 3)),
        )
        == 23
    )


def test_rejects_incompatible_or_out_of_domain_coordinates() -> None:
    indexer = FinitePeriodicDomainIndexer()
    domain = FinitePeriodicDomain(LatticeDimension.TWO, (2, 3))

    with pytest.raises(ValueError, match="dimensions must agree"):
        indexer.execute(domain, LatticeCoordinate(LatticeDimension.ONE, (1,)))
    with pytest.raises(ValueError, match="within the finite periodic domain"):
        indexer.execute(domain, LatticeCoordinate(LatticeDimension.TWO, (2, 0)))
    with pytest.raises(ValueError, match="within the finite periodic domain"):
        indexer.execute(domain, LatticeCoordinate(LatticeDimension.TWO, (-1, 0)))
