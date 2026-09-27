"""Tests for ``PeriodicImageResult`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.core.results import ResultsObject
from physkit.periodic.lattice.finite_domain import (
    LatticeCoordinate,
    LatticeDimension,
    LatticeDisplacement,
    PeriodicImageResult,
)


def test_retains_correlated_coordinate_and_quotient() -> None:
    coordinate = LatticeCoordinate(LatticeDimension.TWO, (1, 2))
    quotient = LatticeDisplacement(LatticeDimension.TWO, (-1, 3))
    result = PeriodicImageResult(coordinate, quotient)

    assert isinstance(result, ResultsObject)
    assert result.coordinate is coordinate
    assert result.quotient is quotient
    with pytest.raises(FrozenInstanceError):
        result.coordinate = coordinate  # type: ignore[misc]


def test_rejects_dimensionally_inconsistent_members() -> None:
    with pytest.raises(ValueError, match="dimensions must agree"):
        PeriodicImageResult(
            LatticeCoordinate(LatticeDimension.ONE, (1,)),
            LatticeDisplacement(LatticeDimension.TWO, (0, 0)),
        )
