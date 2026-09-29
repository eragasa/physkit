"""Verification of PIAB1D result accessors."""

import numpy as np

from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.qm.piab1d.tise_fd import Piab1dTiseFdSolver
from projectkoios.physkit.units import UnitSystem


class TestPiab1dTiseFdResultsEnergies:
    """Own the cohesive evidence in this module."""

    def test_exposes_correlated_eigenpair_quantities(self) -> None:
        results = Piab1dTiseFdSolver().solve(
            model=Piab1D(length=1.0, mass=1.0, unit_system=UnitSystem.NONDIMENSIONAL),
            interior_points=3,
        )

        np.testing.assert_array_equal(
            results.energies.magnitude,
            results.eigenpairs.eigenvalues,
        )
        np.testing.assert_array_equal(
            results.eigenvectors.magnitude,
            results.eigenpairs.eigenvectors,
        )
        assert results.interior_points == 3
        assert results.grid_spacing.magnitude == 0.25
