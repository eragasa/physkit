"""Verification of ``Piab1DAnalyticalResults`` correlation."""

import numpy as np
import pytest

from physkit.qm.piab1d.tise_analytical import (
    Piab1DAnalyticalResults,
)
from physkit.qm.piab1d.base import Piab1D
from physkit.units import UnitSystem, Unitless, VectorQuantity


def test_retains_immutable_correlated_results() -> None:
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)
    results = Piab1DAnalyticalResults(
        model,
        np.array([1, 2]),
        VectorQuantity(np.array([1.0, 4.0]), Unitless()),
    )

    assert results.model is model
    assert not results.quantum_numbers.flags.writeable
    assert not results.energies.magnitude.flags.writeable


def test_rejects_uncorrelated_shapes() -> None:
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)

    with pytest.raises(ValueError, match="match"):
        Piab1DAnalyticalResults(
            model,
            np.array([1, 2]),
            VectorQuantity(np.array([1.0]), Unitless()),
        )
