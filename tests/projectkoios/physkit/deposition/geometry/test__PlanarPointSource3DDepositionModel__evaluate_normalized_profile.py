"""Software verification for planar point-source normalized profiles."""

import numpy as np

from projectkoios.physkit.deposition.geometry.plane_point import (
    PlanarPointSource3DDepositionModel,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestPlanarPointSource3DDepositionModel:
    """Verify the public normalized-profile operation."""

    def test_evaluate_normalized_profile_matches_closed_form_with_conversion(
        self,
    ) -> None:
        """Mixed compatible length units retain the closed-form profile."""
        model = PlanarPointSource3DDepositionModel(
            source_to_substrate_distance=ScalarQuantity(
                magnitude=2.0,
                unit=PhysicalUnit(expression="centimeter"),
            )
        )
        result = model.evaluate_normalized_profile(
            lateral_offsets=VectorQuantity(
                magnitude=np.asarray([0.0, 20.0, 40.0], dtype=np.float64),
                unit=PhysicalUnit(expression="millimeter"),
            )
        )

        assert isinstance(result.normalized_thickness.unit, Unitless)
        assert np.allclose(
            result.normalized_thickness.magnitude,
            np.asarray([1.0, 2.0**-1.5, 5.0**-1.5], dtype=np.float64),
            rtol=1.0e-14,
            atol=0.0,
        )
        assert result.request.model is model
