"""Construction tests for ``TownsendFixedPointCurrentEvaluator``."""

import numpy as np
import pytest

from projectkoios.physkit.plasmas.gas_discharge.townsend import (
    TownsendFixedPointCurrentEvaluator,
)


class TestTownsendFixedPointCurrentEvaluatorInit:
    """Verify fixed-point numerical-policy fields."""

    def test__init__retains_valid_policy(self) -> None:
        evaluator = TownsendFixedPointCurrentEvaluator(
            relative_tolerance=1e-10,
            maximum_iterations=500,
        )

        assert evaluator.relative_tolerance == 1e-10
        assert evaluator.maximum_iterations == 500

    @pytest.mark.parametrize("value", [0.0, -1.0])
    def test__init__rejects_nonpositive_tolerance(self, value: float) -> None:
        with pytest.raises(ValueError, match="relative_tolerance must be positive"):
            TownsendFixedPointCurrentEvaluator(relative_tolerance=value)

    @pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
    def test__init__rejects_nonfinite_tolerance(self, value: float) -> None:
        with pytest.raises(ValueError, match="relative_tolerance must be finite"):
            TownsendFixedPointCurrentEvaluator(relative_tolerance=value)

    def test__init__rejects_nonpositive_iteration_limit(self) -> None:
        with pytest.raises(ValueError, match="maximum_iterations must be positive"):
            TownsendFixedPointCurrentEvaluator(maximum_iterations=0)

    def test__init__rejects_boolean_iteration_limit(self) -> None:
        with pytest.raises(
            TypeError, match="maximum_iterations must be a built-in integer"
        ):
            TownsendFixedPointCurrentEvaluator(  # type: ignore[arg-type]
                maximum_iterations=True
            )
