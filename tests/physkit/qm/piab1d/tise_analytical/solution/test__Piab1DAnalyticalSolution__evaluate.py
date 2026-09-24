"""Verification of ``Piab1DAnalyticalSolution.evaluate``."""

import numpy as np
import pytest

from physkit.core.results import ResultsObject
from physkit.qm.piab1d.tise_analytical import (
    Piab1DAnalyticalResults,
    Piab1DAnalyticalSolution,
)
from physkit.qm.piab1d.base import Piab1D
from physkit.units import PhysicalUnit, UnitSystem, Unitless


def test_returns_nondimensional_closed_form_results() -> None:
    solution = Piab1DAnalyticalSolution(
        Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)
    )

    results = solution.evaluate(3)

    assert isinstance(results, ResultsObject)
    assert isinstance(results, Piab1DAnalyticalResults)
    np.testing.assert_array_equal(results.quantum_numbers, [1, 2, 3])
    np.testing.assert_array_equal(
        results.energies.magnitude,
        np.pi**2 * np.array([1.0, 4.0, 9.0]) / 2.0,
    )
    assert isinstance(results.energies.unit, Unitless)


def test_returns_well_scaled_metal_energies() -> None:
    solution = Piab1DAnalyticalSolution(
        Piab1D(
            10.0,
            5.485_799_090_65e-4,
            UnitSystem.METAL,
        )
    )

    results = solution.evaluate(2)

    assert results.energies.unit == PhysicalUnit("electron_volt")
    np.testing.assert_allclose(
        results.energies.magnitude,
        [0.376_030_162_3, 1.504_120_649_2],
        rtol=2.0e-9,
        atol=0.0,
    )


def test_validates_model_and_count() -> None:
    with pytest.raises(TypeError, match="Piab1D"):
        Piab1DAnalyticalSolution(object())  # type: ignore[arg-type]

    solution = Piab1DAnalyticalSolution(
        Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)
    )
    with pytest.raises(TypeError, match="built-in int"):
        solution.evaluate(True)
    with pytest.raises(ValueError, match="positive"):
        solution.evaluate(0)
