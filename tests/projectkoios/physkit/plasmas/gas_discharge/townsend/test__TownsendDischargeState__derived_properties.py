"""Derived-property tests for ``TownsendDischargeState``."""

import math

import pytest

from projectkoios.physkit.plasmas.gas_discharge.townsend import (
    TownsendDischargeState,
)


class TestTownsendDischargeStateDerivedProperties:
    """Verify avalanche gain and secondary-emission feedback."""

    def test__derived_properties__match_represented_formulas(self) -> None:
        state = TownsendDischargeState(
            primary_current_amperes=1e-12,
            first_townsend_coefficient_per_metre=200.0,
            gap_length_metres=0.01,
            secondary_emission_coefficient=0.02,
        )

        expected_gain = math.exp(2.0)
        assert state.avalanche_gain == pytest.approx(expected_gain, rel=1e-15)
        assert state.feedback_factor == pytest.approx(
            0.02 * (expected_gain - 1.0), rel=1e-15
        )

    def test__feedback_factor__is_zero_when_secondary_emission_is_zero(self) -> None:
        state = TownsendDischargeState(
            primary_current_amperes=1e-12,
            first_townsend_coefficient_per_metre=1000.0,
            gap_length_metres=1.0,
            secondary_emission_coefficient=0.0,
        )

        assert math.isinf(state.avalanche_gain)
        assert state.feedback_factor == 0.0
