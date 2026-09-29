"""Construction tests for ``TownsendCurrentResult``."""

import math

import pytest

from projectkoios.physkit.plasmas.gas_discharge.townsend import TownsendCurrentResult


class TestTownsendCurrentResultInit:
    """Verify the closed current-result representation."""

    def test__init__retains_converged_result(self) -> None:
        result = TownsendCurrentResult(
            current_amperes=2e-12,
            avalanche_gain=2.0,
            feedback_factor=0.1,
            term_count=4,
            converged=True,
        )

        assert result.current_amperes == 2e-12
        assert result.avalanche_gain == 2.0
        assert result.feedback_factor == 0.1
        assert result.term_count == 4
        assert result.converged is True

    def test__init__accepts_infinite_breakdown_current(self) -> None:
        result = TownsendCurrentResult(
            current_amperes=math.inf,
            avalanche_gain=100.0,
            feedback_factor=1.1,
            term_count=0,
            converged=False,
        )

        assert math.isinf(result.current_amperes)
        assert result.converged is False

    def test__init__rejects_negative_term_count(self) -> None:
        with pytest.raises(ValueError, match="term_count must be nonnegative"):
            TownsendCurrentResult(1.0, 1.0, 0.0, -1, True)

    def test__init__rejects_boolean_term_count(self) -> None:
        with pytest.raises(TypeError, match="term_count must be a built-in integer"):
            TownsendCurrentResult(1.0, 1.0, 0.0, True, True)  # type: ignore[arg-type]

    def test__init__rejects_non_boolean_convergence(self) -> None:
        with pytest.raises(TypeError, match="converged must be a built-in boolean"):
            TownsendCurrentResult(1.0, 1.0, 0.0, 1, 1)  # type: ignore[arg-type]
