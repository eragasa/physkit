# FOUNDATIONS-FD1 — Documented discrete 1D Laplacian capability contract

**Status:** Awaiting human redisposition of corrected contract revision 3; contract unaccepted

**Task ID:** `FOUNDATIONS-FD1`

**Template ID:** `PHYSKIT-CAPABILITY-DEVELOPMENT`

**Active stage:** `human_contract_acceptance`

**Active checkpoint:** `FOUNDATIONS-FD1-HC02`

**Latest HC02 disposition:** `REMAND`

**Contract revision target:** 3

**Artifact path:** Path A — reusable library interface required and notebook artifact required

**Successor authorization:** `false`; successor `null`

## Repository and starting state

- Repository: `https://github.com/eragasa/physkit`
- Branch: `main`
- Starting revision and initial `origin/main`: `1ce0e53afe435cba8551875166ff5fc34bd68945`
- Initial working tree:

  ```text
  ## main...origin/main
  ?? package-lock.json
  ```

The unrelated untracked `package-lock.json` must remain uninspected, unmodified, unstaged, and undeleted.

## Accepted HC01 scope retained

The capability remains one integrated, internally layered, discrete-first Path A capability covering a closed uniform grid, homogeneous-Dirichlet active state space, discrete linear-operator hierarchy, centered finite-difference $+d^2/dx^2$, real/complex state application, CSR with dense inspection, synchronized source/MyST/Sphinx/notebook documentation, and proportional VVUQ. HC01 did not accept a public API, implementation, notebook, evidence result, lifecycle state, validation conclusion, or support claim.

## HC02 human REMAND

The proposed contract is not accepted. The human requires contract revision 3 to:

1. separate immutable `UniformGrid1D` geometry from homogeneous-Dirichlet state-space semantics;
2. introduce a proposed public `HomogeneousDirichletStateSpace1D` equivalent owning boundary data, active indices/coordinates/dimension, restriction, embedding, real/complex vector interpretation, and semantic identity;
3. make discrete operator domain and codomain explicit state spaces rather than grid/shape identities;
4. retain scalar scaling with domain/codomain and defer the general public `compose` method;
5. define the exact weighted norm, relative error, and observed-order formulas and exact accepted refinement pairs;
6. use MyST Markdown Sphinx pages and stable equation labels in the maintained concept page;
7. correct inheritance/containment/association/deferred-use diagrams and notebook synchronization; and
8. prohibit runtime equation registries, specifications, LaTeX metadata APIs, symbolic catalogs, or custom renderers.

This human-authorized remand is the only correction pass for this disposition. After correction, one fresh independent read-only Mode A review is required. Any remaining material or protected finding returns directly to the human; no automatic review/correction loop is authorized.

## Exact ownership

Parent coordinator owns exactly:

1. `.pi/active-state.json`;
2. `.pi/tasks/foundations-fd1.md`.

Capability architect owns exactly:

1. `docs/capabilities/foundations/uniform-grid-dirichlet-laplacian.md`.

Production source, tests/evidence, notebooks/user documentation implementation, Sphinx implementation, dependencies, packaging, and CI have empty ownership. The immutable template and role files remain unchanged.

## Required retained boundaries

Retain the inheritance hierarchy `LinearOperator -> DiscreteLinearOperator1D -> FiniteDifferenceLaplacian1D`, positive second-derivative sign, homogeneous-Dirichlet $N=3$ matrix $[-2/h^2]$, eager canonical CSR construction, defensive sparse/dense ownership, real-to-`float64` and complex-to-`complex128` behavior, future kinetic-energy scaling seam without Laplacian inheritance, Path A, five evidence dispositions, source-documentation standard, three-stage notebook, clean-surface migration recommendation, and ten-step lightweight VVUQ process.

Do not add a boundary-validation method without a concrete consumer. Do not add general composition. Do not add programmatic equation metadata. Existing competing implementations remain untouched.

## Review boundary

The fresh review must check grid/state-space separation; restriction/embedding; semantic identity; operator domain/codomain; composition deferral and scaling retention; sign/CSR/$N=3$; exact numerical formulas; observable immutability; MyST/Sphinx buildability; equation labels/authority; class diagrams; notebook synchronization; VVUQ proportionality; and absence of equation infrastructure or implementation.

Mechanical formatting may be corrected before this single final review. A review PASS is proposal readiness only, not contract acceptance.

## Prohibited work and stop condition

Do not modify source, tests, notebooks, examples, dependencies, packaging, CI, Sphinx implementation files, intake/harness documents, chain templates, role files, closed task records, or `package-lock.json`. Do not begin implementation, verification writing, evidence production, notebook editing, migration, repair, deprecation, PIAB, lifecycle, or successor work.

After correction, fresh review, parent validation, exact commit, and fast-forward push, stop again at `FOUNDATIONS-FD1-HC02 — human_contract_acceptance` for explicit human disposition.

## HC02 final review result

The single fresh independent read-only Mode A review returned `PASS` with no material or protected findings. No automatic follow-up correction is authorized. Parent deterministic validation passed. Remote freshness remains required immediately before the exact boundary commit and fast-forward push. After those checks, the task remains stopped at `FOUNDATIONS-FD1-HC02 — human_contract_acceptance`; the latest disposition remains `REMAND` and contract revision 3 remains proposed and unaccepted.
