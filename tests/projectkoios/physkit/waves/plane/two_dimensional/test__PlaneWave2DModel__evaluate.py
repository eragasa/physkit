"""Numerical verification for two-dimensional complex plane waves."""

import numpy as np

from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)
from projectkoios.physkit.waves.plane.two_dimensional.model import (
    PlaneWave2DModel,
    PlaneWave2DParameters,
)


class TestPlaneWave2DModel:
    """Verify Cartesian evaluation and a periodic Fourier-space signature."""

    def test_evaluate_has_the_requested_periodic_fft_peak(self) -> None:
        """An on-grid plane wave occupies its expected discrete Fourier mode."""
        sample_count = 32
        domain_length = 8.0
        mode_x = 3
        mode_y = -4
        coordinates = np.linspace(
            0.0,
            domain_length,
            sample_count,
            endpoint=False,
        )
        model = PlaneWave2DModel(
            parameters=PlaneWave2DParameters(
                amplitude=ScalarQuantity(magnitude=1.0, unit=Unitless()),
                wave_vector=VectorQuantity(
                    magnitude=np.array(
                        [
                            2.0 * np.pi * mode_x / domain_length,
                            2.0 * np.pi * mode_y / domain_length,
                        ]
                    ),
                    unit=PhysicalUnit(expression="1 / meter"),
                ),
                angular_frequency=ScalarQuantity(
                    magnitude=0.0,
                    unit=PhysicalUnit(expression="1 / second"),
                ),
                phase_offset=ScalarQuantity(magnitude=0.0, unit=Unitless()),
            )
        )

        evaluation = model.evaluate(
            x_coordinates=VectorQuantity(
                magnitude=coordinates,
                unit=PhysicalUnit(expression="meter"),
            ),
            y_coordinates=VectorQuantity(
                magnitude=coordinates,
                unit=PhysicalUnit(expression="meter"),
            ),
            time=ScalarQuantity(
                magnitude=0.0,
                unit=PhysicalUnit(expression="second"),
            ),
        )
        spectrum = np.fft.fft2(evaluation.field_values.magnitude)
        peak_y, peak_x = np.unravel_index(np.argmax(np.abs(spectrum)), spectrum.shape)
        frequencies = np.fft.fftfreq(
            sample_count,
            d=domain_length / sample_count,
        )

        assert np.isclose(
            2.0 * np.pi * frequencies[peak_x], 2.0 * np.pi * mode_x / domain_length
        )
        assert np.isclose(
            2.0 * np.pi * frequencies[peak_y], 2.0 * np.pi * mode_y / domain_length
        )
        assert np.allclose(
            np.abs(evaluation.field_values.magnitude),
            1.0,
            rtol=0.0,
            atol=1.0e-15,
        )
