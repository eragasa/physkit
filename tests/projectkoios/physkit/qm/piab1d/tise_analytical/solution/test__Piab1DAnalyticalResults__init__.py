"""Verification of ``Piab1DAnalyticalResults`` correlation."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab1d.base import Piab1D
from projectkoios.physkit.qm.piab1d.tise_analytical import (
    Piab1DAnalyticalResults,
)
from projectkoios.physkit.units import Unitless, UnitSystem, VectorQuantity


class TestPiab1DAnalyticalResultsInit:
    """Own the cohesive evidence in this module."""

    def test_retains_immutable_correlated_results(self) -> None:
        model = Piab1D(length=1.0, mass=1.0, unit_system=UnitSystem.NONDIMENSIONAL)
        results = Piab1DAnalyticalResults(
            model=model,
            quantum_numbers=np.array([1, 2]),
            energies=VectorQuantity(magnitude=np.array([1.0, 4.0]), unit=Unitless()),
        )

        assert results.model is model
        assert not results.quantum_numbers.flags.writeable
        assert not results.energies.magnitude.flags.writeable

    def test_rejects_uncorrelated_shapes(self) -> None:
        model = Piab1D(length=1.0, mass=1.0, unit_system=UnitSystem.NONDIMENSIONAL)

        with pytest.raises(ValueError, match="match"):
            Piab1DAnalyticalResults(
                model=model,
                quantum_numbers=np.array([1, 2]),
                energies=VectorQuantity(magnitude=np.array([1.0]), unit=Unitless()),
            )
