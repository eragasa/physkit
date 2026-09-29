"""Tests for ``IntegralLatticeOperation`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from projectkoios.physkit.periodic.lattice.finite_domain import LatticeDimension
from projectkoios.physkit.periodic.lattice.symmetry import IntegralLatticeOperation


def test_retains_an_exact_unimodular_integer_matrix() -> None:
    operation = IntegralLatticeOperation(
        "shear",
        LatticeDimension.TWO,
        ((1, 1), (0, 1)),
    )

    assert operation.identifier == "shear"
    assert operation.matrix == ((1, 1), (0, 1))
    with pytest.raises(FrozenInstanceError):
        operation.identifier = "other"  # type: ignore[misc]


def test_rejects_invalid_identity_shape_entries_and_determinant() -> None:
    with pytest.raises(ValueError, match="identifier must be nonempty"):
        IntegralLatticeOperation("", LatticeDimension.ONE, ((1,),))
    with pytest.raises(ValueError, match="row count must match dimension"):
        IntegralLatticeOperation("bad", LatticeDimension.TWO, ((1, 0),))
    with pytest.raises(TypeError, match="built-in integers"):
        IntegralLatticeOperation("bad", LatticeDimension.TWO, ((1, 0), (0, True)))
    with pytest.raises(ValueError, match="must be unimodular"):
        IntegralLatticeOperation("scale", LatticeDimension.TWO, ((2, 0), (0, 1)))
