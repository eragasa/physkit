"""Tests for finite-shape compatibility under lattice operations."""

from projectkoios.physkit.periodic.lattice.finite_domain import (
    FinitePeriodicDomain,
    LatticeDimension,
)
from projectkoios.physkit.periodic.lattice.symmetry import (
    IntegralLatticeOperation,
    LatticeOperationCompatibilityAuditor,
)


def test_maps_axis_extents_and_reports_mismatch() -> None:
    operation = IntegralLatticeOperation(
        "cycle",
        LatticeDimension.THREE,
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
    )
    source = FinitePeriodicDomain(LatticeDimension.THREE, (2, 3, 4))
    auditor = LatticeOperationCompatibilityAuditor()

    compatible = auditor.execute(
        source,
        FinitePeriodicDomain(LatticeDimension.THREE, (3, 4, 2)),
        operation,
    )
    mismatch = auditor.execute(source, source, operation)

    assert compatible.compatible
    assert mismatch.issue_codes == ("SOLID_STATE.LATTICE_OPERATION.EXTENT_MISMATCH",)


def test_reports_dimension_and_operation_class_incompatibilities() -> None:
    source = FinitePeriodicDomain(LatticeDimension.TWO, (2, 3))
    one_dimensional = FinitePeriodicDomain(LatticeDimension.ONE, (2,))
    one_dimensional_operation = IntegralLatticeOperation(
        "identity", LatticeDimension.ONE, ((1,),)
    )
    shear = IntegralLatticeOperation("shear", LatticeDimension.TWO, ((1, 1), (0, 1)))
    auditor = LatticeOperationCompatibilityAuditor()

    dimension_result = auditor.execute(
        source, one_dimensional, one_dimensional_operation
    )
    shear_result = auditor.execute(source, source, shear)

    assert dimension_result.issue_codes == (
        "SOLID_STATE.LATTICE_OPERATION.OPERATION_DIMENSION",
        "SOLID_STATE.LATTICE_OPERATION.TARGET_DIMENSION",
    )
    assert shear_result.issue_codes == (
        "SOLID_STATE.LATTICE_OPERATION.NOT_SIGNED_PERMUTATION",
    )
