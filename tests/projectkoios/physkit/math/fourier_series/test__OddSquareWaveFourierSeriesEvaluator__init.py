"""Construction tests for ``OddSquareWaveFourierSeriesEvaluator``."""

import numpy as np
import pytest

from projectkoios.physkit.math.fourier_series import (
    OddSquareWaveFourierSeriesEvaluator,
)


class TestOddSquareWaveFourierSeriesEvaluatorInit:
    """Verify the finite odd-harmonic truncation contract."""

    def test__init__accepts_positive_built_in_integer(self) -> None:
        evaluator = OddSquareWaveFourierSeriesEvaluator(term_count=3)

        assert evaluator.term_count == 3

    @pytest.mark.parametrize("term_count", [0, -1])
    def test__init__rejects_nonpositive_integer(self, term_count: int) -> None:
        with pytest.raises(ValueError, match="term_count must be positive"):
            OddSquareWaveFourierSeriesEvaluator(term_count=term_count)

    def test__init__rejects_boolean(self) -> None:
        with pytest.raises(TypeError, match="built-in integer"):
            OddSquareWaveFourierSeriesEvaluator(term_count=True)  # type: ignore[arg-type]

    def test__init__rejects_numpy_integer(self) -> None:
        with pytest.raises(TypeError, match="built-in integer"):
            OddSquareWaveFourierSeriesEvaluator(  # type: ignore[arg-type]
                term_count=np.int64(2)
            )
