"""Verification of analytical PIAB1D time propagation."""

import numpy as np
import pytest

from physkit.qm.piab1d import Piab1D
from physkit.qm.piab1d.tdse_analytical import (
    Piab1dTdseAnalyticalResults,
    Piab1dTdseAnalyticalSolver,
)
from physkit.qm.piab1d.tise_analytical import Piab1DAnalyticalSolution
from physkit.units import (
    ComplexVectorQuantity,
    PhysicalUnit,
    UnitSystem,
    Unitless,
    VectorQuantity,
)


def test_applies_exact_spectral_phases_and_conserves_norm() -> None:
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)
    tise = Piab1DAnalyticalSolution(model).evaluate(2)
    initial = ComplexVectorQuantity(
        np.array([1.0, 1.0j]) / np.sqrt(2.0),
        Unitless(),
    )
    times = VectorQuantity(np.array([0.0, 0.1, 0.3]), Unitless())

    results = Piab1dTdseAnalyticalSolver().solve(tise, initial, times)

    expected = initial.magnitude[:, np.newaxis] * np.exp(
        -1.0j
        * np.outer(tise.energies.magnitude, times.magnitude)
        / model.hbar_quantity.magnitude
    )
    assert isinstance(results, Piab1dTdseAnalyticalResults)
    np.testing.assert_allclose(results.coefficients.magnitude, expected)
    np.testing.assert_allclose(results.norms.magnitude, 1.0)
    assert not results.coefficients.magnitude.flags.writeable


def test_converts_physical_times_before_phase_evaluation() -> None:
    model = Piab1D(10.0, 5.485_799_090_65e-4, UnitSystem.METAL)
    tise = Piab1DAnalyticalSolution(model).evaluate(1)
    initial = ComplexVectorQuantity(np.array([1.0 + 0.0j]), Unitless())

    results = Piab1dTdseAnalyticalSolver().solve(
        tise,
        initial,
        VectorQuantity(
            np.array([0.0, 100.0]),
            PhysicalUnit("femtosecond"),
        ),
    )

    np.testing.assert_allclose(results.times.magnitude, [0.0, 0.1])
    assert results.times.unit == PhysicalUnit("picosecond")
    expected = np.exp(
        -1.0j
        * tise.energies.magnitude[0]
        * 0.1
        / model.hbar_quantity.magnitude
    )
    np.testing.assert_allclose(results.coefficients.magnitude[0, 1], expected)


def test_rejects_invalid_initial_state_and_times() -> None:
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)
    tise = Piab1DAnalyticalSolution(model).evaluate(2)
    solver = Piab1dTdseAnalyticalSolver()

    with pytest.raises(ValueError, match="normalized"):
        solver.solve(
            tise,
            ComplexVectorQuantity(np.array([1.0, 1.0]), Unitless()),
            VectorQuantity(np.array([0.0]), Unitless()),
        )
    with pytest.raises(ValueError, match="begin at zero"):
        solver.solve(
            tise,
            ComplexVectorQuantity(np.array([1.0, 0.0]), Unitless()),
            VectorQuantity(np.array([0.1]), Unitless()),
        )
    with pytest.raises(ValueError, match="nondecreasing"):
        solver.solve(
            tise,
            ComplexVectorQuantity(np.array([1.0, 0.0]), Unitless()),
            VectorQuantity(np.array([0.0, 0.2, 0.1]), Unitless()),
        )
