# Class `projectkoios.physkit.periodic.lattice.metric.NearestLatticeImageResolver`

## Current contract

The stateless resolver finds the integer direct-lattice translation minimizing
the Cartesian norm of one finite fractional displacement under a
`DirectLatticeMetric`.

Componentwise rounding provides an initial radius but is not assumed to be the
answer. The smallest singular value of the direct basis bounds every integer
translation that can improve that radius. Exhaustive enumeration of the finite
bounded index box therefore avoids a heuristic neighbor-shell cutoff.

## Limits

The resolver supports the two- and three-dimensional metric owner only. Runtime
can grow for severely ill-conditioned bases because the complete candidate box
can be large. Tied nearest images have no separately modeled physical
preference.

## Navigation

- [Parent module](../index.md)
- [Result class](../NearestLatticeImageResult/index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/metric.py::NearestLatticeImageResolver`
- Tests: `tests/projectkoios/physkit/periodic/lattice/metric/test__NearestLatticeImageResolver__execute.py`

## Evidence

Tests include a skewed basis whose nearest translation lies many index steps
from the componentwise-rounded translation, plus an independent 3D bounded
reference. They establish represented numerical behavior, not a molecular-
simulation cutoff policy or material validation.
