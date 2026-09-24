"""Verification of ``Piab1dTiseFdSolver.solve``."""

import numpy as np
import pytest

from physkit.core.results import ResultsObject
from physkit.qm.piab1d.tise_fd import (
    Piab1dTiseFdResults,
    Piab1dTiseFdSolver,
)
from physkit.qm.piab1d.base import Piab1D
from physkit.units import PhysicalUnit, UnitSystem, Unitless


def test_solves_nondimensional_dirichlet_box() -> None:
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)

    results = Piab1dTiseFdSolver().solve(model, 3)

    assert isinstance(results, ResultsObject)
    assert isinstance(results, Piab1dTiseFdResults)
    np.testing.assert_array_equal(
        results.hamiltonian.to_dense().magnitude,
        np.array(
            [
                [16.0, -8.0, 0.0],
                [-8.0, 16.0, -8.0],
                [0.0, -8.0, 16.0],
            ]
        ),
    )
    assert isinstance(results.hamiltonian.unit, Unitless)


def test_solves_in_native_metal_units_without_si_scaled_matrix() -> None:
    model = Piab1D(
        10.0,
        5.485_799_090_65e-4,
        UnitSystem.METAL,
    )

    results = Piab1dTiseFdSolver().solve(model, 8)

    assert results.grid_spacing.unit == PhysicalUnit("angstrom")
    assert results.hamiltonian.unit == PhysicalUnit("electron_volt")
    assert results.energies.unit == PhysicalUnit("electron_volt")
    assert np.max(np.abs(results.hamiltonian.data)) < 20.0
    np.testing.assert_allclose(
        results.energies.magnitude,
        results.closed_form_discrete_energies().magnitude,
        rtol=64.0 * np.finfo(np.float64).eps,
        atol=0.0,
    )


def test_validates_model_and_interior_point_count() -> None:
    solver = Piab1dTiseFdSolver()
    model = Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL)

    with pytest.raises(TypeError, match="Piab1D"):
        solver.solve(object(), 3)  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="built-in int"):
        solver.solve(model, True)
    with pytest.raises(ValueError, match="positive"):
        solver.solve(model, 0)
