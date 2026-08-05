# HARNESS-CAPABILITY-1 — Reusable capability-workflow bootstrap

**Status:** Awaiting renewed human review after narrow blocking-evidence REMAND correction
**Task ID:** `HARNESS-CAPABILITY-1`
**Reusable template ID:** `PHYSKIT-CAPABILITY-DEVELOPMENT`
**Current checkpoint:** `HARNESS-CAPABILITY-1-HC01` (`pending-renewed-human-review`)

## Human disposition and bounded intake

The human issued a second `REMAND` at revision `eae9dbc4b960a8e655d9e281f7e25afea3e82a63`. This is not acceptance. HARNESS-CAPABILITY-1 remains active; closeout and successor work remain prohibited.

The human issued a further narrow `REMAND` at revision `4909d3593b9816e2592aa912787648ccc866e8df` for one deterministic blocking-evidence routing defect. This correction owns exactly `.pi/chains/capability-development.chain.json`, this task record, and `.pi/active-state.json`. It removes the ambiguous special evidence outcome/route while preserving all accepted template, A/B/C/D applicability, contract-reacceptance, bounded-correction, evidence-readiness, and human-acceptance boundaries. No role file is authorized or changed.

- **Requested outcome:** separate library/notebook applicability, make the reusable chain an immutable template, separate evidence readiness from human evidence acceptance, validate, commit, push, and stop for renewed review.
- **Repository / branch / starting revision:** `/Users/eugene/repos/physkit`; `main`; `eae9dbc4b960a8e655d9e281f7e25afea3e82a63`.
- **Complete starting status:** `## main...origin/main` and unrelated untracked `package-lock.json` only; its contents were not inspected.
- **Initially authorized paths:** active state, this task, chain template, architect, implementation, notebook/documentation, and integration-reviewer definitions.
- **Conditionally authorized path:** `.pi/agents/physkit-verification.md`, modified only because Correction 2 explicitly requires every specialized role to use template/task-instance startup semantics; leaving its old “active chain” preflight would deterministically contradict the immutable-template model.
- **Prohibited work:** every other path; creation of any file; capability selection or activation; capability source/test/notebook/evidence work; PIAB; remaining notebook work; closeout; successor work.
- **Known user work:** untracked `package-lock.json`, preserved uninspected, unmodified, unstaged, and undeleted.
- **Protected decisions:** all capability, scientific, numerical, API, pedagogical, evidence-acceptance, validation, canonical-artifact, lifecycle, support, final-acceptance, and successor decisions.
- **Expected evidence:** duplicate-free JSON, agent and stage resolution, four paths and independent axes, immutable-template semantics, seven structural traces, fresh read-only review, parent verification, exact staging, remote freshness, and diff check.
- **Review mode:** material control-plane correction with independent read-only review and renewed human checkpoint.
- **Stop conditions:** missing/contradictory authority, unexpected worktree change, ambiguous ownership, failed deterministic check, unresolved material review finding, non-fast-forward remote, or protected decision.
- **Successor authorization:** `false`; successor `null`.

The prior bounded-intake, explicit contract gate, five-class evidence records, material-contract reacceptance, bounded correction/escalation, and common role-preflight mechanisms are preserved.

## Immutable reusable-template model

`.pi/chains/capability-development.chain.json` is a static `reusable-chain-template`, not current runtime state. It records:

- availability for human-authorized instantiation;
- `.pi/active-state.json` as the sole runtime authority;
- the requirement that a human-authorized active task instantiate the template ID with a task-instance identity, active stage, and exact ownership; and
- the rule that activation and progress update active state and the task record, never the template’s runtime status.

The template therefore has no mutable `status`, `active_task`, or `selected_capability` fields. Template availability alone grants no work. The current bootstrap records no capability-workflow instance, no selected capability, and no capability ownership.

Every specialized role reads the template but reconstructs current authority from active state and the active task. It must verify an explicit template-ID instantiation, active current stage, and exact ownership. It fails on missing or inactive task-instance authority, not merely because the immutable template has no mutable active status.

## Independent applicability axes and four paths

The accepted capability contract must separately record:

```text
reusable_library_interface: required | not-required-with-human-rationale
notebook_artifact: required | exception-with-human-rationale
```

No decision on one axis determines the other. The human-accepted contract selects exactly one path consistent with both values:

| Path | Library axis | Notebook axis | Required stages | Axis-specific skips |
|---|---|---|---|---|
| A — library plus notebook | required | required | implementation; explicit notebook; PhysKit reconstruction; exploration/API documentation; five-class evidence | alternative artifact skipped because notebook is required |
| B — notebook only | not required with human rationale | required | explicit notebook; appropriate exploration/documentation; five-class evidence | implementation and reconstruction skipped only under accepted library-omission clause; no lifecycle state inferred |
| C — library plus approved notebook exception | required | exception with human rationale | implementation; API-consistent documentation; adequate alternative explaining/demonstrating accepted library behavior; five-class evidence | notebook stages skipped only under accepted notebook-exception clause and claim limits |
| D — neither library nor notebook | not required with human rationale | exception with human rationale | adequate alternative; five-class evidence | production and notebook stages require two separate accepted clauses, two rationales, and resulting claim limits |

One omission rationale cannot satisfy the other axis. A skipped stage must cite its exact accepted contract clause. Missing work is not an exception or Not applicable.

## Preserved 24-stage dependency sequence

1. bounded intake
2. human capability scope
3. contract drafting with both axes and A/B/C/D selection
4. human contract acceptance
5. ownership and implementation plan
6. conditional implementation (A/C)
7. conditional explicit notebook construction (A/B)
8. conditional PhysKit notebook reconstruction (A)
9. conditional exploration/user documentation (A/B/C)
10. conditional alternative pedagogical artifact (C/D)
11. mandatory five-class evidence production and assessment
12. independent integration review
13. correction classification
14. bounded nonmaterial owner correction
15. material contract correction
16. renewed human contract acceptance
17. revised ownership and implementation plan
18. verification replay
19. independent re-review
20. correction-cycle disposition
21. human escalation
22. parent readiness verification
23. human final disposition
24. closeout only after explicit human acceptance

Every claim-bearing writer retains actual `human_contract_acceptance:explicitly-accepted` prerequisites. Material contract revision still invalidates affected work, requires renewed acceptance and a revised plan, and cannot route directly to verification replay. One ordinary automatic correction/replay/re-review cycle remains the limit.

## Evidence readiness versus human acceptance

Parent verification checks readiness only. It verifies truthful five-class result records; traceability to accepted applicability clauses; required methods, references, criteria, provenance, paths, reviewers, results, limitations, and claim boundaries; truthful obligation states plus observed outcomes (`passed`, `failed`, `indeterminate`, or `not-run`); consistency with accepted blocking rules; completed applicable checks and independent review; no unresolved material integration finding; and readiness for human disposition. A failed required obligation remains `required-incomplete` with observed outcome `failed`; the failure cannot be hidden as absence.

Parent verification does **not** accept evidence adequacy, physical or pedagogical validation, uncertainty conclusions, canonical-artifact status, lifecycle status, or support claims. Earlier contract acceptance accepts obligations and blocking rules, not later evidence results.

Any incomplete, deferred, failed, or unresolved result that violates its accepted blocking rule routes to correction classification or human escalation before parent verification. It cannot reach human final disposition through a readiness pass.

The human final checkpoint alone owns acceptance, limitation, remand, rejection, or deferral of the implemented/pedagogical outcome, evidence claims and adequacy, physical/pedagogical validation conclusions, uncertainty conclusions, artifact roles and canonical proposals, claim limits, and any separately authorized lifecycle proposal. Lifecycle assignment remains outside this workflow unless independently authorized.

## Seven hypothetical structural traces

No trace selects a real capability or modifies production artifacts.

### Trace 1 — Path A: library plus notebook

- **Applicability-axis decisions:** library `required`; notebook `required`.
- **Applicable and skipped stages:** implementation, explicit notebook, reconstruction, exploration/API docs, and evidence apply; alternative is skipped.
- **Skip authority:** accepted notebook-required contract clause.
- **Ownership:** exact separate contract, source, notebook/docs, and evidence paths; reviewer read-only.
- **Startup preflight result:** PASS only with active state/task instance, template ID, active stage, and exact ownership.
- **Evidence state:** five truthful class records consistent with blocking rules.
- **Human checkpoints:** scope, contract acceptance, and final disposition; parent performs readiness verification only.
- **Final stop:** human final checkpoint; no closeout without accept.

### Trace 2 — Path B: notebook only

- **Applicability-axis decisions:** library `not-required-with-human-rationale`; notebook `required`.
- **Applicable and skipped stages:** explicit notebook, exploration/docs, and evidence apply; implementation, reconstruction, and alternative are skipped.
- **Skip authority:** accepted library-omission clause for implementation/reconstruction and notebook-required clause for the alternative.
- **Ownership:** no source ownership; exact notebook/docs and evidence paths.
- **Startup preflight result:** PASS only for active instance/stage/ownership; template availability insufficient.
- **Evidence state:** five truthful records; no Candidate or other lifecycle inference.
- **Human checkpoints:** contract acceptance and final disposition; parent performs readiness verification only.
- **Final stop:** human final disposition.

### Trace 3 — Path C: library plus approved notebook exception

- **Applicability-axis decisions:** library `required`; notebook `exception-with-human-rationale`.
- **Applicable and skipped stages:** implementation, API-consistent docs, adequate alternative, and evidence apply; explicit notebook/reconstruction are skipped.
- **Skip authority:** accepted notebook-exception clause and explicit claim limits; notebook exception does not remove implementation.
- **Ownership:** exact source, docs/alternative, and evidence paths.
- **Startup preflight result:** PASS only for instantiated active task, active stages, and exact ownership.
- **Evidence state:** alternative explains/demonstrates accepted library behavior and all five classes are recorded truthfully.
- **Human checkpoints:** contract/exception acceptance and final disposition; parent performs readiness verification only.
- **Final stop:** human final disposition.

### Trace 4 — Path D: neither library nor notebook

- **Applicability-axis decisions:** library `not-required-with-human-rationale`; notebook `exception-with-human-rationale`.
- **Applicable and skipped stages:** adequate alternative and evidence apply; implementation and all notebook stages are skipped.
- **Skip authority:** two separate accepted clauses—library omission and notebook exception—with separate rationales and claim limits.
- **Ownership:** no source/notebook ownership; exact alternative and evidence paths.
- **Startup preflight result:** PASS only with active instance/stage/ownership.
- **Evidence state:** two rationales and resulting claim limits plus five truthful evidence records.
- **Human checkpoints:** contract acceptance and final disposition; parent performs readiness verification only.
- **Final stop:** human final disposition.

### Trace 5 — immutable-template activation

- **Applicability-axis decisions:** a human-authorized task separately selects both axes and one consistent path.
- **Applicable and skipped stages:** resolved from that selected path without mutating the template.
- **Skip authority:** accepted axis-specific contract clauses.
- **Ownership:** exact task-instance ownership recorded in active state and the active task.
- **Startup preflight result:** PASS because runtime authority explicitly instantiates the template; template remains unchanged and is not treated as active state.
- **Evidence state:** selected-path five-class obligations are active but no result is inferred from template availability.
- **Human checkpoints:** scope and contract gates remain task-instance runtime state.
- **Final stop:** active task stage or human checkpoint recorded only in runtime authority; template retains no runtime status.

### Trace 6 — complete evidence package

- **Applicability-axis decisions:** any separately accepted valid A/B/C/D combination.
- **Applicable and skipped stages:** every required selected-path stage is complete and every skip is resolved.
- **Skip authority:** axis-specific accepted clauses.
- **Ownership:** exact producers and read-only reviewer recorded in the task instance.
- **Startup preflight result:** PASS for the active instance, stage, and ownership.
- **Evidence state:** required fields and provenance complete; results obey blocking rules; independent review complete.
- **Human checkpoints:** parent verifies readiness without accepting adequacy; human final checkpoint owns evidence and validation disposition.
- **Final stop:** human accept/remand/limit/reject/defer decision; no inferred closeout.

### Trace 7 — blocking-rule violation

- **Applicability-axis decisions:** any valid path; axis decisions remain unchanged by the evidence failure.
- **Applicable and skipped stages:** selected-path applicability remains intact; no new skip is inferred.
- **Skip authority:** existing axis-specific accepted clauses only.
- **Ownership:** exact evidence owner and reviewer identify the violation.
- **Startup preflight result:** PASS for authorized evidence assessment in the active instance.
- **Evidence state:** incomplete/deferred/failed/unresolved result is truthfully labeled but violates its accepted advancement rule.
- **Human checkpoints:** correction classification or human escalation occurs before parent verification; parent readiness fails.
- **Final stop:** correction or escalation checkpoint; blocking evidence cannot reach final acceptance.

All traces fail if either axis silently determines the other, a role treats the template as runtime authority, parent verification accepts evidence/validation, or blocking evidence advances.

## Deterministic blocking-evidence classification and routing

The special `evidence-result-violates-accepted-blocking-rule` outcome and ambiguous `correction_classification-or-human_escalation` route are removed. Blocking evidence now uses the existing taxonomy with correction-cycle exhaustion taking precedence:

| Condition/classification | Exactly one next route |
|---|---|
| `correction_cycle_count >= 1` and any unresolved finding → `bounded-cycle-exhausted` | `human_escalation` |
| First-cycle evidence failure correctable without changing any accepted applicability, model, convention, API, method/reference, criterion/tolerance, learning objective, evidence obligation, or claim boundary/limit → `accepted-in-scope-nonmaterial-conformance` | exact responsible owner through `nonmaterial_owner_specific_correction` → `verification_replay` → `integration_rereview` → new classification/disposition |
| Resolution accepts a failed result, waives a blocking requirement, limits a claim beyond the contract, or makes another protected decision → `material-protected-decision` | `human_escalation` |
| Otherwise, resolution changes an accepted method, reference, criterion, tolerance, applicability, evidence obligation, API, model, learning objective, or claim boundary without requiring a protected disposition → `material-contract-revision` | `material_contract_correction` → renewed human contract acceptance → revised plan → replay every invalidated applicable stage → independent review |
| `no-material-findings` | `parent_verification` |

Parent verification remains blocked until correction disposition reports no material finding, the evidence result is consistent with its accepted blocking rule, and no blocking evidence violation remains.

## Three narrow structural traces

### Blocking Trace 1 — correctable first-cycle evidence failure

- **Classification:** `accepted-in-scope-nonmaterial-conformance`; count is below one and no accepted contract choice changes.
- **Single route:** responsible evidence owner via `nonmaterial_owner_specific_correction` → `verification_replay` → `integration_rereview` → fresh classification and correction-cycle disposition.
- **Parent gate:** blocked until replay/re-review yields a successful no-material-finding disposition consistent with the blocking rule.
- **Final stop:** re-review/classification if unresolved; otherwise parent readiness, never direct final acceptance.

### Blocking Trace 2 — criterion or claim change

- **Classification:** apply exclusive precedence: protected human disposition first; therefore accepting failure, waiving the block, or imposing a beyond-contract limitation is `material-protected-decision`. Only a criterion/claim change that requires no protected disposition is `material-contract-revision`.
- **Single route:** the first exclusive match controls: protected decision → `human_escalation`; otherwise contract revision → architect/reacceptance/revised plan/full invalidated replay/review.
- **Ordinary correction:** prohibited; neither classification may enter `nonmaterial_owner_specific_correction`.
- **Final stop:** renewed contract checkpoint or human escalation.

### Blocking Trace 3 — correction-cycle exhaustion

- **Classification:** `bounded-cycle-exhausted` takes precedence for any unresolved finding when count is at least one.
- **Single route:** `human_escalation`.
- **Automatic correction:** no second owner correction/replay loop is allowed.
- **Parent/final gates:** parent verification and human final acceptance remain blocked.
- **Final stop:** human escalation.

Each trace has exactly one next route under its stated condition. Classification precedence is exhaustion, then protected disposition, then material contract revision, then nonmaterial conformance. Route values containing ambiguous `or` alternatives are prohibited, including human-final remand and limit routing, which must name one human-specified target.

## Validation and review status

The first fresh independent review of this second REMAND returned `REMAND` with four findings: two residual runtime-like template fields, a contradictory Path D reconstruction skip requirement, no explicit failed-evidence representation, and task/active-state checkpoint disagreement. The parent corrected all four. The next fresh re-review returned `REMAND` for two consistency findings: Stage 11 omitted failed/unresolved outcomes in its applicability prose, and the verification role still referred to an “actual chain” rather than task-instance prerequisite resolution. The parent corrected both. A third fresh re-review correctly found that expanding the verification role beyond startup semantics exceeded its conditional authorization. The parent restored that file to a startup-only diff and encoded failure truthfully in the template as a separate observed outcome alongside the obligation state. A fourth fresh independent read-only re-review returned `PASS` with no blocker, high, medium, or low findings. Deterministic validation and parent verification passed.

For the narrow routing REMAND, the first fresh review found overlapping protected/contract classifications and residual ambiguous human-final route values. The parent made classification precedence exclusive and replaced those values with single human-specified targets. Fresh independent re-review returned `PASS`. Narrow deterministic validation and parent verification passed. Exact staging, remote freshness, commit, and fast-forward push remain required before presentation.

Separate excluded governance debt remains unchanged: historical status markers in `AGENTS.md`, `.02`, and `.04`.

## Stop boundary

After successful correction, validation, review, commit, and push, stop at renewed human review. Do not record human acceptance, close HARNESS-CAPABILITY-1, instantiate a capability workflow, select a capability, resume PIAB, activate remaining notebook work, or authorize a successor.
