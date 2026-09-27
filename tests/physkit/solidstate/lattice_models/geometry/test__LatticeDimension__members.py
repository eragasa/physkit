"""Tests for supported finite-lattice dimensions."""

from physkit.solidstate.lattice_models.geometry import LatticeDimension


def test_declares_exact_supported_dimensions() -> None:
    assert tuple(LatticeDimension) == (
        LatticeDimension.ONE,
        LatticeDimension.TWO,
        LatticeDimension.THREE,
    )
    assert tuple(member.value for member in LatticeDimension) == (1, 2, 3)
