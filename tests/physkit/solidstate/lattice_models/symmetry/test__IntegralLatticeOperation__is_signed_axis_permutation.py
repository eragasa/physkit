"""Tests for signed-axis-permutation classification."""

from physkit.solidstate.lattice_models.geometry import LatticeDimension
from physkit.solidstate.lattice_models.symmetry import IntegralLatticeOperation


def test_distinguishes_axis_permutations_from_general_unimodular_operations() -> None:
    cycle = IntegralLatticeOperation(
        "cycle",
        LatticeDimension.THREE,
        ((0, -1, 0), (0, 0, 1), (1, 0, 0)),
    )
    shear = IntegralLatticeOperation(
        "shear", LatticeDimension.TWO, ((1, 1), (0, 1))
    )

    assert cycle.is_signed_axis_permutation
    assert not shear.is_signed_axis_permutation
