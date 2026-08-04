# NOTEBOOK-ORG-1 — Bounded notebook organization

**Status:** Awaiting human scope decision
**Task ID:** `NOTEBOOK-ORG-1`
**Chain ID:** `NOTEBOOK-ORG-1`
**Current checkpoint:** `NOTEBOOK-ORG-1-HC01` (`pending`)

## Purpose

Use the accepted inventory and classification principles to perform small, human-selected notebook-organization batches. This task governs later organization of the existing notebook collection; it does not itself authorize a batch or any notebook change.

## Inputs and authority

- `docs/harness/physkit.harness.05-notebook-curriculum-inventory-and-options.md` — accepted inventory snapshot;
- `docs/harness/physkit.harness.06-subject-taxonomy-and-multiview-classification.md` — accepted nonexclusive classification model;
- `docs/harness/physkit.harness.07-notebook-canonical-path-mapping.md` — advisory path-mapping proposal, not blanket-accepted;
- `AGENTS.md` — repository operational policy;
- `.pi/active-state.json` — sole authority for current runtime coordination.

None of `.07`'s 127 paths, filename changes, duplicate dispositions, or proposed batches is accepted merely by reference here. PIAB remains parked.

## Authorized scope and current status

Current status is **Awaiting human scope decision**. The only current work is coordination at `NOTEBOOK-ORG-1-HC01`. Curator ownership is empty and no notebook path is writable until the human supplies a valid exact batch and the parent records it in active state and this task. No migration, rename, content edit, reference update, duplicate resolution, repair, or notebook execution is currently authorized.

## Human scope checkpoint — NOTEBOOK-ORG-1-HC01

The human must **select, revise, or reject one exact first batch**. The checkpoint does not preselect viscoelasticity, PIAB, or any other subject.

A valid affirmative response must identify:

1. exact source paths;
2. exact destination paths;
3. whether each filename change is accepted;
4. whether content changes are allowed and their exact limits;
5. whether reference updates are allowed and their exact path limits;
6. required verification, including whether notebook execution is required; and
7. explicit exclusions.

Until that response exists and is recorded, Stage 1 remains blocking, curator ownership remains empty, no notebook path is writable, and no migration may begin. A revision request remains at this checkpoint; rejection or deferral stops the task without a successor.

## Ownership

- **Parent coordinator:** owns `.pi/active-state.json`, task coordination, scope recording, correction routing, parent verification, repository safety, and human handoff.
- **Notebook curator (`physkit-notebook-curator`):** sole notebook writer; owns only exact notebook and notebook-local reference paths explicitly authorized by the human and recorded after `HC01`. Current ownership: **empty**.
- **Notebook verifier (`physkit-notebook-verifier`):** read-only deterministic verification.
- **Integration reviewer (`physkit-integration-reviewer`):** independently read-only integration review.
- **Human:** owns curriculum, exact mapping and filenames, duplicate and repair dispositions, physical and pedagogical decisions, evidence applicability and acceptance, final acceptance, and any successor decision.

No role may expand the human-approved path set. One owner applies to each write path.

## Ordered workflow

Follow `.pi/chains/notebook-organization.chain.json` in order: human scope checkpoint; curator preparation; deterministic verification; integration review; curator correction if findings require it; verification replay; integration re-review; parent verification; human final acceptance; and closeout. Correction returns to the curator. Review roles remain read-only. Parent verification is not human acceptance.

## Required evidence

For a path-only migration, require at least:

- pre- and post-move notebook JSON parsing;
- pre- and post-move SHA-256 byte identity;
- repository search for old-path references;
- staged-path isolation;
- pure-rename confirmation;
- independent read-only integration review; and
- parent verification.

Additional evidence depends on the accepted batch. Notebook execution, numerical verification, physical validation, and pedagogical validation are separate evidence classes and are required only through an explicit human decision; one does not substitute for another.

## Prohibited paths and decisions

Before `HC01` resolves affirmatively, every notebook path is prohibited. Throughout the task, source, tests, examples, dependencies, packaging, CI, harness policy documents, PIAB work, curriculum views, schemas, validators, runtime code, and any path outside the exact accepted batch remain prohibited unless a later explicit human decision revises this task. No agent may choose mappings, filename changes, duplicates, repairs, lifecycle states, canonical status, or validation conclusions.

## Review and correction

The verifier reports deterministic findings without repair. The independent integration reviewer reports findings without repair. Material findings return through the parent to the curator, who may correct only within the accepted scope. Every affected deterministic check is replayed and the corrected result is independently rereviewed. Unresolved material findings block parent verification.

## Stop behavior

Stop:

- at `NOTEBOOK-ORG-1-HC01`;
- on unclear scope or ownership;
- on unexpected dirty paths;
- when a destination path collides;
- when tracked references would break;
- when content changes unexpectedly;
- when required evidence or review is missing or fails;
- at human final acceptance, rejection, or deferral; and
- after closeout, with no automatic successor.

Successor authorization is false and successor is `null`. Silence, passing checks, review, commit, push, or closeout does not authorize another batch or task.
