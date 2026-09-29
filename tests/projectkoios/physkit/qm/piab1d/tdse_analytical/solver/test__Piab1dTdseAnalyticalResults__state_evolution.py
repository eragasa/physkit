"""Verification of analytical PIAB1D sampled-state evolution."""

import numpy as np

from projectkoios.physkit.qm.piab1d import Piab1D
from projectkoios.physkit.qm.piab1d.tdse_analytical import Piab1dTdseAnalyticalSolver
from projectkoios.physkit.qm.piab1d.tise_analytical import Piab1DAnalyticalSolution
from projectkoios.physkit.units import (
    ComplexVectorQuantity,
    Unitless,
    UnitSystem,
    VectorQuantity,
)


class TestPiab1dTdseAnalyticalResultsStateEvolution:
    """Verify coordinate-space states in represented-time order."""

    def test__state_evolution_respects_dirichlet_boundaries(self) -> None:
        box_length = 2.0
        midpoint = box_length / 2.0
        represented_times = np.array([0.0, 0.25], dtype=np.float64)
        boundary_tolerance = 1.0e-15
        model = Piab1D(
            length=box_length,
            mass=1.0,
            unit_system=UnitSystem.NONDIMENSIONAL,
        )
        tise = Piab1DAnalyticalSolution(model=model).evaluate(count=1)
        results = Piab1dTdseAnalyticalSolver().solve(
            tise_results=tise,
            initial_coefficients=ComplexVectorQuantity(
                magnitude=np.array([1.0 + 0.0j]),
                unit=Unitless(),
            ),
            times=VectorQuantity(
                magnitude=represented_times,
                unit=Unitless(),
            ),
        )
        coordinates = VectorQuantity(
            magnitude=np.array([0.0, midpoint, box_length], dtype=np.float64),
            unit=Unitless(),
        )

        evolution = results.state_evolution(coordinates=coordinates)

        assert len(evolution) == represented_times.size
        amplitude_matrix = np.column_stack(
            tuple(state.amplitudes.magnitude for state in evolution)
        )
        np.testing.assert_allclose(
            amplitude_matrix[[0, -1], :],
            0.0,
            atol=boundary_tolerance,
        )
        np.testing.assert_allclose(amplitude_matrix[1, 0], 1.0)
        assert isinstance(next(iter(evolution)).amplitudes.unit, Unitless)
