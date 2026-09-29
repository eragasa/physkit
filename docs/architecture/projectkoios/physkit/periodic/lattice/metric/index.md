# Module `projectkoios.physkit.periodic.lattice.metric`

## Current responsibility

The module owns metric geometry derived from nominal two- and three-dimensional
direct Bravais lattices. It correlates direct and reciprocal basis matrices,
covariant and contravariant metrics, fundamental-region measure, fractional-to-
Cartesian mapping, and exact nearest periodic images.

## Public contract

`DirectLatticeMetric` accepts only `DirectLattice2D` or `DirectLattice3D`, owns
an immutable copy of the source geometry, and exposes finite binary64 arrays.
`NearestLatticeImageResolver` minimizes Cartesian distance over integer lattice
translations without a heuristic neighbor-shell cutoff. Its
`NearestLatticeImageResult` retains the original fractional displacement, chosen
integer translation, and fractional and Cartesian image vectors.

The numerical bases use one caller-declared consistent length convention. The
module does not attach units, infer a material, construct an effective-mass
tensor, or validate a physical model.

## Navigation

- [Class `DirectLatticeMetric`](DirectLatticeMetric/index.md)
- [Class `NearestLatticeImageResolver`](NearestLatticeImageResolver/index.md)
- [Class `NearestLatticeImageResult`](NearestLatticeImageResult/index.md)
- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/metric.py`
- Tests: `tests/projectkoios/physkit/periodic/lattice/metric/`
- Teaching note: `docs/lecturenotes/solidstate/lattices/nonorthogonal-metric-geometry/index.md`
- Laboratory: `notebooks/solidstate/lattices/nonorthogonal-metric-geometry.ipynb`

## Evidence

Focused tests cover 2D and 3D metric identities, direct/reciprocal duality,
large/small finite measure preservation, immutable storage, scaled Cartesian
consistency checks, fractional-coordinate mapping, a skew-cell case where
componentwise rounding is not nearest, an exact search beyond a fixed neighbor
shell, and three-dimensional agreement with an independent bounded reference.
These checks establish represented software and numerical behavior only.
