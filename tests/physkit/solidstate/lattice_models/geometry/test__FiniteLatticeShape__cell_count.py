"""Tests for ``FiniteLatticeShape.cell_count``."""

from physkit.solidstate.lattice_models.geometry import (
    FiniteLatticeShape,
    LatticeDimension,
)


def test_multiplies_all_axis_extents() -> None:
    assert FiniteLatticeShape(LatticeDimension.ONE, (4,)).cell_count == 4
    assert FiniteLatticeShape(LatticeDimension.TWO, (2, 3)).cell_count == 6
    assert FiniteLatticeShape(LatticeDimension.THREE, (2, 3, 4)).cell_count == 24
