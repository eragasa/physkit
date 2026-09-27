"""Tests for ``FinitePeriodicDomain`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
    LatticeSiteOrdering,
)


def test_retains_positive_integer_extents_and_ordering() -> None:
    domain = FinitePeriodicDomain(LatticeDimension.THREE, (2, 3, 4))

    assert domain.dimension is LatticeDimension.THREE
    assert domain.extents == (2, 3, 4)
    assert domain.ordering is LatticeSiteOrdering.LAST_AXIS_FASTEST
    with pytest.raises(FrozenInstanceError):
        domain.extents = (1, 1, 1)  # type: ignore[misc]


def test_rejects_noncanonical_or_invalid_extents() -> None:
    with pytest.raises(ValueError, match="count must match dimension"):
        FinitePeriodicDomain(LatticeDimension.TWO, (2,))
    with pytest.raises(TypeError, match="built-in integers"):
        FinitePeriodicDomain(LatticeDimension.ONE, (True,))
    with pytest.raises(ValueError, match="extents must be positive"):
        FinitePeriodicDomain(LatticeDimension.TWO, (2, 0))
    with pytest.raises(TypeError, match="ordering must be LatticeSiteOrdering"):
        FinitePeriodicDomain(
            LatticeDimension.ONE,
            (2,),
            "last_axis_fastest",  # type: ignore[arg-type]
        )
