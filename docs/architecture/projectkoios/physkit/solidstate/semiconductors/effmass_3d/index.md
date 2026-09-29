# `projectkoios.physkit.solidstate.semiconductors.effmass_3d`

This package owns exact free-particle reference models on physical periodic
primitive cells. These models verify geometry, reciprocal indexing, units,
Bloch phases, effective-mass conventions, and normalization; they do not
perform electronic-structure calculations.

This implementation applies the conventions verified first by the maintained
2D methodological review to a three-dimensional primitive-cell contract.

- [`PeriodicPrimitiveCell3D`](PeriodicPrimitiveCell3D/index.md) owns an
  invertible physical direct basis, reciprocal basis, metric, and volume.
- [`CartesianEffectiveMassTensor3D`](CartesianEffectiveMassTensor3D/index.md)
  owns the symmetric positive-definite Cartesian mass tensor.
- [`PeriodicFreeParticle3D`](PeriodicFreeParticle3D/index.md) evaluates exact
  Bloch-mode wave vectors and kinetic energies.
- [`PeriodicPlaneWave3DSampler`](PeriodicPlaneWave3DSampler/index.md) samples
  normalized Bloch plane waves at fractional coordinates.

The maintained laboratory uses `UnitSystem.METAL`. Direct lengths are measured
in angstrom, particle masses in dalton, action in electron-volt picosecond, and
energies in electron-volt. Compound-unit conversion is explicit because these
practical units cannot be combined by assuming a unit numerical conversion
factor.
