"""Tests for generational Townsend-current evaluation."""

import math

import pytest

from projectkoios.physkit.plasmas.gas_discharge.townsend import (
    TownsendClosedFormCurrentEvaluator,
    TownsendDischargeState,
    TownsendGenerationalCurrentEvaluator,
)


class TestTownsendGenerationalCurrentEvaluatorExecute:
    """Verify geometric generation accumulation and stopping behavior."""

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

    def test__execute__tail_corrected_current_matches_closed_form(self) -> None:
        state = self.state()
        expected = TownsendClosedFormCurrentEvaluator().execute(state)
        evaluator = TownsendGenerationalCurrentEvaluator(relative_tolerance=1e-14)

        result = evaluator.execute(state)

        assert result.current_amperes == pytest.approx(
            expected.current_amperes, rel=2e-15
        )
        assert result.term_count > 1
        assert result.converged is True

    def test__execute__uncorrected_sum_converges_to_requested_tolerance(self) -> None:
        state = self.state()
        expected = TownsendClosedFormCurrentEvaluator().execute(state)
        evaluator = TownsendGenerationalCurrentEvaluator(
            relative_tolerance=1e-10,
            apply_tail_correction=False,
        )

        result = evaluator.execute(state)

        assert result.current_amperes == pytest.approx(
            expected.current_amperes, rel=2e-10
        )
        assert result.converged is True

    def test__execute__reports_iteration_limit(self) -> None:
        evaluator = TownsendGenerationalCurrentEvaluator(
            relative_tolerance=1e-16,
            maximum_iterations=1,
        )

        result = evaluator.execute(self.state())

        assert result.term_count == 2
        assert result.converged is False

    def test__execute__returns_zero_for_zero_primary_current(self) -> None:
        result = TownsendGenerationalCurrentEvaluator().execute(
            self.state(primary_current=0.0)
        )

        assert result.current_amperes == 0.0
        assert result.term_count == 1
        assert result.converged is True

    def test__execute__marks_breakdown_threshold(self) -> None:
        result = TownsendGenerationalCurrentEvaluator().execute(
            self.state(secondary_emission=0.2)
        )

        assert math.isinf(result.current_amperes)
        assert result.term_count == 0
        assert result.converged is False

    def test__execute__rejects_non_state(self) -> None:
        with pytest.raises(TypeError, match="state must be TownsendDischargeState"):
            TownsendGenerationalCurrentEvaluator().execute(None)  # type: ignore[arg-type]
