# `projectkoios.physkit.solidstate.interatomic_potentials.pair.base`

This module owns `RadialPairPotential`,
`RadialPairPotentialEvaluationRequest`, and
`RadialPairPotentialEvaluation`. The abstract boundary defines the common
unit-aware sampled operation while each concrete family owns its formula and
evaluator.

The shared boundary is intentionally species-agnostic. Selecting parameter sets
by chemical-species pair, assigning atoms to positions, and maintaining an
atomistic structure are separate prospective ownership concerns. They are not
implicitly supplied by a radial potential or by this module.
