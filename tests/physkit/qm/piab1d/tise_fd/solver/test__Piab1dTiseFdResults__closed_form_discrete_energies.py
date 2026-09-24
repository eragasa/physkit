"""Verification of the PIAB1D closed-form discrete spectrum."""

import numpy as np

from physkit.qm.piab1d.base import Piab1D
from physkit.qm.piab1d.tise_fd import Piab1dTiseFdSolver
from physkit.units import UnitSystem


def test_matches_nondimensional_centered_difference_formula() -> None:
    results = Piab1dTiseFdSolver().solve(
        Piab1D(1.0, 1.0, UnitSystem.NONDIMENSIONAL),
        3,
    )
    indices = np.array([1.0, 2.0, 3.0])

    np.testing.assert_array_equal(
        results.closed_form_discrete_energies().magnitude,
        32.0 * np.sin(indices * np.pi / 8.0) ** 2,
    )
