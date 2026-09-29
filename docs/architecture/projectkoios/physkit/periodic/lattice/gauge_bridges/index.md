# Module `projectkoios.physkit.periodic.lattice.gauge_bridges`

## Current responsibility

The module constructs an explicit site-diagonal unitary from centered
uniform-link twist gauge to quotient-seam twist gauge and compares compatible
represented scalar operators through that bridge without implicit matrix
densification.

## Public contract

`TwistGaugeBridgeConstructor` returns a correlated transformation and source and
target fibers. `TwistGaugeEquivalenceAnalyzer` checks finite domain, fibers,
basis identity, matrix unit, and energy-reference identity before evaluating a
caller-toleranced maximum absolute residual. It does not infer physical
alignment, choose tolerances, impose Hermiticity, or establish scientific
validation.

## Navigation

- [`TwistGaugeBridgeConvention`](TwistGaugeBridgeConvention/index.md)
- [`TwistGaugeBridgeResult`](TwistGaugeBridgeResult/index.md)
- [`TwistGaugeBridgeConstructor`](TwistGaugeBridgeConstructor/index.md)
- [`TwistGaugeEquivalenceIssueCode`](TwistGaugeEquivalenceIssueCode/index.md)
- [`TwistGaugeEquivalenceResult`](TwistGaugeEquivalenceResult/index.md)
- [`TwistGaugeEquivalenceAnalyzer`](TwistGaugeEquivalenceAnalyzer/index.md)
- [Parent package](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py`
- Tests: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/`
- Provenance: `docs/provenance/finite-periodic-lattice-source-mapping.md`

## Evidence

Implementation conformance is supported by tests of the diagonal phases,
declared transformation direction, correlated result invariants, represented
compatibility gates, exact zero residual, and a controlled matrix perturbation.
The tests establish represented software behavior only.
