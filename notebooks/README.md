# Project Koios PhysKit notebooks

Notebooks are computational laboratories, not library implementation modules.
Reusable mathematics, numerical representations, models, solvers, and plotting
behavior belong under `src/python/projectkoios/physkit/` with ordinary tests.
See [`docs/lecture-notes/README.md`](../docs/lecture-notes/README.md) for the full
artifact-ownership policy.

## Notebook review and migration directions

1. Evaluate scientific or pedagogical intent, narrative structure, equations,
   figures, saved outputs, exercises, and implementation as separate layers.
   Broken or incomplete code does not by itself justify retiring the other
   layers.
2. Identify exact and semantic duplicates without executing unknown code.
3. Preserve the exact artifact until every valuable layer has a named
   destination; retain its hash and presentation lineage when consolidation is
   not yet complete.
4. Select one subject-oriented canonical path.
5. Separate narrative, reusable behavior, and one-off experiment assembly.
6. Extract reusable behavior into a defining package module with tests.
7. Replace notebook-local implementations with defining-module imports.
8. Clear stale outputs only after their informational or presentation value has
   been reviewed and a maintained replacement exists.
9. Execute a notebook only when its dependencies and expected resource use are
   understood. Report execution separately from scientific or pedagogical
   validation.

These directions govern review and migration. Historical dispositions and path
changes are recorded in [`CHANGES.MD`](CHANGES.MD), not below the operating
instructions.

## Maintained organization

Maintained laboratories use subject-oriented paths:

| Area | Directory | Maintained ownership examples |
| --- | --- | --- |
| Mathematical foundations | `foundations/` | Fourier and periodic methods |
| Numerical methods | `numerics/` | Differentiation and represented operators |
| Mechanics | `mechanics/` | Continuum stress laboratories |
| Plasma physics | `plasma-physics/` | Gas-discharge models |
| Quantum mechanics | `qm/` | PIAB1D/2D/3D and QHO1D laboratories |
| Solid-state physics | `solidstate/` | Lattices, tight binding, pair potentials, phase fields, and periodic electronic models |
| Thermal physics | `thermal/` | Statistical mechanics, thermodynamics, and transport |
| Deposition | `deposition/` | Source-geometry laboratories |
| Materials | `materials/` | Mixture and composition laboratories |
| Waves | `waves/` | Generic complex plane waves |

A maintained notebook should link to prerequisite narrative documentation,
state learning objectives, import reusable behavior from `projectkoios.physkit`,
include bounded executable checks, distinguish calculated output from expected
behavior, and end with interpretation or exercises.

## Migration states

- `scratch/` contains exploratory material and is not a supported package API or
  maintained curriculum surface.
- Root-level notebooks and older domain directories remain migration candidates.
  Their current location does not imply support, correctness, or pedagogical
  validation.
- Notebook-local `.py` files are migration candidates, not an alternative source
  tree. Move reusable behavior into the package before depending on it from a
  maintained laboratory.
- Exact duplicates should have one reviewed survivor. Preserve lineage in this
  index or Git history rather than retaining multiple active copies.

## Change history

See [`CHANGES.MD`](CHANGES.MD) for the chronological extraction, consolidation,
relocation, and retirement record.
