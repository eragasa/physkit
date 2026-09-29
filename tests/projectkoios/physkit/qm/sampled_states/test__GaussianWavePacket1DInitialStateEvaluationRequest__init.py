"""Construction tests for ``GaussianWavePacket1DInitialStateEvaluationRequest``."""

import numpy as np
import pytest

from projectkoios.physkit.qm.sampled_states import (
    GaussianWavePacket1DInitialStateEvaluationRequest,
    GaussianWavePacket1DInitialStateModel,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


class TestGaussianWavePacket1DInitialStateEvaluationRequestInit:
    """Verify the complete packet-evaluation input contract."""

    @staticmethod
    def _model() -> GaussianWavePacket1DInitialStateModel:
        return GaussianWavePacket1DInitialStateModel(
            center=ScalarQuantity(magnitude=0.0, unit=Unitless()),
            width=ScalarQuantity(magnitude=1.0, unit=Unitless()),
            wavenumber=ScalarQuantity(magnitude=0.0, unit=Unitless()),
        )

    def test__init_retains_model_and_nonempty_coordinates(self) -> None:
        coordinates = VectorQuantity(
            magnitude=np.array([0.0], dtype=np.float64),
            unit=Unitless(),
        )

        request = GaussianWavePacket1DInitialStateEvaluationRequest(
            model=self._model(),
            coordinates=coordinates,
        )

        assert request.coordinates is coordinates

    def test__init_rejects_empty_coordinates(self) -> None:
        empty_coordinates = VectorQuantity(
            magnitude=np.array([], dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(ValueError, match="coordinates must be nonempty"):
            GaussianWavePacket1DInitialStateEvaluationRequest(
                model=self._model(),
                coordinates=empty_coordinates,
            )

    def test__init_rejects_nonmodel_input(self) -> None:
        invalid_model: GaussianWavePacket1DInitialStateModel | str = (
            "not a packet model"
        )
        coordinates = VectorQuantity(
            magnitude=np.array([0.0], dtype=np.float64),
            unit=Unitless(),
        )

        with pytest.raises(
            TypeError, match="model must be GaussianWavePacket1DInitialStateModel"
        ):
            GaussianWavePacket1DInitialStateEvaluationRequest(
                model=invalid_model,  # type: ignore[arg-type]
                coordinates=coordinates,
            )

    def test__init_rejects_nonvector_coordinates(self) -> None:
        invalid_coordinates: VectorQuantity | tuple[float, ...] = (0.0,)

        with pytest.raises(TypeError, match="coordinates must be VectorQuantity"):
            GaussianWavePacket1DInitialStateEvaluationRequest(
                model=self._model(),
                coordinates=invalid_coordinates,  # type: ignore[arg-type]
            )
