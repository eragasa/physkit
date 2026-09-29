"""Tests for exact integral-operation determinants."""

from projectkoios.physkit.periodic.lattice.finite_domain import LatticeDimension
from projectkoios.physkit.periodic.lattice.symmetry import IntegralLatticeOperation


def test_evaluates_one_two_and_three_dimensional_determinants() -> None:
    assert (
        IntegralLatticeOperation("reflect", LatticeDimension.ONE, ((-1,),)).determinant
        == -1
    )
    assert (
        IntegralLatticeOperation(
            "swap", LatticeDimension.TWO, ((0, 1), (1, 0))
        ).determinant
        == -1
    )
    assert (
        IntegralLatticeOperation(
            "cycle",
            LatticeDimension.THREE,
            ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
        ).determinant
        == 1
    )
