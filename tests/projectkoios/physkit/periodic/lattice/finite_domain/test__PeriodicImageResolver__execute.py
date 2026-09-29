"""Tests for periodic finite-periodic-domain image resolution."""

import pytest

from projectkoios.physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeCoordinate,
    LatticeDimension,
    PeriodicImageResolver,
)


def test_wraps_each_axis_and_retains_euclidean_quotients() -> None:
    result = PeriodicImageResolver().execute(
        FinitePeriodicDomain(LatticeDimension.THREE, (4, 5, 6)),
        LatticeCoordinate(LatticeDimension.THREE, (-1, 7, -9)),
    )

    assert result.coordinate.components == (3, 2, 3)
    assert result.quotient.components == (-1, 1, -2)


def test_rejects_dimensionally_incompatible_inputs() -> None:
    with pytest.raises(ValueError, match="dimensions must agree"):
        PeriodicImageResolver().execute(
            FinitePeriodicDomain(LatticeDimension.TWO, (2, 3)),
            LatticeCoordinate(LatticeDimension.ONE, (1,)),
        )
