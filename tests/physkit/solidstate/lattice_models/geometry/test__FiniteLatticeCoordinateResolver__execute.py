"""Tests for last-axis-fastest index resolution."""

import pytest

from physkit.solidstate.lattice_models.geometry import (
    FiniteLatticeCoordinateResolver,
    FiniteLatticeIndexer,
    FiniteLatticeShape,
    LatticeDimension,
)


def test_inverts_indexing_for_every_site_in_a_three_dimensional_shape() -> None:
    shape = FiniteLatticeShape(LatticeDimension.THREE, (2, 3, 4))
    resolver = FiniteLatticeCoordinateResolver()
    indexer = FiniteLatticeIndexer()

    for index in range(shape.cell_count):
        coordinate = resolver.execute(shape, index)
        assert coordinate.dimension is LatticeDimension.THREE
        assert indexer.execute(shape, coordinate) == index

    assert resolver.execute(shape, 23).components == (1, 2, 3)


def test_rejects_boolean_and_out_of_domain_indices() -> None:
    shape = FiniteLatticeShape(LatticeDimension.ONE, (4,))
    resolver = FiniteLatticeCoordinateResolver()

    with pytest.raises(TypeError, match="built-in integer"):
        resolver.execute(shape, True)
    with pytest.raises(ValueError, match="within the finite shape"):
        resolver.execute(shape, -1)
    with pytest.raises(ValueError, match="within the finite shape"):
        resolver.execute(shape, 4)
