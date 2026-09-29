"""Numerical verification for the dimensionless delta-comb band model."""

import numpy as np

from projectkoios.physkit.solidstate.electronic.kronig_penney.delta_comb import (
    DimensionlessKronigPenneyDeltaComb,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


class TestDimensionlessKronigPenneyDeltaComb:
    """Verify the free limit and retained dispersion relation."""

    @staticmethod
    def _phase_parameters() -> VectorQuantity:
        """Construct one increasing reduced phase grid."""
        return VectorQuantity(
            magnitude=np.linspace(0.01, 4.0 * np.pi, 4000),
            unit=Unitless(),
        )

    def test_sample_allowed_bands_reduces_to_folded_free_states(self) -> None:
        """Zero barrier strength permits every sampled free state."""
        model = DimensionlessKronigPenneyDeltaComb(
            barrier_strength=ScalarQuantity(magnitude=0.0, unit=Unitless())
        )
        phases = self._phase_parameters()

        sampling = model.sample_allowed_bands(phase_parameters=phases)

        assert np.array_equal(
            sampling.allowed_phase_parameters.magnitude,
            phases.magnitude,
        )
        assert np.allclose(
            np.cos(sampling.bloch_phases.magnitude),
            np.cos(phases.magnitude),
            rtol=0.0,
            atol=5.0e-16,
        )
        assert np.array_equal(
            sampling.reduced_energies.magnitude,
            phases.magnitude**2,
        )

    def test_sample_allowed_bands_satisfies_delta_comb_dispersion(self) -> None:
        """Every retained state has a real first-zone Bloch phase."""
        model = DimensionlessKronigPenneyDeltaComb(
            barrier_strength=ScalarQuantity(magnitude=4.0, unit=Unitless())
        )
        phases = self._phase_parameters()

        sampling = model.sample_allowed_bands(phase_parameters=phases)
        retained_dispersion = model.dispersion_values(
            phase_parameters=sampling.allowed_phase_parameters
        )

        assert sampling.allowed_phase_parameters.magnitude.size < phases.magnitude.size
        assert np.allclose(
            np.cos(sampling.bloch_phases.magnitude),
            retained_dispersion.magnitude,
            rtol=0.0,
            atol=5.0e-15,
        )
