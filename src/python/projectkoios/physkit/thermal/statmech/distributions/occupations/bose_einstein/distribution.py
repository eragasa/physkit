"""Dimensionless Bose--Einstein occupation distribution."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.thermal.statmech.distributions.occupations.base import (
    IdealOccupationEvaluation,
    IdealOccupationEvaluationRequest,
    IdealOccupationStatistic,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


@dataclass(frozen=True, slots=True)
class BoseEinsteinOccupationEvaluator:
    """Evaluate the dimensionless Bose--Einstein occupation formula."""

    def action(
        self,
        *,
        request: IdealOccupationEvaluationRequest,
    ) -> IdealOccupationEvaluation:
        """Return Bose--Einstein factors on the positive domain."""
        if not isinstance(request, IdealOccupationEvaluationRequest):
            raise TypeError("request must be IdealOccupationEvaluationRequest")
        if request.statistic is not IdealOccupationStatistic.BOSE_EINSTEIN:
            raise ValueError("request statistic must be Bose-Einstein")
        with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
            values = 1.0 / np.expm1(request.dimensionless_energy_offsets)
        if not np.all(np.isfinite(values)):
            raise ValueError(
                "dimensionless energy offsets produce occupation factors outside "
                "the finite binary64 range"
            )
        return IdealOccupationEvaluation(
            request=request,
            occupation_factors=VectorQuantity(
                magnitude=np.asarray(values, dtype=np.float64),
                unit=Unitless(),
            ),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class BoseEinsteinOccupationDistribution(
    ActionizedDataObject[
        IdealOccupationEvaluationRequest,
        IdealOccupationEvaluation,
    ]
):
    """Expose the dimensionless Bose--Einstein occupation façade."""

    actionizer: BoseEinsteinOccupationEvaluator = field(
        default_factory=BoseEinsteinOccupationEvaluator,
        init=False,
        repr=False,
        compare=False,
    )

    def evaluate(
        self,
        *,
        energies: VectorQuantity,
        chemical_potential: ScalarQuantity,
        temperature: ScalarQuantity,
    ) -> IdealOccupationEvaluation:
        """Evaluate Bose--Einstein factors on physical energy coordinates."""
        return self._respond(
            request=IdealOccupationEvaluationRequest(
                statistic=IdealOccupationStatistic.BOSE_EINSTEIN,
                energies=energies,
                chemical_potential=chemical_potential,
                temperature=temperature,
            )
        )
