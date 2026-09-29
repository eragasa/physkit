"""Numerical verification for the dimensionless QHO1D finite representation."""

import numpy as np

from projectkoios.physkit.qm.qho1d.tise.finite_difference.model import (
    DimensionlessQho1D,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless


class TestDimensionlessQho1D:
    """Verify reduced energies and continuously normalized eigenfunctions."""

    @staticmethod
    def _quantity(magnitude: float) -> ScalarQuantity:
        """Construct one unitless scalar for this evidence owner."""
        return ScalarQuantity(magnitude=magnitude, unit=Unitless())

    def test_solve_tise_finite_difference_approaches_analytical_energies(
        self,
    ) -> None:
        """The lowest represented levels approximate the continuum spectrum."""
        model = DimensionlessQho1D(
            mass=self._quantity(1.0),
            angular_frequency=self._quantity(1.0),
            hbar=self._quantity(1.0),
        )

        solution = model.solve_tise_finite_difference(
            lower_bound=self._quantity(-8.0),
            upper_bound=self._quantity(8.0),
            point_count=240,
        )
        analytical = model.analytical_energies(count=5)

        assert np.allclose(
            solution.energies.magnitude[:5],
            analytical.magnitude,
            rtol=1.3e-3,
            atol=6.0e-4,
        )

    def test_solve_tise_finite_difference_continuously_normalizes_columns(
        self,
    ) -> None:
        """Each returned eigenfunction has unit rectangular-rule norm."""
        model = DimensionlessQho1D(
            mass=self._quantity(1.0),
            angular_frequency=self._quantity(1.0),
            hbar=self._quantity(1.0),
        )

        solution = model.solve_tise_finite_difference(
            lower_bound=self._quantity(-7.0),
            upper_bound=self._quantity(7.0),
            point_count=180,
        )
        represented_norms = (
            np.sum(
                np.abs(solution.eigenfunctions.magnitude[:, :8]) ** 2,
                axis=0,
            )
            * solution.grid_spacing.magnitude
        )

        assert np.allclose(
            represented_norms,
            1.0,
            rtol=0.0,
            atol=2.0e-14,
        )
