"""Tests for ``LocalizedOnsiteTerm`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from projectkoios.physkit.periodic.lattice.finite_domain import (
    LatticeCoordinate,
    LatticeDimension,
)
from projectkoios.physkit.periodic.lattice.hopping import LocalizedOnsiteTerm


def test_retains_site_and_finite_coefficient_components() -> None:
    site = LatticeCoordinate(LatticeDimension.TWO, (0, -1))
    term = LocalizedOnsiteTerm(site, 0.2, -0.1)

    assert term.site is site
    assert term.real == 0.2
    assert term.imaginary == -0.1
    with pytest.raises(FrozenInstanceError):
        term.real = 0.0  # type: ignore[misc]


def test_rejects_non_float_or_nonfinite_components() -> None:
    site = LatticeCoordinate(LatticeDimension.ONE, (0,))
    with pytest.raises(TypeError, match="built-in floats"):
        LocalizedOnsiteTerm(site, True, 0.0)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="must be finite"):
        LocalizedOnsiteTerm(site, 0.0, float("nan"))
