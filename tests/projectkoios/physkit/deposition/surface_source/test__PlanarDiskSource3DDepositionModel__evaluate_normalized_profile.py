"""Software verification for planar finite-disk normalized profiles."""

import numpy as np

from projectkoios.physkit.deposition.surface_source.disk import (
    DiskSourcePolarQuadrature,
    PlanarDiskSource3DDepositionModel,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestPlanarDiskSource3DDepositionModel:
    """Verify the public finite-disk normalized-profile operation."""

    @staticmethod
    def _model(
        *,
        radius_metre: float,
        cosine_exponent: float = 1.0,
    ) -> PlanarDiskSource3DDepositionModel:
        """Construct one disk model for this evidence owner."""
        return PlanarDiskSource3DDepositionModel(
            source_to_substrate_distance=ScalarQuantity(
                magnitude=1.0,
                unit=PhysicalUnit(expression="meter"),
            ),
            source_radius=ScalarQuantity(
                magnitude=radius_metre,
                unit=PhysicalUnit(expression="meter"),
            ),
            cosine_exponent=ScalarQuantity(
                magnitude=cosine_exponent,
                unit=Unitless(),
            ),
        )

    def test_evaluate_normalized_profile_is_on_axis_normalized_and_decreasing(
        self,
    ) -> None:
        """A finite Lambertian disk gives a positive decreasing radial profile."""
        result = self._model(radius_metre=0.5).evaluate_normalized_profile(
            lateral_offsets=VectorQuantity(
                magnitude=np.linspace(0.0, 2.0, 41, dtype=np.float64),
                unit=PhysicalUnit(expression="meter"),
            ),
            quadrature=DiskSourcePolarQuadrature(
                radial_point_count=161,
                azimuthal_point_count=240,
            ),
        )

        assert isinstance(result.normalized_thickness.unit, Unitless)
        assert np.isclose(result.normalized_thickness.magnitude[0], 1.0)
        assert np.all(result.normalized_thickness.magnitude > 0.0)
        assert np.all(np.diff(result.normalized_thickness.magnitude) < 0.0)

    def test_small_disk_limit_agrees_with_point_source_profile(self) -> None:
        """A small isotropic disk approaches the isotropic point-source shape."""
        lateral_offsets = np.asarray([0.0, 0.5, 1.0, 2.0], dtype=np.float64)
        result = self._model(
            radius_metre=1.0e-3,
            cosine_exponent=0.0,
        ).evaluate_normalized_profile(
            lateral_offsets=VectorQuantity(
                magnitude=lateral_offsets,
                unit=PhysicalUnit(expression="meter"),
            ),
            quadrature=DiskSourcePolarQuadrature(
                radial_point_count=81,
                azimuthal_point_count=180,
            ),
        )
        expected = (1.0 + lateral_offsets**2) ** (-1.5)

        assert np.allclose(
            result.normalized_thickness.magnitude,
            expected,
            rtol=2.0e-6,
            atol=0.0,
        )
