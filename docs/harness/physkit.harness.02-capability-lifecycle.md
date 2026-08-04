# PhysKit Capability Lifecycle

## 1. Document status and authority

**Status:** Proposed for human review

**Proposed path:**
`docs/harness/physkit.harness.02-capability-lifecycle.md`

This document proposes policy only. Committing or publishing it does not
constitute acceptance. It gains authority only through explicit human review
and acceptance, and only within the scope accepted by that review.

If accepted, this document would govern how a bounded PhysKit capability may be
classified and moved between lifecycle states. It would not itself:

- classify any existing capability or artifact;
- accept a capability contract or public API;
- accept evidence, tolerances, models, conventions, or learning objectives;
- select a canonical implementation or notebook;
- authorize an agent to promote, regress, deprecate, or archive anything;
- create active Pi runtime state or the rest of a control plane.

Every classification of existing PhysKit material remains pending.

## 2. Purpose

The purpose of this policy is to provide a small, human-controlled vocabulary
for moving a bounded pedagogical or computational capability from exploration
toward human-accepted support, and eventually through correction, withdrawal,
or historical preservation when necessary.

The policy separates three questions that must not be collapsed:

1. What human-recognized capability is under consideration?
2. What lifecycle claims may currently be made about it?
3. What evidence exists for distinct kinds of verification and validation?

Passing a check can add evidence. It cannot, by itself, answer all three
questions or cause a lifecycle transition.

## 3. Scope and exclusions

This policy applies to bounded PhysKit capabilities and to the artifacts and
evidence associated with them. It proposes:

- lifecycle states and transition rules;
- capability–artifact relationships;
- independent evidence classifications;
- a preferred contract for supported student-facing notebooks;
- treatment of notebook-only work and supporting infrastructure;
- human and agent authority boundaries;
- correction, regression, deprecation, and historical-preservation rules.

This policy does not:

- design or implement the rest of the PhysKit Pi control plane;
- define a record schema, directory layout, agent, chain, skill, checkpoint, or
  runtime-state format;
- select a pilot capability;
- classify any existing module, notebook, test, fixture, document, or
  capability group;
- select any physical model, approximation, mathematical formulation,
  numerical convention, public API, implementation, notebook, learning
  objective, reference, invariant, or tolerance;
- repair source, tests, notebooks, or documentation;
- change `README.md` or establish a derived project-status mechanism.

## 4. Definitions

### 4.1 Capability

A **capability** is a bounded, human-recognized unit of pedagogical or
computational functionality with an explicit intended use and boundary.
Examples of possible boundaries include a particular kind of conversion,
analytic calculation, numerical solution, visualization-supported lesson, or
empirical correlation. These examples do not classify any repository content.

A capability exists as a governance subject only after a human recognizes its
boundary. Similar files need not belong to one capability, and one capability
may span many files.

### 4.2 Capability contract

A **capability contract** is a human-accepted statement, appropriate to the
capability, of its intended use, audience where applicable, scope, exclusions,
physical and mathematical basis, conventions, inputs, outputs, units, public
interface where applicable, expected behavior, and evidence obligations.

A proposed contract is not accepted merely because an agent drafted it or an
implementation satisfies it. Protected scientific, numerical, API, and
pedagogical choices require human acceptance.

### 4.3 Artifact

An **artifact** is a concrete representation or source of evidence associated
with a capability. Artifacts may include:

- notebooks;
- library objects;
- tests;
- fixtures;
- reference cases;
- visualizations;
- documentation;
- validation or uncertainty records.

A file is not automatically a capability merely because it exists. A file may
support multiple capabilities, and a capability may have several alternative,
exploratory, canonical, generated, or historical artifacts.

### 4.4 Canonical artifact

A **canonical artifact** is the human-designated representation to which a
specific accepted claim refers. Canonical status is scoped: an artifact could,
for example, be canonical for a student-facing explanation without being the
canonical reusable implementation. Only a human may declare or replace a
canonical artifact.

### 4.5 Lifecycle state

A **lifecycle state** limits the support and maturity claims that may be made
about a capability. It is not a score and is not inferred from file location,
code volume, passing tests, publication, age, or evidence count.

### 4.6 Evidence classification

An **evidence classification** identifies what kind of claim a body of evidence
addresses. Evidence classifications are orthogonal to lifecycle states and to
one another. Evidence may be incomplete, disputed, stale, or inapplicable even
when other evidence is strong.

### 4.7 Human approval

**Human approval** means an explicit, reviewable decision by a person with the
relevant project and subject-matter authority. Silence, a merge, a commit, an
agent recommendation, or the absence of a failing check is not approval unless
a separately accepted policy explicitly says otherwise. This proposal creates
no such alternative mechanism.

## 5. Proposed lifecycle states

The proposed vocabulary is intentionally limited to five states:
**Exploratory**, **Candidate**, **Supported**, **Deprecated**, and
**Historical**. Exploratory, Candidate, and Supported describe increasing
maturity of a current capability. Deprecated and Historical preserve honest
withdrawal and provenance without pretending that old evidence is current.

### 5.1 Exploratory

**Meaning**

Work is being used to investigate a pedagogical or computational idea. Its
boundary, contract, implementation, conventions, or intended use may still
change.

**Entry requirements**

- A human recognizes the work as a bounded exploration or permits it to remain
  an artifact associated with a prospective capability.
- Its exploratory status is made clear wherever a support claim might
  otherwise be inferred.
- Known material assumptions and limitations are recorded to the extent needed
  for safe interpretation.

**Allowed work**

- direct mathematical and physical construction;
- notebook experiments and pedagogical prototypes;
- competing implementations and conventions;
- feasibility checks, test prototypes, and evidence collection;
- proposals for a capability boundary and contract.

**Prohibited claims**

- that the capability or API is supported, canonical, validated, or accepted;
- that an exploratory notebook represents supported library functionality;
- that passing exploratory checks establishes suitability for teaching or
  scientific use.

**Exit requirements**

To enter Candidate, a human must accept a bounded proposed capability and
contract as ready for implementation and evidence development. To enter
Historical, a human must decide that the exploration is no longer current and
should be preserved rather than pursued.

**Permitted transitions**

- Exploratory → Candidate
- Exploratory → Historical

**Required human approval**

Human approval is required for both transitions and for selecting any protected
contract choice. Agents may recommend either transition but may not perform it.

**Newly discovered defects**

Defects and discrepancies are recorded as exploratory findings. They do not
cause an automatic state change, but they may block a proposal to enter
Candidate. Material safety, scientific, or pedagogical concerns must be
escalated to a human before claims or reuse continue.

### 5.2 Candidate

**Meaning**

A human has accepted the capability boundary and a contract for bounded
implementation and evaluation, but the capability is not currently Supported.
Candidate means “under review against an accepted contract,” not “nearly
supported.” A return to Candidate from Supported or Deprecated preserves, and
does not deny, the earlier support history.

**Entry requirements**

- an explicitly bounded, human-accepted capability contract;
- identified intended users or uses;
- identified artifacts and artifact roles sufficient to evaluate the contract;
- declared evidence requirements for every evidence classification, including
  accepted rationales for any class proposed as not applicable;
- no unresolved decision disguised as an implementation detail.

**Allowed work**

- implementation of the accepted contract;
- deterministic checks and notebook execution;
- reference-case, convergence, comparison, validation, and UQ work as required;
- documentation and canonical-artifact proposals;
- correction of discrepancies within the accepted contract;
- collection and review of evidence.

**Prohibited claims**

- that the capability is supported merely because its contract is accepted;
- that an API or notebook is canonical unless a human has separately declared
  it so;
- that test passage establishes numerical, physical, or pedagogical validation;
- that unresolved or rejected evidence satisfies promotion requirements.

**Exit requirements**

To enter Supported, all promotion-blocking requirements must be resolved, the
required evidence must be available and accepted by the appropriate humans,
canonical artifacts and public claims must be explicitly selected, and a human
must approve promotion. To regress to Exploratory, a human must determine that
the contract or boundary requires material reconsideration. To enter
Historical, a human must withdraw the candidate from current consideration
while preserving its record.

**Permitted transitions**

- Candidate → Supported
- Candidate → Exploratory
- Candidate → Historical

**Required human approval**

Every transition requires explicit human approval. Humans also accept the
contract, evidence obligations, evidence findings, tolerances, and canonical
artifacts. Agents may implement and assess conformance but may not convert those
results into approval.

**Newly discovered defects**

Defects are recorded against the affected contract clause and evidence claims.
A defect blocks promotion whenever it leaves a required claim unresolved. A
human decides whether correction remains within Candidate scope, the capability
regresses to Exploratory, or current work is preserved as Historical.

### 5.3 Supported

**Meaning**

A human has accepted a bounded capability for stated uses under a specific
contract, with identified canonical artifacts, accepted evidence, documented
limitations, and maintenance expectations. Support does not extend beyond the
accepted scope.

**Entry requirements**

- all Candidate entry and exit requirements are satisfied;
- the capability contract, public API where applicable, and canonical artifacts
  are explicitly accepted by humans;
- every evidence classification is dispositioned proportionally as required,
  conditionally required, not applicable with accepted rationale, or resolved
  from a previously blocking state;
- accepted limitations, environments, versions, references, and tolerances are
  stated;
- maintenance, defect-reporting, and review expectations are understood;
- explicit human promotion approval is recorded.

**Allowed work**

- use within the accepted support boundary;
- maintenance, documentation, examples, and compatible extension;
- deterministic regression checks and evidence renewal;
- proposed contract changes evaluated through Candidate work;
- correction that preserves the accepted contract and historical record.

**Prohibited claims**

- support outside the accepted uses, versions, limitations, or evidence scope;
- automatic validation of new models, parameter regimes, audiences, or
  implementations by analogy;
- treating a passing regression suite as proof that all evidence remains
  current;
- unreviewed replacement of canonical APIs, notebooks, or conventions.

**Exit requirements**

A human may regress the capability to Candidate when the accepted contract can
remain the evaluation basis but support claims are no longer adequately
substantiated. A human may move it to Deprecated when support is being
withdrawn or a replacement or retirement path is intended. A Supported
capability does not move directly to Historical; withdrawal should remain
visible through Deprecated first.

**Permitted transitions**

- Supported → Candidate
- Supported → Deprecated

**Required human approval**

Promotion to Supported, changes to the supported contract, regression, and
deprecation all require explicit human approval. Agents may flag that a support
claim is no longer justified and recommend an immediate human review, but may
not change the state.

**Newly discovered defects**

A newly discovered defect must be recorded without rewriting the evidence that
supported the earlier decision. A human must assess affected uses and decide
whether to:

- retain Supported with a documented limitation and correction plan;
- place a human-declared hold on affected support claims while review occurs;
- regress to Candidate for renewed evaluation; or
- withdraw support through Deprecated.

Until that decision, agents must surface the defect and must not repeat an
affected claim as if the defect were unknown. A hold is a temporary human
instruction, not an additional lifecycle state.

### 5.4 Deprecated

**Meaning**

The capability was previously Supported, but a human has declared that support
is being withdrawn or that users should move away from it. Deprecated preserves
the former contract and evidence while making the current support limitation
explicit.

**Entry requirements**

- a human decision to withdraw or phase out support;
- a stated reason, affected scope, effective timing, and known consequences;
- a migration or replacement statement where one exists, without requiring a
  replacement to exist;
- preservation of the evidence and decisions that led to prior support.

**Allowed work**

- critical corrections and migration assistance;
- compatibility maintenance explicitly approved for the deprecation period;
- documentation of limitations, replacements, and provenance;
- evidence collection needed to understand residual risk.

**Prohibited claims**

- that the capability remains generally supported;
- that a proposed replacement is supported or canonical without its own human
  decision;
- erasure or rewriting of the formerly accepted contract and evidence;
- silent removal that prevents users from understanding the change.

**Exit requirements**

To enter Historical, a human must determine that current support and migration
obligations have ended and that preservation is the remaining purpose. If work
is to be restored, it must return to Candidate for renewed evaluation rather
than directly to Supported.

**Permitted transitions**

- Deprecated → Historical
- Deprecated → Candidate

**Required human approval**

Deprecation, restoration to Candidate, and transition to Historical each
require explicit human approval.

**Newly discovered defects**

New defects are appended to the current record and reflected in warnings or
migration guidance as humans direct. They may accelerate withdrawal, but no
agent may unilaterally change timing, remove artifacts, or declare the
capability Historical.

### 5.5 Historical

**Meaning**

The capability or exploration is retained for provenance, reproducibility,
comparison, or pedagogical history, but it is not current and carries no support
claim.

**Entry requirements**

- a human decision that current development, evaluation, support, or migration
  obligations have ended;
- clear historical labeling;
- preservation of relevant provenance, prior decisions, known defects, and the
  lifecycle path by which the material became historical.

**Allowed work**

- preservation, indexing, provenance correction, and non-destructive annotation;
- reproducibility work that does not misstate present support;
- reference by successor work with clear historical context.

**Prohibited claims**

- that historical material is supported, current, canonical for current use,
  or validated for a new use;
- rewriting old evidence or decisions to match current understanding;
- silently reviving historical artifacts as current implementation.

**Exit requirements**

Historical is terminal for that recorded lifecycle line. Renewed work begins as
a new Exploratory or Candidate lifecycle line, as humans decide, linked to but
not overwriting the historical one.

**Permitted transitions**

- none within the same lifecycle line

**Required human approval**

Entry requires explicit human approval. Any successor or revival requires a new
human decision and a new current lifecycle line.

**Newly discovered defects**

Defects are appended as later findings with dates and provenance. Historical
records are not rewritten to imply that earlier reviewers knew the later fact.

## 6. Transition rules

1. Lifecycle transitions are explicit human decisions; they are never computed
   from test results, evidence counts, agent confidence, elapsed time, merge
   status, or file location.
2. An agent may recommend a transition only by identifying the applicable
   contract, evidence, discrepancies, unresolved decisions, and proposed
   rationale.
3. Entry and exit requirements are conjunctive unless a human explicitly
   accepts a scoped exception. An exception must identify its rationale and the
   claims it limits; it must not be treated as silent satisfaction.
4. Promotion means movement toward Supported. Promotion requires accepted
   evidence, but accepted evidence does not require or trigger promotion.
5. Regression and withdrawal are legitimate integrity-preserving outcomes, not
   process failures to conceal.
6. A contract change that materially alters the physical model, approximation,
   mathematical or numerical convention, public behavior, supported use, or
   learning objective requires renewed human review. Existing support does not
   automatically cover the change.
7. Artifacts may mature, be replaced, or become historical without forcing a
   capability transition, provided the capability's accepted claims remain
   satisfied and humans approve any canonical replacement.
8. A capability transition does not automatically classify every associated
   artifact at the same state.
9. Transition records must preserve the prior state, decision, evidence available
   at the time, approver, rationale, effective scope, and later superseding
   decision. This policy does not prescribe a schema for those records.

## 7. Capability–artifact relationships

A capability is the governed unit; files and other artifacts are representations
or evidence. Therefore:

- a file's existence, importability, or location under `src/` does not create a
  capability or establish support;
- a notebook's pedagogical value does not make it a supported library API;
- a test's relationship to a file does not prove that it tests an accepted
  capability contract;
- a capability may use multiple artifacts with explicit roles;
- one artifact may support multiple capabilities, but each claimed relationship
  must be stated rather than inferred;
- alternatives and historical artifacts may be retained without being
  canonical;
- canonical selection and replacement are human decisions scoped to a stated
  role.

An associated artifact should identify, directly or through accepted
traceability, which capability and contract claim it supports, its role, its
status relative to that role, and any relevant version or provenance. This
policy does not define the storage format for that information.

## 8. Independent evidence classifications

Lifecycle status and evidence are separate. PhysKit uses the following evidence
classifications:

### 8.1 Software verification

Evidence that implementation behavior conforms to an accepted software
contract: interfaces, types, shapes, units handling, error behavior,
serialization, determinism where promised, compatibility, and regression
behavior.

Software verification does not by itself establish numerical correctness,
physical adequacy, learning effectiveness, or uncertainty characterization.

### 8.2 Numerical verification

Evidence that equations or algorithms are implemented and solved as intended.
It may include analytic comparisons, manufactured solutions, invariant checks,
convergence studies, independent implementations, reference cases, and declared
tolerances.

Agreement between explicit notebook code and PhysKit for a shared baseline case
is numerical-verification evidence only to the extent justified by the
comparison design. Shared mistakes, inadequate references, or accepted loose
tolerances remain possible.

### 8.3 Physical validation

Evidence that the selected model and its results are adequate for a stated
physical use. It may involve experimental data, established theory, trusted
benchmarks, domain review, stated regimes of validity, and model-discrepancy
analysis.

Physical validation is scoped to a model, regime, use, and evidence basis. It is
not implied by numerically solving the selected equations correctly.

### 8.4 Pedagogical validation

Evidence that a student-facing capability supports accepted learning objectives
for intended learners in an intended setting. It may include instructor review,
learner observation, assessment results, accessibility review, or other
human-accepted pedagogical methods.

A clear notebook, an executed notebook, or agreement with a library result does
not automatically establish pedagogical validation.

### 8.5 Uncertainty quantification

Evidence that relevant input, parameter, numerical, model-form, empirical, or
measurement uncertainties have been identified and characterized appropriately
for the stated use. Applicability and required depth depend on the capability.

A deterministic tolerance check is not automatically UQ. Conversely, an
accepted rationale may establish that UQ is not applicable to a tightly bounded
capability.

### 8.6 Independence rules

- Evidence may contribute to more than one classification only when the claim
  and rationale for each use are explicit.
- Passing software tests cannot silently stand in for another classification.
- Numerical agreement cannot silently stand in for physical or pedagogical
  validation.
- Validation in one parameter regime, environment, audience, or use does not
  automatically transfer to another.
- Evidence can become stale without an automatic lifecycle transition; the
  staleness must be surfaced for human disposition.
- Humans accept evidence claims and tolerances. Agents may run checks, collect
  outputs, identify discrepancies, and recommend a disposition.

## 9. Pedagogical notebook contract

Every Supported student-facing capability should preferably have a
human-designated canonical notebook with two visible stages. A human may accept
an exception when a notebook is unsuitable, but the rationale and an adequate
alternative pedagogical representation must be explicit.

### 9.1 Stage 1: Explicit construction

Stage 1 exposes, as applicable:

- the physical model;
- assumptions and regime of use;
- state space;
- equations and operators;
- parameters, units, and data provenance;
- initial and boundary conditions;
- basis, mesh, or grid;
- discretization;
- arrays or matrices;
- algorithm or solver steps;
- intermediate results;
- visible Python implementation.

The target computation must not be hidden behind PhysKit during this stage.
Supporting packages may be used transparently, but the learner must be able to
see the construction relevant to the accepted learning objectives.

### 9.2 Stage 2: PhysKit application

Stage 2 uses the human-accepted public PhysKit API to reproduce a shared
baseline case and then perform reusable work such as:

- parameter sweeps;
- multiple initial or boundary conditions;
- model comparisons;
- convergence studies;
- ensembles;
- comparative visualization.

Where practical, the explicit and library implementations should be compared
using human-declared invariants, references, or tolerances. The comparison must
state what is being compared, why the reference is suitable, and what scope of
agreement is claimed.

Agreement is numerical-verification evidence. It is not automatically physical
validation, pedagogical validation, software verification beyond the exercised
contract, or UQ.

### 9.3 Notebook acceptance limits

Execution without errors, saved outputs, attractive visualizations, and a
passing baseline comparison are relevant evidence but do not make a notebook
canonical. Humans select the notebook, learning objectives, intended learners,
scientific and numerical conventions, and acceptable evidence.

## 10. Notebook-only work

Exploratory and pedagogically useful notebooks may exist before any reusable
library API is accepted. A notebook-only capability may remain Exploratory, and
a human may accept it as Candidate for bounded pedagogical evaluation without
committing to library extraction.

Not every notebook should become library functionality. Extraction is warranted
only when humans accept a reusable capability boundary and API need.

Notebook-only work must not be represented as a Supported library capability.
Misrepresentation is prevented by requiring all of the following for a library
support claim:

- a human-recognized library capability boundary;
- an accepted contract and public API;
- identified canonical library artifacts;
- proportional accepted evidence;
- explicit human promotion to Supported.

Absent those decisions, notebook code remains notebook-local even if it is
reusable-looking, imported elsewhere, well tested within the notebook, or
published. Labels and documentation must state its actual scope and lifecycle
state without implying library support.

This policy leaves unresolved whether a notebook-only pedagogical capability
may eventually become Supported without a reusable PhysKit API; that is a human
policy decision recorded in Section 16.

## 11. Supporting infrastructure

Supporting infrastructure may include plotting helpers, result containers,
serialization, notebook-execution helpers, test utilities, and validation
helpers. Infrastructure need not have an artificial standalone teaching
notebook when it has no independent pedagogical purpose.

Infrastructure must identify which pedagogical or computational capability or
capabilities it supports and which contract claims depend on it. Its evidence
requirements should follow the risks it introduces. For example, a plotting
helper may require software checks and truthful labeling, while serialization
may additionally require compatibility and round-trip evidence.

Infrastructure does not inherit Supported status merely because a Supported
capability uses it. Conversely, an internal infrastructure defect can affect a
Supported capability's evidence and must be assessed through that capability's
defect process.

If infrastructure is exposed as a public, independently promised function, a
human may recognize it as a capability in its own right. This proposal makes no
such classification.

## 12. Proportional evidence requirements

Evidence obligations must be tailored to the capability's claims and risks. A
unit conversion, analytic model, numerical solver, empirical materials
correlation, and teaching visualization need not satisfy identical evidence
plans.

For each capability and each evidence classification, humans must accept one of
these dispositions:

- **Required:** evidence must be accepted before promotion to Supported and
  maintained as specified.
- **Conditionally required:** stated conditions determine when evidence becomes
  required; the conditions and interim claim limits must be accepted.
- **Not applicable:** a human accepts a rationale explaining why the
  classification does not apply to the bounded claim.
- **Unresolved—blocking promotion:** applicability, method, reference,
  tolerance, adequacy, or acceptance remains undecided, so promotion is
  prohibited.

These dispositions describe obligations, not positive findings. “Required” does
not mean “satisfied,” and “not applicable” is not a default for missing work.

Proportionality may consider:

- whether the capability is exact, analytic, numerical, empirical, or
  data-driven;
- intended users and consequences of error;
- parameter range and regime of validity;
- discretization, solver, and conditioning risks;
- external data quality and provenance;
- sensitivity to assumptions and uncertainty;
- pedagogical purpose and learner prerequisites;
- stability and compatibility promises.

Agents may propose an evidence plan and rationale. Humans decide applicability,
references, invariants, tolerances, sufficiency, and acceptance.

## 13. Human and agent authority

### 13.1 Human authority

Humans retain authority to:

- recognize and bound a capability;
- define intended users, uses, and learning objectives;
- select physical models and approximations;
- select mathematical formulations and numerical conventions;
- accept capability contracts and public APIs;
- select canonical implementations, notebooks, references, and artifacts;
- define and accept invariants, tolerances, and evidence requirements;
- declare software or numerical verification adequate;
- declare physical or pedagogical validation;
- accept UQ or a not-applicable rationale;
- approve every lifecycle transition;
- promote, regress, replace, deprecate, withdraw, or preserve a capability;
- accept exceptions and the limits they impose.

Different decisions may require different project, physics, numerical,
software, or pedagogical expertise. This proposal does not assign people or
roles to those approvals.

### 13.2 Agent authority

Agents may:

- inspect artifacts within an authorized scope;
- identify discrepancies, missing relationships, stale evidence, and defects;
- propose capability boundaries, contracts, evidence plans, and transitions;
- implement a human-accepted contract;
- run deterministic checks and authorized comparisons;
- collect and summarize evidence with provenance and limitations;
- recommend correction, regression, deprecation, or other transitions.

Agents must not unilaterally:

- select physical models or approximations;
- select mathematical or numerical conventions;
- declare a public API or artifact canonical;
- define learning objectives;
- accept references, invariants, tolerances, evidence, exceptions, or
  not-applicable rationales;
- declare software or numerical verification sufficient;
- declare physical or pedagogical validation;
- declare UQ adequate;
- promote, replace, regress, deprecate, withdraw, archive, or revive a
  capability.

Agents must distinguish observed facts, inferences, proposals, and human
acceptance. An agent's successful check or recommendation has evidentiary value
only within its stated method and limitations.

## 14. Regression, deprecation, and historical preservation

Correction must preserve the distinction between what was believed then and
what is known now.

- New evidence is appended or linked; earlier evidence is not rewritten to
  appear current or prescient.
- Corrections identify the affected versions, artifacts, claims, regimes, and
  users where known.
- A compatible correction may occur within a lifecycle state, but humans decide
  whether accepted claims and canonical artifacts remain intact.
- Material uncertainty about a Supported claim may justify human-declared claim
  limits, regression to Candidate, or withdrawal through Deprecated.
- Regression does not erase prior support. It records that the current evidence
  or contract no longer justifies the same claim.
- Deprecation communicates withdrawal, timing, consequences, and migration
  guidance without retroactively denying that support was once accepted.
- Historical preservation retains provenance, prior decisions, evidence,
  defects, and superseding links. It makes no current support claim.
- Replacement is not automatic. A successor must establish its own capability
  boundary, contract, evidence, canonical artifacts, and human-approved state.
- Historical material is not silently repurposed. Revival begins a new linked
  lifecycle line.

## 15. Relationship to the accepted baseline

This proposal follows the capability baseline identified as accepted by the
human instruction for this planning step:

`docs/harness/physkit.harness.01-capability-baseline.md`

That acceptance does not rewrite the baseline's embedded proposal-era status or
its recorded limits. The baseline remains a revision- and worktree-qualified
inspection snapshot. It records observations, discrepancies, capability
groupings, evidence gaps, and protected human decisions. It explicitly assigns
no maturity and leaves every classification pending.

This proposal does not reinterpret those findings as lifecycle assignments. In
particular, it does not infer a state from source declarations, imports, test
source, notebooks, documentation, saved output, discrepancies, or capability
group membership recorded in the baseline.

If this policy is accepted, applying it to any bounded capability requires a
separate human-reviewed decision using current evidence. The baseline may be
cited as historical planning evidence, but it must remain unchanged as a record
of its stated revision and worktree. Later evidence should supersede or qualify
its observations through new records rather than rewriting it.

## 16. Unresolved human decisions

Human review must still decide:

1. whether to accept, revise, or reject the five proposed lifecycle states and
   permitted transitions;
2. what form constitutes explicit approval and who has authority for each kind
   of scientific, numerical, software, pedagogical, and project decision;
3. whether temporary support holds need policy beyond the bounded mechanism
   described here;
4. what minimum traceability is required among capabilities, contracts,
   artifacts, evidence, decisions, and versions;
5. what record formats, locations, update rules, and retention rules should be
   designed later, if any;
6. when evidence becomes stale and what review cadence is appropriate for
   different capability types;
7. whether and under what requirements a notebook-only pedagogical capability
   may become Supported without a reusable PhysKit API;
8. what exceptions to the preferred two-stage canonical notebook contract are
   acceptable;
9. which evidence acceptance decisions require domain experts, instructors,
   learners, maintainers, or multiple reviewers;
10. how public status summaries might eventually be derived without competing
    with capability-level authority;
11. whether a future pilot should be selected and, only then, which bounded
    capability it should be.

None of these decisions is resolved by committing this proposal.

## 17. Explicit non-decisions

This document explicitly does not:

1. assign a lifecycle state to any existing PhysKit capability or artifact;
2. select a pilot capability;
3. select a canonical implementation, library object, notebook, test,
   visualization, document, reference case, or fixture;
4. select a physical model, approximation, equation, operator, boundary or
   initial condition, basis, mesh, grid, discretization, algorithm, or solver;
5. select units, parameter conventions, matrix orientation, indexing, public
   API, learning objectives, references, invariants, or tolerances;
6. declare any test passing or any capability verified or validated;
7. decide that any existing notebook should become library functionality;
8. classify any existing infrastructure as independent or supported;
9. repair or replace any source, test, notebook, example, or documentation;
10. update `README.md` or establish current project status;
11. create capability records, schemas, agents, chains, skills, checkpoints,
    `.pi/`, runtime state, or any other control-plane component;
12. accept this proposal merely because it is committed or published.
