"""Tests for last-axis-fastest index resolution."""

import pytest

from projectkoios.physkit.periodic.lattice.finite_domain import (
    FinitePeriodicCoordinateResolver,
    FinitePeriodicDomain,
    FinitePeriodicDomainIndexer,
    LatticeDimension,
)


def test_inverts_indexing_for_every_site_in_a_three_dimensional_shape() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.THREE, (2, 3, 4))
    resolver = FinitePeriodicCoordinateResolver()
    indexer = FinitePeriodicDomainIndexer()

    for index in range(domain.cell_count):
        coordinate = resolver.execute(domain, index)
        assert coordinate.dimension is LatticeDimension.THREE
        assert indexer.execute(domain, coordinate) == index

    assert resolver.execute(domain, 23).components == (1, 2, 3)


def test_rejects_boolean_and_out_of_domain_indices() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.ONE, (4,))
    resolver = FinitePeriodicCoordinateResolver()

    with pytest.raises(TypeError, match="built-in integer"):
        resolver.execute(domain, True)
    with pytest.raises(ValueError, match="within the finite periodic domain"):
        resolver.execute(domain, -1)
    with pytest.raises(ValueError, match="within the finite periodic domain"):
        resolver.execute(domain, 4)
