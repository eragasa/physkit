"""Construction tests for ``AntoineTemperatureRange``."""

import pytest

from projectkoios.physkit.thermal.thermo.vaporpressure.antoine import (
    AntoineTemperatureRange,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity


class TestAntoineTemperatureRangeInit:
    """Verify compatible physical temperature bounds and affine conversion."""

    def test__init_correlates_compatible_units_in_kelvin(self) -> None:
        validity_range = AntoineTemperatureRange(
            lower=ScalarQuantity(
                magnitude=26.85,
                unit=PhysicalUnit(expression="degree_Celsius"),
            ),
            upper=ScalarQuantity(
                magnitude=400.0,
                unit=PhysicalUnit(expression="kelvin"),
            ),
        )

        assert validity_range.lower_in_kelvin.magnitude == pytest.approx(300.0)
        assert validity_range.upper_in_kelvin.magnitude == 400.0

    def test__init_rejects_nonincreasing_bounds(self) -> None:
        kelvin = PhysicalUnit(expression="kelvin")

        with pytest.raises(ValueError, match="upper must be greater than lower"):
            AntoineTemperatureRange(
                lower=ScalarQuantity(magnitude=400.0, unit=kelvin),
                upper=ScalarQuantity(magnitude=300.0, unit=kelvin),
            )
