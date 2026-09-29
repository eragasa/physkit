"""Construction tests for ``TownsendDischargeState``."""

import numpy as np
import pytest

from projectkoios.physkit.plasmas.gas_discharge.townsend import (
    TownsendDischargeState,
)


class TestTownsendDischargeStateInit:
    """Verify exact nonnegative finite SI parameters."""

    def test__init__retains_valid_parameters(self) -> None:
        state = TownsendDischargeState(
            primary_current_amperes=1e-12,
            first_townsend_coefficient_per_metre=200.0,
            gap_length_metres=0.01,
            secondary_emission_coefficient=0.02,
        )

        assert state.primary_current_amperes == 1e-12
        assert state.first_townsend_coefficient_per_metre == 200.0
        assert state.gap_length_metres == 0.01
        assert state.secondary_emission_coefficient == 0.02

    @pytest.mark.parametrize(
        "parameter_name",
        [
            "primary_current_amperes",
            "first_townsend_coefficient_per_metre",
            "gap_length_metres",
            "secondary_emission_coefficient",
        ],
    )
    def test__init__rejects_negative_parameter(self, parameter_name: str) -> None:
        parameters = {
            "primary_current_amperes": 1e-12,
            "first_townsend_coefficient_per_metre": 200.0,
            "gap_length_metres": 0.01,
            "secondary_emission_coefficient": 0.02,
        }
        parameters[parameter_name] = -1.0

        with pytest.raises(ValueError, match=f"{parameter_name} must be nonnegative"):
            TownsendDischargeState(**parameters)  # type: ignore[arg-type]

    @pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
    def test__init__rejects_nonfinite_parameter(self, value: float) -> None:
        with pytest.raises(ValueError, match="gap_length_metres must be finite"):
            TownsendDischargeState(
                primary_current_amperes=1e-12,
                first_townsend_coefficient_per_metre=200.0,
                gap_length_metres=value,
                secondary_emission_coefficient=0.02,
            )

    def test__init__rejects_non_float_parameter(self) -> None:
        with pytest.raises(TypeError, match="built-in float"):
            TownsendDischargeState(  # type: ignore[arg-type]
                primary_current_amperes=1,
                first_townsend_coefficient_per_metre=200.0,
                gap_length_metres=0.01,
                secondary_emission_coefficient=0.02,
            )
