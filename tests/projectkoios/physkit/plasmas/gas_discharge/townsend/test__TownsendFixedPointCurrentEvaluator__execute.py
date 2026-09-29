"""Tests for fixed-point Townsend-current evaluation."""

import math

import pytest

from projectkoios.physkit.plasmas.gas_discharge.townsend import (
    TownsendClosedFormCurrentEvaluator,
    TownsendDischargeState,
    TownsendFixedPointCurrentEvaluator,
)


class TestTownsendFixedPointCurrentEvaluatorExecute:
    """Verify fixed-point convergence and threshold behavior."""

    @staticmethod
    def state(
        *, primary_current: float = 1e-12, secondary_emission: float = 0.02
    ) -> TownsendDischargeState:
        """Return the shared synthetic discharge state."""
        return TownsendDischargeState(
            primary_current_amperes=primary_current,
            first_townsend_coefficient_per_metre=200.0,
            gap_length_metres=0.01,
            secondary_emission_coefficient=secondary_emission,
        )

    def test__execute__converges_to_closed_form(self) -> None:
        state = self.state()
        expected = TownsendClosedFormCurrentEvaluator().execute(state)
        evaluator = TownsendFixedPointCurrentEvaluator(relative_tolerance=1e-18)

        result = evaluator.execute(state)

        assert result.current_amperes == pytest.approx(
            expected.current_amperes, rel=2e-6
        )
        assert result.term_count > 1
        assert result.converged is True

    def test__execute__reports_iteration_limit(self) -> None:
        evaluator = TownsendFixedPointCurrentEvaluator(
            relative_tolerance=1e-18,
            maximum_iterations=1,
        )

        result = evaluator.execute(self.state())

        assert result.term_count == 1
        assert result.converged is False

    def test__execute__returns_zero_for_zero_primary_current(self) -> None:
        result = TownsendFixedPointCurrentEvaluator().execute(
            self.state(primary_current=0.0)
        )

        assert result.current_amperes == 0.0
        assert result.term_count == 1
        assert result.converged is True

    def test__execute__marks_breakdown_threshold(self) -> None:
        result = TownsendFixedPointCurrentEvaluator().execute(
            self.state(secondary_emission=0.2)
        )

        assert math.isinf(result.current_amperes)
        assert result.term_count == 0
        assert result.converged is False

    def test__execute__rejects_non_state(self) -> None:
        with pytest.raises(TypeError, match="state must be TownsendDischargeState"):
            TownsendFixedPointCurrentEvaluator().execute(None)  # type: ignore[arg-type]
