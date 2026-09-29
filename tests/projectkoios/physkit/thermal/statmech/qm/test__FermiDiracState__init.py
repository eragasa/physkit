"""Construction tests for ``FermiDiracState``."""

import pytest

from projectkoios.physkit.thermal.statmech.qm import FermiDiracState
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity


class TestFermiDiracStateInit:
    """Verify the explicit shared-energy-unit contract."""

    def test__init__retains_positive_thermal_energy_and_chemical_potential(
        self,
    ) -> None:
        unit = PhysicalUnit(expression="electron_volt")
        state = FermiDiracState(
            thermal_energy=ScalarQuantity(magnitude=0.025, unit=unit),
            chemical_potential=ScalarQuantity(magnitude=1.5, unit=unit),
        )

        assert state.thermal_energy.magnitude == 0.025
        assert state.chemical_potential.magnitude == 1.5

    def test__init__rejects_nonpositive_thermal_energy(self) -> None:
        unit = PhysicalUnit(expression="joule")

        with pytest.raises(ValueError, match="thermal_energy must be positive"):
            FermiDiracState(
                thermal_energy=ScalarQuantity(magnitude=0.0, unit=unit),
                chemical_potential=ScalarQuantity(magnitude=0.0, unit=unit),
            )

    def test__init__rejects_different_energy_units(self) -> None:
        with pytest.raises(ValueError, match="must use the same unit"):
            FermiDiracState(
                thermal_energy=ScalarQuantity(
                    magnitude=1.0,
                    unit=PhysicalUnit(expression="joule"),
                ),
                chemical_potential=ScalarQuantity(
                    magnitude=1.0,
                    unit=PhysicalUnit(expression="electron_volt"),
                ),
            )
