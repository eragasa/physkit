"""Construction tests for ``MaxwellBoltzmannGasState``."""

import pytest

from projectkoios.physkit.thermal.statmech.kinetic_theory import (
    MaxwellBoltzmannGasState,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, Unitless


class TestMaxwellBoltzmannGasStateInit:
    """Verify explicit temperature and molar-mass unit contracts."""

    @staticmethod
    def _temperature(*, magnitude: float) -> ScalarQuantity:
        return ScalarQuantity(
            magnitude=magnitude,
            unit=PhysicalUnit(expression="kelvin"),
        )

    @staticmethod
    def _molar_mass(*, magnitude: float) -> ScalarQuantity:
        return ScalarQuantity(
            magnitude=magnitude,
            unit=PhysicalUnit(expression="kilogram / mole"),
        )

    def test__init_retains_positive_physical_quantities(self) -> None:
        temperature = self._temperature(magnitude=300.0)
        molar_mass = self._molar_mass(magnitude=0.0280134)

        state = MaxwellBoltzmannGasState(
            temperature=temperature,
            molar_mass=molar_mass,
        )

        assert state.temperature is temperature
        assert state.molar_mass is molar_mass

    def test__init_converts_compatible_temperature_and_molar_mass_units(self) -> None:
        state = MaxwellBoltzmannGasState(
            temperature=ScalarQuantity(
                magnitude=26.85,
                unit=PhysicalUnit(expression="degree_Celsius"),
            ),
            molar_mass=ScalarQuantity(
                magnitude=28.0134,
                unit=PhysicalUnit(expression="gram / mole"),
            ),
        )

        assert state.temperature_in_kelvin.magnitude == pytest.approx(300.0)
        assert state.molar_mass_in_si.magnitude == pytest.approx(0.0280134)

    @pytest.mark.parametrize(
        "temperature_kelvin",
        [0.0, -1.0],
        ids=["absolute-zero", "below-absolute-zero"],
    )
    def test__init_rejects_nonpositive_absolute_temperature(
        self,
        temperature_kelvin: float,
    ) -> None:
        with pytest.raises(ValueError, match="above absolute zero"):
            MaxwellBoltzmannGasState(
                temperature=self._temperature(magnitude=temperature_kelvin),
                molar_mass=self._molar_mass(magnitude=0.0280134),
            )

    @pytest.mark.parametrize(
        "molar_mass",
        [0.0, -1.0],
        ids=["zero", "negative"],
    )
    def test__init_rejects_nonpositive_molar_mass(self, molar_mass: float) -> None:
        with pytest.raises(ValueError, match="molar_mass must be positive"):
            MaxwellBoltzmannGasState(
                temperature=self._temperature(magnitude=300.0),
                molar_mass=self._molar_mass(magnitude=molar_mass),
            )

    def test__init_rejects_incompatible_temperature_unit(self) -> None:
        with pytest.raises(ValueError, match="compatible with temperature"):
            MaxwellBoltzmannGasState(
                temperature=ScalarQuantity(
                    magnitude=300.0,
                    unit=PhysicalUnit(expression="meter"),
                ),
                molar_mass=self._molar_mass(magnitude=0.0280134),
            )

    def test__init_rejects_unitless_molar_mass(self) -> None:
        with pytest.raises(TypeError, match="physical molar-mass unit"):
            MaxwellBoltzmannGasState(
                temperature=self._temperature(magnitude=300.0),
                molar_mass=ScalarQuantity(magnitude=0.0280134, unit=Unitless()),
            )
