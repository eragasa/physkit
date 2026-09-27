"""Tests for ``ScalarHoppingTerm`` construction."""

from dataclasses import FrozenInstanceError

import pytest

from physkit.solidstate.lattice_models.geometry import (
    LatticeDimension,
    LatticeDisplacement,
)
from physkit.solidstate.lattice_models.lattice_models import ScalarHoppingTerm


def test_retains_finite_binary64_components_and_displacement() -> None:
    displacement = LatticeDisplacement(LatticeDimension.TWO, (-1, 2))
    term = ScalarHoppingTerm(displacement, -0.5, 0.25)

    assert term.displacement is displacement
    assert term.real == -0.5
    assert term.imaginary == 0.25
    with pytest.raises(FrozenInstanceError):
        term.real = 0.0  # type: ignore[misc]


def test_rejects_non_float_or_nonfinite_components() -> None:
    displacement = LatticeDisplacement(LatticeDimension.ONE, (0,))
    with pytest.raises(TypeError, match="built-in floats"):
        ScalarHoppingTerm(displacement, 1, 0.0)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="must be finite"):
        ScalarHoppingTerm(displacement, float("nan"), 0.0)
    with pytest.raises(ValueError, match="must be finite"):
        ScalarHoppingTerm(displacement, 0.0, float("inf"))
