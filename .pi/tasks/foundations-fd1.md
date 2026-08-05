# FOUNDATIONS-FD1 — Documented discrete 1D Laplacian capability contract

**Status:** Awaiting human contract acceptance

**Task ID:** `FOUNDATIONS-FD1`

**Template ID:** `PHYSKIT-CAPABILITY-DEVELOPMENT`

**Current stage:** `human_contract_acceptance` pending (`FOUNDATIONS-FD1-HC02`)

**Resolved checkpoint:** `FOUNDATIONS-FD1-HC01` accepted by explicit human decision

**Selected capability:** integrated, internally layered uniform closed 1D grid, active interior state, homogeneous-Dirichlet discrete linear operator, and finite-difference Laplacian

**Artifact path:** Path A — reusable library interface required and notebook artifact required

**Successor authorization:** `false`; successor `null`

## Repository and starting state

- Repository: `https://github.com/eragasa/physkit`
- Branch: `main`
- Starting revision and initial `origin/main`: `a056157909f1dabc679332c73cabdda956075417`
- Initial working tree:

  ```text
  ## main...origin/main
  ?? package-lock.json
  ```

The unrelated untracked `package-lock.json` must remain uninspected, unmodified, unstaged, and undeleted.

## HC01 accepted scope

The human selected one integrated but internally layered, discrete-first capability covering only:

- a uniform closed grid on $[a,b]$ with $b>a$, $N\geq3$, and $h=(b-a)/(N-1)$;
- active indices $1,\ldots,N-2$ and $V_h=\mathbb F^{N-2}$ for $\mathbb F\in\{\mathbb R,\mathbb C\}$;
- homogeneous Dirichlet endpoint semantics;
- a general discrete linear-operator abstraction with a one-dimensional specialization;
- $\mathbf D_{2,h}=h^{-2}\operatorname{tridiag}(1,-2,1)$ representing $d^2/dx^2$, not its negative;
- CSR as the proposed canonical computational representation derived from one stencil rule, with explicit dense inspection;
- application to real and complex active states;
- complete NumPy-style source documentation, minimal Sphinx API/concept documentation with generated and conceptual diagrams, and one three-stage notebook; and
- a proportional lightweight VVUQ development profile.

The hierarchy must be equivalent in meaning to `LinearOperator -> DiscreteLinearOperator1D -> FiniteDifferenceLaplacian1D`. A future quantum kinetic-energy operator uses or scales the Laplacian; it must not subclass it. Symbolic production support is deferred and may not determine the discrete API.

Path A is selected with independent axes `reusable_library_interface: required` and `notebook_artifact: required`. This scope decision accepts neither the proposed API nor an implementation, notebook path, evidence result, lifecycle state, canonical artifact, validation conclusion, or support claim.

## Exact ownership

The parent coordinator owns exactly:

1. `.pi/active-state.json`; and
2. `.pi/tasks/foundations-fd1.md`.

The capability architect owns exactly:

1. `docs/capabilities/foundations/uniform-grid-dirichlet-laplacian.md`.

Production source, tests, evidence outputs, notebooks, Sphinx implementation files, dependencies, packaging, and CI have no active writer ownership. The immutable chain template and role files remain unchanged.

## External technical reference boundary

The architect may inspect `eragasa/ksdft2effmass` revision `355df16a7ca4071b70bc844a00ba21949af7c7c6` as a read-only technical reference for source-documentation quality, NumPy docstrings, scientific/numerical documentation, exception semantics, Sphinx API documentation, proportional VVUQ classification, and synchronized source/tests/Sphinx/examples.

The architect must not import its harness, CPN, checkpoint/evidence/checksum/ownership machinery, skills, chains, agents, serialization/Rust requirements, class-per-file rules, or campaign/HPC controls.

## Contract requirements

The sole material artifact must address all 28 content areas in the human authorization, including the mathematical/state-space contract, hierarchy and composition boundaries, CSR/dense behavior, proposed public API, invariants/error taxonomy, real/complex behavior, source-documentation standard, Sphinx bootstrap and diagram surfaces, three-stage notebook, Path A, lightweight VVUQ profile, all five evidence dispositions, acceptance criteria, competing implementation treatment, exclusions, unresolved contract decisions, and implementation authorization boundary.

The evidence proposals are: software verification required; numerical verification required; physical validation proposed for human-approved Not applicable within mathematical/numerical claims only; pedagogical validation required but proportional; and UQ proposed for human-approved Not applicable because no uncertainty-bearing claim is made.

## Review and correction

Mode A applies. One fresh independent read-only review must cover mathematics, state space, boundaries/sign, inheritance/composition, future quantum suitability, discrete-first scope, symbolic deferral, source and Sphinx documentation, diagram authority, Path A, proportional VVUQ, exclusion of ksdft2effmass ceremony, and absence of premature implementation.

At most one consolidated contract correction pass is allowed. An unresolved protected choice is escalated to the human rather than silently resolved.

## Prohibited work and stop condition

Do not modify source, tests, notebooks, examples, dependencies, packaging, CI, Sphinx files, chain templates, role files, existing harness/intake documents, or `package-lock.json`. Do not begin implementation, verification writing, Sphinx creation, notebook editing, migration, deprecation, repair, lifecycle assignment, PIAB, or successor work.

After drafting, validation, independent review, any single allowed correction, parent verification, exact commit, and fast-forward push, stop at `human_contract_acceptance`. Human acceptance cannot be inferred from review, validation, commit, or push.

## Consolidated Mode A correction

The independent read-only review returned `REMAND`. The parent classified the findings as deterministic in-scope proposal conformance, not a new protected choice, and activated the architect for the single allowed consolidated correction pass (`correction_cycle_count: 1`). The correction must resolve the Sphinx/MyST/build-command/Graphviz dependency issue; both diagram surfaces and their authority; the $N=3$ CSR edge case; eager construction and wrapper dtype/ownership behavior; semantic grid compatibility; explicit continuous/discrete/software/reference/physical distinctions; and exact proportional VVUQ and pedagogical-review wording. A fresh read-only rereview is required. No second automatic correction is authorized.

## Mode A rereview and human contract checkpoint

The architect completed the single consolidated correction pass. A fresh independent read-only Mode A rereview returned `PASS` with no blocker, major, or minor findings. The correction cycle count is `1`; no second automatic correction is authorized. Parent deterministic contract validation passed. Remote freshness remains required immediately before the boundary commit and push.

Checkpoint `FOUNDATIONS-FD1-HC02` requests explicit human disposition of the sole material contract: accept, revise, reject, or defer. Implementation and every dependent writer stage remain unauthorized while this checkpoint is pending.
