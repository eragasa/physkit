"""Compatibility-checked sparse composition of scalar finite-lattice operators.

Compatibility is exact over the finite periodic domain, twist fiber, basis identity,
matrix unit, and energy-reference identity. Addition is defined only after a correlated
passing compatibility result and preserves sparse storage without implicit
densification. These software checks do not align representations, convert units,
change gauges, establish Hermiticity, or provide physical or scientific validation.

This implementation preserves the represented behavior of
``ksdft2effmass.solid_state.operator_composition`` at donor revision
``2578d398b1d0aa3bfafb45f73b39c79ede5f5c42``. The legacy ``SHAPE`` issue name and
``"shape"`` value remain unchanged for compatibility, although the compared metadata
is a :class:`~physkit.periodic.lattice.finite_domain.FinitePeriodicDomain`.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from physkit.units import ComplexSparseMatrixQuantity

from .represented_operators import ScalarFiniteLatticeOperator


class ScalarFiniteLatticeOperatorCompatibilityIssueCode(StrEnum):
    """Comparison-critical metadata mismatches that prohibit operator addition."""

    SHAPE = "shape"
    TWIST_FIBER = "twist_fiber"
    BASIS = "basis"
    UNIT = "unit"
    ENERGY_REFERENCE = "energy_reference"


@dataclass(frozen=True, slots=True)
class ScalarFiniteLatticeOperatorCompatibilityResult:
    """Retain exact operands and their represented compatibility outcome.

    Parameters
    ----------
    left
        Exact left represented operator supplied to compatibility analysis.
    right
        Exact right represented operator supplied to compatibility analysis.
    issue_codes
        Sorted unique issue codes that exactly describe metadata disagreement between
        ``left`` and ``right``.
    """

    left: ScalarFiniteLatticeOperator
    right: ScalarFiniteLatticeOperator
    issue_codes: tuple[ScalarFiniteLatticeOperatorCompatibilityIssueCode, ...]

    def __post_init__(self) -> None:
        """Validate exact operands, canonical issue ordering, and issue completeness."""
        if type(self.left) is not ScalarFiniteLatticeOperator:
            raise TypeError("left must be ScalarFiniteLatticeOperator")
        if type(self.right) is not ScalarFiniteLatticeOperator:
            raise TypeError("right must be ScalarFiniteLatticeOperator")
        if type(self.issue_codes) is not tuple or any(
            type(code) is not ScalarFiniteLatticeOperatorCompatibilityIssueCode
            for code in self.issue_codes
        ):
            raise TypeError(
                "issue_codes must contain "
                "ScalarFiniteLatticeOperatorCompatibilityIssueCode"
            )
        ordered = tuple(sorted(set(self.issue_codes), key=lambda code: code.value))
        if self.issue_codes != ordered:
            raise ValueError("issue_codes must be sorted and unique")
        expected: set[ScalarFiniteLatticeOperatorCompatibilityIssueCode] = set()
        if self.left.domain != self.right.domain:
            expected.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.SHAPE)
        if self.left.twist_fiber != self.right.twist_fiber:
            expected.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.TWIST_FIBER)
        if self.left.basis_identifier != self.right.basis_identifier:
            expected.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.BASIS)
        if self.left.matrix.unit != self.right.matrix.unit:
            expected.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.UNIT)
        if self.left.energy_reference != self.right.energy_reference:
            expected.add(
                ScalarFiniteLatticeOperatorCompatibilityIssueCode.ENERGY_REFERENCE
            )
        expected_ordered = tuple(sorted(expected, key=lambda code: code.value))
        if self.issue_codes != expected_ordered:
            raise ValueError("issue_codes must exactly describe operand compatibility")

    @property
    def compatible(self) -> bool:
        """Return whether direct represented matrix addition is defined."""
        return not self.issue_codes


class ScalarFiniteLatticeOperatorCompatibilityAnalyzer:
    """Check represented metadata required before adding scalar operators."""

    __slots__ = ()

    def execute(
        self,
        left: ScalarFiniteLatticeOperator,
        right: ScalarFiniteLatticeOperator,
    ) -> ScalarFiniteLatticeOperatorCompatibilityResult:
        """Return exact operands and every represented compatibility issue.

        Parameters
        ----------
        left
            Left scalar finite-lattice operator.
        right
            Right scalar finite-lattice operator.

        Returns
        -------
        ScalarFiniteLatticeOperatorCompatibilityResult
            Correlated operands and canonically ordered metadata mismatches.
        """
        if type(left) is not ScalarFiniteLatticeOperator:
            raise TypeError("left must be ScalarFiniteLatticeOperator")
        if type(right) is not ScalarFiniteLatticeOperator:
            raise TypeError("right must be ScalarFiniteLatticeOperator")
        issues: set[ScalarFiniteLatticeOperatorCompatibilityIssueCode] = set()
        if left.domain != right.domain:
            issues.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.SHAPE)
        if left.twist_fiber != right.twist_fiber:
            issues.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.TWIST_FIBER)
        if left.basis_identifier != right.basis_identifier:
            issues.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.BASIS)
        if left.matrix.unit != right.matrix.unit:
            issues.add(ScalarFiniteLatticeOperatorCompatibilityIssueCode.UNIT)
        if left.energy_reference != right.energy_reference:
            issues.add(
                ScalarFiniteLatticeOperatorCompatibilityIssueCode.ENERGY_REFERENCE
            )
        return ScalarFiniteLatticeOperatorCompatibilityResult(
            left,
            right,
            tuple(sorted(issues, key=lambda code: code.value)),
        )


class ScalarFiniteLatticeOperatorAdder:
    """Add compatible scalar represented operators without implicit densification."""

    __slots__ = ()

    def execute(
        self,
        identifier: str,
        left: ScalarFiniteLatticeOperator,
        right: ScalarFiniteLatticeOperator,
        compatibility: ScalarFiniteLatticeOperatorCompatibilityResult,
    ) -> ScalarFiniteLatticeOperator:
        """Return the canonical sparse sum after correlated compatibility evidence.

        Parameters
        ----------
        identifier
            Nonempty identity for the represented sum.
        left
            Left scalar finite-lattice operator.
        right
            Right scalar finite-lattice operator.
        compatibility
            Passing result produced for the exact ``left`` and ``right`` objects.

        Returns
        -------
        ScalarFiniteLatticeOperator
            Sparse represented sum with composition provenance.
        """
        if type(identifier) is not str:
            raise TypeError("identifier must be a string")
        if not identifier:
            raise ValueError("identifier must be nonempty")
        if type(left) is not ScalarFiniteLatticeOperator:
            raise TypeError("left must be ScalarFiniteLatticeOperator")
        if type(right) is not ScalarFiniteLatticeOperator:
            raise TypeError("right must be ScalarFiniteLatticeOperator")
        if type(compatibility) is not ScalarFiniteLatticeOperatorCompatibilityResult:
            raise TypeError(
                "compatibility must be ScalarFiniteLatticeOperatorCompatibilityResult"
            )
        if compatibility.left is not left or compatibility.right is not right:
            raise ValueError("compatibility result must correlate the exact operands")
        if not compatibility.compatible:
            raise ValueError("compatibility result must pass before operator addition")
        matrix = ComplexSparseMatrixQuantity.from_csr(
            left.matrix.to_csr() + right.matrix.to_csr(), left.matrix.unit
        )
        return ScalarFiniteLatticeOperator(
            identifier,
            matrix,
            left.domain,
            left.twist_fiber,
            left.basis_identifier,
            left.energy_reference,
            (
                ("composer", type(self).__name__),
                ("left_operator", left.identifier),
                ("right_operator", right.identifier),
            ),
        )
