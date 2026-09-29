"""Inheritance tests for ``DataObject``."""

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.core.data import DataObject
from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.qm.sampled_states import (
    GaussianWavePacket1DInitialState,
    GaussianWavePacket1DInitialStateEvaluationRequest,
    GaussianWavePacket1DInitialStateModel,
    SampledQuantumState1D,
)


class TestDataObjectInheritance:
    """Verify the shared data-object boundary reaches concrete packet records."""

    def test__inheritance_reaches_gaussian_packet_contracts(self) -> None:
        assert issubclass(ResultsObject, DataObject)
        assert issubclass(ActionizedDataObject, DataObject)
        assert issubclass(GaussianWavePacket1DInitialStateModel, DataObject)
        assert issubclass(
            GaussianWavePacket1DInitialStateEvaluationRequest,
            DataObject,
        )
        assert issubclass(SampledQuantumState1D, DataObject)
        assert issubclass(GaussianWavePacket1DInitialState, DataObject)
