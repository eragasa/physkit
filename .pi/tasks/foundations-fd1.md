# FOUNDATIONS-FD1 — Accepted contract and implementation-plan handoff

**Status:** Bounded source-conformance correction completed; formal verification and notebook stages inactive

**Task ID:** `FOUNDATIONS-FD1`

**Template ID:** `PHYSKIT-CAPABILITY-DEVELOPMENT`

**Current stage:** `implementation` — corrected production-source handoff completed

**Resolved checkpoint:** `FOUNDATIONS-FD1-HC02 — ACCEPT`

**Accepted contract:** revision 3, exact artifact at `5766b281bfea890cc522cf651f36bd93c0493cbb`

**Artifact path:** Path A — reusable library interface required and notebook artifact required

**Implementation authorized:** completed only for FD1-SRC-F01 through FD1-SRC-F03 in the three correction-owned source paths; writer ownership inactive

**Successor authorization:** `false`; successor `null`

## Repository and administrative scope

- Repository: `https://github.com/eragasa/physkit`
- Branch: `main`
- Starting revision and initial `origin/main`: `5766b281bfea890cc522cf651f36bd93c0493cbb`
- Initial working tree:

  ```text
  ## main...origin/main
  ?? package-lock.json
  ```

This administrative step modifies exactly:

1. `.pi/active-state.json` — parent coordinator;
2. `.pi/tasks/foundations-fd1.md` — parent coordinator; and
3. `docs/capabilities/foundations/uniform-grid-dirichlet-laplacian.md` — capability architect scope, limited to acceptance status and acceptance record.

The unrelated untracked `package-lock.json` remains uninspected, unmodified, unstaged, and undeleted. The reusable chain and all role files remain immutable. Production, verification, evidence, Sphinx, documentation, notebook, dependency, packaging, and CI ownership remain inactive during this step.

## HC02 acceptance record

The human resolved `FOUNDATIONS-FD1-HC02 — human_contract_acceptance` with disposition `ACCEPT` for contract revision 3 exactly as represented at `5766b281bfea890cc522cf651f36bd93c0493cbb`.

Acceptance includes one integrated, internally layered Path A capability; immutable geometry-only `UniformGrid1D`; separate `HomogeneousDirichletStateSpace1D`; homogeneous-Dirichlet active space $V_h=\mathbb F^{N-2}$ for real or complex fields; `LinearOperator`; `DiscreteLinearOperator1D`; `FiniteDifferenceLaplacian1D`; explicit domain and codomain; scalar scaling with general composition deferred; positive $+d^2/dx^2$ convention; eager canonical SciPy CSR with dense inspection derived from CSR; real and complex application; the $N=3$ edge case; exact weighted norm, relative error, observed-order definitions, modes, grids, refinement pairs, and tolerances; complete NumPy-style source documentation; MyST/Sphinx documentation; generated inheritance and conceptual Graphviz diagrams; the canonical three-stage notebook; the lightweight VVUQ profile; and M1 new-clean-surface direction with competing implementations untouched.

Accepted evidence dispositions are:

- software verification: required;
- numerical verification: required;
- physical validation: `not-applicable-human-accepted-rationale`, because the capability makes no physical-model adequacy claim;
- pedagogical validation: required through proportional human checklist review; no formal learner study is required; and
- uncertainty quantification: `not-applicable-human-accepted-rationale`, because the capability makes no uncertainty-bearing claim.

Truncation error, convergence, resolution loss, and floating-point behavior remain numerical verification rather than UQ.

At the general base-class level, `LinearOperator.domain -> object` and `LinearOperator.codomain -> object` are accepted only as the minimal typing boundary for this capability. They establish no general PhysKit state-space hierarchy. `FiniteDifferenceLaplacian1D` must narrow both properties to `HomogeneousDirichletStateSpace1D`. Any general state-space abstraction, protocol, generic type system, or composition framework requires a separate future contract.

Acceptance does not authorize implementation, source changes, tests or evidence production, Sphinx creation, notebook creation or execution, adapters, migration, legacy repair, deprecation, deletion or relocation, symbolic operators, equation metadata infrastructure, quantum kinetic energy, Hamiltonians, eigensolvers, PIAB, lifecycle assignment, or successor work.

## Exact planned ownership — inactive until separately authorized

Every anticipated repository write path has exactly one owner. “Create” and “modify” refer to the anticipated implementation operation, not authorization in this step.

| Role owner | Exact path | Operation | Planned responsibility |
|---|---|---:|---|
| parent coordinator, narrow configuration exception | `pyproject.toml` | modify | add only a `docs` optional-dependency group containing `sphinx>=8,<10` and `myst-parser>=5.1,<6`; no notebook, Graphviz-wrapper, equation, or unrelated dependency |
| `physkit.physkit-implementation` | `src/physkit/discretization/grid_1d.py` | modify additively | add geometry-only `UniformGrid1D`; preserve existing `Grid1D` and `ActiveSetType1D` declarations and behavior |
| `physkit.physkit-implementation` | `src/physkit/discretization/state_space_1d.py` | create | implement `HomogeneousDirichletStateSpace1D` |
| `physkit.physkit-implementation` | `src/physkit/operators/base.py` | create | implement `LinearOperator` and private scalar-scaled wrapper behavior |
| `physkit.physkit-implementation` | `src/physkit/operators/discrete_1d.py` | create | implement `DiscreteLinearOperator1D` |
| `physkit.physkit-implementation` | `src/physkit/operators/finite_difference_1d.py` | create | implement `FiniteDifferenceLaplacian1D` and eager canonical CSR stencil |
| `physkit.physkit-implementation` | `src/physkit/discretization/__init__.py` | modify | export `UniformGrid1D` and `HomogeneousDirichletStateSpace1D` while preserving legacy exports |
| `physkit.physkit-implementation` | `src/physkit/operators/__init__.py` | create | export exactly the accepted operator names |
| `physkit.physkit-verification` | `tests/physkit/discretization/test_uniform_grid_1d.py` | create | grid validation, geometry, immutability, ownership, and public discretization import checks |
| `physkit.physkit-verification` | `tests/physkit/discretization/test_homogeneous_dirichlet_state_space_1d.py` | create | state-space identity, active data, restriction, embedding, dtype, exceptions, ownership, and public import checks |
| `physkit.physkit-verification` | `tests/physkit/operators/test_linear_operator.py` | create | base/discrete operator contracts, scalar scaling, domain/codomain preservation, typing limitation, and public operator import checks |
| `physkit.physkit-verification` | `tests/physkit/operators/test_finite_difference_laplacian_1d.py` | create | independent tridiagonal and componentwise stencil oracles; CSR, sign, $N=3,4,8$, real/complex application, scaling, and exact convergence tests |
| `physkit.physkit-verification` | `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | create | single proportional VVUQ and five-class evidence summary, including recorded pedagogical checklist disposition |
| `physkit.physkit-notebook-documentation` | `docs/conf.py` | create | exact accepted MyST/Sphinx configuration |
| `physkit.physkit-notebook-documentation` | `docs/index.md` | create | exact toctree and Graphviz `dot` installation/PATH prerequisite documentation |
| `physkit.physkit-notebook-documentation` | `docs/api/operators.md` | create | MyST autodoc/autoclass and generated inheritance diagram |
| `physkit.physkit-notebook-documentation` | `docs/concepts/uniform-grid-dirichlet-laplacian.md` | create | maintained concept surface and exactly ten stable labeled equations |
| `physkit.physkit-notebook-documentation` | `docs/_static/diagrams/uniform-grid-dirichlet-laplacian.dot` | create | conceptual Graphviz diagram and legend |
| `physkit.physkit-notebook-documentation` | `notebooks/numerics/differentiation/uniform-grid-dirichlet-laplacian.ipynb` | create | canonical three-stage notebook and proportional pedagogical-checklist material |
| `physkit.physkit-capability-integration-reviewer` | all planned artifacts above | read-only | independent integrated review; no repairs |
| capability architect | accepted contract path only | inactive/read-only | writes only if a material contract finding is routed, followed by renewed human contract acceptance |

The narrow planned `pyproject.toml` assignment is an explicit parent-owned configuration exception because the current specialized writer role definitions do not authorize packaging metadata. It remains inactive and requires separate implementation authorization. Jupyter and `nbconvert` are external execution-environment prerequisites, not planned repository dependencies: preflight must run `python -m jupyter nbconvert --version` and import `nbformat` and `nbconvert` before notebook work. If either prerequisite is unavailable, stop and request human authorization for an exact repository-managed dependency change rather than adding one silently.

## Dependency order and permitted concurrency

1. **Plan activation gate.** A later explicit human instruction must activate exact planned ownership and implementation; until then all planned writer ownership is inactive.
2. **Dependency metadata.** The parent-owned `pyproject.toml` change precedes reproducible Sphinx environment installation.
3. **Production foundation.** `UniformGrid1D` precedes `HomogeneousDirichletStateSpace1D`; both precede the operator hierarchy. `LinearOperator` precedes `DiscreteLinearOperator1D`, which precedes `FiniteDifferenceLaplacian1D`; package exports follow defining modules.
4. **Explicit notebook Stage 1.** After ownership activation, Stage 1 may run concurrently with production implementation because it uses direct NumPy/SciPy construction only, does not import the new API, and its path does not overlap source paths.
5. **Library reconstruction.** Notebook Stage 2 and API-facing documentation wait for completed accepted API implementation and public exports.
6. **Exploration and synchronization.** Notebook Stage 3, concept equations, API page, conceptual DOT, and synchronization checks follow Stage 2.
7. **Verification.** Software and numerical verification begin only after all selected Path A implementation, documentation, and notebook artifacts are complete; verification does not assess partial source.
8. **Evidence summary.** The consolidated five-class summary follows test execution, notebook execution, Sphinx build, and documentation synchronization checks.
9. **Independent review.** Read-only integration review follows all writer handoffs and the complete evidence summary.
10. **Correction.** Any correction is sequential with respect to review of affected artifacts; affected checks replay before re-review.
11. **Parent verification and human stop.** Parent verification follows successful review/correction disposition and stops at `human_final_acceptance`.

Read-only inspection and nonmutating checks may run concurrently. Parent configuration work, source work, and notebook Stage 1 may run concurrently only after separate ownership activation because their paths and seams are nonoverlapping. No overlapping writers are permitted.

## Integration seams

- `src/physkit/discretization/__init__.py` is the public seam for accepted grid and state-space imports used by tests, docs, and notebook Stage 2.
- `src/physkit/operators/__init__.py` is the public seam for the exact operator hierarchy.
- `HomogeneousDirichletStateSpace1D.semantic_identity` is the compatibility seam among geometry, state interpretation, operator domain/codomain, tests, diagrams, and notebook comparison.
- The immutable state-space instance is both concrete Laplacian domain and codomain; base-class `object` annotations do not create a general hierarchy.
- The eager owned CSR matrix is the computational authority; dense inspection derives only from CSR. Tests use independent direct tridiagonal and componentwise-stencil oracles, not production matrix construction helpers.
- `docs/concepts/uniform-grid-dirichlet-laplacian.md` is the maintained equation authority; source docstrings remain API-behavior authority; tests and notebook synchronize with both.
- Notebook Stage 1 is independent of PhysKit; Stage 2 compares the accepted API to Stage 1; Stage 3 uses the exact accepted modes, grids, norms, refinement pairs, and tolerances.
- `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` is the single final evidence-summary path consumed by independent review and parent verification.
- Pedagogical checklist material is prepared in the notebook by `physkit.physkit-notebook-documentation`; the actual checklist disposition is recorded, without inventing human acceptance, in the verification-owned summary.

## Planned implementation slices

### Production source

1. Add `UniformGrid1D` to `src/physkit/discretization/grid_1d.py` without changing existing competing declarations. Implement accepted scalar validation, $N\ge3$, spacing, coordinates, defensive `float64` copies, geometry-only behavior, and observable immutability.
2. Create `src/physkit/discretization/state_space_1d.py` with exact semantic identity, immutable grid containment, boundaries, active indices/coordinates, dimension, restriction and embedding, finite numeric validation, dtype rules, exceptions, and owned C-contiguous outputs.
3. Create the three operator defining modules. Implement exact domain/codomain, shape/dtype, `apply`, `@`, private scalar scaling, eager canonical owned CSR, defensive sparse/dense copies, and the $N=3$ construction branch. Do not add public composition or any general state-space abstraction.
4. Update/create package exports only after defining modules exist. Every maintained first-party module and public member receives complete NumPy-style documentation.

### Verification and evidence

- Public-import checks live in the four exact test paths above; no fifth import-test path is planned.
- Independent oracle coverage lives in `test_finite_difference_laplacian_1d.py` and directly constructs expected arrays/stencil values without calling production construction helpers.
- Convergence coverage in that same file uses $u_n=\sin(n\pi x)$ for $n=1,2$, $N=17,33,65,129$, the exact weighted norm and relative error, monotonic decrease, and only $p_{n;33,65}$ and $p_{n;65,129}\in[1.90,2.10]$.
- Software and numerical verification remain distinct in assertions and summary claims. Physical validation and UQ retain the accepted Not-applicable rationales. Pedagogical validation remains required and human-owned through the proportional checklist; notebook execution is not pedagogical acceptance.

### Notebook and documentation

- Stage 1 exposes raw mathematical/computational construction, restriction/embedding, CSR/dense forms, real/complex action, and $N=3$ without PhysKit.
- Stage 2 reconstructs Stage 1 with the accepted public API and compares geometry, semantic identity, domain/codomain, matrices, real/complex action, and scaling.
- Stage 3 performs the accepted convergence exploration and a bounded under-resolution illustration, explicitly classifying truncation, resolution, and floating-point effects as numerical verification.
- `docs/index.md` documents that Sphinx does not install Graphviz and that the system `dot` executable must be installed and on `PATH`.
- No rendered Graphviz product or `docs/_build` output is committed.

## Proposed validation commands

Environment and imports:

```bash
git rev-parse --show-toplevel
git rev-parse HEAD
git branch --show-current
git remote -v
git status --short --branch --untracked-files=all
python -m pip install -e '.[dev,docs]'
python -m compileall -q src/physkit
python -c "from physkit.discretization import UniformGrid1D, HomogeneousDirichletStateSpace1D; from physkit.operators import LinearOperator, DiscreteLinearOperator1D, FiniteDifferenceLaplacian1D"
```

Tests:

```bash
python -m pytest -q \
  tests/physkit/discretization/test_uniform_grid_1d.py \
  tests/physkit/discretization/test_homogeneous_dirichlet_state_space_1d.py \
  tests/physkit/operators/test_linear_operator.py \
  tests/physkit/operators/test_finite_difference_laplacian_1d.py
python -m pytest -q
```

Sphinx and Graphviz:

```bash
dot -V
dot -Tsvg docs/_static/diagrams/uniform-grid-dirichlet-laplacian.dot \
  -o /tmp/uniform-grid-dirichlet-laplacian.svg
sphinx-build -W --keep-going -b html docs docs/_build/html
```

Notebook execution uses the externally provisioned Jupyter/nbconvert environment and fails closed if preflight is unavailable:

```bash
python -m jupyter nbconvert --version
python -c "import nbformat, nbconvert; print(nbformat.__version__, nbconvert.__version__)"
python -m jupyter nbconvert --execute --to notebook \
  notebooks/numerics/differentiation/uniform-grid-dirichlet-laplacian.ipynb \
  --output-dir /tmp \
  --output uniform-grid-dirichlet-laplacian.executed.ipynb
```

Final deterministic checks:

```bash
git diff --check
git status --short --branch --untracked-files=all
```

Also parse source and executed notebook JSON and reject any `output_type: error`; confirm each of the ten required MyST equation labels occurs exactly once repository-wide; confirm no public `compose`, equation registry/specification/decorator/renderer/catalog, parallel RST page, or tracked `_build`/rendered Graphviz product was introduced; and report any pre-existing legacy full-suite failure without repairing excluded paths or changing accepted criteria.

## M1 excluded legacy paths and work

M1 is additive. The only planned legacy-containing file modification is the addition of `UniformGrid1D` beside existing declarations in `src/physkit/discretization/grid_1d.py`; existing `Grid1D` and `ActiveSetType1D` behavior remains untouched. The existing `src/physkit/discretization/__init__.py` is modified only to add accepted exports while preserving legacy exports.

Explicitly untouched:

- `src/physkit/core/boundaries.py`;
- `src/physkit/core/grids.py`;
- `src/physkit/core/state.py`;
- `src/physkit/core/operator.py`;
- `src/physkit/numerics/finite_difference.py`;
- `src/physkit/numerics/differentiation/__init__.py`;
- `src/physkit/numerics/differentiation/laplacian.py`;
- `src/physkit/math/operators/__init__.py`;
- `src/physkit/math/operators/base.py`;
- `src/physkit/math/operators/continuous1d.py`;
- `src/physkit/math/operators/discrete1d.py`;
- `tests/physkit/discretization/test_ActiveSetType1D.py`;
- `tests/physkit/discretization/test_Grid1D.py`;
- `notebooks/numerics/differentiation/finite-difference-laplacian-1d.ipynb`;
- all existing QM, PIAB, Hamiltonian, eigensolver, Poisson, example, adapter, migration, deprecation, lifecycle, and CI paths; and
- `package-lock.json`.

No adapter, migration, repair, deprecation, deletion, relocation, replacement, symbolic operator, equation metadata infrastructure, kinetic-energy operator, Hamiltonian, eigensolver, PIAB work, lifecycle assignment, or successor is planned or authorized.

## Correction routing and review

- production-source finding → `physkit.physkit-implementation` within unchanged exact source ownership;
- test or evidence finding → `physkit.physkit-verification`;
- notebook, MyST/Sphinx, conceptual DOT, or user-documentation finding → `physkit.physkit-notebook-documentation`;
- task, active-state, ownership, dependency-metadata, or orchestration finding → parent coordinator;
- nonmaterial contract clarification → capability architect after parent classification;
- material contract revision → capability architect, then renewed explicit human contract acceptance and a recomputed ownership plan before dependent replay;
- protected decision → immediate human escalation.

The independent reviewer never repairs reviewed work. `correction_cycle_count` is already `1` from the HC02 remand correction, so the immutable workflow's one ordinary automatic correction allowance is exhausted and **no automatic implementation correction/replay/re-review cycle remains**. Any later finding routes directly to `bounded-cycle-exhausted` and human escalation unless a separate human decision explicitly authorizes otherwise.

## Explicitly human-authorized post-handoff source correction

Starting from `25c96cf43ce8820e79fce670e400451a4eedd1ca`, the human authorized one bounded conformance correction for FD1-SRC-F01 (Boolean contamination before NumPy coercion), FD1-SRC-F02 (endpoint canonicalization exception taxonomy), and FD1-SRC-F03 (scaling canonicalization exception taxonomy). This authorization is external to the reusable template's automatic correction loop: `correction_cycle_count` remains historically `1` and is neither reset nor incremented.

During correction, `physkit.physkit-implementation` owns exactly `src/physkit/discretization/grid_1d.py`, `src/physkit/discretization/state_space_1d.py`, and `src/physkit/operators/base.py`. The parent owns exactly `.pi/active-state.json` and this task record. No test, evidence, contract, notebook, documentation, dependency, lifecycle, PIAB, or successor work is authorized. The accepted contract remains revision 3 at `5766b281bfea890cc522cf651f36bd93c0493cbb`.

## Production-source implementation authorization

The human explicitly authorized the `implementation` stage from `d5fc0dee79ebff5dbe6375f9b0c32661853b1e83` for exactly these seven source-writer paths:

1. `src/physkit/discretization/grid_1d.py`;
2. `src/physkit/discretization/state_space_1d.py`;
3. `src/physkit/discretization/__init__.py`;
4. `src/physkit/operators/base.py`;
5. `src/physkit/operators/discrete_1d.py`;
6. `src/physkit/operators/finite_difference_1d.py`; and
7. `src/physkit/operators/__init__.py`.

The parent coordinator owns only `.pi/active-state.json` and this task record. Ownership does not overlap. Tests, evidence, Sphinx, documentation pages, diagrams, notebooks, dependencies, packaging, CI, legacy changes, PIAB, lifecycle, final acceptance, and successor work remain inactive.

## Production-source handoff

**Result:** completed for the bounded production-source layer; source-writer ownership is now inactive.

**Starting revision:** `d5fc0dee79ebff5dbe6375f9b0c32661853b1e83`

**Accepted authority:** FOUNDATIONS-FD1 contract revision 3 at `5766b281bfea890cc522cf651f36bd93c0493cbb` and the exact implementation plan committed at the starting revision.

### Exact source changes

- modified `src/physkit/discretization/grid_1d.py` additively with immutable geometry-only `UniformGrid1D`; legacy `Grid1D` and `ActiveSetType1D` remain unchanged;
- created `src/physkit/discretization/state_space_1d.py` with immutable `HomogeneousDirichletStateSpace1D`, exact semantic identity, restriction, embedding, and real/complex canonicalization;
- modified `src/physkit/discretization/__init__.py` to preserve legacy exports and add the accepted grid/state-space exports;
- created `src/physkit/operators/base.py` with `LinearOperator` and a private immutable scaled wrapper;
- created `src/physkit/operators/discrete_1d.py` with `DiscreteLinearOperator1D` and defensive dense inspection;
- created `src/physkit/operators/finite_difference_1d.py` with the eager canonical positive-second-derivative CSR Laplacian, including exact `N=3` behavior; and
- created `src/physkit/operators/__init__.py` with exactly the accepted public operator exports.

### Complete source-writer and parent reading inventory

`AGENTS.md`; `.pi/active-state.json`; `.pi/tasks/foundations-fd1.md`; `.pi/chains/capability-development.chain.json`; `.pi/agents/physkit-implementation.md`; `docs/capabilities/foundations/uniform-grid-dirichlet-laplacian.md`; `src/physkit/discretization/grid_1d.py`; `src/physkit/discretization/state_space_1d.py`; `src/physkit/discretization/__init__.py`; `src/physkit/__init__.py`; `pyproject.toml`; `src/physkit/core/grids.py`; `src/physkit/core/state.py`; `src/physkit/core/operator.py`; `src/physkit/numerics/finite_difference.py`; `src/physkit/numerics/differentiation/laplacian.py`; `src/physkit/math/operators/base.py`; `src/physkit/math/operators/continuous1d.py`; `src/physkit/math/operators/discrete1d.py`; `tests/physkit/discretization/test_ActiveSetType1D.py`; and `tests/physkit/discretization/test_Grid1D.py`.

### Developmental checks

- exact seven-path `.venv/bin/python -m py_compile`: PASS;
- accepted public imports with `PYTHONPATH=src`: PASS;
- temporary comprehensive writer smoke check: PASS after correcting an overly strict temporary bitwise floating-point oracle; no repository test artifact was created;
- parent temporary smoke check covering validation, ownership, semantic identity, restriction/embedding, inheritance, domain/codomain identity, CSR canonicalization and defensive copies, exact `N=3,4,8` matrices, negative definiteness, real/complex application, scaling, public documentation presence, and absence of `compose`: PASS after correcting a bug in the temporary parent script;
- unchanged legacy discretization tests: `17 passed`;
- `git diff --check`: PASS; and
- parent complete source inspection and read-only contract-conformance verification: PASS with no unresolved finding.

These are developmental implementation checks only. They are not the required software-verification or numerical-verification evidence and do not establish physical validation, pedagogical validation, UQ, final acceptance, lifecycle status, or support.

### Explicitly untouched

`pyproject.toml`; all tests; evidence summaries; Sphinx configuration/pages; diagrams; notebooks; dependencies; packaging; CI; all competing `core`, `math.operators`, `numerics`, QM, and PIAB implementations; lifecycle records; and `package-lock.json`.

## Explicitly human-authorized source-correction handoff

**Result:** FD1-SRC-F01, FD1-SRC-F02, and FD1-SRC-F03 corrected in exactly the three source-owned paths; source-writer ownership is inactive after handoff.

**Starting revision:** `25c96cf43ce8820e79fce670e400451a4eedd1ca`

**Authority:** explicit human bounded authorization outside the reusable template's automatic correction loop. The historical `correction_cycle_count` remains `1`; it was not reset, incremented, consumed, or reinterpreted.

### Corrected findings

- `FD1-SRC-F01` — `_validated_numeric_vector` now detects Boolean elements before ordinary NumPy coercion can erase their type. Pure Boolean arrays and mixed Boolean/numeric sequences raise `TypeError` through `restrict`, `embed`, `apply`, and `@`; object, string, ragged, and nonnumeric inputs remain `TypeError`; wrong rank, wrong length, and nonfinite numeric inputs remain `ValueError`; valid real and complex inputs retain canonical owned C-contiguous outputs.
- `FD1-SRC-F02` — after endpoint semantic-type validation, controlled built-in-float canonicalization maps correctly typed but unrepresentable endpoints to `ValueError`; nonfinite endpoints remain `ValueError`; wrong semantic types and Booleans remain `TypeError`; valid endpoints remain built-in `float` without changing grid semantics.
- `FD1-SRC-F03` — after scale-factor semantic-type validation, controlled built-in scalar canonicalization maps correctly typed but unrepresentable factors to `ValueError`; nonfinite canonical factors remain `ValueError`; wrong semantic types and Booleans remain `TypeError`; valid factors remain built-in `float` or `complex` without changing dtype, domain, codomain, ownership, or application semantics.

### Developmental checks and parent verification

- exact three-path `.venv/bin/python -m py_compile`: PASS;
- required exception-taxonomy smoke cases, including every human-specified Boolean and large-integer case: PASS;
- valid real/complex restriction, embedding, application, and ordinary scaling: PASS;
- exact `N=3,4,8` matrices, public imports, defensive ownership, and absence of public `compose`: PASS;
- unchanged legacy discretization tests: `17 passed in 0.03s`;
- complete parent read-only inspection of the three-source-file diff: PASS, with no unrelated refactor, unintended input narrowing, or unresolved finding; and
- coordination JSON parsing, exact-path isolation, diff checks, and complete status are required before commit.

These are developmental correction checks only, not formal software-verification or numerical-verification evidence. The accepted FD1 contract remains revision 3 at `5766b281bfea890cc522cf651f36bd93c0493cbb` and was not revised.

### Root-policy synchronization and preserved history

State revision 18 projects the accepted `AGENTS.md` content revision `283a9bb0681892d71698c9eba314342b54924503`. The administrative acceptance record is revision `25c96cf43ce8820e79fce670e400451a4eedd1ca`. The earlier root-policy acceptance decision at `a806fcdd5c1c63881a3bd41c7aea2827300818b9` remains unchanged as historical provenance. A new durable decision record limits the flexible numerical pedagogy acceptance to its stated boundary and defers analytical, symbolic, formal-proof, and mixed-modality workflow design without authorizing chain, role, FD1-contract, notebook, lifecycle, PIAB, or successor work.

## Completion and stop

State revision 18 records the corrected production-source layer as complete. Source-writer ownership and every formal test/evidence, Sphinx, documentation, diagram, notebook, dependency, packaging, and CI writer role are inactive. PIAB remains parked. Successor authorization is `false` and successor is `null`. The next planned writer stage remains inactive pending separate human authorization.

Any finding after this handoff requires human disposition; no automatic post-handoff correction cycle is available. Tests, notebook execution, Sphinx build, review, commit, push, silence, or implementation completion do not imply software or numerical verification, evidence adequacy, final acceptance, lifecycle status, support, closeout, or successor authorization.
