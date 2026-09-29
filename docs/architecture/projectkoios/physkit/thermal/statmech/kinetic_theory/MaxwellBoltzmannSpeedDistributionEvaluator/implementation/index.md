# `MaxwellBoltzmannSpeedDistributionEvaluator` implementation

## Current implementation

Evaluation validates the typed request, converts state quantities to kelvin and
kilograms per mole, converts requested speeds to metres per second, applies the
density formula with NumPy operations, and converts the result to reciprocal
requested-speed units.

## Navigation

- [Mathematics](mathematics/index.md)
- [Testing](testing/index.md)
- [Source lineage](references/index.md)
- [Class contract](../index.md)

## Evidence boundary

Mapped tests establish the software contract, unit conversion, selected formula
values, finite-grid normalization, and analytic peak location for synthetic test
data. They do not scientifically validate Maxwell–Boltzmann assumptions for a
real gas.
