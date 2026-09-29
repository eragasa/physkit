"""Software and numerical verification for the Lennard--Jones 12-6 model."""

import numpy as np

from projectkoios.physkit.solidstate.interatomic_potentials.pair.lennard_jones_12_6.parameters import (  # noqa: E501
    LennardJonesPotentialParameters,
)
from projectkoios.physkit.solidstate.interatomic_potentials.pair.lennard_jones_12_6.potential import (  # noqa: E501
    LennardJonesPotential,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


class TestLennardJonesPotential:
    """Verify characteristic values and radial-force sign convention."""

    @staticmethod
    def _model(
        *,
        well_depth_electron_volt: float,
        zero_crossing_distance: float,
        distance_unit: str,
    ) -> LennardJonesPotential:
        """Construct one model for this evidence owner."""
        return LennardJonesPotential(
            parameters=LennardJonesPotentialParameters(
                well_depth=ScalarQuantity(
                    magnitude=well_depth_electron_volt,
                    unit=PhysicalUnit(expression="electron_volt"),
                ),
                zero_crossing_distance=ScalarQuantity(
                    magnitude=zero_crossing_distance,
                    unit=PhysicalUnit(expression=distance_unit),
                ),
            )
        )

    def test_evaluate_matches_zero_crossing_and_equilibrium_values(self) -> None:
        """The analytical zero, minimum, and force values are retained."""
        model = self._model(
            well_depth_electron_volt=2.0,
            zero_crossing_distance=0.3,
            distance_unit="nanometer",
        )
        equilibrium_nanometre = model.equilibrium_distance.magnitude

        result = model.evaluate(
            distances=VectorQuantity(
                magnitude=np.asarray(
                    [0.3, equilibrium_nanometre],
                    dtype=np.float64,
                ),
                unit=PhysicalUnit(expression="nanometer"),
            ),
            energy_unit=PhysicalUnit(expression="electron_volt"),
            force_unit=PhysicalUnit(expression="electron_volt / nanometer"),
        )

        assert np.allclose(
            result.potential_energies.magnitude,
            np.asarray([0.0, -2.0], dtype=np.float64),
            rtol=1.0e-13,
            atol=1.0e-13,
        )
        assert np.allclose(
            result.radial_forces.magnitude,
            np.asarray([160.0, 0.0], dtype=np.float64),
            rtol=1.0e-13,
            atol=1.0e-12,
        )
        assert result.request.model is model

    def test_radial_force_is_negative_energy_derivative(self) -> None:
        """Centered differentiation independently checks the force formula."""
        model = self._model(
            well_depth_electron_volt=1.0,
            zero_crossing_distance=1.0,
            distance_unit="angstrom",
        )
        center = 1.4
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
            rtol=2.0e-9,
            atol=0.0,
        )
