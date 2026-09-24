"""Verification of analytical PIAB1D wavefunction evaluation."""

import numpy as np

from physkit.qm.piab1d import Piab1D
from physkit.qm.piab1d.tdse_analytical import Piab1dTdseAnalyticalSolver
from physkit.qm.piab1d.tise_analytical import Piab1DAnalyticalSolution
from physkit.units import (
    ComplexVectorQuantity,
    UnitSystem,
    Unitless,
    VectorQuantity,
)


def test_evaluates_continuum_basis_and_dirichlet_boundaries() -> None:
    model = Piab1D(2.0, 1.0, UnitSystem.NONDIMENSIONAL)
    tise = Piab1DAnalyticalSolution(model).evaluate(1)
    results = Piab1dTdseAnalyticalSolver().solve(
        tise,
        ComplexVectorQuantity(np.array([1.0 + 0.0j]), Unitless()),
        VectorQuantity(np.array([0.0, 0.25]), Unitless()),
    )

    wavefunctions = results.wavefunctions(
        VectorQuantity(np.array([0.0, 1.0, 2.0]), Unitless())
    )

    assert wavefunctions.magnitude.shape == (3, 2)
    np.testing.assert_allclose(wavefunctions.magnitude[[0, 2], :], 0.0, atol=1e-15)
    np.testing.assert_allclose(wavefunctions.magnitude[1, 0], 1.0)
    assert isinstance(wavefunctions.unit, Unitless)
