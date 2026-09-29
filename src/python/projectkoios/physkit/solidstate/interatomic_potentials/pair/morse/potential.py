r"""Morse radial pair-potential façade."""

from __future__ import annotations

from dataclasses import dataclass

from projectkoios.physkit.solidstate.interatomic_potentials.pair.base import (
    RadialPairPotential,
    RadialPairPotentialEvaluation,
    RadialPairPotentialEvaluationRequest,
)
from projectkoios.physkit.solidstate.interatomic_potentials.pair.morse.parameters import (  # noqa: E501
    MorsePotentialParameters,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


@dataclass(frozen=True, slots=True, kw_only=True)
class MorsePotential(RadialPairPotential):
    r"""Represent $V(r)=D[(1-e^{-a(r-r_e)})^2-1]$."""

    parameters: MorsePotentialParameters

    def __post_init__(self) -> None:
        """Check the complete Morse parameter record."""
        self._check_arg_parameters()

    def _check_arg_parameters(self) -> None:
        """Require Morse potential parameters."""
        if not isinstance(self.parameters, MorsePotentialParameters):
            raise TypeError("parameters must be MorsePotentialParameters")

    @property
    def equilibrium_distance(self) -> ScalarQuantity:
        """Return the represented equilibrium separation."""
        return self.parameters.equilibrium_distance

    def evaluate(
        self,
        *,
        distances: VectorQuantity,
        energy_unit: PhysicalUnit,
        force_unit: PhysicalUnit,
    ) -> RadialPairPotentialEvaluation:
        """Evaluate potential energy and signed radial force."""
        from projectkoios.physkit.solidstate.interatomic_potentials.pair.morse.evaluator import (  # noqa: E501
            MorsePotentialEvaluator,
        )

        request = RadialPairPotentialEvaluationRequest(
            model=self,
            distances=distances,
            energy_unit=energy_unit,
            force_unit=force_unit,
        )
        return MorsePotentialEvaluator().action(request=request)
