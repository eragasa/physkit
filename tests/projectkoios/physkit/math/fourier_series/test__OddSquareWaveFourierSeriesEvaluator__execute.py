"""Evaluation tests for ``OddSquareWaveFourierSeriesEvaluator``."""

import numpy as np
import pytest
from numpy.typing import NDArray

from projectkoios.physkit.math.fourier_series import (
    OddSquareWaveFourierSeriesEvaluator,
)


class TestOddSquareWaveFourierSeriesEvaluatorExecute:
    """Verify the represented finite odd-harmonic sum."""

    def test__execute__matches_one_term_formula(self) -> None:
        angles = np.array([-np.pi / 2.0, 0.0, np.pi / 2.0], dtype=np.float64)
        evaluator = OddSquareWaveFourierSeriesEvaluator(term_count=1)

        result = evaluator.execute(angles)

        expected = (4.0 / np.pi) * np.sin(angles)
        np.testing.assert_allclose(result, expected, rtol=0.0, atol=1e-15)

    def test__execute__matches_independent_three_term_sum(self) -> None:
        angles = np.array([[-1.25, -0.3], [0.4, 1.1]], dtype=np.float64)
        before = angles.copy()
        evaluator = OddSquareWaveFourierSeriesEvaluator(term_count=3)

        result = evaluator.execute(angles)

        expected = (4.0 / np.pi) * (
            np.sin(angles) + np.sin(3.0 * angles) / 3.0 + np.sin(5.0 * angles) / 5.0
        )
        np.testing.assert_allclose(result, expected, rtol=0.0, atol=1e-15)
        np.testing.assert_array_equal(angles, before)
        assert result.shape == angles.shape
        assert result.dtype == np.dtype(np.float64)
        assert not np.shares_memory(result, angles)

    @pytest.mark.parametrize(
        "angles",
        [
            np.array([0.0], dtype=np.float32),
            np.array([0], dtype=np.int64),
            np.array([False], dtype=np.bool_),
        ],
        ids=["float32", "int64", "boolean"],
    )
    def test__execute__rejects_non_float64_array(
        self,
        angles: NDArray[np.float32] | NDArray[np.int64] | NDArray[np.bool_],
    ) -> None:
        evaluator = OddSquareWaveFourierSeriesEvaluator(term_count=2)

        with pytest.raises(TypeError, match="float64 dtype"):
            evaluator.execute(angles)  # type: ignore[arg-type]

    @pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
    def test__execute__rejects_nonfinite_angles(self, value: float) -> None:
        evaluator = OddSquareWaveFourierSeriesEvaluator(term_count=2)
        angles = np.array([value], dtype=np.float64)

        with pytest.raises(ValueError, match="only finite values"):
            evaluator.execute(angles)

    def test__execute__rejects_nonarray_input(self) -> None:
        evaluator = OddSquareWaveFourierSeriesEvaluator(term_count=2)

        with pytest.raises(TypeError, match="NumPy array"):
            evaluator.execute([0.0])  # type: ignore[arg-type]
