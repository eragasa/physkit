"""Dimensionless Fermi--Dirac occupation distribution."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.special import expit

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.thermal.statmech.distributions.occupations.base import (
    IdealOccupationEvaluation,
    IdealOccupationEvaluationRequest,
    IdealOccupationStatistic,
)
from projectkoios.physkit.units import ScalarQuantity, Unitless, VectorQuantity


@dataclass(frozen=True, slots=True)
class FermiDiracOccupationEvaluator:
    """Evaluate the dimensionless Fermi--Dirac occupation formula."""

    def action(
        self,
        *,
        request: IdealOccupationEvaluationRequest,
    ) -> IdealOccupationEvaluation:
        """Return stable Fermi--Dirac occupation factors."""
        if not isinstance(request, IdealOccupationEvaluationRequest):
            raise TypeError("request must be IdealOccupationEvaluationRequest")
        if request.statistic is not IdealOccupationStatistic.FERMI_DIRAC:
            raise ValueError("request statistic must be Fermi-Dirac")
        return IdealOccupationEvaluation(
            request=request,
            occupation_factors=VectorQuantity(
                magnitude=np.asarray(
                    expit(-request.dimensionless_energy_offsets),
                    dtype=np.float64,
                ),
                unit=Unitless(),
            ),
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class FermiDiracOccupationDistribution(
    ActionizedDataObject[
        IdealOccupationEvaluationRequest,
        IdealOccupationEvaluation,
    ]
):
    """Expose the dimensionless Fermi--Dirac occupation façade."""

    actionizer: FermiDiracOccupationEvaluator = field(
        default_factory=FermiDiracOccupationEvaluator,
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
        """Evaluate Fermi--Dirac factors on physical energy coordinates."""
        return self._respond(
            request=IdealOccupationEvaluationRequest(
                statistic=IdealOccupationStatistic.FERMI_DIRAC,
                energies=energies,
                chemical_potential=chemical_potential,
                temperature=temperature,
            )
        )
