"""Software and numerical verification for the Morse pair model."""

import numpy as np

from projectkoios.physkit.solidstate.interatomic_potentials.pair.morse.parameters import (  # noqa: E501
    MorsePotentialParameters,
)
from projectkoios.physkit.solidstate.interatomic_potentials.pair.morse.potential import (  # noqa: E501
    MorsePotential,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestMorsePotential:
    """Verify the minimum, force direction, and derivative relationship."""

    @staticmethod
    def _model(
        *,
        dissociation_energy_electron_volt: float,
        inverse_range_per_angstrom: float,
        equilibrium_distance_angstrom: float,
    ) -> MorsePotential:
        """Construct one model for this evidence owner."""
        return MorsePotential(
            parameters=MorsePotentialParameters(
                dissociation_energy=ScalarQuantity(
                    magnitude=dissociation_energy_electron_volt,
                    unit=PhysicalUnit(expression="electron_volt"),
                ),
                inverse_range=ScalarQuantity(
                    magnitude=inverse_range_per_angstrom,
                    unit=PhysicalUnit(expression="1 / angstrom"),
                ),
                equilibrium_distance=ScalarQuantity(
                    magnitude=equilibrium_distance_angstrom,
                    unit=PhysicalUnit(expression="angstrom"),
                ),
            )
        )

    def test_evaluate_has_expected_minimum_and_force_directions(self) -> None:
        """The equilibrium force vanishes between repulsive and attractive sides."""
        model = self._model(
            dissociation_energy_electron_volt=2.0,
            inverse_range_per_angstrom=1.5,
            equilibrium_distance_angstrom=2.0,
        )

        result = model.evaluate(
            distances=VectorQuantity(
                magnitude=np.asarray([1.8, 2.0, 2.2], dtype=np.float64),
                unit=PhysicalUnit(expression="angstrom"),
            ),
            energy_unit=PhysicalUnit(expression="electron_volt"),
            force_unit=PhysicalUnit(expression="electron_volt / angstrom"),
        )

        assert np.isclose(result.potential_energies.magnitude[1], -2.0)
        assert np.isclose(result.radial_forces.magnitude[1], 0.0)
        assert result.radial_forces.magnitude[0] > 0.0
        assert result.radial_forces.magnitude[2] < 0.0

    def test_radial_force_is_negative_energy_derivative(self) -> None:
        """Centered differentiation independently checks the corrected sign."""
        model = self._model(
            dissociation_energy_electron_volt=1.0,
            inverse_range_per_angstrom=2.0,
            equilibrium_distance_angstrom=1.5,
        )
        center = 1.8
        step = 1.0e-5
        result = model.evaluate(
            distances=VectorQuantity(
                magnitude=np.asarray(
                    [center - step, center, center + step],
                    dtype=np.float64,
                ),
                unit=PhysicalUnit(expression="angstrom"),
            ),
            energy_unit=PhysicalUnit(expression="electron_volt"),
            force_unit=PhysicalUnit(expression="electron_volt / angstrom"),
        )
        numerical_force = -(
            result.potential_energies.magnitude[2]
            - result.potential_energies.magnitude[0]
        ) / (2.0 * step)

        assert np.isclose(
            result.radial_forces.magnitude[1],
            numerical_force,
            rtol=5.0e-10,
            atol=0.0,
        )
