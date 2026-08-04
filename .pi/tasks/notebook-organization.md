# NOTEBOOK-ORG-1 — Bounded notebook organization

**Status:** Awaiting human final acceptance
**Task ID:** `NOTEBOOK-ORG-1`
**Chain ID:** `NOTEBOOK-ORG-1`
**Current checkpoint:** `human_final_acceptance` (`pending`; existing chain Stage 9)

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

Current status is **Awaiting human final acceptance**. The human accepted exactly four path-only viscoelasticity mappings at `NOTEBOOK-ORG-1-HC01`, and those four byte-preserving moves have completed verification, independent review, and parent verification. The eight source/destination identities below are the completed bounded scope; no notebook path is currently writable. Notebook content changes, reference updates, notebook execution, closeout, and every other notebook path remain prohibited.

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

### Recorded HC01 human response

**Disposition:** Accepted bounded scope on 2026-08-04. This accepts only the following four mappings incorporated from `.07` at revision `68b7d92678f9ee7ba5eef5f452d3bbb494ff2eed`:

1. `notebooks/viscoelasticity/01-compliance-functions.ipynb` → `notebooks/materials-physics/viscoelasticity/compliance-functions.ipynb`
2. `notebooks/viscoelasticity/02-stress-relaxation.ipynb` → `notebooks/materials-physics/viscoelasticity/stress-relaxation.ipynb`
3. `notebooks/viscoelasticity/03-laplace-transform-and-oscillations.ipynb` → `notebooks/materials-physics/viscoelasticity/laplace-transform-and-oscillations.ipynb`
4. `notebooks/viscoelasticity/04-time-temperature-superposition.ipynb` → `notebooks/materials-physics/viscoelasticity/time-temperature-superposition.ipynb`

Accepted operations and limits:

- the filename changes shown above are accepted, with no additional normalization;
- notebook contents must remain byte-for-byte identical;
- notebook execution and reference updates are prohibited;
- all four sources must parse as JSON and all four destinations must parse after moving;
- pre/post SHA-256 hashes must match;
- tracked old-path references, destination collisions, content changes, or ownership ambiguity stop execution;
- verification requires pure-renames, staged-path isolation, `git diff --check`, read-only notebook verification, independent read-only integration review, and parent verification;
- every path and decision outside this exact set remains excluded;
- this authorization reaches the final-human-acceptance checkpoint only and does not authorize closeout or a successor.

## Ownership

- **Parent coordinator:** owns `.pi/active-state.json`, task coordination, scope recording, correction routing, parent verification, repository safety, and human handoff.
- **Notebook curator (`physkit-notebook-curator`):** sole notebook writer. Current ownership is exactly these eight path identities and only for the four accepted byte-preserving moves:
  - `notebooks/viscoelasticity/01-compliance-functions.ipynb`
  - `notebooks/materials-physics/viscoelasticity/compliance-functions.ipynb`
  - `notebooks/viscoelasticity/02-stress-relaxation.ipynb`
  - `notebooks/materials-physics/viscoelasticity/stress-relaxation.ipynb`
  - `notebooks/viscoelasticity/03-laplace-transform-and-oscillations.ipynb`
  - `notebooks/materials-physics/viscoelasticity/laplace-transform-and-oscillations.ipynb`
  - `notebooks/viscoelasticity/04-time-temperature-superposition.ipynb`
  - `notebooks/materials-physics/viscoelasticity/time-temperature-superposition.ipynb`
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

## Execution record — accepted four-notebook batch

### Curator handoff

The curator completed the four accepted `git mv` operations without notebook content edits, execution, or reference updates. All sources existed and were tracked; all destinations were absent; all sources and destinations parsed as JSON. The curator did not modify `.pi/` and did not commit independently.

A first preflight attempt stopped safely before moving because the subagent harness created an unexpected untracked `.pi-subagents/` artifact and the command used unavailable `python`. The parent removed only that harness-generated artifact, retained `package-lock.json` untouched, classified the exact tracked old-path occurrences, and replayed Stage 2 with project artifacts disabled and `python3`. This was a preflight replay, not a notebook correction cycle.

Exact old-path searches found only accepted scope/ownership provenance in `.pi/active-state.json` and this task, historical inventory identities in `.05`, and advisory mapping/history prose in `.07`. None is a Markdown link, import, include, or operational path reference; no tracked reference would break.

### SHA-256 identity and JSON results

| Source → destination | Pre/post SHA-256 | Source JSON | Destination JSON |
|---|---|---:|---:|
| `notebooks/viscoelasticity/01-compliance-functions.ipynb` → `notebooks/materials-physics/viscoelasticity/compliance-functions.ipynb` | `c23d7c945bccdb96a7eed70c0e0632b6bb69e8593f8e1eb9aeff4e2f0bf42c9d` | PASS | PASS |
| `notebooks/viscoelasticity/02-stress-relaxation.ipynb` → `notebooks/materials-physics/viscoelasticity/stress-relaxation.ipynb` | `89c218784fec4475202e9fa9476848232c625db2e1c2b6b43eba7c645c463bab` | PASS | PASS |
| `notebooks/viscoelasticity/03-laplace-transform-and-oscillations.ipynb` → `notebooks/materials-physics/viscoelasticity/laplace-transform-and-oscillations.ipynb` | `86d3016a67fe92e461ce58d2c0eae84a7ec36df2e9a522b0e152b536444fda56` | PASS | PASS |
| `notebooks/viscoelasticity/04-time-temperature-superposition.ipynb` → `notebooks/materials-physics/viscoelasticity/time-temperature-superposition.ipynb` | `f10226ebf34461ea45a36d73d81347788c94acd328b2e27989c4ebe9b2db50ae` | PASS | PASS |

### Deterministic verification

The read-only notebook verifier returned **PASS**. It confirmed four exact `R100` renames, identical Git object IDs, zero notebook insertions or deletions, exact staged-path isolation, absent worktree sources, present destinations, valid pre/post JSON, matching hashes, no unauthorized notebook path, no operational old-path reference, `git diff --check --cached` success, and untouched/untracked `package-lock.json`. Notebook execution was prohibited and not performed.

### Integration review

The independent read-only integration reviewer returned **PASS** with no blocker, high, or medium findings. It independently confirmed the four accepted `R100` mappings, byte and Git-object identity, valid JSON, matching hashes, zero content change, path isolation, nonbreaking provenance/history references, preserved exclusions, PIAB parking, and successor denial.

The reviewer recorded two low residual declarative limitations: the unchanged chain and curator-agent files retain initialization-era status/scope prose. Active state remains the sole current-state authority, the task supplies the exact accepted ownership, and the chain's ordered stages remain executable. The human explicitly prohibited agent or chain changes for this batch, so no harness redesign or correction is required.

### Correction cycles

No notebook or coordination correction was required after deterministic verification or integration review. Conditional Stages 5–7 were skipped. The earlier safe curator preflight replay occurred before any move and is not a content correction cycle.

### Parent verification and commit readiness

The parent coordinator independently replayed the mapping, baseline/worktree JSON parsing, byte comparisons, SHA-256 checks, source/destination existence, baseline destination absence, staged `R100` pairs, zero insertion/deletion checks, excluded-path checks, `git diff --check --cached`, agent/chain nonmutation, PIAB parking, and successor denial. **Parent verification: PASS.**

The batch is ready to commit and push after final staged-scope validation and immediate remote re-fetch. Commit and push do not imply human acceptance. Final human acceptance remains pending at the existing chain Stage 9 identifier `human_final_acceptance`; no `NOTEBOOK-ORG-1-HC02` identifier existed consistently in the unchanged task and chain, so none was invented. Closeout and successor work remain unauthorized.

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
