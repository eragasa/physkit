# `projectkoios.physkit.materials.mixtures.sublattice`

This module owns:

- [`SublatticeSpecification`](SublatticeSpecification/index.md), which declares
  ordered allowed species and formula-unit multiplicity;
- immutable `SublatticeSiteFractions` records;
- [`SiteFractionMixture`](SiteFractionMixture/index.md), which owns one
  normalized vector per sublattice;
- typed overall-composition requests and results; and
- [`SiteCountMixtureNormalizer`](SiteCountMixtureNormalizer/index.md), which
  constructs site fractions from aligned counts.
