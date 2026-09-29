# Class `projectkoios.physkit.periodic.lattice.gauge_bridges.TwistGaugeEquivalenceAnalyzer`

## Current contract

`execute(source, target, bridge, absolute_tolerance=...)` first compares the
finite domain, expected source and target fibers, basis identity, matrix unit,
and energy-reference identity. When compatible, it computes the sparse residual
`H_target - U H_source U^dagger` and records its maximum stored absolute value.

## Invariants

- Matrix arithmetic does not run when represented prerequisites disagree.
- The caller owns the finite nonnegative acceptance tolerance.
- Sparse matrices are not implicitly densified.
- The analyzer does not align bases, convert units, or infer physical gauge
  equivalence beyond the supplied represented metadata.

## Navigation

- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py::TwistGaugeEquivalenceAnalyzer`
- Test: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeEquivalenceAnalyzer__execute.py::test__execute__compares_equivalent_and_perturbed_matrices_after_bridge`

## Evidence

Implementation conformance is supported by compatible, perturbed, basis-mismatch,
and domain-mismatch cases. The controlled `0.01` perturbation establishes the
represented residual calculation under the test conditions, not scientific
validation.
