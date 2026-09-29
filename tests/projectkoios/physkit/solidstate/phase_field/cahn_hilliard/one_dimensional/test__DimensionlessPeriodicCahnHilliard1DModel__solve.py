"""Numerical verification for dimensionless periodic 1D Cahn--Hilliard evolution."""

import numpy as np

from projectkoios.physkit.solidstate.phase_field.cahn_hilliard.base import (
    DimensionlessCahnHilliardParameters,
)
from projectkoios.physkit.solidstate.phase_field.cahn_hilliard.one_dimensional.model import (  # noqa: E501
    DimensionlessPeriodicCahnHilliard1DModel,
    DimensionlessPeriodicCahnHilliard1DState,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


class TestDimensionlessPeriodicCahnHilliard1DModel:
    """Verify constant solutions, snapshots, and discrete conservation."""

    @staticmethod
    def _model() -> DimensionlessPeriodicCahnHilliard1DModel:
        """Construct one bounded reduced model for this evidence owner."""
        return DimensionlessPeriodicCahnHilliard1DModel(
            parameters=DimensionlessCahnHilliardParameters(
                mobility=ScalarQuantity(magnitude=1.0, unit=Unitless()),
                gradient_penalty=ScalarQuantity(
                    magnitude=1.0e-2,
                    unit=Unitless(),
                ),
                time_step=ScalarQuantity(magnitude=1.0e-5, unit=Unitless()),
            )
        )

    def test_solve_preserves_a_constant_field_and_final_snapshot(self) -> None:
        """A uniform field is stationary and the final step is always retained."""
        initial = DimensionlessPeriodicCahnHilliard1DState(
            field_values=VectorQuantity(
                magnitude=np.full(16, 0.25, dtype=np.float64),
                unit=Unitless(),
            ),
            domain_length=ScalarQuantity(magnitude=1.0, unit=Unitless()),
        )

        solution = self._model().solve(
            initial_state=initial,
            step_count=5,
            snapshot_stride=2,
        )

        assert solution.step_indices == (0, 2, 4, 5)
        assert np.array_equal(
            solution.final_state.field_values.magnitude,
            initial.field_values.magnitude,
        )

    def test_solve_conserves_the_discrete_periodic_mean(self) -> None:
        """The zero Fourier mode remains fixed under nonlinear evolution."""
        generator = np.random.default_rng(20260930)
        values = 0.05 * generator.standard_normal(64)
        initial = DimensionlessPeriodicCahnHilliard1DState(
            field_values=VectorQuantity(
                magnitude=np.asarray(values, dtype=np.float64),
                unit=Unitless(),
            ),
            domain_length=ScalarQuantity(magnitude=1.0, unit=Unitless()),
        )

        solution = self._model().solve(
            initial_state=initial,
            step_count=200,
            snapshot_stride=50,
        )

        assert np.isclose(
            solution.final_state.mean_field.magnitude,
            initial.mean_field.magnitude,
            rtol=0.0,
            atol=2.0e-15,
        )
