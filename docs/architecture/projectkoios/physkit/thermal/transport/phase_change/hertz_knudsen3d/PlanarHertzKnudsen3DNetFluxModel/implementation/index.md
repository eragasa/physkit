# `PlanarHertzKnudsen3DNetFluxModel` implementation

The evaluator converts temperatures, pressures, and particle mass to SI units;
evaluates separate nonnegative one-way evaporation and condensation fluxes; and
forms signed net number and mass fluxes before converting to requested units.

The model is specifically three-dimensional with a planar two-dimensional
interface. The two tangential Maxwell velocity integrations normalize to one;
the remaining positive normal-velocity moment produces the represented formula.

## Navigation

- [Mathematics](mathematics/index.md)
- [References](references/index.md)
- [Testing](testing/index.md)
- [Class](../index.md)
