# Project Koios PhysKit agent instructions

## Repository purpose

`projectkoios-physkit` owns reusable computational-physics models,
mathematical representations, numerical methods, unit-aware quantities, and
pedagogical examples under `projectkoios.physkit`.

The repository is not a research-campaign control plane. Do not add workflow
engines, runtime coordination state, generic harness implementation,
material-specific acceptance policy, or production calculator execution to the
package. Reusable optimization contracts and algorithms belong to
`projectkoios-optimization`.

## Project Koios layout

- The distribution is `projectkoios-physkit`.
- The import namespace is `projectkoios.physkit`.
- Maintained Python source lives under
  `src/python/projectkoios/physkit/`.
- The top-level `projectkoios` directory is a PEP 420 implicit namespace and
  must not contain `__init__.py`.
- Tests mirror source ownership under `tests/projectkoios/physkit/`.
- Current-state architecture documentation mirrors package, module, and class
  ownership under `docs/architecture/projectkoios/physkit/`.
- Exact extraction and adaptation lineage belongs under `docs/provenance/`.

Package, module, and class architecture pages describe current contracts rather
than plans or workflow state. Architecture-relevant source changes update their
owning pages and mapped tests in the same change. Keep implementation
conformance, numerical verification, scientific validation, pedagogical
validation, uncertainty quantification, and human acceptance distinct.

## Authority and scope

Follow explicit human instructions and the nearest applicable `AGENTS.md`.
Work only within the authorized repository and task. Do not infer successor
work from completion of the current task.

A separate capability-contract file is not required. Ask for clarification when
a material scientific, pedagogical, ownership, or public-API decision remains
unresolved; do not manufacture process artifacts to avoid asking directly.

## Working-tree safety

Inspect the working tree before editing. Preserve unrelated modifications and
untracked files, and do not inspect unrelated private content. Avoid destructive
Git operations such as reset, clean, forced checkout, or history rewriting.
Commit, push, release, and changes to another repository require explicit human
authorization.

External donor repositories are read-only references unless changes are
explicitly authorized. Do not introduce runtime dependencies on local donor
checkouts.

## Development

- Python 3.14 or newer is required.
- Follow [`docs/developer/index.md`](docs/developer/index.md) for maintained code
  and testing conventions.
- Prefer nominal runtime ownership and explicit type checks where ownership
  matters; do not introduce structural protocols without an explicit need.
- Run focused tests before the complete suite, compile changed Python modules,
  build the wheel, and run `git diff --check`.
- Do not repair unrelated failures unless requested; report them separately.

## Scientific integrity

Do not silently change physical models, approximations, mathematical
conventions, units, invariants, or validation claims. Preserve exact source
provenance when migrating established behavior.

Passing tests or executing a notebook establishes only its declared software or
numerical result. It does not establish every scientific or pedagogical claim.

## Teaching and manuscript content

Follow [`docs/lecture-notes/README.md`](docs/lecture-notes/README.md) for the
ownership of lecture notes, notebooks, reusable visualizers, computational
studies, figure scripts, and generated images.

## Reporting

Report changed paths, validation performed, relevant limitations, and unresolved
decisions. Mention unrelated working-tree state when it affects safety or
interpretation. Do not claim scientific validation, human acceptance, release,
or successor authorization from task completion alone.
