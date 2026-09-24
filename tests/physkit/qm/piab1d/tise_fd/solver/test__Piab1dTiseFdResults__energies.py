"""Verification of PIAB1D result accessors."""

import numpy as np

from physkit.qm.piab1d.base import Piab1D
from physkit.qm.piab1d.tise_fd import Piab1dTiseFdSolver
from physkit.units import UnitSystem


def test_exposes_correlated_eigenpair_quantities() -> None:
    results = Piab1dTiseFdSolver().solve(
        Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL),
        3,
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
