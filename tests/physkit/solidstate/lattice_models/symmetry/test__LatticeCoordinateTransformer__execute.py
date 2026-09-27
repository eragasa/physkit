"""Tests for integral transformation of lattice coordinates."""

import pytest

from physkit.solidstate.lattice_models.geometry import (
    LatticeCoordinate,
    LatticeDimension,
)
from physkit.solidstate.lattice_models.symmetry import (
    IntegralLatticeOperation,
    LatticeCoordinateTransformer,
)


def test_applies_the_declared_integral_matrix() -> None:
    operation = IntegralLatticeOperation(
        "cycle",
        LatticeDimension.THREE,
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
    )

    result = LatticeCoordinateTransformer().execute(
        operation, LatticeCoordinate(LatticeDimension.THREE, (1, 2, 3))
    )

    assert result.components == (2, 3, 1)


def test_rejects_dimensionally_incompatible_inputs() -> None:
    operation = IntegralLatticeOperation(
        "identity", LatticeDimension.ONE, ((1,),)
    )
    with pytest.raises(ValueError, match="dimensions must agree"):
        LatticeCoordinateTransformer().execute(
            operation, LatticeCoordinate(LatticeDimension.TWO, (1, 2))
        )
