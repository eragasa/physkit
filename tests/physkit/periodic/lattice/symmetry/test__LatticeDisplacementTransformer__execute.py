"""Tests for integral transformation of lattice displacements."""

from physkit.periodic.lattice.finite_domain import (
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.periodic.lattice.symmetry import (
    IntegralLatticeOperation,
    LatticeDisplacementTransformer,
)


def test_applies_signed_axis_permutations_to_displacements() -> None:
    operation = IntegralLatticeOperation(
        "swap_reflect",
        LatticeDimension.TWO,
        ((0, -1), (1, 0)),
    )

    result = LatticeDisplacementTransformer().execute(
        operation, LatticeDisplacement(LatticeDimension.TWO, (2, -3))
    )

    assert result.components == (3, 2)
