# PhysKit agent instructions

## Repository purpose

PhysKit is a pedagogically motivated computational-physics library. Reusable
physics, numerical methods, data models, and visualization behavior belong in
the Python package. Lecture notes and notebooks explain and exercise those
capabilities without becoming substitute implementations.

PhysKit is not a research-campaign control plane. Do not add workflow engines,
runtime coordination state, or generic harness implementation to `src/physkit`.

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
Commit, push, release, and changes to other repositories require explicit
authorization.

External donor repositories are read-only references unless explicitly stated
otherwise. Do not introduce runtime dependencies on local donor checkouts.

## Development

- PhysKit is imported as `physkit` and requires Python 3.14 or newer.
- Follow [`docs/developer/index.md`](docs/developer/index.md) for maintained
  code and testing conventions.
- Keep reusable implementation under `src/physkit/` and verification under
  `tests/`.
- Prefer nominal runtime ownership and explicit type checks where ownership
  matters; do not introduce structural protocols without an explicit need.
- Run focused tests and `git diff --check` for changed code.
- Do not repair unrelated failures unless requested; report them separately.

## Scientific integrity

Do not silently change physical models, approximations, mathematical
conventions, units, invariants, or validation claims. Preserve source provenance
when migrating established behavior.

Keep software verification, numerical verification, physical validation,
pedagogical validation, and uncertainty quantification distinct. Passing tests
or executing a notebook does not establish every scientific or pedagogical
claim.

## Teaching and manuscript content

Follow [`docs/lecture-notes/README.md`](docs/lecture-notes/README.md) for the
ownership of lecture notes, notebooks, reusable visualizers, computational
studies, figure scripts, and generated images.

## Reporting

Report the files changed, validation performed, relevant limitations, and any
unresolved decision. Mention unrelated working-tree state when it affects safety
or interpretation. Do not claim human acceptance, scientific validation, or
successor authorization from task completion alone.
