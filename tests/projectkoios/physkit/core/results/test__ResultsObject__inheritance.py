"""Verification of the nominal results-object boundary."""

from projectkoios.physkit.core.results import ResultsObject
from projectkoios.physkit.qm.piab1d.tdse_analytical import Piab1dTdseAnalyticalResults
from projectkoios.physkit.qm.piab1d.tdse_fd import Piab1dTdseFdResults
from projectkoios.physkit.qm.piab1d.tise_analytical import Piab1DAnalyticalResults
from projectkoios.physkit.qm.piab1d.tise_fd import Piab1dTiseFdResults


class TestResultsObjectInheritance:
    """Verify direct result ownership by the nominal result boundary."""

    def test__direct_result_types_inherit_results_object(self) -> None:
        assert Piab1DAnalyticalResults.__bases__ == (ResultsObject,)
        assert Piab1dTiseFdResults.__bases__ == (ResultsObject,)
        assert Piab1dTdseAnalyticalResults.__bases__ == (ResultsObject,)
        assert Piab1dTdseFdResults.__bases__ == (ResultsObject,)
