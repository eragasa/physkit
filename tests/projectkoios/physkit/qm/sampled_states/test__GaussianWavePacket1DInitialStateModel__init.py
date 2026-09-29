"""Construction tests for ``GaussianWavePacket1DInitialStateModel``."""

import pytest

from projectkoios.physkit.qm.sampled_states import (
    GaussianWavePacket1DInitialStateModel,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless


class TestGaussianWavePacket1DInitialStateModelInit:
    """Verify intrinsic Gaussian-packet parameter invariants."""

    def test__init_rejects_nonpositive_width(self) -> None:
        zero_width = 0.0

        with pytest.raises(ValueError, match="width must be positive"):
            GaussianWavePacket1DInitialStateModel(
                center=ScalarQuantity(magnitude=0.0, unit=Unitless()),
                width=ScalarQuantity(magnitude=zero_width, unit=Unitless()),
                wavenumber=ScalarQuantity(magnitude=0.0, unit=Unitless()),
            )
