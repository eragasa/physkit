# HARNESS-CAPABILITY-1 — Reusable capability-workflow bootstrap

**Status:** Awaiting renewed human final review after REMAND correction
**Task ID:** `HARNESS-CAPABILITY-1`
**Reusable chain ID:** `PHYSKIT-CAPABILITY-DEVELOPMENT` (`inactive`)
**Current checkpoint:** `HARNESS-CAPABILITY-1-HC01` (`pending-renewed-human-review`)

## Human disposition and boundary

The human remanded the workflow at revision `b5fab2caf6971b7866f85133c99387c70dc629a8` for material reusable-control-flow corrections. This is `REMAND`/`REVISE`, not acceptance. Administrative closeout is prohibited. HARNESS-CAPABILITY-1 remains active; no successor is authorized.

The parent coordinator is the sole writer and owns exactly these existing paths:

1. `.pi/active-state.json`
2. `.pi/tasks/capability-workflow-bootstrap.md`
3. `.pi/chains/capability-development.chain.json`
4. `.pi/agents/physkit-capability-architect.md`
5. `.pi/agents/physkit-implementation.md`
6. `.pi/agents/physkit-verification.md`
7. `.pi/agents/physkit-notebook-documentation.md`
8. `.pi/agents/physkit-capability-integration-reviewer.md`

No other file may be created or modified. The unrelated untracked `package-lock.json` remains uninspected, unmodified, and unstaged. No capability contract, source, test, evidence, notebook, documentation, API, physics, lifecycle, or pedagogical artifact is selected or changed. PIAB remains parked and remaining notebook work remains inactive.

## Bounded bootstrap intake

- **Requested outcome:** harden the existing reusable inactive workflow gates and stop for renewed human review.
- **Repository / branch / starting revision:** `/Users/eugene/repos/physkit`; `main`; `b5fab2caf6971b7866f85133c99387c70dc629a8`.
- **Complete starting working-tree state:** `main...origin/main` with only unrelated untracked `package-lock.json`; its contents were not inspected.
- **Initially allowed paths:** exactly the eight paths above.
- **Prohibited paths/work:** every other path; production capability work; chain activation; capability selection; PIAB; remaining notebook work; closeout; successor work.
- **Known user work:** unrelated untracked `package-lock.json`, preserved without content inspection.
- **Protected decisions:** capability scope, intended use, physical model, approximation, mathematical/numerical convention, API, learning objectives, canonical artifacts, evidence applicability/criteria/adequacy, physical and pedagogical validation, tolerances, claim boundaries, lifecycle, final acceptance, and successor authorization.
- **Expected evidence:** duplicate-free JSON; exact agent resolution; gate and branch structure; five dry-run traces; independent fresh read-only review; parent verification; exact staged-path isolation; remote freshness; diff check.
- **Review mode:** Mode A material control-plane correction with independent read-only review and renewed human review.
- **Stop conditions:** missing or contradictory authority; unexpected worktree changes; scope/ownership ambiguity; failed deterministic check; unresolved reviewer material finding; inability to fast-forward push; any protected decision.
- **Successor authorization:** `false`; successor `null`.

## Corrected reusable control flow

The reusable chain now has 24 ordered stages:

1. `bounded_intake`
2. `human_capability_scope`
3. `contract_drafting`
4. `human_contract_acceptance`
5. `ownership_and_implementation_plan`
6. `implementation` (conditional path A)
7. `explicit_notebook_construction` (conditional paths A/B)
8. `library_notebook_reconstruction` (conditional path A)
9. `exploration_and_documentation` (conditional paths A/B)
10. `alternative_pedagogical_artifact` (conditional path C)
11. `evidence_production_and_assessment` (mandatory five-class disposition stage after selected artifacts)
12. `integration_review`
13. `correction_classification`
14. `nonmaterial_owner_specific_correction`
15. `material_contract_correction`
16. `renewed_human_contract_acceptance`
17. `revised_ownership_and_implementation_plan`
18. `verification_replay`
19. `integration_rereview`
20. `correction_cycle_disposition`
21. `human_escalation`
22. `parent_verification`
23. `human_final_acceptance`
24. `closeout`

Human capability scope requires completed bounded intake. Every implementation, test/evidence, notebook, documentation, alternative-artifact, correction-writer, or replay stage includes `human_contract_acceptance:explicitly-accepted` in its actual prerequisite list. Material contract correction then creates a renewed acceptance gate and revised plan before invalidated dependent work can resume. Earliest-start prose is not used as the contract gate.

## Human-selected artifact path

The accepted contract, never an agent, must select exactly one:

- **A — library-backed pedagogical capability:** implementation, explicit notebook construction, PhysKit reconstruction, exploration/documentation, and evidence production/assessment.
- **B — notebook-only capability:** explicit construction, appropriate exploration/documentation, and evidence production/assessment; reusable API and library reconstruction are prohibited.
- **C — human-approved notebook or reusable-interface exception:** an adequate alternative pedagogical artifact and evidence production/assessment, with explicit rationale and affected claim limits.

Every skipped stage must cite the accepted contract clause and human-approved rationale. Missing work cannot be silently treated as an exception or `Not applicable`. Integration review waits for every required stage of the selected path and verifies every skip record.

Explicit construction additionally requires completed ownership and implementation planning and exact notebook/documentation ownership. It may overlap source implementation only when the accepted plan records independence from unaccepted implementation behavior and the paths are exact and nonoverlapping.

## Five-class evidence disposition mechanism

The accepted contract and completed ownership plan must each record, for software verification, numerical verification, physical validation, pedagogical validation, and uncertainty quantification:

- applicability or human-accepted non-applicability rationale;
- required claim;
- producer or responsible role;
- exact artifact/evidence-summary path when written;
- method or reference;
- human-accepted criterion or unresolved criterion;
- reviewer;
- result state;
- limitations and claim boundary; and
- whether unresolved status blocks final handoff.

Result states distinguish `required-completed`, `required-incomplete`, `not-applicable-human-accepted-rationale`, `deferred-explicit-claim-limitation`, and `unresolved-blocking`. A bounded Candidate handoff may retain incomplete or deferred evidence only with explicit claim limits and a human-owned blocking/nonblocking disposition. Deferred, missing, difficult, unavailable, or unreviewed evidence is neither Not applicable nor satisfied. Agents collect and assess; humans accept applicability, criteria, adequacy, physical validation, and pedagogical validation.

## Contract correction, correction loop, and final dispositions

The parent classifies findings before correction:

- nonmaterial conformance clarification leaves every accepted protected decision unchanged;
- material contract revision changes capability scope, physical model, approximation, mathematical/numerical convention, public API, intended use, learning objective, canonical-artifact requirement, evidence obligation, reference, invariant, tolerance, or claim boundary.

A material revision returns to the architect, produces a revised proposal, invalidates affected implementation/evidence/notebook/documentation/review results, stops at renewed explicit human contract acceptance, and requires a revised ownership and implementation plan. It cannot route directly to verification replay, and final acceptance cannot retroactively substitute for contract reacceptance.

One automatic ordinary nonmaterial correction/replay/re-review cycle is permitted and counted. No material findings route to parent verification. In-scope nonmaterial findings route to the exact owner, replay every affected check, and receive independent re-review. A protected decision or material revision goes to its human gate. Any new or unresolved finding after the one-cycle limit requires human escalation.

Final human dispositions are `accept`, `remand`, `limit`, `reject`, or `defer`. Only explicit `accept` permits closeout. Remand and limit return to an exact owned stage or human checkpoint without widening scope; reject and defer stop.

## Mandatory role startup preflight

All five specialized role definitions now require authority reconstruction before work: `AGENTS.md`, active state, active task, active chain, accepted contract when it exists, exact owned/prohibited paths, evidence obligations, repository identity/revision/branch/remotes/full status, stop conditions, and successor authorization. Initial contract drafting must explicitly verify its authorized exception to contract presence. Every role fails closed on missing, stale, contradictory, ambiguous, inactive, or insufficient authority. The read-only reviewer performs the same reconstruction and verifies every writer's preflight record.

## Required dry-run traces

These traces are structural and hypothetical only; no capability or production artifact is selected or modified.

### Trace 1 — normal library-backed capability

- **Applicable:** bounded intake, scope, contract draft/acceptance, plan, implementation, evidence, explicit notebook, library reconstruction, exploration/documentation, integration review, correction disposition, parent verification, final human checkpoint.
- **Skipped:** alternative pedagogical artifact, citing accepted path-A clause; conditional correction stages absent when no findings.
- **Prerequisites:** source and every notebook/evidence writer waits for explicit contract acceptance and completed plan; reconstruction also waits for implementation/API and explicit construction.
- **Ownership:** exact separate contract, source, test/evidence, notebook/documentation paths; reviewer read-only.
- **Evidence:** all five class records required; incomplete/deferred states retain claim limits and blockers.
- **Correction:** nonmaterial finding gets at most one owner/replay/re-review cycle; material contract finding uses renewed acceptance.
- **Final stop:** human final checkpoint; no closeout without explicit accept.

### Trace 2 — notebook-only Candidate, no reusable API

- **Applicable:** intake, scope, contract/acceptance, plan, evidence, explicit construction, exploration/documentation, integration review, disposition, parent verification, final human checkpoint.
- **Skipped:** implementation and library reconstruction, each citing accepted path-B clause and human rationale; alternative artifact cites path-B clause.
- **Prerequisites:** notebook/evidence work still requires explicit contract acceptance and completed plan.
- **Ownership:** exact contract, notebook/documentation, and applicable evidence paths; no source ownership.
- **Evidence:** five dispositions remain mandatory; Candidate may truthfully carry required-incomplete/deferred evidence with explicit limits and human-owned handoff blocking status.
- **Correction/final stop:** bounded routing as above; stop at human final checkpoint.

### Trace 3 — human-approved exception with adequate alternative

- **Applicable:** intake, scope, contract/acceptance, plan, evidence, alternative pedagogical artifact, integration review, disposition, parent verification, final checkpoint.
- **Skipped:** implementation, explicit notebook, library reconstruction, and exploration only with accepted path-C clause, human rationale, adequate alternative, and claim limits.
- **Prerequisites:** alternative writer and evidence work require explicit contract acceptance and completed plan.
- **Ownership:** exact contract, alternative-artifact/documentation, and evidence paths; no inferred source/test/notebook ownership.
- **Evidence:** five explicit records; exception does not imply evidence non-applicability.
- **Correction/final stop:** bounded routing; stop at human final checkpoint.

### Trace 4 — material contract finding at integration review

- **Route:** integration review → correction classification (`material-contract-revision`) → architect revised proposal → renewed human contract acceptance.
- **Invalidation:** affected plan, source, evidence, notebook/documentation/alternative, review, and parent results become invalid.
- **Resume prerequisite:** explicit reacceptance plus revised plan; then replay every applicable selected-path stage and review.
- **Failure guard:** direct architect-to-verification replay is forbidden.
- **Final stop:** renewed contract checkpoint until human reaccepts; later human final checkpoint only after rebuilt work passes.

### Trace 5 — new material finding after permitted cycle

- **Route:** initial in-scope nonmaterial finding → exact owner correction → affected verification replay → independent re-review; count becomes one. Any new material or unresolved finding → correction-cycle disposition → human escalation.
- **No loop:** a second automatic correction is prohibited.
- **Ownership/evidence:** unchanged exact owners and all affected evidence remain unresolved until human direction.
- **Final stop:** human escalation with remand, limit, reject, or defer options; parent verification and closeout remain blocked.

All five traces fail closed if implementation can precede explicit contract acceptance, material revision can bypass renewed acceptance, or missing/deferred evidence can become Not applicable without human-accepted rationale.

## Validation and governance debt

Initial fresh independent review returned REMAND after finding an evidence self-dependency, missing revised-plan prerequisites, ambiguous cycle-limit precedence, a blocking-evidence handoff bypass, a parent-verification disposition bypass, and one stale stage reference. The parent corrected each finding. A second fresh independent read-only reviewer returned PASS with no blocker, high, medium, or low findings. Parent structural verification passed. Review artifacts were disabled and no repository-local review artifact was created. Exact staging, remote freshness, commit, and fast-forward push are the remaining execution checks before renewed human review.

Separate governance debt, explicitly excluded from correction: stale historical status markers in `AGENTS.md`, `.02`, and `.04`. Their historical contents are not normalized by this task.

## Stop boundary

After correction, validation, independent review, parent verification, exact commit, and fast-forward push, set the active task to awaiting renewed human final acceptance and stop. Do not record human acceptance, perform closeout, activate the chain, select a capability, resume PIAB, activate remaining notebook work, or authorize a successor.
