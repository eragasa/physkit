# Nonorthogonal lattice geometry notebook migration

This record binds the maintained metric-geometry package behavior, lecture note,
and laboratory to the two reviewed exploratory notebooks preserved on local
candidate branch `work/review-preserved-notebooks` at
`154b4b865bb6329cc214700bc828892d5cc1d1ee`. That branch preserves the same
notebook bytes originally reviewed at `d43df75d121ee33ec4ac660cb1ec58f3d9456b3d`.

## Source identities

| Source path | Git blob | SHA-256 |
| --- | --- | --- |
| `notebooks/solid-state-physics/crystal-structure/metric-tensor-2d.ipynb` | `7395defd54dd5e805af57ac23151aa83d11c4475` | `d9f6aea9c4766f6d2a682af41038f110caf097e5c13a02a1e1d4f29af0cdd927` |
| `notebooks/solid-state-physics/crystal-structure/metric-tensor-3d.ipynb` | `0fc08e8852ad74089e9ff8692885719d4f35bf4a` | `eef5adbde7a1fdbcc85db47ea37cb3453855d2425d042fedc59c6cb37ad09b5e` |

## Retained layers

The maintained lesson retains and consolidates:

- direct metric `g=A^T A`, inverse metric, and reciprocal metric identities;
- fractional-to-Cartesian coordinate mapping;
- two-dimensional mixed derivatives for a constant nonorthogonal basis;
- the distinction between geometric and constitutive tensors;
- metric and Cartesian plane-wave and Bloch-shift equivalence;
- skew-cell nearest-image behavior; and
- two- and three-dimensional visual interpretation.

## Semantic adaptations

- Reusable metric and nearest-image behavior moved to
  `projectkoios.physkit.periodic.lattice.metric` with focused tests.
- The two dimensional source files became one maintained lecture-note and
  laboratory pair under the canonical `solidstate/lattices` hierarchy.
- The notebook imports package owners rather than defining local metric or
  nearest-image functions.
- The deleted harness-contract link and dimensional-series boilerplate were not
  migrated. The maintained laboratory links to its live prerequisite note and
  includes exercises and explicit evidence boundaries.
- The source notebooks used a bounded neighborhood around componentwise
  rounding. The maintained resolver instead derives a complete finite search
  bound from the smallest singular value of the direct basis; it therefore does
  not silently present a heuristic shell as a general nearest-image method.
- The package accepts only nominal `DirectLattice2D` and `DirectLattice3D`
  inputs and requires all derived binary64 metric arrays to remain finite.

## Evidence boundary

The source notebooks' saved outputs showed successful execution of their stated
assertions without saved errors. The migration tests package invariants and the
maintained notebook is executed as a bounded software check. Neither source nor
migration evidence establishes a material model, scientific validation,
uncertainty quantification, pedagogical validation, or human acceptance.
