"""Verification of finite-difference PIAB1D time propagation."""

import numpy as np
import pytest

from physkit.qm.piab1d import Piab1D
from physkit.qm.piab1d.tdse_fd import Piab1dTdseFdResults, Piab1dTdseFdSolver
from physkit.qm.piab1d.tise_fd import Piab1dTiseFdSolver
from physkit.units import ComplexVectorQuantity, UnitSystem, Unitless, VectorQuantity


def test_propagates_eigenstate_by_global_phase() -> None:
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)
    tise = Piab1dTiseFdSolver().solve(model, 5)
    initial = ComplexVectorQuantity(
        tise.eigenvectors.magnitude[:, 0].astype(np.complex128),
        Unitless(),
    )
    times = VectorQuantity(np.array([0.0, 0.1, 0.2]), Unitless())

    results = Piab1dTdseFdSolver().solve(tise, initial, times)

    phases = np.exp(
        -1.0j
        * tise.energies.magnitude[0]
        * times.magnitude
        / model.hbar_quantity.magnitude
    )
    expected = initial.magnitude[:, np.newaxis] * phases
    assert isinstance(results, Piab1dTdseFdResults)
    np.testing.assert_allclose(results.states.magnitude, expected, atol=2e-15)
    np.testing.assert_allclose(results.norms.magnitude, 1.0, atol=2e-15)
    np.testing.assert_allclose(
        results.energy_expectations.magnitude,
        tise.energies.magnitude[0],
        atol=2e-14,
    )


def test_rejects_invalid_coordinate_state() -> None:
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)
    tise = Piab1dTiseFdSolver().solve(model, 3)
    solver = Piab1dTdseFdSolver()
    times = VectorQuantity(np.array([0.0]), Unitless())

    with pytest.raises(ValueError, match="interior grid"):
        solver.solve(
            tise,
            ComplexVectorQuantity(np.array([1.0, 0.0]), Unitless()),
            times,
        )
    with pytest.raises(ValueError, match="normalized"):
        solver.solve(
            tise,
            ComplexVectorQuantity(np.ones(3), Unitless()),
            times,
        )
