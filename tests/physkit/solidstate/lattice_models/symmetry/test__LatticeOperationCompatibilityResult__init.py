"""Tests for lattice-operation compatibility findings."""

import pytest

from physkit.core.results import ResultsObject
from physkit.solidstate.lattice_models.symmetry import (
    LatticeOperationCompatibilityResult,
)


def test_retains_consistent_status_and_sorted_unique_issue_codes() -> None:
    compatible = LatticeOperationCompatibilityResult(True, ())
    incompatible = LatticeOperationCompatibilityResult(
        False,
        ("SOLID_STATE.LATTICE_OPERATION.EXTENT_MISMATCH",),
    )

    assert isinstance(compatible, ResultsObject)
    assert compatible.compatible
    assert not incompatible.compatible


def test_rejects_inconsistent_or_nondeterministic_findings() -> None:
    with pytest.raises(ValueError, match="status must agree"):
        LatticeOperationCompatibilityResult(False, ())
    with pytest.raises(ValueError, match="sorted and unique"):
        LatticeOperationCompatibilityResult(False, ("B", "A"))
    with pytest.raises(ValueError, match="sorted and unique"):
        LatticeOperationCompatibilityResult(False, ("A", "A"))
