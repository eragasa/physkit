"""Dimensionless Maxwell--Boltzmann occupation factor."""

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
class MaxwellBoltzmannOccupationEvaluator:
    """Evaluate the dimensionless Maxwell--Boltzmann occupation factor."""

    def action(
        self,
        *,
        request: IdealOccupationEvaluationRequest,
    ) -> IdealOccupationEvaluation:
        """Return finite Maxwell--Boltzmann factors."""
        if not isinstance(request, IdealOccupationEvaluationRequest):
            raise TypeError("request must be IdealOccupationEvaluationRequest")
        if request.statistic is not IdealOccupationStatistic.MAXWELL_BOLTZMANN:
            raise ValueError("request statistic must be Maxwell-Boltzmann")
        with np.errstate(over="ignore", under="ignore"):
            values = np.exp(-request.dimensionless_energy_offsets)
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
class MaxwellBoltzmannOccupationDistribution(
    ActionizedDataObject[
        IdealOccupationEvaluationRequest,
        IdealOccupationEvaluation,
    ]
):
    """Expose the dimensionless Maxwell--Boltzmann occupation façade."""

    actionizer: MaxwellBoltzmannOccupationEvaluator = field(
        default_factory=MaxwellBoltzmannOccupationEvaluator,
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
        """Evaluate Maxwell--Boltzmann factors on physical energies."""
        return self._respond(
            request=IdealOccupationEvaluationRequest(
                statistic=IdealOccupationStatistic.MAXWELL_BOLTZMANN,
                energies=energies,
                chemical_potential=chemical_potential,
                temperature=temperature,
            )
        )
