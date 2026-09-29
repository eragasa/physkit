"""Verification of analytical PIAB1D time propagation."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab1d import Piab1D
from projectkoios.physkit.qm.piab1d.tdse_analytical import (
    Piab1dTdseAnalyticalResults,
    Piab1dTdseAnalyticalSolver,
)
from projectkoios.physkit.qm.piab1d.tise_analytical import Piab1DAnalyticalSolution
from projectkoios.physkit.units import (
    ComplexVectorQuantity,
    PhysicalUnit,
    Unitless,
    UnitSystem,
    VectorQuantity,
)


class TestPiab1dTdseAnalyticalSolverSolve:
    """Own the cohesive evidence in this module."""

    def test_applies_exact_spectral_phases_and_conserves_norm(self) -> None:
        model = Piab1D(length=1.0, mass=1.0, unit_system=UnitSystem.NONDIMENSIONAL)
        tise = Piab1DAnalyticalSolution(model=model).evaluate(count=2)
        initial = ComplexVectorQuantity(
            magnitude=np.array([1.0, 1.0j]) / np.sqrt(2.0), unit=Unitless()
        )
        times = VectorQuantity(magnitude=np.array([0.0, 0.1, 0.3]), unit=Unitless())

        results = Piab1dTdseAnalyticalSolver().solve(
            tise_results=tise, initial_coefficients=initial, times=times
        )

        expected = initial.magnitude[:, np.newaxis] * np.exp(
            -1.0j
            * np.outer(tise.energies.magnitude, times.magnitude)
            / model.hbar_quantity.magnitude
        )
        assert isinstance(results, Piab1dTdseAnalyticalResults)
        np.testing.assert_allclose(results.coefficients.magnitude, expected)
        np.testing.assert_allclose(results.norms.magnitude, 1.0)
        assert not results.coefficients.magnitude.flags.writeable

    def test_converts_physical_times_before_phase_evaluation(self) -> None:
        model = Piab1D(
            length=10.0, mass=5.485_799_090_65e-4, unit_system=UnitSystem.METAL
        )
        tise = Piab1DAnalyticalSolution(model=model).evaluate(count=1)
        initial = ComplexVectorQuantity(
            magnitude=np.array([1.0 + 0.0j]), unit=Unitless()
        )

        results = Piab1dTdseAnalyticalSolver().solve(
            tise_results=tise,
            initial_coefficients=initial,
            times=VectorQuantity(
                magnitude=np.array([0.0, 100.0]),
                unit=PhysicalUnit(expression="femtosecond"),
            ),
        )

        np.testing.assert_allclose(results.times.magnitude, [0.0, 0.1])
        assert results.times.unit == PhysicalUnit(expression="picosecond")
        expected = np.exp(
            -1.0j * tise.energies.magnitude[0] * 0.1 / model.hbar_quantity.magnitude
        )
        np.testing.assert_allclose(results.coefficients.magnitude[0, 1], expected)

    def test_rejects_invalid_initial_state_and_times(self) -> None:
        model = Piab1D(length=1.0, mass=1.0, unit_system=UnitSystem.NONDIMENSIONAL)
        tise = Piab1DAnalyticalSolution(model=model).evaluate(count=2)
        solver = Piab1dTdseAnalyticalSolver()

        with pytest.raises(ValueError, match="normalized"):
            solver.solve(
                tise_results=tise,
                initial_coefficients=ComplexVectorQuantity(
                    magnitude=np.array([1.0, 1.0]), unit=Unitless()
                ),
                times=VectorQuantity(magnitude=np.array([0.0]), unit=Unitless()),
            )
        with pytest.raises(ValueError, match="begin at zero"):
            solver.solve(
                tise_results=tise,
                initial_coefficients=ComplexVectorQuantity(
                    magnitude=np.array([1.0, 0.0]), unit=Unitless()
                ),
                times=VectorQuantity(magnitude=np.array([0.1]), unit=Unitless()),
            )
        with pytest.raises(ValueError, match="nondecreasing"):
            solver.solve(
                tise_results=tise,
                initial_coefficients=ComplexVectorQuantity(
                    magnitude=np.array([1.0, 0.0]), unit=Unitless()
                ),
                times=VectorQuantity(
                    magnitude=np.array([0.0, 0.2, 0.1]), unit=Unitless()
                ),
            )
