"""Evaluation tests for ``OccupiedEigenfunctionDensityEvaluator``."""

import numpy as np
import pytest

from projectkoios.physkit.qm.eigenfunctions import (
    SampledEigenfunction1D,
    SampledEigenfunctions1D,
)
from projectkoios.physkit.thermal.statmech.qm import (
    OccupiedEigenfunctionDensityEvaluator,
)
from projectkoios.physkit.units import (
    ComplexVectorQuantity,
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestOccupiedEigenfunctionDensityEvaluatorEvaluate:
    """Verify occupation-weighted sampled eigenfunction densities."""

    @staticmethod
    def _eigenfunctions(
        *,
        amplitudes: np.ndarray,
        amplitude_unit: PhysicalUnit | Unitless,
    ) -> SampledEigenfunctions1D:
        coordinates = VectorQuantity(
            magnitude=np.arange(amplitudes.shape[0], dtype=np.float64),
            unit=Unitless(),
        )
        return SampledEigenfunctions1D(
            eigenfunctions=tuple(
                SampledEigenfunction1D(
                    eigenvalue=ScalarQuantity(
                        magnitude=float(index + 1),
                        unit=Unitless(),
                    ),
                    coordinates=coordinates,
                    amplitudes=ComplexVectorQuantity(
                        magnitude=amplitudes[:, index],
                        unit=amplitude_unit,
                    ),
                )
                for index in range(amplitudes.shape[1])
            )
        )

    def test__evaluate_sums_complex_eigenfunction_probability_densities(
        self,
    ) -> None:
        eigenfunctions = self._eigenfunctions(
            amplitudes=np.array(
                [
                    [1.0 + 1.0j, 2.0 + 0.0j],
                    [0.0 + 0.0j, 0.0 + 3.0j],
                ],
                dtype=np.complex128,
            ),
            amplitude_unit=PhysicalUnit(expression="meter ** -0.5"),
        )
        occupations = VectorQuantity(
            magnitude=np.array([0.25, 0.5], dtype=np.float64),
            unit=Unitless(),
        )
        evaluator = OccupiedEigenfunctionDensityEvaluator()

        evaluation = evaluator.evaluate(
            eigenfunctions=eigenfunctions,
            occupations=occupations,
        )

        assert evaluation.request.eigenfunctions is eigenfunctions
        assert evaluation.request.occupations is occupations
        np.testing.assert_allclose(
            evaluation.density.magnitude,
            np.array([2.5, 4.5], dtype=np.float64),
            rtol=0.0,
            atol=0.0,
        )
        assert evaluation.density.unit == PhysicalUnit(
            expression="(meter ** -0.5) ** 2"
        )

    def test__evaluate_rejects_occupation_count_mismatch(self) -> None:
        eigenfunctions = self._eigenfunctions(
            amplitudes=np.ones((3, 2), dtype=np.complex128),
            amplitude_unit=Unitless(),
        )

        with pytest.raises(ValueError, match="must match the eigenfunctions"):
            OccupiedEigenfunctionDensityEvaluator().evaluate(
                eigenfunctions=eigenfunctions,
                occupations=VectorQuantity(
                    magnitude=np.ones(3, dtype=np.float64),
                    unit=Unitless(),
                ),
            )

    def test__evaluate_rejects_negative_occupations(self) -> None:
        eigenfunctions = self._eigenfunctions(
            amplitudes=np.ones((3, 1), dtype=np.complex128),
            amplitude_unit=Unitless(),
        )

        with pytest.raises(ValueError, match="occupations must be nonnegative"):
            OccupiedEigenfunctionDensityEvaluator().evaluate(
                eigenfunctions=eigenfunctions,
                occupations=VectorQuantity(
                    magnitude=np.array([-1.0], dtype=np.float64),
                    unit=Unitless(),
                ),
            )
