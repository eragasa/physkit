# HARNESS-CAPABILITY-1 — Reusable capability-workflow bootstrap

**Status:** Awaiting human final acceptance
**Task ID:** `HARNESS-CAPABILITY-1`
**Reusable chain ID:** `PHYSKIT-CAPABILITY-DEVELOPMENT` (`inactive`)
**Current checkpoint:** `HARNESS-CAPABILITY-1-HC01` (`pending`; human final acceptance)

## Purpose and boundary

Build and verify the reusable PhysKit capability-development workflow: five specialized project roles, one inactive reusable chain, and current coordination in active state. This is a harness-development task, not a scientific capability task. It selects no learner purpose, physics model, mathematical or numerical representation, API, notebook, evidence criterion, lifecycle state, or pilot. PIAB remains parked.

## Source policies and patterns

Authoritative local boundaries:

- `AGENTS.md` — repository operating policy and human authority;
- `docs/harness/physkit.harness.02-capability-lifecycle.md` — lifecycle and evidence-class distinctions within its accepted role;
- `docs/harness/physkit.harness.04-minimal-pi-control-plane.md` — bounded sequence, ownership, review, notebook, checkpoint, and closeout principles;
- `.pi/active-state.json` — sole current runtime-coordination authority.

Generic ksdft2effmass `dev` patterns were inspected read-only only for stable coordination conventions: role frontmatter, exact writer ownership, separate source/test/documentation writers, ordered stages, human gates, independent read-only review, owner correction, and stop-before-successor behavior. No research-campaign, DFT, HPC, CPN, Rust, serialization, backend, branch, or project-specific scientific policy is imported.

## Exact bootstrap ownership

The parent coordinator is the sole bounded bootstrap writer and owns exactly:

- `.pi/active-state.json`;
- `.pi/agents/physkit-capability-architect.md`;
- `.pi/agents/physkit-implementation.md`;
- `.pi/agents/physkit-verification.md`;
- `.pi/agents/physkit-notebook-documentation.md`;
- `.pi/agents/physkit-capability-integration-reviewer.md`;
- `.pi/tasks/capability-workflow-bootstrap.md`; and
- `.pi/chains/capability-development.chain.json`.

No source, test, notebook, user-documentation, capability-contract, evidence-summary, or physics-capability ownership is active. The reusable roles acquire exact nonoverlapping paths only through a later human-authorized capability task.

## Role responsibilities and nonoverlap

- **Parent coordinator:** activation, task and active-state coordination, exact ownership assignment, correction routing, final parent verification, and human checkpoint presentation.
- **Capability architect:** exact task-owned contract/architecture proposals only; cannot implement or accept its own contract.
- **Implementation writer:** exact task-owned production source under `src/physkit/` only after contract acceptance; cannot write tests or notebooks.
- **Verification writer:** exact task-owned tests under `tests/` and later explicitly justified evidence summaries; cannot repair production source.
- **Notebook/documentation writer:** exact task-owned notebooks and user-facing documentation; cannot alter source or tests.
- **Capability integration reviewer:** independent and read-only; routes findings to the appropriate owner.
- **Human:** owns capability scope and every protected scientific, mathematical, numerical, API, pedagogical, evidence-acceptance, canonical-artifact, lifecycle, final-acceptance, and successor decision.

Multiple specialized writers are retained. Ownership must be exact and nonoverlapping; compatible work may proceed concurrently only with explicit seams and dependency gates.

## Reusable chain requirements

`.pi/chains/capability-development.chain.json` encodes sixteen ordered stages from human scope through closeout. Human capability scope gates contract drafting. Human contract acceptance gates implementation. Source, test/evidence, and notebook/documentation ownership remain separate. Explicit notebook construction may begin after contract acceptance only when independent of unaccepted implementation behavior; library reconstruction requires the implemented accepted API. Review is read-only, findings route to their owners, corrections trigger verification replay and re-review, parent verification is not human acceptance, and closeout authorizes no successor. Lifecycle promotion is outside the chain without separate human authority.

The chain is reusable but inactive. No capability is selected or activated.

## Explicit exclusions

Do not create or modify source, tests, notebooks, user documentation, curriculum views, evidence stores, checkpoint files, skills, schemas, validators, runtime code, dependencies, packaging, CI, planning documents, existing agents/tasks/chains, or `AGENTS.md`. Do not activate PIAB or any capability; define physics, numerical conventions, APIs, tolerances, evidence applicability, canonical artifacts, or lifecycle states; or authorize a successor. `package-lock.json` remains unrelated, uninspected, unmodified, and unstaged.

## Notebook and evidence boundaries

The notebook writer normally exposes: (1) explicit physical/mathematical/computational construction and direct verification, (2) reconstruction through the accepted PhysKit API with an explicit comparison, and (3) multiple cases, sweeps, comparisons, visualization, and bounded interpretation. Execution or agreement does not establish physical or pedagogical acceptance.

The workflow keeps software verification, numerical verification, physical validation, pedagogical validation, and uncertainty quantification distinct. Missing evidence is not `Not applicable` without accepted human justification.

## Notebook-pilot operational lessons

- use `python3` when Python is required;
- treat unexpected repository-local subagent artifacts as a stop condition;
- do not leave `.pi-subagents/` or similar temporary directories in the repository;
- place temporary review artifacts outside the repository or disable repository artifact creation;
- validate exact staged-path isolation before commit; and
- require parent verification rather than inferring success from a subagent report.

## Validation, review, and findings

Deterministic validation and one independent read-only review are required before commit. Validation must cover JSON parsing and duplicate keys, active-state/task/agent/chain consistency, all sixteen ordered stages and gates, inactive/no-capability status, empty source/test/notebook ownership, role nonoverlap, owner-specific correction, evidence-class separation, PIAB parking, successor denial, exact staged paths, excluded-path preservation, temporary-artifact absence, and `git diff --check`.

Independent review status: **PASS**. The read-only capability integration reviewer found no blocker, high, medium, or material findings. It confirmed role nonoverlap, retention of multiple specialized writers, human scope and contract gates, notebook-stage ordering, evidence-class separation, owner-specific correction, inactive/no-capability state, PIAB and notebook-work parking, successor denial, operational lessons, and absence of foreign scientific-policy leakage. Repository artifact creation was disabled and no durable reviewer artifact was created.

The only low finding was pre-existing declarative staleness in excluded, already accepted notebook-workflow files. Active state is the sole current authority, those files grant no current authorization, and changing them is prohibited by this task. No correction or re-review was required.

Parent structural verification: **PASS**. Using `python3`, the parent independently checked duplicate-free JSON, eight-path/role/task/chain consistency, all sixteen ordered stages, the human gates, exact empty capability ownership, writer separation, owner-specific correction routing, notebook dependencies, evidence distinctions, inactive-chain/no-capability status, PIAB parking, successor denial, temporary-artifact absence, and `git diff --check`. Final staged-path and remote-freshness checks remain required immediately before commit.

## Evidence limitations and pending decision

This bootstrap can establish only structural and coordination consistency of the role and chain definitions. It does not execute the reusable chain, exercise future multi-writer handoffs, validate any physics or numerical method, establish pedagogical effectiveness, accept an API or capability contract, or assign lifecycle status.

Final human acceptance of `HARNESS-CAPABILITY-1` is pending. Acceptance would accept only this reusable inactive workflow surface. Successor authorization is `false`; successor is `null`.
