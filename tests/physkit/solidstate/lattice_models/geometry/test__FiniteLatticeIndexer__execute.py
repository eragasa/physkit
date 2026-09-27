"""Tests for last-axis-fastest finite-lattice indexing."""

import pytest

from physkit.solidstate.lattice_models.geometry import (
    FiniteLatticeIndexer,
    FiniteLatticeShape,
    LatticeCoordinate,
    LatticeDimension,
)


def test_uses_last_axis_fastest_in_all_supported_dimensions() -> None:
    indexer = FiniteLatticeIndexer()

    assert indexer.execute(
        FiniteLatticeShape(LatticeDimension.ONE, (4,)),
        LatticeCoordinate(LatticeDimension.ONE, (3,)),
    ) == 3
    assert indexer.execute(
        FiniteLatticeShape(LatticeDimension.TWO, (2, 3)),
        LatticeCoordinate(LatticeDimension.TWO, (1, 2)),
    ) == 5
    assert indexer.execute(
        FiniteLatticeShape(LatticeDimension.THREE, (2, 3, 4)),
        LatticeCoordinate(LatticeDimension.THREE, (1, 2, 3)),
    ) == 23


def test_rejects_incompatible_or_out_of_domain_coordinates() -> None:
    indexer = FiniteLatticeIndexer()
    shape = FiniteLatticeShape(LatticeDimension.TWO, (2, 3))

    with pytest.raises(ValueError, match="dimensions must agree"):
        indexer.execute(shape, LatticeCoordinate(LatticeDimension.ONE, (1,)))
    with pytest.raises(ValueError, match="within the finite shape"):
        indexer.execute(shape, LatticeCoordinate(LatticeDimension.TWO, (2, 0)))
    with pytest.raises(ValueError, match="within the finite shape"):
        indexer.execute(shape, LatticeCoordinate(LatticeDimension.TWO, (-1, 0)))
