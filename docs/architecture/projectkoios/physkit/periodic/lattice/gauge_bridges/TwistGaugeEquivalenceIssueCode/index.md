# Class `projectkoios.physkit.periodic.lattice.gauge_bridges.TwistGaugeEquivalenceIssueCode`

## Current contract

The enumeration reports represented prerequisites that block gauge-equivalence
matrix arithmetic: `DOMAIN`, `SOURCE_FIBER`, `TARGET_FIBER`, `BASIS`, `UNIT`,
and `ENERGY_REFERENCE`.

## Invariants

- Identifiers are uppercase constants with lowercase represented values.
- `DOMAIN = "domain"` names finite-periodic-domain incompatibility and replaces
  the donor's legacy `SHAPE = "shape"` issue identity.

## Navigation

- [Parent module](../index.md)

## Local mapping

- Code: `src/python/projectkoios/physkit/periodic/lattice/gauge_bridges.py::TwistGaugeEquivalenceIssueCode`
- Test: `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeEquivalenceAnalyzer__execute.py::test__execute__compares_equivalent_and_perturbed_matrices_after_bridge`

## Evidence

Implementation conformance is supported by exact basis and domain issue-code
assertions in the mapped test.
