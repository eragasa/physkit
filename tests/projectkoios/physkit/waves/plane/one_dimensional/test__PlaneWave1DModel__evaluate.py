"""Software verification for one-dimensional complex plane waves."""

import numpy as np

from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)
from projectkoios.physkit.waves.plane.one_dimensional.model import (
    PlaneWave1DModel,
    PlaneWave1DParameters,
)


class TestPlaneWave1DModel:
    """Verify phase values and compatible unit conversion."""

    def test_evaluate_matches_characteristic_quarter_cycle_phases(self) -> None:
        """The represented complex field follows the stated phase convention."""
        model = PlaneWave1DModel(
            parameters=PlaneWave1DParameters(
                amplitude=ScalarQuantity(magnitude=2.0, unit=Unitless()),
                wave_number=ScalarQuantity(
                    magnitude=np.pi,
                    unit=PhysicalUnit(expression="1 / meter"),
                ),
                angular_frequency=ScalarQuantity(
                    magnitude=2.0 * np.pi,
                    unit=PhysicalUnit(expression="1 / second"),
                ),
                phase_offset=ScalarQuantity(magnitude=0.0, unit=Unitless()),
            )
        )

        evaluation = model.evaluate(
            positions=VectorQuantity(
                magnitude=np.array([0.0, 50.0, 100.0]),
                unit=PhysicalUnit(expression="centimeter"),
            ),
            time=ScalarQuantity(
                magnitude=250.0,
                unit=PhysicalUnit(expression="millisecond"),
            ),
        )

        assert np.allclose(
            evaluation.field_values.magnitude,
            np.array([-2.0j, 2.0 + 0.0j, 2.0j]),
            rtol=0.0,
            atol=1.0e-14,
        )
