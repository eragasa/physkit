# FOUNDATIONS-FD1 preliminary verification evidence

**Status:** Preliminary task-local early formal-verification record; the reusable `evidence_production_and_assessment` stage is not complete.

**Accepted authority:** `docs/capabilities/foundations/uniform-grid-dirichlet-laplacian.md`, contract revision 3 accepted at `5766b281bfea890cc522cf651f36bd93c0493cbb`

**Execution baseline:** repository `https://github.com/eragasa/physkit`, branch `main`, starting revision `5ae0b8792e29cb764866d2600acc3ce47924536e`, active-state revision 19

## Startup preflight

Preflight passed. `AGENTS.md`, `.pi/active-state.json`, `.pi/tasks/foundations-fd1.md`, `.pi/chains/capability-development.chain.json`, `.pi/agents/physkit-verification.md`, the accepted contract, intake, accepted production modules and exports, legacy discretization tests, and `pyproject.toml` were read and reconciled. Active state and the task record explicitly instantiate `PHYSKIT-CAPABILITY-DEVELOPMENT` as `FOUNDATIONS-FD1`, resolve `human_contract_acceptance:explicitly-accepted`, record the completed ownership and implementation plan, and activate only `physkit.physkit-verification` at `task-local-early-formal-verification`.

The explicit human FD1-local prerequisite exception waives only the reusable template ordering that would otherwise place notebook and documentation stages before test and preliminary-evidence authoring. It does not complete the evidence stage or waive any notebook, documentation, review, parent-verification, or human-acceptance obligation.

Exact writer ownership was limited to the four test modules and this summary. Production source, chain and role definitions, notebooks, Sphinx/API/concept documentation, diagrams, dependencies, packaging, CI, lifecycle, PIAB, closeout, and successor state were prohibited. The initial complete status was:

```text
## main...origin/main
 M .pi/active-state.json
 M .pi/tasks/foundations-fd1.md
?? package-lock.json
```

The two modified coordination files are parent-owned activation changes. The unrelated `package-lock.json` was not inspected or altered. Successor authorization is false and the stop condition is this early-verification handoff.

## Environment and commands

The required interpreter was `/Users/eugene/repos/physkit/.venv/bin/python`; nothing was installed. Environment versions were Python 3.14.6, NumPy 2.5.1, SciPy 1.18.0, and pytest 9.1.1.

| Command | Result |
|---|---|
| `/Users/eugene/repos/physkit/.venv/bin/python -m pytest -q tests/physkit/discretization/test_uniform_grid_1d.py tests/physkit/discretization/test_homogeneous_dirichlet_state_space_1d.py tests/physkit/operators/test_linear_operator.py tests/physkit/operators/test_finite_difference_laplacian_1d.py` | Initial author-test classification failure (`105 passed, 1 failed`); the rectangular numeric array was correctly reclassified from wrong semantic type to wrong rank, without changing an accepted criterion |
| same exact four-module command after test correction | PASS: `106 passed in 0.15s` |
| same exact four-module command after parent completeness additions | PASS: `110 passed in 0.19s` |
| `/Users/eugene/repos/physkit/.venv/bin/python -m pytest -q tests/physkit/discretization/test_ActiveSetType1D.py tests/physkit/discretization/test_Grid1D.py` | PASS: `17 passed in 0.05s` |
| `/Users/eugene/repos/physkit/.venv/bin/python -m pytest -q` | UNRELATED COLLECTION FAILURE: two errors in constants tests because `PhysicalConstantsProtocol` cannot be imported from `physkit.constants`; no excluded path was repaired |
| deterministic convergence-value reporting command | PASS; values recorded below |

## Claims, methods, and results

### Software-verification checks

The focused tests check only accepted public behavior:

- exact public operator `__all__`, defining-class identity, and explicit absence of composition, symbolic, equation-registry/specification/decorator/renderer/catalog, and quantum APIs from the public namespace;
- geometry/state-space separation, scalar validation, finite/order/size invariants, exact geometry, immutability, defensive coordinate ownership, and unrepresentable huge positive/negative values in both endpoint positions;
- exact state-space semantic identity, active data, boundaries, restriction and embedding, real/complex canonical dtype, C-contiguous ownership, input non-retention, and required exception taxonomy;
- abstract operator hierarchy, the accepted general `object` typing boundary, `@` delegation, CSR-derived dense inspection, scalar validation and observable real/complex scaling behavior, endpoint preservation, scaled-result ownership/C-contiguity/input non-aliasing, and immutability; and
- concrete Laplacian domain/codomain narrowing, CSR format and canonicalization, sign, symmetry, negative definiteness, defensive sparse/dense ownership, real/complex application, scaling, and `N=3` behavior.

No private wrapper fields are accessed. Valid scaling canonicalization is established externally through public dtype, application, domain, codomain, and shape behavior.

### Independent software/numerical oracles

`tests/physkit/operators/test_finite_difference_laplacian_1d.py` does not call a production construction helper for its references. It builds the expected matrices entry-by-entry in a dense zero array for `N=3,4,8`, and separately applies the component stencil to explicitly zero-padded full vectors. Real and complex application and scaling use the accepted tolerance

```text
rtol = 5e-14
atol = 5e-14 * max(1, ||reference||_inf)
```

All checks passed. The `N=3`, `[0,1]` matrix was exactly `[[-8.0]]`; the tested matrices were symmetric negative definite with negative diagonal and positive adjacent off-diagonal entries, confirming the accepted `+d²/dx²` sign.

### Bounded convergence evidence

For `u_n(x)=sin(n*pi*x)`, exact derivative `-(n*pi)^2 u_n`, `[0,1]`, `n=1,2`, `N=17,33,65,129`, and the accepted weighted discrete relative norm, the observed values were:

| Mode | Relative errors for `N=17,33,65,129` | `p(33,65)` | `p(65,129)` |
|---:|---|---:|---:|
| 1 | `3.2086359550396746e-3`, `8.029324607680985e-4`, `2.0078148840046783e-4`, `5.0198395912248674e-5` | `1.9996523773349906` | `1.9999130934348877` |
| 2 | `1.2785169233341841e-2`, `3.2086359550396776e-3`, `8.029324607689942e-4`, `2.0078148840175068e-4` | `1.9986095691700794` | `1.9996523773273818` |

Errors decreased on every refinement and every accepted order lay in `[1.90,2.10]`. This is numerical verification limited to the accepted modes, grids, interval, norm, homogeneous boundaries, and binary64 environment; it is not physical validation, pedagogical validation, or UQ.

## Five-class preliminary disposition

### Software verification

- **Applicability:** required.
- **Required claim:** implementation conforms to the accepted public API, invariants, error taxonomy, ownership, CSR, real/complex behavior, domain/codomain, and scaling contract.
- **Producer and paths:** `physkit.physkit-verification`; the four focused test modules and this summary.
- **Method/reference:** independent arrays and public behavior against contract Sections 6–13, criteria 1–4 and 6.
- **Criterion:** exact requirements and accepted application tolerance above.
- **Reviewer:** later `physkit.physkit-capability-integration-reviewer`; not invoked in this slice.
- **Result state / observed outcome:** `required-incomplete` / `passed` for the authorized focused checks.
- **Limitations and claim boundary:** preliminary evidence remains unreviewed and later cross-artifact synchronization is unavailable; no physical, pedagogical, lifecycle, or support claim.
- **Blocks final handoff:** yes, until later required artifacts, review, replay as applicable, and human disposition are complete.

### Numerical verification

- **Applicability:** required.
- **Required claim:** the implementation represents the accepted stencil and meets the bounded second-order claim.
- **Producer and paths:** `physkit.physkit-verification`; `tests/physkit/operators/test_finite_difference_laplacian_1d.py` and this summary.
- **Method/reference:** independent entry-by-entry tridiagonal oracle, componentwise zero-boundary stencil oracle, analytical sine derivative, exact weighted norm, grids, and refinement pairs from contract Sections 5 and 13.
- **Criterion:** exact matrices for `N=3,4,8`; accepted application tolerance; monotone errors; only `p(33,65)` and `p(65,129)` in `[1.90,2.10]` for modes 1 and 2.
- **Reviewer:** later integration reviewer; not invoked in this slice.
- **Result state / observed outcome:** `required-incomplete` / `passed` for the authorized numerical checks.
- **Limitations and claim boundary:** restricted to `[0,1]`, modes 1 and 2, listed grids and norm, homogeneous boundaries, and this binary64 environment. No high-frequency, nonsmooth, physical-model, or uncertainty claim.
- **Blocks final handoff:** yes, because review and the complete selected Path A artifact/evidence stage remain pending.

### Physical validation

- **Applicability:** `not-applicable-human-accepted-rationale`; the accepted capability makes no physical-model adequacy claim.
- **Required claim:** no physical-validation conclusion is claimed.
- **Producer/path:** disposition recorded by `physkit.physkit-verification` in this summary.
- **Method/reference and criterion:** contract Sections 4–5 and the human-accepted non-applicability rationale.
- **Reviewer:** later integration reviewer.
- **Result state / observed outcome:** `not-applicable-human-accepted-rationale` / `not-run`.
- **Limitations and claim boundary:** any later physical use requires model- and regime-specific validation; numerical agreement cannot satisfy this class.
- **Blocks final handoff:** no for this accepted rationale.

### Pedagogical validation

- **Applicability:** required through proportional human checklist review; no formal learner study is required.
- **Required claim:** a human checklist confirms that the accepted distinctions, objectives, stages, and equations are exposed without material ambiguity.
- **Producer/path:** notebook/documentation writer later prepares the notebook material; verification records the later disposition in this path.
- **Method/reference and criterion:** contract Sections 2 and 14; every accepted objective and stage correctly explained with no material misconception or accessibility blocker.
- **Reviewer:** later integration reviewer, then human.
- **Result state / observed outcome:** `required-incomplete` / `not-run`.
- **Limitations and claim boundary:** notebook work is prohibited in this slice; execution would not itself establish pedagogical validation or broad educational effectiveness.
- **Blocks final handoff:** yes.

### Uncertainty quantification

- **Applicability:** `not-applicable-human-accepted-rationale`; inputs are deterministic and exact for the bounded claims, with no uncertainty distribution or interval claim.
- **Required claim:** no UQ conclusion is claimed.
- **Producer/path:** disposition recorded by `physkit.physkit-verification` in this summary.
- **Method/reference and criterion:** contract Sections 4–5 and the human-accepted non-applicability rationale.
- **Reviewer:** later integration reviewer.
- **Result state / observed outcome:** `not-applicable-human-accepted-rationale` / `not-run`.
- **Limitations and claim boundary:** truncation, convergence, resolution loss, and floating-point behavior remain numerical verification, not UQ.
- **Blocks final handoff:** no for this accepted rationale.

## Failures, limitations, and replay obligations

The only focused-test failure was an authoring error in exception classification for a rectangular numeric vector. The test was corrected to the already accepted wrong-rank `ValueError` rule and all four focused modules were replayed successfully; no criterion or source behavior changed.

The complete repository suite remains unable to collect because of two unrelated constants import errors in `tests/physkit/constants/test_ConstantsCGS.py` and `tests/physkit/constants/test_ConstantsSI.py`. This does not invalidate the passing focused and unchanged legacy runs, but it prevents a claim that the complete repository suite passes. No excluded source/test path was changed.

After any future source correction affecting grid, state-space, operator, scalar scaling, or Laplacian behavior, replay all four focused modules, both unchanged legacy discretization modules, the convergence-value report, and the complete repository suite without weakening criteria. After later notebook/documentation construction, refresh this preliminary summary and run all synchronization, Sphinx, notebook, integration-review, and parent-verification checks authorized at that time.
