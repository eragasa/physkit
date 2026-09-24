"""Verification of finite-difference PIAB1D sampled wavefunctions."""

import numpy as np

from physkit.qm.piab1d import Piab1D
from physkit.qm.piab1d.tdse_fd import Piab1dTdseFdSolver
from physkit.qm.piab1d.tise_fd import Piab1dTiseFdSolver
from physkit.units import (
    ComplexVectorQuantity,
    PhysicalUnit,
    UnitSystem,
    Unitless,
    VectorQuantity,
)


def test_converts_discrete_amplitudes_to_spacing_normalized_samples() -> None:
    model = Piab1D(10.0, 5.485_799_090_65e-4, UnitSystem.METAL)
    tise = Piab1dTiseFdSolver().solve(model, 4)
    initial = ComplexVectorQuantity(
        tise.eigenvectors.magnitude[:, 0].astype(np.complex128),
        Unitless(),
    )
    results = Piab1dTdseFdSolver().solve(
        tise,
        initial,
        VectorQuantity(np.array([0.0, 0.1]), PhysicalUnit("picosecond")),
    )

    wavefunctions = results.sampled_wavefunctions
    weighted_norms = (
        tise.grid_spacing.magnitude
        * np.sum(np.abs(wavefunctions.magnitude) ** 2, axis=0)
    )

    np.testing.assert_allclose(weighted_norms, 1.0)
    assert wavefunctions.unit == PhysicalUnit("(angstrom) ** -0.5")
    assert results.times.unit == PhysicalUnit("picosecond")
