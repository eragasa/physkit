r"""Townsend avalanche and secondary-emission current evaluators.

The represented model uses SI current, length, and inverse-length magnitudes.
The closed-form, generational, and fixed-point evaluators share one immutable
state and one correlated result representation.
"""

import math
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TownsendDischargeState:
    """Represent parameters for the Townsend secondary-emission current model.

    Parameters
    ----------
    primary_current_amperes
        Nonnegative finite built-in float primary current in amperes.
    first_townsend_coefficient_per_metre
        Nonnegative finite built-in float first Townsend ionization coefficient
        in reciprocal metres.
    gap_length_metres
        Nonnegative finite built-in float discharge-gap length in metres.
    secondary_emission_coefficient
        Nonnegative finite built-in float dimensionless secondary-emission
        coefficient.
    """

    primary_current_amperes: float
    first_townsend_coefficient_per_metre: float
    gap_length_metres: float
    secondary_emission_coefficient: float

    def __post_init__(self) -> None:
        """Validate exact scalar types and nonnegative finite magnitudes."""
        self._validate_nonnegative_finite_float(
            self.primary_current_amperes, "primary_current_amperes"
        )
        self._validate_nonnegative_finite_float(
            self.first_townsend_coefficient_per_metre,
            "first_townsend_coefficient_per_metre",
        )
        self._validate_nonnegative_finite_float(
            self.gap_length_metres, "gap_length_metres"
        )
        self._validate_nonnegative_finite_float(
            self.secondary_emission_coefficient,
            "secondary_emission_coefficient",
        )

    @staticmethod
    def _validate_nonnegative_finite_float(value: float, name: str) -> None:
        if type(value) is not float:
            raise TypeError(f"{name} must be a built-in float")
        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite")
        if value < 0.0:
            raise ValueError(f"{name} must be nonnegative")

    @property
    def avalanche_gain(self) -> float:
        r"""Return $\exp(\alpha d)$, or positive infinity after overflow."""
        exponent = self.first_townsend_coefficient_per_metre * self.gap_length_metres
        try:
            return math.exp(exponent)
        except OverflowError:
            return math.inf

    @property
    def feedback_factor(self) -> float:
        r"""Return the dimensionless factor $\gamma_e(M-1)$."""
        if self.secondary_emission_coefficient == 0.0:
            return 0.0
        return self.secondary_emission_coefficient * (self.avalanche_gain - 1.0)


@dataclass(frozen=True, slots=True)
class TownsendCurrentResult:
    """Record one Townsend-current evaluation outcome."""

    current_amperes: float
    avalanche_gain: float
    feedback_factor: float
    term_count: int
    converged: bool

    def __post_init__(self) -> None:
        """Validate the closed result representation."""
        if type(self.current_amperes) is not float:
            raise TypeError("current_amperes must be a built-in float")
        if type(self.avalanche_gain) is not float:
            raise TypeError("avalanche_gain must be a built-in float")
        if type(self.feedback_factor) is not float:
            raise TypeError("feedback_factor must be a built-in float")
        if type(self.term_count) is not int:
            raise TypeError("term_count must be a built-in integer")
        if self.term_count < 0:
            raise ValueError("term_count must be nonnegative")
        if type(self.converged) is not bool:
            raise TypeError("converged must be a built-in boolean")


@dataclass(frozen=True, slots=True)
class TownsendClosedFormCurrentEvaluator:
    """Evaluate the closed-form Townsend secondary-emission current."""

    def execute(self, state: TownsendDischargeState) -> TownsendCurrentResult:
        """Return the closed-form current or the represented breakdown outcome."""
        if type(state) is not TownsendDischargeState:
            raise TypeError("state must be TownsendDischargeState")

        gain = state.avalanche_gain
        feedback = state.feedback_factor
        if feedback >= 1.0:
            return TownsendCurrentResult(
                current_amperes=math.inf,
                avalanche_gain=gain,
                feedback_factor=feedback,
                term_count=0,
                converged=False,
            )
        if state.primary_current_amperes == 0.0:
            current = 0.0
        else:
            current = state.primary_current_amperes * gain / (1.0 - feedback)
        return TownsendCurrentResult(
            current_amperes=float(current),
            avalanche_gain=gain,
            feedback_factor=feedback,
            term_count=0,
            converged=True,
        )


@dataclass(frozen=True, slots=True)
class TownsendGenerationalCurrentEvaluator:
    """Evaluate Townsend current by accumulating secondary-emission generations.

    Parameters
    ----------
    relative_tolerance
        Positive finite built-in float stopping tolerance for the newest
        generation relative to accumulated current.
    maximum_iterations
        Positive built-in integer number of secondary generations attempted
        after the primary avalanche term.
    apply_tail_correction
        Exact built-in boolean selecting analytic correction of the geometric
        tail after convergence.
    """

    relative_tolerance: float = 1e-12
    maximum_iterations: int = 10_000
    apply_tail_correction: bool = True

    def __post_init__(self) -> None:
        """Validate numerical-policy fields."""
        if type(self.relative_tolerance) is not float:
            raise TypeError("relative_tolerance must be a built-in float")
        if not math.isfinite(self.relative_tolerance):
            raise ValueError("relative_tolerance must be finite")
        if self.relative_tolerance <= 0.0:
            raise ValueError("relative_tolerance must be positive")
        if type(self.maximum_iterations) is not int:
            raise TypeError("maximum_iterations must be a built-in integer")
        if self.maximum_iterations <= 0:
            raise ValueError("maximum_iterations must be positive")
        if type(self.apply_tail_correction) is not bool:
            raise TypeError("apply_tail_correction must be a built-in boolean")

    def execute(self, state: TownsendDischargeState) -> TownsendCurrentResult:
        """Return the generational current accumulation outcome."""
        if type(state) is not TownsendDischargeState:
            raise TypeError("state must be TownsendDischargeState")

        gain = state.avalanche_gain
        feedback = state.feedback_factor
        if feedback >= 1.0:
            return TownsendCurrentResult(
                current_amperes=math.inf,
                avalanche_gain=gain,
                feedback_factor=feedback,
                term_count=0,
                converged=False,
            )
        if state.primary_current_amperes == 0.0:
            return TownsendCurrentResult(
                current_amperes=0.0,
                avalanche_gain=gain,
                feedback_factor=feedback,
                term_count=1,
                converged=True,
            )

        generation_current = state.primary_current_amperes * gain
        total_current = generation_current
        term_count = 1
        converged = False
        for _ in range(self.maximum_iterations):
            generation_current *= feedback
            total_current += generation_current
            term_count += 1
            if abs(generation_current) <= self.relative_tolerance * abs(total_current):
                converged = True
                break

        if converged and self.apply_tail_correction:
            total_current += generation_current * feedback / (1.0 - feedback)
        return TownsendCurrentResult(
            current_amperes=float(total_current),
            avalanche_gain=gain,
            feedback_factor=feedback,
            term_count=term_count,
            converged=converged,
        )


@dataclass(frozen=True, slots=True)
class TownsendFixedPointCurrentEvaluator:
    """Evaluate Townsend current by fixed-point iteration.

    Parameters
    ----------
    relative_tolerance
        Positive finite built-in float stopping tolerance.
    maximum_iterations
        Positive built-in integer iteration limit.
    """

    relative_tolerance: float = 1e-12
    maximum_iterations: int = 10_000

    def __post_init__(self) -> None:
        """Validate numerical-policy fields."""
        if type(self.relative_tolerance) is not float:
            raise TypeError("relative_tolerance must be a built-in float")
        if not math.isfinite(self.relative_tolerance):
            raise ValueError("relative_tolerance must be finite")
        if self.relative_tolerance <= 0.0:
            raise ValueError("relative_tolerance must be positive")
        if type(self.maximum_iterations) is not int:
            raise TypeError("maximum_iterations must be a built-in integer")
        if self.maximum_iterations <= 0:
            raise ValueError("maximum_iterations must be positive")

    def execute(self, state: TownsendDischargeState) -> TownsendCurrentResult:
        """Return the fixed-point current iteration outcome."""
        if type(state) is not TownsendDischargeState:
            raise TypeError("state must be TownsendDischargeState")

        gain = state.avalanche_gain
        feedback = state.feedback_factor
        if feedback >= 1.0:
            return TownsendCurrentResult(
                current_amperes=math.inf,
                avalanche_gain=gain,
                feedback_factor=feedback,
                term_count=0,
                converged=False,
            )
        if state.primary_current_amperes == 0.0:
            return TownsendCurrentResult(
                current_amperes=0.0,
                avalanche_gain=gain,
                feedback_factor=feedback,
                term_count=1,
                converged=True,
            )

        current = state.primary_current_amperes * gain
        converged = False
        term_count = 0
        for _ in range(self.maximum_iterations):
            next_current = state.primary_current_amperes * gain + feedback * current
            term_count += 1
            if abs(next_current - current) <= self.relative_tolerance * max(
                1.0, abs(next_current)
            ):
                current = next_current
                converged = True
                break
            current = next_current

        return TownsendCurrentResult(
            current_amperes=float(current),
            avalanche_gain=gain,
            feedback_factor=feedback,
            term_count=term_count,
            converged=converged,
        )
