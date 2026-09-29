# `projectkoios.physkit.solidstate.semiconductors.effmass_2d`

This package owns exact free-particle reference models on physical periodic
primitive cells. These models verify geometry, reciprocal indexing, units,
Bloch phases, effective-mass conventions, and normalization; they do not
perform electronic-structure calculations.

The first maintained implementation is deliberately two-dimensional. It serves
as a methodological review before a separate three-dimensional primitive-cell
contract is introduced.

- [`PeriodicPrimitiveCell2D`](PeriodicPrimitiveCell2D/index.md) owns an
  invertible physical direct basis, reciprocal basis, metric, and area.
- [`CartesianEffectiveMassTensor2D`](CartesianEffectiveMassTensor2D/index.md)
  owns the symmetric positive-definite Cartesian mass tensor.
- [`PeriodicFreeParticle2D`](PeriodicFreeParticle2D/index.md) evaluates exact
  Bloch-mode wave vectors and kinetic energies.
- [`PeriodicPlaneWave2DSampler`](PeriodicPlaneWave2DSampler/index.md) samples
  normalized Bloch plane waves at fractional coordinates.

The maintained laboratory uses `UnitSystem.METAL`. Direct lengths are measured
in angstrom, particle masses in dalton, action in electron-volt picosecond, and
energies in electron-volt. Compound-unit conversion is explicit because these
practical units cannot be combined by assuming a unit numerical conversion
factor.
