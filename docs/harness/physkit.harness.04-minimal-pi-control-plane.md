# Minimal PhysKit Pi Control Plane

## 1. Document status, purpose, and limits

**Status:** Proposed for human review

**Proposed path:**
`docs/harness/physkit.harness.04-minimal-pi-control-plane.md`

This document proposes a minimal control-plane design. It does not implement the
control plane. Committing or publishing it does not constitute acceptance, and
acceptance would not by itself authorize bootstrap implementation.

The proposed PhysKit Pi control plane is a human-in-the-loop coordination layer
for moving bounded pedagogical physics capabilities through:

- scoping;
- contract definition;
- implementation;
- evidence production;
- notebook construction;
- independent review;
- correction;
- human acceptance;
- lifecycle management.

It governs authorization boundaries, active-work coordination, ownership,
ordering, checkpoints, evidence descriptions, review, closeout, and links to
human decisions. It does not own or decide the scientific or pedagogical content
of a capability.

Humans retain authority over:

- capability boundaries;
- physical models and approximations;
- mathematical and numerical conventions;
- public APIs;
- canonical notebooks and other canonical artifacts;
- learning objectives and pedagogical claims;
- references, invariants, tolerances, and evidence acceptance;
- lifecycle transitions;
- physical and pedagogical validation;
- support, deprecation, replacement, and archival decisions.

Agents may inspect, propose, implement accepted work, run deterministic checks,
collect evidence, identify discrepancies, review, and recommend. Agent
assertions, Pi runtime state, generated evidence, reviewer conclusions, and
parent verification do not substitute for accepted repository contracts or
human decisions.

### 1.1 Authority vocabulary

This proposal uses the following terms deliberately:

- **Proposal:** content offered for human review; it has no accepted authority
  merely because it exists or is committed.
- **Accepted policy or contract:** a repository artifact whose bounded content a
  human has explicitly accepted.
- **Active state:** the current operational authorization and coordination view;
  it is not a scientific specification or historical evidence.
- **Generated evidence:** outputs of a stated method with provenance and
  limitations; it is not accepted merely because generation succeeded.
- **Reviewer conclusion:** an independent finding or recommendation; it does not
  change policy, contracts, lifecycle state, or acceptance.
- **Parent verification:** the coordinating parent's check that scope, artifacts,
  evidence, reviews, and repository state satisfy the accepted process; it is
  not human acceptance.
- **Human decision:** the only authority for protected choices and final
  acceptance.

### 1.2 Source of reusable coordination lessons

The `dev` branch of `eragasa/ksdft2effmass`, inspected read-only at Git tree
`29eef9b5ed894d528d905f4556a905804983e305`, demonstrates reusable mechanisms
such as bounded tasks, explicit ownership, ordered work, human checkpoints,
evidence envelopes, independent review, and stop-before-successor behavior.

PhysKit does not import that project's research-campaign purpose, scientific
workflow, CPN/DFT/HPC policy, serialization policy, Rust requirements, branch
policy, project-specific roles, or authority structure. Its many task, chain,
checkpoint, evidence, skill, and harness-incubation surfaces also demonstrate a
risk: current status can be repeated in multiple prose and structured locations
and become contradictory. PhysKit therefore proposes one active-state authority
and a smaller bootstrap.

## 2. One authoritative active-state representation

### 2.1 Proposed authority

Exactly one repository path is proposed as authoritative for current active
control-plane state:

`/.pi/active-state.json`

The leading slash denotes the repository root. This file does not yet exist and
is not authorized for creation by this proposal.

The choice of a small machine-readable file, rather than a prose status page,
is intended to make the active task, authorization, checkpoint, and successor
state explicit and mechanically inspectable. This proposal defines the minimum
information ownership needed for review; it does not accept a JSON Schema or an
implementation.

### 2.2 Information owned by the active-state authority

The proposed active-state file alone owns the current values of:

- control-plane format/version identifier;
- current branch and revision context when recorded;
- active bounded task identifier and concise purpose, or an explicit `none`;
- authorized scope and prohibited scope for that task;
- current phase in the accepted bounded work sequence;
- responsible role ownership and repository path boundaries;
- unresolved human checkpoint, or an explicit `none`;
- accepted prerequisite decisions and their repository/commit references;
- evidence and review artifacts expected or currently available by reference;
- blockers and fail-closed reason;
- whether successor work is authorized;
- parked work, including the selected PIAB pilot;
- last human decision affecting active authorization, by durable reference;
- last verified update revision and updater.

The file should contain normalized facts and references, not long explanations,
scientific contracts, reviewer prose, chat transcripts, command logs, or copied
evidence.

### 2.3 Durable contracts and historical evidence

Durable policy, capability contracts, lifecycle decisions, canonical-artifact
decisions, and accepted planning artifacts remain versioned repository documents
under their human-approved paths, normally `docs/harness/` for control-plane and
capability-governance material. Evidence remains attached to the capability or
bounded task through later accepted conventions. Git history preserves prior
versions and decision boundaries.

The active-state file points to these artifacts and commits. It does not restate
their scientific or pedagogical content and cannot supersede them. Updating
active state changes current coordination only; it does not rewrite historical
evidence or accepted contracts.

### 2.4 Human-decision recording

A protected human decision becomes durable only when its decision-bearing scope,
outcome, consequences, and relevant artifact/commit references are recorded in
a human-reviewed repository artifact or accepted decision boundary. The active
state then records a normalized pointer to that durable decision and the
operational authorization it creates or removes.

Conversation alone may communicate a decision, but the control plane must not
claim durable cross-session authority until the decision is recorded and
reviewed at the applicable boundary. Silence, timeout, a passing check, an agent
summary, or a merge without explicit decision content is not human acceptance.

### 2.5 Derived summaries

README statements, dashboards, issue labels, pull-request summaries, agent
messages, generated reports, and convenience status pages are derived and
non-authoritative. They must cite the active-state revision and must not be used
to reconstruct or override current authorization when they disagree with
`/.pi/active-state.json`.

### 2.6 Contradiction prevention

The proposed design prevents competing current-state prose by these rules:

1. `AGENTS.md` may state how to find active state but must not copy the current
   task, phase, or checkpoint.
2. `docs/harness/` artifacts describe durable policy, decisions, plans, and
   history, not mutable current task status.
3. Task, chain, checkpoint, and evidence stores are not part of the first
   bootstrap.
4. If later introduced, those stores may supply referenced detail but may not
   become a second current-state authority.
5. A session begins by reading the active-state file and the durable artifacts
   it references.
6. If the active-state file is missing, malformed, stale relative to a known
   human decision, internally contradictory, or points to missing authority,
   work fails closed and stops at a human checkpoint.
7. Summaries are regenerated or corrected from the active authority; the active
   authority is never inferred from summaries.

## 3. Minimum repository surfaces

The first bootstrap should use only surfaces that are necessary to establish
human authority, session instructions, and one active-state authority.

| Surface | Proposed purpose and authority | First bootstrap | Classification | Why a simpler existing surface is insufficient |
|---|---|---:|---|---|
| Root `AGENTS.md` | Repository-wide operating policy: human authority, preservation of user work, required startup checks, single active-state pointer, fail-closed rules, and review modes. It is policy, not active status. | Required | PhysKit-local policy using generic coordination rules | The current repository has no root instruction file; chat context is not durable across sessions. |
| `/.pi/active-state.json` | Sole authority for current task, phase, scope, ownership, checkpoint, blockers, parked work, and successor authorization. | Required | Generic state shape with PhysKit-local contents | Prose planning documents are historical/durable and must not be edited into mutable status pages. Git status alone cannot express authorization or human checkpoints. |
| `docs/harness/` | Durable human-reviewed baseline, lifecycle policy, pilot decision support, this control-plane proposal, and later accepted contracts/decisions. | Required existing surface; no additional bootstrap file proposed | PhysKit-local | Active state cannot carry scientific contracts or historical rationale. The existing `.01`–`.04` series already supplies the durable planning surface. |
| `/.pi/agents/` | Possible future project-specific role definitions. | Excluded initially | Potentially generic mechanism with PhysKit-local prompts | Built-in/manual role assignment plus `AGENTS.md` is sufficient for the first bounded bootstrap. Agent files would add machinery before stable responsibilities are exercised. |
| Task records | Possible future durable per-task detail when one active-state envelope is insufficient. | Excluded initially | Potentially generic | The first bootstrap and one parked pilot need only one active bounded task in active state. Separate records would duplicate authority prematurely. |
| Ordered chains | Possible future executable ordering for repeated, accepted workflows. | Excluded initially | Generic | The proposed sequence can be followed manually. A chain before the process is exercised risks encoding unaccepted omissions and transitions. |
| Human checkpoint store | Possible future structured persistence for multiple or long-lived checkpoints. | Excluded initially | Generic mechanics; PhysKit-local decisions | Mode A GitHub review plus one unresolved-checkpoint field and durable decision references in active state are sufficient initially. A store is justified only when checkpoint volume or recovery needs exceed that model. |
| Evidence record store | Possible future structured evidence catalog. | Excluded initially | Generic envelope; PhysKit-local claims and acceptance | No capability execution is authorized. The common envelope can be tested in later planning before choosing storage or schema. |
| Skills | Possible future repeatable procedures for checkpoint resolution, evidence collection, or closeout. | Excluded initially | Generic or PhysKit-local depending on content | The initial process is small and policy-driven. A skill would duplicate prose before repetition demonstrates a stable procedure. |
| `harness/pi` | Possible future generic textual resources or extracted generic harness implementation boundary. | Excluded initially | Generic | No generic package or resource set is accepted, and two bootstrap files do not justify extraction. |
| `harness/pi/local` | Possible future PhysKit-specific shadow/configuration over generic harness resources. | Excluded initially | PhysKit-local | There is no accepted generic harness to configure or shadow. |

No task store, checkpoint store, evidence store, agent definition, skill, chain,
validator, schema, or harness runtime is proposed for creation in the first
bootstrap.

## 4. Minimal roles and ownership

Roles describe responsibilities, not necessarily distinct agents or people. The
parent coordinator assigns bounded ownership for each task, and humans retain
protected decision authority.

### 4.1 Parent coordinator and final verifier

Owns intake, repository safety, authority reconstruction, orchestration, scope
control, checkpoint escalation, review synthesis, correction routing, final
process verification, and the human handoff. The parent may not convert its
verification into human acceptance. It is the only orchestration owner for the
active task.

### 4.2 Capability-contract or architecture owner

Drafts bounded policy, architecture, capability contracts, and decision options.
It must distinguish proposals from accepted choices and stop at every protected
human decision. It does not implement a proposed contract unless separately
assigned after acceptance.

### 4.3 Implementation owner

Makes only changes authorized by an accepted contract and bounded plan. It owns
correction of implementation defects within its path scope and reports changed
files, checks, limitations, and decisions requiring escalation.

### 4.4 Software and numerical verification owner

Designs and executes authorized deterministic checks against accepted software
and mathematical claims, preserves evidence-class distinctions, and reports
failures without changing contracts or tolerances. For small work this
responsibility may be held by the implementation owner for evidence production,
but the evidence and support claim still require independent review and human
acceptance.

### 4.5 Notebook and documentation owner

Owns the visible pedagogical construction, library-based stage, explanatory
prose, visualization, and documentation consistency within accepted learning
objectives and scientific conventions. It does not declare pedagogical
validation or select a canonical artifact.

### 4.6 Independent read-only integration reviewer

Inspects the integrated change, contracts, evidence, notebook/documentation,
and scope from outside the writer path. It reports findings only and does not
repair the work it reviews. Independent read-only review is required for:

- material policy, contract, or control-plane changes;
- public API changes;
- capability evidence used for a support claim;
- canonical-artifact proposals;
- material scientific, numerical, or pedagogical changes.

### 4.7 Proportional role collapsing

For small, low-risk work, the parent may combine parent coordination with
architecture, verification planning, or documentation coordination. One writer
may implement and produce its own deterministic checks when path ownership is
clear. Role collapsing must not:

- combine a material writer with the independent reviewer;
- remove a required human checkpoint;
- let a reviewer edit the reviewed work;
- let an implementation owner accept its own evidence;
- blur evidence classes or protected decisions.

Only a human may authorize omission of a normally required role or review for a
material change. Routine, non-material corrections may use the proportional
rules already accepted for the task.

### 4.8 Non-overlapping ownership and correction

Every bounded task must identify one owner per write path. Concurrent writers
must have non-overlapping paths and an explicit integration seam; otherwise
writes are sequential. The original owner corrects findings in its scope. The
parent assigns cross-cutting corrections to one writer, then returns the result
to the independent reviewer. Reviewers do not become correction writers during
the same review cycle.

## 5. Standard bounded work sequence

The default sequence is:

1. **Bounded intake.** Parent records the requested outcome, repository/revision,
   allowed paths, exclusions, known user work, protected decisions, and stop
   conditions.
2. **Human scope decision.** Human accepts or revises the capability/task
   boundary and authorization. This is a human checkpoint.
3. **Capability-contract proposal.** Architecture/contract owner proposes the
   pedagogical, physical, mathematical, numerical, software, artifact, evidence,
   and exclusion boundaries.
4. **Human contract acceptance.** Human accepts, revises, or rejects the contract
   and evidence obligations. This is a mandatory human checkpoint. No
   implementation may begin before it resolves affirmatively.
5. **Bounded implementation plan.** Parent or implementation owner maps accepted
   clauses to paths, ownership, ordering, checks, review, and stop rules without
   reopening protected decisions.
6. **Implementation.** One writer per path applies only authorized changes.
7. **Verification and evidence production.** Deterministic checks and authorized
   comparisons produce evidence envelopes; failures remain failures.
8. **Canonical-notebook and documentation work.** The two-stage notebook and
   documentation are produced against accepted objectives and APIs. The work may
   propose canonical status but cannot assign it.
9. **Independent read-only review.** Reviewer checks scope, contracts, software,
   numerical evidence, notebook/documentation, unsupported claims, and residual
   risks.
10. **Correction and re-review.** Parent assigns accepted corrections to the
    responsible writer; affected evidence is regenerated and the reviewer
    rechecks material changes.
11. **Parent verification.** Parent confirms repository safety, accepted scope,
    ownership, checks, evidence completeness, review disposition, no hidden
    protected decisions, and clean handoff boundaries.
12. **Human acceptance.** Human accepts, remands, limits, or rejects the work,
    evidence, artifact roles, and any proposed lifecycle transition. This is a
    mandatory human checkpoint.
13. **Closeout and lifecycle recording.** Only the human-approved outcome is
    recorded; derived summaries are updated from authority; the task closes and
    stops without starting a successor.

### 5.1 Proportional steps and omissions

- Steps 1, 2, 3, 4, 11, 12, and 13 are mandatory for a new capability or a
  material contract/support decision.
- A bounded task under an already accepted contract may omit Steps 2–4 only when
  its authorization cites that contract and introduces no protected ambiguity.
- Step 5 may be brief for a one-file deterministic correction, but ownership,
  validation, and stop rules must still be explicit.
- Steps 7 and 9 may be proportional to risk, but required evidence floors and
  independent review for material changes or support claims cannot be omitted by
  an agent.
- Step 8 is required for a student-facing supported-capability proposal unless a
  human accepts the lifecycle policy's bounded exception.
- A human authorizes every material omission. The reason and resulting claim
  limits must be visible.

### 5.2 Safe concurrency

Safe concurrency is limited to:

- read-only inspection of independent areas;
- independent review perspectives;
- deterministic checks that do not mutate shared artifacts;
- writers in explicitly isolated worktrees or non-overlapping paths with an
  accepted integration seam.

Ordering is mandatory between contract acceptance and implementation, between
implementation and claim-bearing verification, between correction and re-review,
and between parent verification and final human acceptance. In a shared dirty
worktree, ordinary writers run sequentially.

### 5.3 Fail-closed behavior

Work stops without a success claim when:

- active authority is missing, stale, malformed, or contradictory;
- repository state contains a material unexpected change;
- scope or ownership is ambiguous;
- an accepted prerequisite or human decision is absent;
- a protected choice is unresolved;
- a required deterministic check fails or was not run;
- required evidence, provenance, review, or acceptance is missing;
- a reviewer identifies an unresolved material finding;
- a push or durable review boundary cannot be established when required.

Failure does not authorize widening scope, changing tolerances, replacing
references, rewriting expected results, or launching a successor.

### 5.4 Human checkpoint behavior

At every human checkpoint, the parent presents:

- the exact decision requested;
- bounded options and consequences;
- relevant contract/evidence/review links;
- unresolved risks;
- the work that remains blocked.

Silence or timeout is not approval. Rejection or deferral stops the task. After
acceptance, only the explicitly authorized next phase may begin. Closeout always
ends with no successor active unless a separate human decision activates it.

## 6. Review modes

### 6.1 Mode A — Single-File Verification

Mode A applies to one material policy, capability contract, control-plane design,
status-authority definition, protected decision artifact, or canonical-artifact
decision at a time.

The human receives:

- one proposed file and its GitHub revision;
- authority/status marker;
- exact scope and non-decisions;
- evidence and source references used;
- independent read-only findings where material;
- deterministic structural validation;
- complete repository status and untouched-path report;
- explicit accept, revise, reject, or defer options.

Mode A stops for explicit human acceptance. It must not create, activate, or
start successor work merely because the file was committed or reviewed. A
material policy or protected decision discovered during any other mode returns
to Mode A or an explicit human checkpoint.

This `.04` proposal is a Mode A artifact.

### 6.2 Mode B — Final-Report Verification

Mode B applies only to bounded execution that follows already accepted contracts,
protected decisions, path ownership, and acceptance rules. It may cover several
implementation, test, notebook, documentation, and evidence artifacts when none
introduces a new protected choice.

The human receives:

- accepted authority and task scope cited by path and revision;
- files changed and explicitly untouched;
- commands/checks with results and environment;
- evidence envelopes and evidence-class labels;
- independent review findings and dispositions;
- parent-verification result;
- residual risks, omitted checks, and claim limits;
- complete repository status;
- explicit human acceptance options.

Mode B cannot accept a contract change, policy change, new model, new numerical
convention, public API choice, canonical artifact, learning objective, tolerance,
evidence applicability decision, validation claim, or lifecycle transition. A
material ambiguity, unsupported claim, or proposed change in any of those areas
stops Mode B and returns the decision to Mode A or a human checkpoint.

## 7. Common evidence envelope

The control plane preserves the evidence classes established by `.02`:

- software verification;
- numerical verification;
- physical validation;
- pedagogical validation;
- uncertainty quantification.

It does not redefine their applicability or acceptance. A common evidence
envelope should contain, as applicable:

| Field | Required meaning |
|---|---|
| Claim | The bounded statement the evidence addresses; no broader claim is implied. |
| Evidence class | Exactly which `.02` classification is addressed. |
| Method | Deterministic check, analytic comparison, experiment, review method, or other accepted method. |
| Inputs | Versions, parameters, fixtures, artifacts, and preconditions. |
| Environment | Relevant software, hardware, interpreter, dependency, and execution context. |
| Result | Observed output and pass/fail/indeterminate status without interpretation inflation. |
| Reference or invariant | Independent source, accepted formula, fixture, invariant, or baseline. |
| Tolerance or acceptance rule | Human-accepted rule and what it measures, or explicit unresolved status. |
| Provenance | Producer, command/procedure, time, revision, artifact paths, and checksums where warranted. |
| Limitations | Missing checks, validity bounds, assumptions, known defects, and transfer limits. |
| Reviewer | Independent reviewer identity and conclusion, or explicit not-yet-reviewed status. |
| Human-acceptance status | Proposed, pending, accepted, rejected, superseded, or not applicable only by human decision. |

This table is a design requirement, not a schema or evidence store.

### 7.1 Evidence authority distinctions

- **Agent finding:** a provisional observation or recommendation; it may trigger
  correction or escalation but cannot accept a claim.
- **Deterministic check:** reproducible evidence that its stated procedure
  produced its recorded result; it does not establish another evidence class.
- **Independent review:** a read-only assessment of scope, method, evidence, and
  claims; it can find blockers but cannot make protected decisions.
- **Parent verification:** confirmation that the accepted process and handoff are
  complete; it cannot accept scientific or pedagogical claims.
- **Human acceptance:** the decision that evidence and remaining limitations are
  adequate for a bounded claim and any associated lifecycle action.

Evidence must remain appendable and historically honest. A later defect or
superseding result is linked rather than rewriting earlier evidence to appear
current.

## 8. Notebooks as first-class pedagogical artifacts

For a student-facing capability proposed for support, the control plane should
normally require one human-designated canonical notebook after human review. The
notebook should contain:

1. an explicit construction exposing the physical model, assumptions, state
   space, mathematics, numerical representation where applicable, intermediate
   values, and visible Python without hiding the target computation behind
   PhysKit;
2. a corresponding construction using the human-accepted PhysKit public API to
   reproduce a shared baseline;
3. repeated cases, parameter exploration, comparison, convergence where
   applicable, or visualization appropriate to the accepted learning
   objectives.

The notebook must distinguish physical model, mathematical formulation, finite
representation, software behavior, and interpretation. Agreement between the
explicit and library stages is numerical-verification evidence only within its
accepted references and tolerances. Successful execution is software evidence;
it does not automatically establish physical validation, pedagogical
validation, UQ, canonical status, or lifecycle promotion.

This proposal does not design, select, execute, or modify a PIAB notebook.

## 9. Generic versus PhysKit-local boundary

### 9.1 Potentially generic mechanisms

The following mechanisms could be reusable across projects if later experience
justifies extraction:

- bounded task envelopes;
- ownership and non-overlap records;
- ordered coordination and fail-closed transitions;
- checkpoint mechanics;
- review records and read-only review separation;
- common evidence-envelope mechanics;
- parent-verification and closeout mechanics;
- a single active-state representation.

Generic mechanisms should know how to represent coordination and provenance,
not what physical model, pedagogy, evidence applicability, tolerance, or
lifecycle decision is correct.

### 9.2 PhysKit-local policy

The following remain PhysKit-local:

- pedagogical capability contracts;
- the two-stage notebook expectation and any exception;
- physical models and approximations;
- mathematical and numerical protected decisions;
- public PhysKit API and canonical-artifact decisions;
- learning objectives and pedagogical claims;
- evidence applicability and minimum floors from `.02`;
- physical, numerical, pedagogical, and UQ acceptance;
- the PhysKit capability lifecycle;
- support, deprecation, replacement, and historical decisions.

### 9.3 Dependency direction

PhysKit-local coordination may consume a future generic harness contract.
Generic harness code must not import PhysKit scientific policy, live inside
`src/physkit`, or embed the PIAB pilot. If later implementation should consume
an extracted generic Python harness, that must be proposed as a future
architectural boundary with separate package, dependency, migration, and review
decisions. This statement is not authorization to create, extract, copy, or
publish such a harness now.

## 10. Minimum bootstrap manifest

The next phase should propose and review the following exact two-file bootstrap,
sequentially. This manifest is not authorization to create either file.

| Order | Exact path | Purpose | Authority | Classification | Why required | Review mode |
|---:|---|---|---|---|---|---|
| 1 | `AGENTS.md` | Establish repository-wide human authority, startup checks, user-work preservation, single-active-state rule, bounded sequence, review modes, fail-closed behavior, and prohibition on inferred acceptance. | Authoritative repository operating policy after explicit human acceptance; never current task status. | PhysKit-local policy using generic coordination principles | Sessions otherwise depend on chat or global configuration and cannot reliably reconstruct project authority. | Mode A — Single-File Verification; stop for human acceptance before file 2. |
| 2 | `.pi/active-state.json` | Establish the sole current active-state authority with the minimum fields in Section 2, initially recording bootstrap status, no authorized successor, and the PIAB pilot parked. | Authoritative only for current coordination after explicit human acceptance; references but cannot replace durable contracts and decisions. | Generic state shape with PhysKit-local values | Git status and planning prose cannot represent current authorization, blockers, ownership, checkpoints, and parked work without contradiction. | Mode A — Single-File Verification; stop for human acceptance before any PIAB work. |

The bootstrap should not create agent definitions, task records, chains,
checkpoint stores, evidence stores, skills, schemas, validators, `harness/pi`,
`harness/pi/local`, or runtime Python. Those surfaces require evidence from
actual bounded use and a later human-reviewed need.

### 10.1 Bootstrap completion condition

The bootstrap is complete only when both files have individually passed Mode A,
the active-state file points to the accepted authority documents and records no
unauthorized active successor, the parent verifies repository status and
cross-file consistency, and a human explicitly accepts bootstrap closeout.
Closeout stops with the PIAB pilot still parked. Resuming PIAB requires another
bounded human authorization.

## 11. Parked analytical PIAB pilot

`docs/harness/physkit.harness.03-pilot-capability-selection.md` contains the
candidate comparison and preliminary boundary. The human selected Option A in
conversation: analytical stationary states of the one-dimensional infinite
square well remain the intended first pilot.

That selection is preserved without rewriting `.03`. Pilot contract planning is
deliberately parked until:

1. this control-plane proposal is explicitly accepted;
2. the two-file bootstrap is separately authorized, created, reviewed, and
   human-accepted;
3. the resulting active-state authority records the bootstrap closed, the PIAB
   pilot parked, and no successor active;
4. a later human decision explicitly authorizes resuming bounded PIAB contract
   planning.

No PIAB API, canonical artifact, notebook, tolerance, evidence obligation,
lifecycle state, verification, validation, or implementation has been accepted.
The superseded PIAB-contract drafting instruction was stopped before a file was
created. No abandoned PIAB `.04` exists or is cited as an artifact, draft, or
historical authority.

## 12. Proposed decisions, unresolved decisions, non-decisions, and authorization limits

### 12.1 Decisions proposed by this file

Human review is asked to accept, revise, or reject these proposals:

1. one active-state authority at `/.pi/active-state.json`;
2. durable policies/contracts/evidence remain separate and are referenced, not
   copied into active state;
3. derived summaries are non-authoritative;
4. the six-responsibility model with proportional role collapsing and mandatory
   independent read-only review for material changes or support claims;
5. the thirteen-step bounded work sequence and explicit human checkpoints;
6. Mode A single-file and Mode B final-report verification;
7. the common evidence-envelope fields and authority distinctions;
8. notebooks as first-class two-stage pedagogical artifacts;
9. the generic-versus-PhysKit-local boundary;
10. the sequential two-file minimum bootstrap manifest;
11. continued parking of the selected PIAB pilot through bootstrap closeout.

### 12.2 Decisions still requiring human acceptance

- whether this control-plane design is accepted;
- whether `AGENTS.md` and `/.pi/active-state.json` are the correct minimum
  bootstrap paths;
- the exact active-state fields and initial values;
- the content of the future root instruction file;
- who may fill each role for a bounded task;
- when a change is material enough to require independent review;
- what evidence storage or checkpoint persistence, if any, later use justifies;
- whether and when schemas, validators, agents, skills, chains, or generic
  harness extraction become necessary;
- bootstrap authorization and acceptance;
- later authorization to resume PIAB capability-contract planning;
- all open decisions retained by `.01`, `.02`, and `.03` unless explicitly
  addressed by a future human decision.

### 12.3 Matters deliberately not decided

- a JSON Schema or validator for active state;
- task, checkpoint, evidence, chain, or ownership record formats;
- project-specific agent prompts or model selection;
- generic harness package APIs, resource layout, extraction, or distribution;
- implementation language or runtime architecture;
- CI, dependency, packaging, serialization, or release policy;
- PIAB contract, API, notebook, tolerance, evidence plan, or implementation;
- canonical status of any existing PhysKit artifact;
- lifecycle state of PIAB or any other capability;
- whether notebook-only work may become Supported;
- repository-wide status derivation beyond the non-authoritative-summary rule.

### 12.4 Actions explicitly not authorized

Acceptance or commitment of this proposal would not authorize:

- creation or modification of `AGENTS.md`, `.pi/`, agents, skills, chains, task
  stores, checkpoint stores, evidence stores, schemas, validators, runtime code,
  `harness/pi`, or `harness/pi/local`;
- source, test, notebook, example, dependency, packaging, CI, or existing
  documentation changes;
- bootstrap implementation without a separate human instruction;
- PIAB contract planning or implementation;
- selection of a PhysKit API or canonical artifact;
- definition or acceptance of a numerical tolerance;
- verification, physical-validation, pedagogical-validation, UQ, support, or
  lifecycle claims;
- cleanup or classification of competing implementations;
- launch of a successor task after any checkpoint or closeout without explicit
  human authorization.
