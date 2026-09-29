"""Numerical verification for dimensionless periodic 2D Cahn--Hilliard evolution."""

import numpy as np

from projectkoios.physkit.solidstate.phase_field.cahn_hilliard.base import (
    DimensionlessCahnHilliardParameters,
)
from projectkoios.physkit.solidstate.phase_field.cahn_hilliard.two_dimensional.model import (  # noqa: E501
    DimensionlessPeriodicCahnHilliard2DModel,
    DimensionlessPeriodicCahnHilliard2DState,
)
from projectkoios.physkit.units import MatrixQuantity, ScalarQuantity, Unitless


class TestDimensionlessPeriodicCahnHilliard2DModel:
    """Verify constant solutions and discrete conservation on rectangles."""

    @staticmethod
    def _model() -> DimensionlessPeriodicCahnHilliard2DModel:
        """Construct one bounded reduced model for this evidence owner."""
        return DimensionlessPeriodicCahnHilliard2DModel(
            parameters=DimensionlessCahnHilliardParameters(
                mobility=ScalarQuantity(magnitude=1.0, unit=Unitless()),
                gradient_penalty=ScalarQuantity(
                    magnitude=1.0e-2,
                    unit=Unitless(),
                ),
                time_step=ScalarQuantity(magnitude=1.0e-5, unit=Unitless()),
            )
        )

    def test_solve_preserves_a_constant_rectangular_field(self) -> None:
        """A uniform field is stationary on a non-square periodic grid."""
        initial = DimensionlessPeriodicCahnHilliard2DState(
            field_values=MatrixQuantity(
                magnitude=np.full((8, 12), -0.2, dtype=np.float64),
                unit=Unitless(),
            ),
            domain_length_x=ScalarQuantity(magnitude=1.0, unit=Unitless()),
            domain_length_y=ScalarQuantity(magnitude=1.5, unit=Unitless()),
        )

        solution = self._model().solve(
            initial_state=initial,
            step_count=5,
            snapshot_stride=3,
        )

        assert solution.step_indices == (0, 3, 5)
        assert np.array_equal(
            solution.final_state.field_values.magnitude,
            initial.field_values.magnitude,
        )

    def test_solve_conserves_the_discrete_periodic_mean(self) -> None:
        """The two-dimensional zero Fourier mode remains fixed."""
        generator = np.random.default_rng(20260930)
        values = 0.05 * generator.standard_normal((24, 32))
        initial = DimensionlessPeriodicCahnHilliard2DState(
            field_values=MatrixQuantity(
                magnitude=np.asarray(values, dtype=np.float64),
                unit=Unitless(),
            ),
            domain_length_x=ScalarQuantity(magnitude=1.0, unit=Unitless()),
            domain_length_y=ScalarQuantity(magnitude=1.25, unit=Unitless()),
        )

        solution = self._model().solve(
            initial_state=initial,
            step_count=100,
            snapshot_stride=25,
        )

        assert np.isclose(
            solution.final_state.mean_field.magnitude,
            initial.mean_field.magnitude,
            rtol=0.0,
            atol=2.0e-15,
        )
