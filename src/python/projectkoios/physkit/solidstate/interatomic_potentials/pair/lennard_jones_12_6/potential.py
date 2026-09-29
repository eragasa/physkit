r"""Lennard--Jones 12-6 radial pair-potential façade."""

from __future__ import annotations

from dataclasses import dataclass

from projectkoios.physkit.solidstate.interatomic_potentials.pair.base import (
    RadialPairPotential,
    RadialPairPotentialEvaluation,
    RadialPairPotentialEvaluationRequest,
)
from projectkoios.physkit.solidstate.interatomic_potentials.pair.lennard_jones_12_6.parameters import (  # noqa: E501
    LennardJonesPotentialParameters,
)
from projectkoios.physkit.units import PhysicalUnit, ScalarQuantity, VectorQuantity


@dataclass(frozen=True, slots=True, kw_only=True)
class LennardJonesPotential(RadialPairPotential):
    r"""Represent $V(r)=4\epsilon[(\sigma/r)^{12}-(\sigma/r)^6]$."""

    parameters: LennardJonesPotentialParameters

    def __post_init__(self) -> None:
        """Check the complete Lennard--Jones parameter record."""
        self._check_arg_parameters()

    def _check_arg_parameters(self) -> None:
        """Require Lennard--Jones parameters."""
        if not isinstance(self.parameters, LennardJonesPotentialParameters):
            raise TypeError("parameters must be LennardJonesPotentialParameters")

    @property
    def equilibrium_distance(self) -> ScalarQuantity:
        """Return the analytical equilibrium separation."""
        return self.parameters.equilibrium_distance

    def evaluate(
        self,
        *,
        distances: VectorQuantity,
        energy_unit: PhysicalUnit,
        force_unit: PhysicalUnit,
    ) -> RadialPairPotentialEvaluation:
        """Evaluate potential energy and signed radial force."""
        from projectkoios.physkit.solidstate.interatomic_potentials.pair.lennard_jones_12_6.evaluator import (  # noqa: E501
            LennardJonesPotentialEvaluator,
        )

        request = RadialPairPotentialEvaluationRequest(
            model=self,
            distances=distances,
            energy_unit=energy_unit,
            force_unit=force_unit,
        )
        return LennardJonesPotentialEvaluator().action(request=request)
