# PhysKit Agent Policy

**Status:** Proposed for human review

This file is the repository-wide operational policy for agents working in PhysKit. A future, explicitly accepted narrower `AGENTS.md` may override it only within its defined scope.

## Repository purpose

PhysKit is a pedagogically motivated computational-physics library. An intended supported capability connects:

1. explicit mathematical and computational construction;
2. reusable library functionality;
3. repeated cases, comparisons, parameter exploration, or visualization; and
4. separately classified verification and validation evidence.

PhysKit is not a research-campaign control plane. Coordination exists to protect bounded library and pedagogical work, not to manage a scientific campaign.

## Policy sources and authority

Apply this hierarchy, from highest to lowest authority:

1. explicit human decisions and bounded authorization;
2. accepted repository policies and capability contracts;
3. this root policy and any future accepted scoped `AGENTS.md` within its scope;
4. the future `.pi/active-state.json`, solely for current runtime coordination;
5. future task, chain, agent, and skill instructions within their accepted scope; and
6. generated reports, evidence, and summaries, which are derived artifacts.

Source documents, each limited to its human-accepted role, are:

- the inspection baseline at `docs/harness/physkit.harness.01-capability-baseline.md`;
- the lifecycle policy at `docs/harness/physkit.harness.02-capability-lifecycle.md`;
- the pilot decision support and recorded selection boundary at `docs/harness/physkit.harness.03-pilot-capability-selection.md`; and
- the control-plane design at `docs/harness/physkit.harness.04-minimal-pi-control-plane.md`.

Runtime state coordinates accepted work; it does not define scientific or pedagogical truth. Runtime state and agent conclusions cannot override human decisions, accepted contracts, source behavior, tests, canonical notebooks, or accepted evidence. Do not infer authority from generated summaries.

Once `.pi/active-state.json` is separately accepted and created, every session must read it and its referenced authorities before work. It is the sole authority for current runtime coordination. Fail closed if it is missing, malformed, stale relative to a known human decision, contradictory, or points to missing authority.

Before that file exists, there is no durable active runtime task; only an explicit human instruction may authorize a bounded task. Never infer or begin successor work. Do not invent an active-state schema.

## Human-owned protected decisions

Explicit human approval is required for:

- capability boundaries;
- intended users and uses;
- capability contracts;
- physical models and approximations;
- mathematical and numerical conventions;
- public APIs and canonical artifacts;
- learning objectives;
- references and physical invariants;
- tolerances and acceptance criteria;
- evidence applicability and acceptance;
- physical and pedagogical validation conclusions;
- lifecycle transitions; and
- support, withdrawal, deprecation, replacement, and archival decisions.

Agents may inspect, analyze, compare, and recommend on these matters, but must not silently decide them or disguise them as implementation details.

## Bounded work and scope control

Every task must identify:

- authorized scope;
- owned paths and one owner per write path;
- prohibited paths;
- applicable accepted contracts;
- required evidence;
- review mode;
- human checkpoints;
- stop condition; and
- successor authorization, if any.

Fail closed when scope, ownership, authority, prerequisites, or a protected decision is unresolved. Follow the bounded work sequence in `.04`, Section 5, proportionally to the accepted task: human acceptance of a capability contract precedes implementation; implementation precedes claim-bearing verification; correction precedes re-review; parent verification precedes final human acceptance; and closeout stops before any successor. Stop at every human checkpoint with no success claim and no automatic successor. Silence, timeout, completion, commit, merge, or push is not acceptance.

## Working-tree protection

Before editing, inspect the repository identity, revision, branch, remotes, and complete working-tree state. Preserve unrelated modifications and untracked files; do not inspect their contents unless authorized. Stage only authorized paths. Avoid destructive Git operations, including forced checkout, reset, clean, overwrite, or history rewriting. Stop if safe isolation is not possible or the repository state differs materially from the authorized baseline.

Report the starting and ending revisions and the complete final working-tree status, including unrelated changes that remain. Never hide a dirty tree behind a path-limited status report.

## Review modes

### Mode A — Single-File Verification

Mode A is required for policies, capability contracts, control-plane designs, authority records, lifecycle decisions, canonical-artifact decisions, and material changes to protected decisions. Present only one material file at a time with its authority/status marker, GitHub revision, scope and non-decisions, source and evidence references, deterministic validation, independent-review findings where required, complete repository status, untouched paths, and explicit accept, revise, reject, or defer options. Stop for explicit human acceptance.

### Mode B — Final-Report Verification

Mode B is allowed only for bounded execution under already accepted contracts and decisions. It may summarize multiple authorized execution artifacts when they introduce no protected choice. Cite accepted authority and scope by path and revision; report changed and untouched files, commands and environment, evidence by class, independent-review disposition, parent verification, residual risks, omitted checks, claim limits, complete status, and explicit human acceptance options. If material ambiguity, an unsupported claim, or a protected decision appears, stop and return to Mode A or an explicit human checkpoint.

## Responsibility and review separation

Assign responsibilities proportionally from the model established in `.04`:

- parent coordination, scope control, correction routing, final verification, and human handoff;
- architecture or capability-contract ownership;
- implementation ownership;
- software and numerical verification ownership;
- notebook and documentation ownership; and
- independent read-only integration review.

Small, low-risk work may collapse compatible roles, but it must preserve path ownership, evidence distinctions, and human checkpoints. Independent read-only review is required for material changes, public support claims, and capability-promotion evidence. The independent reviewer must not repair the work reviewed; findings return to the owning role for correction and then re-review. Do not infer named agent definitions from these responsibilities.

## Evidence discipline

Keep separate:

- agent findings;
- deterministic checks;
- independent review conclusions;
- parent verification; and
- human acceptance.

Classify evidence according to `.02` as software verification, numerical verification, physical validation, pedagogical validation, or uncertainty quantification. Do not collapse one class into another:

- successful execution is not numerical validation;
- numerical agreement is not automatically physical validation;
- notebook execution is not pedagogical acceptance;
- tests do not establish every support claim; and
- unavailable, difficult, missing, or unreviewed evidence cannot be mislabeled `Not applicable`.

State each claim, method, provenance, result, and limitation without inflating interpretation. Humans own evidence applicability, references, tolerances, adequacy, and acceptance. Do not invent schemas or universal tolerances.

## Notebook policy

For a supported pedagogical capability, the accepted capability contract must identify a canonical notebook or an explicitly approved exception, including an adequate alternative when a notebook or reusable library interface is unsuitable. The contract determines the proportional artifact structure in light of the capability's accepted pedagogical modality; no single notebook sequence applies universally.

Where a numerical capability uses both an explicit reference construction and a library-based construction, they must agree under human-accepted references, invariants, and criteria, and the scope of that agreement must be stated. Notebooks are first-class pedagogical artifacts, not substitutes for library tests; execution, saved output, or visual quality does not make a notebook canonical or pedagogically accepted. The independent reusable-library and notebook applicability axes, and their accepted A/B/C/D paths, remain unchanged.

## Pedagogical modalities

### Modality declaration

A human-accepted capability contract should identify its pedagogical modality when that distinction affects artifact structure or evidence. Descriptive labels are:

- numerical;
- analytical;
- symbolic;
- formal-proof; and
- mixed or not-yet-classified.

These labels are policy vocabulary, not a machine-enforced enumeration, schema, registry, validator, or runtime field. The accepted capability contract remains authoritative for the actual artifact structure. A modality label grants no work, selects no canonical artifact, determines neither the reusable-library nor notebook applicability axis, and assigns no lifecycle state.

### Numerical pedagogical sequence

Only the numerical pedagogical sequence is currently defined:

1. mathematical formulation;
2. explicit numerical representation or discretization;
3. transition from transparent prototype to production software;
4. software verification;
5. numerical verification;
6. physical-validation applicability and evidence boundary;
7. uncertainty-quantification applicability and evidence boundary; and
8. library-driven exploration, repeated cases, comparison, and visualization.

This is an intellectual sequence, not a mandatory file or notebook count. A small capability may express it as sections of one notebook. A broader capability may use several notebooks, documentation pages, tests, and evidence records. The human-accepted capability contract decides the proportional artifact decomposition.

Numerical work must keep distinct the mathematical model, numerical representation, production software, software verification, numerical verification, physical validation, pedagogical validation, and uncertainty quantification. In particular:

- successful execution is not software verification by itself;
- software verification is not numerical verification;
- convergence and truncation error are numerical-verification subjects;
- numerical agreement is not automatically physical validation;
- notebook execution is not pedagogical validation;
- deterministic discretization error is not automatically uncertainty quantification;
- physical-validation and uncertainty-quantification applicability and evidence boundaries must be discussed explicitly when relevant;
- a human-approved `Not applicable` disposition requires a claim-based rationale; and
- absent, difficult, missing, deferred, or unreviewed work is not `Not applicable`.

### Prototype-to-production bridge

When applicable, numerical pedagogical artifacts must explain how transparent mathematical or numerical code maps to reusable production software. Proportional topics may include state-space representation; operator domain and codomain; boundary or initial conditions; data ownership and immutability; dtype and units; validation and exception behavior; sparse or dense representation; public API design; testable invariants; documentation; and deferred extensions.

No capability must address every topic merely because it is listed. The human-accepted contract selects the proportional subset. A notebook should not reproduce every internal production-source detail; it should explain the mapping between the explicit reference construction and the accepted public abstraction.

### Deferred modalities

No general pedagogical sequence is currently accepted for analytical work, symbolic computation, formal or machine-checked proof, or mixed-modality artifacts. This policy proposes none of their stages, evidence obligations, tools, artifact types, or acceptance criteria.

When a capability materially depends on one of these modalities and no accepted capability-specific sequence exists, agents must stop for bounded human scope and contract decisions. They must not invent, infer, or derive a workflow from the numerical sequence or silently apply that sequence.

Classification safeguards are:

- an analytical reference solution used as a numerical oracle does not make the capability analytically modal;
- equations written in Markdown or LaTeX do not make an artifact a symbolic-computation capability;
- ordinary test assertions do not constitute a formal-proof system;
- use of more than one modality does not automatically create a mixed-modality workflow; and
- modality does not determine whether a reusable library interface or notebook is required; the existing independent applicability axes and A/B/C/D paths remain unchanged.

### Flexibility and non-hardening boundary

This policy revision does not alter the reusable capability-development chain; add or reorder chain stages; modify agent definitions; introduce a modality schema, registry, validator, enumeration implementation, stage graph, or runtime field; prescribe notebook filenames or counts; retroactively invalidate accepted contracts or completed artifacts; revise `FOUNDATIONS-FD1`; authorize notebook work; authorize analytical, symbolic, mixed-modality, or proof-system design; or authorize a successor.

Modality-specific workflows should be hardened only when concrete capabilities demonstrate operational need. Any future hardening requires a separate human-reviewed control-plane revision supported by that demonstrated need.

## Capability lifecycle

Use the lifecycle states defined by `.02` without redefining them: Exploratory, Candidate, Supported, Deprecated, and Historical. Never claim a state or support level unless a human-approved record establishes it. File location, implementation, tests, evidence volume, commit status, and age do not imply lifecycle state. New behavior, parameter regimes, audiences, APIs, or artifacts do not inherit support from existing behavior.

## Generic and PhysKit-local boundaries

Generic coordination machinery must remain separable from PhysKit-specific physics and pedagogy policy. Do not place generic harness implementation in `src/physkit`.

PhysKit-specific policy includes capability contracts, notebook requirements, protected physical and numerical decisions, pedagogical objectives, evidence applicability, and lifecycle and support decisions. This boundary does not authorize generic harness extraction or implementation.

## Bootstrap boundary

`AGENTS.md` establishes repository-wide operational policy. `.pi/active-state.json` may be proposed only through a later, separately authorized Mode A task. The existence or acceptance of `.04` alone justifies no other control-plane surface. Agents, chains, skills, task or checkpoint stores, evidence stores, schemas, validators, and runtime code remain deferred until separately justified and accepted.

Do not place a mutable current-task snapshot in this file.

## PIAB boundary

The analytic one-dimensional infinite-square-well stationary-state capability is the human-selected intended pilot described in `.03`. All PIAB contract, API, notebook, evidence, tolerance, lifecycle, and implementation work remains parked. Neither acceptance of this file nor bootstrap closeout authorizes PIAB work; resumption requires a separate later human decision and bounded authorization. Do not design PIAB while applying this policy.

## Completion reporting

Every final report must contain:

- task outcome;
- starting and ending revisions;
- files changed;
- files explicitly untouched;
- validation performed;
- independent-review disposition when required;
- evidence limitations;
- unresolved decisions;
- complete working-tree status; and
- whether successor work is authorized.

Silence or task completion never implies human acceptance or successor authorization.
