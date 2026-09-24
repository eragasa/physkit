"""Verification of the nominal results-object boundary."""

from physkit.core.results import ResultsObject
from physkit.qm.piab1d.tdse_analytical import Piab1dTdseAnalyticalResults
from physkit.qm.piab1d.tdse_fd import Piab1dTdseFdResults
from physkit.qm.piab1d.tise_analytical import Piab1DAnalyticalResults
from physkit.qm.piab1d.tise_fd import Piab1dTiseFdResults


def test_direct_result_types_inherit_results_object() -> None:
    assert Piab1DAnalyticalResults.__bases__ == (ResultsObject,)
    assert Piab1dTiseFdResults.__bases__ == (ResultsObject,)
    assert Piab1dTdseAnalyticalResults.__bases__ == (ResultsObject,)
    assert Piab1dTdseFdResults.__bases__ == (ResultsObject,)
