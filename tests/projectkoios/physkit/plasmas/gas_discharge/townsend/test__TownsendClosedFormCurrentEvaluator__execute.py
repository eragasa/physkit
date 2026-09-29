"""Tests for the closed-form Townsend-current evaluator."""

import math

import pytest

from projectkoios.physkit.plasmas.gas_discharge.townsend import (
    TownsendClosedFormCurrentEvaluator,
    TownsendDischargeState,
)


class TestTownsendClosedFormCurrentEvaluatorExecute:
    """Verify closed-form current and breakdown threshold behavior."""

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

    def test__execute__matches_closed_form_current(self) -> None:
        state = self.state()

        result = TownsendClosedFormCurrentEvaluator().execute(state)

        gain = math.exp(2.0)
        feedback = 0.02 * (gain - 1.0)
        expected = 1e-12 * gain / (1.0 - feedback)
        assert result.current_amperes == pytest.approx(expected, rel=1e-15)
        assert result.avalanche_gain == pytest.approx(gain, rel=1e-15)
        assert result.feedback_factor == pytest.approx(feedback, rel=1e-15)
        assert result.term_count == 0
        assert result.converged is True

    def test__execute__returns_zero_for_zero_primary_current(self) -> None:
        result = TownsendClosedFormCurrentEvaluator().execute(
            self.state(primary_current=0.0)
        )

        assert result.current_amperes == 0.0
        assert result.converged is True

    def test__execute__marks_breakdown_threshold(self) -> None:
        result = TownsendClosedFormCurrentEvaluator().execute(
            self.state(secondary_emission=0.2)
        )

        assert math.isinf(result.current_amperes)
        assert result.feedback_factor >= 1.0
        assert result.term_count == 0
        assert result.converged is False

    def test__execute__rejects_non_state(self) -> None:
        with pytest.raises(TypeError, match="state must be TownsendDischargeState"):
            TownsendClosedFormCurrentEvaluator().execute(None)  # type: ignore[arg-type]
