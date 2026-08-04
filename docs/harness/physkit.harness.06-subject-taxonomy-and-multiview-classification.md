# PhysKit Subject Taxonomy and Multiview Classification

**Status:** Proposed for human review

## 1. Purpose, authority, and decision boundary

This Mode A proposal defines a conceptual relationship model for organizing PhysKit notebooks while preserving the distinction:

```text
one canonical physical notebook file
many subject memberships
many curriculum views
```

It uses the accepted repository-inspection snapshot at `docs/harness/physkit.harness.05-notebook-curriculum-inventory-and-options.md`, accepted at revision `283c72e988f8bbcbd8b8792cdba25436ce325e2f`. Subject-oriented organization is the human-directed provisional basis for canonical physical storage. That direction does not select a final hierarchy, exclusive subject identity, course sequence, exact path, curriculum ordering, or cross-listing implementation.

The physical path is an administrative repository choice. It is not an epistemic claim of exclusive intellectual ownership. A notebook may simultaneously belong to several subjects, depend on several prerequisites, apply methods in several domains, serve several pedagogical purposes, and appear in several ordered teaching views.

This proposal does not:

- designate any existing notebook as canonical;
- require an exclusive `primary_subject`;
- choose a storage home or exact destination for any notebook;
- finalize folder names, folder depth, or nesting;
- prescribe a course, lecture, prerequisite, or curriculum sequence;
- create a manifest, schema, metadata convention, index, validator, or generator;
- assign lifecycle states or accept pedagogical or scientific claims;
- resolve duplicates, invalid JSON, saved errors, or uncertain classifications;
- move, rename, copy, delete, repair, execute, or rewrite a notebook; or
- resume PIAB contract, API, notebook, evidence, tolerance, lifecycle, or implementation work.

## 2. Sources and method

The proposal is grounded primarily in the complete 127-notebook static inventory in `.05`, including its subject families, model classifications, duplication analysis, curriculum gaps, hierarchy options, and boundary questions. It also preserves the authority boundaries in:

- `AGENTS.md`;
- `docs/harness/physkit.harness.01-capability-baseline.md`;
- `docs/harness/physkit.harness.02-capability-lifecycle.md`;
- `docs/harness/physkit.harness.03-pilot-capability-selection.md`; and
- `docs/harness/physkit.harness.04-minimal-pi-control-plane.md`.

No notebook was executed. The complete inventory was not repeated. No modified working-tree notebook content was inspected. Technical condition, artifact identity, intellectual classification, pedagogical role, and lifecycle state remain separate dimensions.

## 3. Core conceptual objects

### 3.1 Canonical notebook artifact

A canonical notebook artifact is one human-designated authoritative notebook file for a stated role. It has one physical repository path so that edits occur in one place, links resolve to one artifact, duplicate divergence is avoided, verification targets one file, and Git history remains coherent.

Canonical status is a protected human decision and is role-scoped under `.02`. This proposal establishes only the relationship concept; it does not make any notebook canonical.

### 3.2 Administrative storage home

The administrative storage home is the directory containing the canonical notebook. It is selected for repository management, stable links, and discoverability. It does not assert that the notebook belongs exclusively to the directory's named subject.

If a later record needs to identify this choice, a neutral name such as `storage_home` is appropriate. Terms such as `true_subject`, `owner_subject`, or an exclusive `primary_subject` would incorrectly turn a repository-management decision into an intellectual-ownership claim.

### 3.3 Subject membership

Subject membership is a many-to-many relationship between notebooks and intellectual subject areas. A notebook can have several simultaneous memberships without contradiction. For example, an Ising notebook may belong to magnetism, solid-state physics, and statistical mechanics; a carrier notebook may belong to semiconductor physics, statistical mechanics, electromagnetism, carrier transport, and computational physics.

Subject membership is not inferred exclusively from the physical path, filename, current folder, course of origin, or one pedagogical use.

### 3.4 Pedagogical emphasis

Pedagogical emphasis states what a particular notebook is intended to help a learner understand or practice. Two notebooks using the same physical model may emphasize different learning objectives. One Ising notebook might emphasize magnetic order and susceptibility; another might emphasize ensembles, Monte Carlo sampling, fluctuations, and critical behavior.

Pedagogical emphasis may later help select an administrative storage home. It cannot erase other subject memberships, establish pedagogical acceptance, or prescribe curriculum order.

### 3.5 Prerequisite relationship

A prerequisite is a directed conceptual relationship indicating knowledge normally needed to use a notebook effectively. It may point to a concept, method, or subject. It does not require physical directory nesting.

For example:

```text
quantum mechanics
→ solid-state physics
→ semiconductor physics
```

may express conceptual dependence while the relevant notebooks remain in sibling directories. Prerequisite edges are contextual: an introductory qualitative treatment and an advanced derivation may need different prerequisites even when they concern the same model.

### 3.6 Application relationship

An application relationship states that a model, formalism, or computational method is used in another subject or problem area. Statistical mechanics may be applied to magnetism; Poisson's equation may be applied to semiconductor electrostatics; Fourier methods may be applied to waves, quantum mechanics, or electronic structure. Application does not convert every destination notebook into an exclusive member of the method's home subject.

### 3.7 Curriculum view

A curriculum view is an ordered collection of references to canonical notebooks for a particular teaching purpose. A view may represent a course, lecture series, prerequisite pathway, topic review, laboratory sequence, or instructor-selected progression.

Views reference but do not own or duplicate notebook files. The same canonical notebook may appear at different positions in multiple views. No curriculum view or ordering is selected here.

### 3.8 Artifact condition, identity, and lifecycle

These independent classifications must not be collapsed:

- invalid JSON or saved errors are file-condition findings;
- exact or probable duplication is an artifact-identity finding;
- subject membership is an intellectual classification;
- pedagogical emphasis is an intended-use classification; and
- Exploratory, Candidate, Supported, Deprecated, or Historical is a human-controlled capability lifecycle decision under `.02`.

A damaged file can still have several subjects. An exact duplicate does not identify a survivor. A folder does not assign lifecycle state.

## 4. Minimal relationship structure

A later representation could conceptually resemble:

```yaml
notebook:
  canonical_path: path/to/notebook.ipynb
  storage_home: subject-oriented-administrative-home

  subjects:
    - subject-a
    - subject-b

  pedagogical_emphases:
    - emphasis-a

  prerequisites:
    - concept-or-subject-a

  applications:
    - application-area-a

  curriculum_views:
    - view-a
    - view-b
```

This is illustrative only. It is not a schema, accepted field set, metadata contract, manifest, or validator.

### 4.1 Fields likely necessary for later planning

- **Canonical identity/path:** necessary once humans select one authoritative physical artifact, because every view and relationship needs an unambiguous target.
- **Nonexclusive subjects:** necessary to prevent the storage path from becoming the sole classification.
- **Pedagogical emphasis:** useful for distinguishing notebooks that share a model and for applying a storage selection strategy.
- **Curriculum-view references:** necessary only if views are stored in the same relationship source; external curriculum maps may instead own their own ordered references.

### 4.2 Fields whose exact representation should be deferred

- **`storage_home`:** conceptually necessary for folder planning, but redundant with `canonical_path` after physical placement; whether to store it separately should be deferred.
- **Prerequisites:** valuable, but edge granularity, context, strength, and versioning need human decisions before structured storage.
- **Applications:** valuable for discovery, but the distinction among subject, application, method, and example needs usage evidence.
- **Pedagogical emphases:** vocabulary and acceptance process remain unresolved.
- **Curriculum views inside notebook records:** potentially derived from external view definitions and therefore a drift risk.
- **Level, textbook anchor, artifact condition, duplication, and lifecycle:** distinct dimensions that should not be forced into this minimal subject-relationship structure without separate authority decisions.

No exclusive `primary_subject` is necessary or recommended. A later administrative choice may select a `storage_home` without changing the notebook's complete subject set.

## 5. Proposed controlled, nonexclusive subject vocabulary

The vocabulary below is grounded in `.05` but remains proposed. “Folder suitability” evaluates administrative usefulness, not intellectual legitimacy. Specialized terms can remain valuable metadata or curriculum tags even when they should not become physical directories.

| Subject term | Intended meaning and scope | Neighboring or overlapping subjects | Breadth | Physical-folder suitability | Better only as metadata/curriculum tag? |
|---|---|---|---|---|---|
| Computational and mathematical foundations | Units, constants, linear algebra, calculus, transforms, grids, quadrature, and general mathematical/computational prerequisites | every physics domain; advanced computational physics | broad | High as a stable broad home, possibly named `foundations` | No; specific methods beneath it may be tags |
| Mechanics | Kinematics, dynamics, oscillations, variational mechanics, and classical particle systems | waves, continuum mechanics, mathematical foundations | broad | High | No |
| Electromagnetism | Charges, fields, potentials, circuits, magnetostatics, induction, and Maxwell theory | optics, magnetism, semiconductor physics, carrier transport | broad | High | No |
| Waves | General wave motion, superposition, plane waves, dispersion, and spectral representations | optics, mechanics, electromagnetism, quantum mechanics | broad/intermediate | Medium; often combined with optics administratively | Sometimes, if a combined folder is preferred |
| Optics | Geometrical and physical optics, interference, diffraction, and optical applications | waves, electromagnetism, materials physics | broad/intermediate | Medium; current inventory is sparse | Possibly until coverage justifies a folder |
| Modern physics | Introductory transition topics such as relativity, blackbody radiation, de Broglie relations, and elementary quantum models | quantum mechanics, statistical mechanics, atomic physics | broad pedagogical bridge | Medium; useful only if humans want level-oriented storage | Often better as a curriculum tag/view because it is level-dependent |
| Classical thermodynamics | Macroscopic state variables, equations of state, heat, work, entropy, potentials, equilibrium, mixtures, and phase behavior | statistical mechanics, materials physics, materials science | broad | High | No |
| Statistical mechanics | Ensembles, distributions, partition functions, fluctuations, kinetic theory, phase transitions, and microscopic foundations of thermal behavior | thermodynamics, magnetism, semiconductor physics | broad | High | No |
| Quantum mechanics | State spaces, operators, wavefunctions, measurement, spectra, dynamics, and approximation methods | modern physics, atomic physics, solid state, electronic structure | broad | High | No |
| Atomic and molecular physics | Atomic, molecular, and spectroscopic models and observables | quantum mechanics, optics, materials characterization | broad/intermediate | Low to medium given current inventory | Yes until the corpus supports a stable home |
| Nuclear and particle physics | Nuclear structure, reactions, elementary particles, and related methods | modern physics, quantum mechanics | broad/intermediate | Low given little evident coverage | Yes until substantive coverage exists |
| Condensed-matter physics | Umbrella for collective phases and properties of solids, liquids, and complex matter | solid state, magnetism, materials physics, statistical mechanics | very broad | Medium; risks duplicating narrower stable homes | Often best as an umbrella metadata or curriculum view |
| Crystal physics | Symmetry, unit cells, direct/reciprocal lattices, and crystal-specific physical behavior | solid state, lattice dynamics, electronic structure | specialized | Low to medium | Usually metadata or a subview unless enough notebooks justify a folder |
| Lattice dynamics | Vibrations, normal modes, phonons, and thermal consequences of periodic structures | crystal physics, solid state, statistical mechanics | specialized | Low with present coverage | Yes |
| Electronic structure | Electronic states, bands, density of states, tight binding, Bloch and related methods | quantum mechanics, solid state, semiconductor physics | specialized | Medium if a large coherent corpus emerges | Prefer metadata/subview initially |
| Magnetism | Magnetic moments, order, susceptibility, domains, spin models, and magnetic phase behavior | electromagnetism, statistical mechanics, solid state, quantum mechanics | specialized but substantial | Medium; plausible future folder, not required now | Could remain a strong subject tag and view |
| Solid-state physics | Structure and properties of periodic solids, bands, phonons, electrons, and idealized solid models | condensed matter, crystal physics, magnetism, semiconductor physics | broad | High | No |
| Semiconductor physics | Band, carrier, junction, generation, recombination, and device-adjacent physics of semiconductors | solid state, statistical mechanics, electromagnetism, transport | specialized but substantial | High given the observed corpus | No |
| Carrier transport | Mobility, scattering, conductivity, resistivity, drift, diffusion, and transport equations | semiconductor physics, electromagnetism, statistical mechanics | specialized | Low as a top-level folder | Yes, or a later subfolder after exact mapping |
| Materials physics | Physics-centered treatment of structure, properties, phase fields, constitutive response, and microscopic/macroscopic links | condensed matter, continuum mechanics, thermodynamics, materials science | broad synthesis | High | No |
| Materials-science applications | Engineering- and application-oriented property, processing, characterization, thin-film, fracture, and data examples | materials physics, thermodynamics, continuum mechanics | broad application area | Medium to high if kept distinct from physics synthesis | No, though individual techniques remain tags |
| Continuum mechanics | Stress, strain, elasticity, viscoelasticity, constitutive models, and continuum fields | mechanics, materials physics, applied mathematics | broad/specialized boundary | Medium | May be metadata/subview initially; folder suitability depends on corpus growth |
| Advanced computational physics | General or advanced numerical methods, finite differences/elements, Monte Carlo, eigensolvers, sparse methods, fitting, and simulation patterns | foundations and every application domain | broad method layer | High as a stable administrative home for method-centered notebooks | Domain applications should also carry subject tags |

### 5.1 Additional useful tags not yet proposed as top-level folders

`.05` and the boundary examples also motivate `computational physics`, `mathematical physics`, `applied mathematics`, `rheology`, `spectroscopy`, `thin-film processing`, and `device physics`. These are useful discovery or curriculum terms, but the present evidence does not justify requiring them as top-level physical homes. `Computational physics` may be a cross-cutting membership on many notebooks while `advanced computational physics` remains a possible storage home only for notebooks whose dominant emphasis is the method itself.

### 5.2 Vocabulary design guidance

A controlled vocabulary should be nonexclusive, stable enough for links, and small enough for consistent human review. Broad terms are better physical-folder candidates. Specialized terms are often better relationships or view labels. Synonyms and renamed terms would need an accepted governance process; this proposal does not create one.

## 6. Textbook anchors

The following references remain approximate depth and scope anchors only:

| Area | Approximate anchor |
|---|---|
| Introductory undergraduate physics | Young and Freedman |
| Quantum mechanics | Shankar |
| Statistical mechanics | Schroeder |
| Classical thermodynamics | Physics-major macroscopic thermodynamics at approximately compatible depth |
| Solid-state physics | Kittel |
| Semiconductor physics | Sze and Lee |
| Materials-science applications | Callister |
| Materials physics | Physics-centered synthesis without a single prescribed text |

They do not determine mandatory topic order, folder nesting, chapter correspondence, course packaging, exclusive subject membership, or exact placement. No course sequence is prescribed by this proposal.

## 7. Cross-disciplinary examples

### 7.1 Ising model

The Ising Hamiltonian

$$
H=-J\sum_{\langle i,j\rangle}s_i s_j-h\sum_i s_i,
\qquad s_i\in\{-1,+1\},
$$

models interacting localized magnetic moments. Magnetism-centered observables and emphases include magnetization, susceptibility, magnetic order, domains, and ferro–paramagnetic transitions.

It is simultaneously a canonical interacting statistical system through

$$
P(\{s_i\})=\frac{e^{-\beta H}}{Z},
\qquad Z=\sum_{\{s_i\}}e^{-\beta H},
$$

supporting ensembles, Monte Carlo sampling, phase transitions, critical behavior, universality, and fluctuations.

A notebook may therefore have simultaneous memberships such as:

```yaml
subjects:
  - magnetism
  - solid-state-physics
  - statistical-mechanics
```

A magnetization-and-susceptibility lesson and an ensemble-and-Monte-Carlo lesson may use the same model but have different pedagogical emphases. A later storage home may consider that emphasis, but this document does not choose it. The example explicitly recognizes both magnetism and statistical mechanics.

### 7.2 Bloch states

A Bloch-state notebook may simultaneously belong to quantum mechanics, solid-state physics, crystal physics, electronic structure, and semiconductor physics. Quantum mechanics supplies the state/operator and symmetry formalism; periodic solids supply the application, reciprocal-space interpretation, bands, and material context. Neither the general formalism nor the periodic-solid application erases the other membership.

### 7.3 Semiconductor carrier models

A semiconductor carrier notebook may belong to semiconductor physics, solid-state physics, statistical mechanics, electromagnetism, carrier transport, and computational physics. Fermi–Dirac statistics may supply occupations, Poisson's equation may supply electrostatics, and drift–diffusion or scattering models may supply transport. Prerequisite and application edges represent these dependencies better than deeply nested directories.

### 7.4 Phase diagrams

A phase-diagram notebook may belong to classical thermodynamics, materials physics, materials-science applications, and—when a microscopic ensemble or lattice model is used—statistical mechanics. Actual equations, variables, data, and pedagogical purpose must guide classification. The phrase “phase diagram” alone is insufficient.

### 7.5 Viscoelasticity

A viscoelasticity notebook may belong to continuum mechanics, materials physics, rheology, applied mathematics, and computational physics. Its central organizing object may be a constitutive operator, relaxation spectrum, transform, or empirical shift relation even when the application concerns materials. Technical or application context should not conceal the continuum and mathematical memberships.

### 7.6 Particle in a box

A particle-in-a-box notebook may belong to modern physics, quantum mechanics, mathematical physics, and computational physics. Approximate level and pedagogical treatment determine which curriculum views reference it. This classification example does not select a canonical PIAB artifact or location. PIAB remains parked.

## 8. Strategies for one administrative storage home

### Strategy A — Pedagogical-emphasis home

Store the notebook under the broad subject corresponding to its dominant learning objective.

| Criterion | Assessment |
|---|---|
| Clarity | Strong when the objective is explicit and stable |
| Stability | Moderate; revisions can change emphasis |
| Ambiguity | High for notebooks with several equal objectives or audiences |
| Migration cost | Medium; requires notebook-level pedagogical review |
| Interdisciplinary behavior | Honest if all other subjects remain recorded |
| Catch-all risk | Moderate if “foundations” or “advanced” absorbs ambiguous cases |
| Future curriculum views | Strong; emphasis aligns with instructional use but does not replace multiple views |

### Strategy B — Model-origin home

Store the notebook under the domain from which its governing physical model originates.

| Criterion | Assessment |
|---|---|
| Clarity | Strong when model provenance is unambiguous |
| Stability | Generally high because the model changes less often than course use |
| Ambiguity | Material for models such as Ising, Bloch bands, phase fields, and transport systems |
| Migration cost | Medium; requires model-level classification |
| Interdisciplinary behavior | Can understate applications unless memberships are prominent |
| Catch-all risk | Low to moderate; umbrella domains such as condensed matter may become overfull |
| Future curriculum views | Good; views can reference the model from several teaching contexts |

### Strategy C — Stable broad-domain home

Store interdisciplinary notebooks under a broad, durable domain and use subject relationships and curriculum views for specificity.

| Criterion | Assessment |
|---|---|
| Clarity | High at broad scale, lower for local browsing |
| Stability | High |
| Ambiguity | Reduced but not eliminated when several broad domains overlap |
| Migration cost | Lower than fine-grained strategies |
| Interdisciplinary behavior | Strong if relationship records are visible and maintained |
| Catch-all risk | High if broad domains become undifferentiated miscellaneous collections |
| Future curriculum views | Strong; views carry the specificity omitted from storage |

### Advisory recommendation

Use Strategy C as the default planning posture, with Strategy A as a tie-breaker when a broad-domain choice remains ambiguous and the pedagogical emphasis is explicit. Strategy B is useful evidence but should not be a universal rule because model origins are contested for important interdisciplinary cases. This recommendation is advisory only; the administrative storage strategy remains pending human decision.

Regardless of strategy, a later selection must be described as an administrative home, never as exclusive subject ownership.

## 9. Non-sequential physical hierarchy options

No option below uses numeric prefixes or implies teaching order. Folder names and nesting remain provisional.

### Option 1 — Broad subject homes

```text
notebooks/
├── foundations/
├── mechanics/
├── electromagnetism/
├── waves-optics/
├── modern-physics/
├── classical-thermodynamics/
├── statistical-mechanics/
├── quantum-mechanics/
├── solid-state-physics/
├── semiconductor-physics/
├── materials-physics/
├── materials-science/
├── advanced-computational-physics/
└── staging/
```

**Assessment:** Familiar and shallow, compatible with stable broad-domain homes, and close to observed `.05` clusters. `modern-physics` risks mixing level and subject. `staging` risks becoming a miscellaneous or lifecycle surrogate and would require explicit admission/exit rules. Magnetism, electronic structure, carrier transport, and computational methods could remain relationships or indexes rather than top-level folders.

### Option 2 — Broad homes with selective specialized siblings

```text
notebooks/
├── foundations/
├── mechanics/
├── electromagnetism/
├── waves-and-optics/
├── thermodynamics/
├── statistical-mechanics/
├── quantum-mechanics/
├── solid-state-physics/
├── magnetism/
├── semiconductor-physics/
├── materials-physics/
├── materials-science-applications/
└── computational-physics/
```

**Assessment:** Gives magnetism independent visibility and removes a level-based modern-physics home, but increases ambiguous homes for Ising, Bloch, and transport notebooks. It is viable only if nonexclusive subject records are prominent. Continuum mechanics, crystal physics, lattice dynamics, electronic structure, and carrier transport would initially remain tags or views.

### Option 3 — Minimal umbrella homes

```text
notebooks/
├── foundations/
├── classical-physics/
├── thermal-and-statistical-physics/
├── quantum-physics/
├── condensed-matter-and-materials/
├── computational-physics/
└── unresolved/
```

**Assessment:** Stable and low-cost but too coarse for repository browsing and likely to create oversized umbrella and unresolved directories. It relies heavily on a relationship mechanism and generated or hand-maintained indexes. `unresolved` must not become a permanent miscellaneous folder or imply lifecycle status.

### Apparent folders that may be better as relationships

- **Magnetism:** strong subject identity but highly cross-cutting; plausible folder only if corpus and navigation justify it.
- **Electronic structure:** often a specialized intersection of quantum mechanics, solid state, and semiconductors; initially better as a subject tag and curriculum view.
- **Continuum mechanics:** broad enough to become a folder, but current material may be served by materials-physics storage plus a continuum view.
- **Carrier transport:** specialized and application-linked; better as a tag or subview until exact mapping shows a stable corpus.
- **Computational methods:** general methods may warrant a physical home, while domain-specific method use should be represented as cross-cutting membership rather than moved out of its physics context automatically.

No option is selected, and no exact notebook destination is assigned.

## 10. Curriculum-view and cross-reference mechanisms

### 10.1 Comparison

| Mechanism | Human readability/editability | Git diff and notebook churn | Tool compatibility | Multiple subjects/views | Validation and authority/drift risks |
|---|---|---|---|---|---|
| External Markdown curriculum maps | Excellent readability; easy manual editing | Good textual diffs; no notebook churn | Excellent on GitHub and Obsidian; good with Jupyter/Quarto links | Multiple views are natural; subject membership can be narrated but is weakly structured | Low tooling need; manual links and repeated classifications can drift; each map must clearly be a view, not notebook-content or lifecycle authority |
| External structured manifest (YAML/JSON) | Moderate; YAML friendlier than JSON for review | Good diffs if formatting/order is controlled; no notebook churn | GitHub renders text; Jupyter, Quarto, and Obsidian need consumers or conventions | Strong many-to-many subjects, prerequisites, applications, and views | Requires field definitions and validation; can become a competing authority if content, lifecycle, and support claims are mixed into it |
| Notebook metadata | Poor to moderate for ordinary review; editing often tool-mediated | JSON diffs are noisy and every classification edit churns notebooks | Native to Jupyter; other tools can read it but conventions differ | Can store many subjects, but ordered cross-notebook views are awkward | High notebook churn, easy copy drift, and classification changes become entangled with canonical content and verification hashes |
| Generated indexes from human-maintained source data | Derived indexes can be highly readable | Source diffs can be good; generated diffs add noise unless disciplined | Can target GitHub, Jupyter, Quarto, and Obsidian | Strong for many subjects and many course views | Requires generator, validation, provenance, reproducibility, and a clear rule that source data—not generated output—is authoritative |

### 10.2 Advisory recommendation

For the next planning stage, prefer external Markdown curriculum maps for initial human-readable ordered views, paired eventually with one external structured relationship source only if the 127-notebook exact mapping demonstrates that manual cross-listing would drift. Do not place the initial authority in notebook metadata. Generated indexes should be considered only after humans accept the structured source and validation boundary.

This is a recommendation, not an implementation choice. No map, manifest, metadata field, generator, or index is authorized here.

## 11. Later authority division

To prevent contradictory authorities, a later accepted design should assign each fact to one owner:

| Information | Proposed later authority |
|---|---|
| Notebook mathematics, code, narrative, and saved notebook state | The canonical notebook file, within accepted capability/artifact decisions |
| Canonical physical identity and current path | A human-accepted artifact identity/relationship record, with the repository path as its target |
| Subject memberships and pedagogical emphases | One accepted relationship source, not inferred solely from directories or copied into every view |
| Prerequisite and application relationships | The accepted relationship source or a separately accepted conceptual graph, with edge scope explicit |
| Ordered curriculum views | Human-maintained view definitions referencing canonical notebook identities |
| Generated subject/course indexes | Derived output from the accepted relationship and view sources; never independently authoritative |
| Lifecycle state, canonical role, support, and validation claims | Human-approved lifecycle/capability records under `.02`, never the taxonomy, folder, view, or generated index |

A canonical notebook cannot silently accept its own subject classification merely by residing in a folder. Conversely, a relationship source must not overwrite notebook content. A curriculum view owns order only for that view. A generated index must identify its source and must not become authority for notebook contents, physical correctness, pedagogical acceptance, lifecycle state, canonical status, or support claims.

## 12. Exceptional artifacts

| Condition | Later options for human review | Prohibited inference now |
|---|---|---|
| Exploratory notebooks | Keep in a bounded staging area, retain in a subject home with an explicit non-lifecycle role marker, or preserve through a later accepted exploratory-artifact convention | Folder location does not assign Exploratory lifecycle state |
| Historical notebooks | Preserve in place, move only under a separately accepted historical plan, or link from a historical index | Age, errors, or disuse do not assign Historical state |
| Invalid JSON | Quarantine administratively, assess repair, preserve as historical evidence, or consider removal in a later decision | Invalidity does not determine subject, survivor, or lifecycle |
| Saved error outputs | Retain if pedagogically intentional, repair under a later task, clear only with accepted notebook-output policy, or preserve for diagnosis | Saved error does not prove the underlying model is wrong or the subject classification invalid |
| Exact duplicates | Compare provenance and roles, select one survivor, retain intentional variants with distinct roles, or preserve historical copies | Byte identity does not decide which path survives |
| Near-duplicates | Review conceptual and code differences, merge under later authorization, or retain distinct pedagogical emphases | Similarity does not establish identity or redundancy |
| Uncertain classification | Permit multiple provisional memberships, record uncertainty, request domain review, or defer storage-home selection | Uncertainty does not justify a miscellaneous exclusive category |

No move, repair, deletion, survivor selection, or lifecycle decision is made here.

## 13. Boundary-case register

The register uses `.05` groups and paths only as current identities. “Possible” means decision support, not accepted classification or destination.

| Case | Possible subject memberships | Possible pedagogical emphases | Possible storage strategies | Prerequisites | Application relationships | Unresolved human decisions |
|---|---|---|---|---|---|---|
| Ising and magnetism notebooks, including the committed identities under `notebooks/magnetism/` and `notebooks/math/mc/` | magnetism; statistical mechanics; solid-state physics; computational physics | magnetic order/susceptibility; ensembles; Monte Carlo; critical behavior | broad solid-state home; statistical-mechanics home by emphasis; stable broad-domain home | probability; thermal ensembles; spin/lattice model; Monte Carlo where used | statistical mechanics applied to magnetic order; computational methods applied to phase behavior | exact memberships, emphasis per notebook, canonical identity, storage home, view placement |
| Bloch-state and Bloch-band notebooks | quantum mechanics; solid-state physics; crystal physics; electronic structure; semiconductor physics; computational physics | symmetry formalism; periodic potentials; bands; density of states; spinful states | quantum home by formal emphasis; solid-state home by model application; stable broad-domain home | wave mechanics; linear algebra; periodicity; reciprocal space | quantum formalism applied to periodic solids and semiconductors | distinctions among variants, exact memberships, storage homes, duplicate/precursor relationships |
| Semiconductor-band and carrier notebooks | semiconductor physics; solid-state physics; statistical mechanics; electromagnetism; electronic structure; carrier transport; computational physics | band structure; occupation statistics; density; mobility; electrostatics; device-adjacent modeling | semiconductor home; solid-state home for foundations; broad-domain home plus views | quantum mechanics; bands; Fermi–Dirac statistics; electrostatics; transport equations as applicable | statistics and electromagnetism applied to carrier systems; transport applied to devices/materials | physics/device boundary, exact prerequisites, relationship mechanism, storage criteria |
| Phase-diagram and phase-separation material, including Cahn–Hilliard-adjacent work | classical thermodynamics; statistical mechanics; materials physics; materials-science applications; continuum mechanics; computational physics | macroscopic equilibrium; microscopic phase behavior; free-energy functional; materials processing | thermodynamics home; materials-physics home; broad-domain home by emphasis | thermodynamic potentials; phase equilibrium; statistical mechanics or continuum fields where used | thermal/statistical models applied to materials evolution | actual model classification, data/provenance role, storage home, curriculum use |
| Viscoelasticity series | continuum mechanics; materials physics; rheology; applied mathematics; computational physics | creep/recovery; relaxation; constitutive operators; transforms; time–temperature superposition | continuum-mechanics home; materials-physics home; stable broad-domain home | stress/strain; differential equations; transforms; constitutive modeling | mathematical operators applied to materials response | whether continuum mechanics becomes a folder, sequence/view definitions, empirical-model authority |
| PIAB notebooks | modern physics; quantum mechanics; mathematical physics; computational physics | introductory quantization; formal eigenproblem; symbolic derivation; numerical method; library comparison | modern-physics or quantum home by emphasis; stable quantum home plus several views | waves; differential equations; boundary conditions; linear algebra/numerics where applicable | mathematical/computational methods applied to an ideal quantum model | PIAB remains parked; canonical artifact, memberships, placement, duplicate disposition, exact mapping all unresolved |
| Exact duplicate groups from `.05` | inherit possible memberships only after content/provenance review; invalid duplicate pair remains uncertain | may be identical, historical, or intended role variants | no storage strategy until survivor/role decision | depends on content | depends on content | survivor selection, intentional-variant status, provenance, canonical identity, retention |
| Probable near-duplicates: PIAB 2D pair and cosine-Bloch pair | PIAB pair: quantum/computational; Bloch pair: quantum/solid state/electronic structure/semiconductor/computational | original versus extension; derivation versus density-of-states study; exploratory versus lesson | storage by distinct emphasis if retained; single home after later merge; broad-domain homes | content-dependent | numerical methods applied to quantum or band models | whether artifacts are distinct, merge/retention, canonical choice, exact classification |
| Invalid-JSON notebooks identified by `.05` | uncertain until recoverable evidence and provenance are reviewed; filenames are insufficient authority | unknown or historically intended | bounded unresolved/quarantine option only after human decision; no subject home inferred from condition | unknown | unknown | repair, preservation, removal review, identity of exact invalid duplicate, classification evidence |

The exact duplicate groups reported by `.05` are the Fourier-series pair, the PIAB library/comp pair, the invalid `qm_planck_blackbody`/`lesson_01_directlattice` pair, and the tight-binding pair. Their identity finding does not settle intellectual classification or retention. The probable near-duplicate groups are the two-dimensional PIAB pair and the cosine-Bloch pair. The invalid-JSON group remains a technical-condition set, not a subject.

## 14. Advisory synthesis

The evidence supports these advisory conclusions:

1. Treat the physical path as an administrative identifier only.
2. Require nonexclusive subject memberships in any later relationship design.
3. Prefer broad, stable physical homes over deeply nested epistemic claims.
4. Use pedagogical emphasis as a tie-breaker, not as a mechanism for deleting other memberships.
5. Keep curriculum views external to notebook ownership and capable of independent ordering.
6. Begin with human-readable Markdown views; add one structured relationship source only if exact mapping demonstrates a clear need.
7. Keep notebook condition, duplicate identity, subject classification, canonical role, and lifecycle authority separate.

All recommendations remain subject to human review.

## 15. Next planning boundary

Acceptance of this `.06` may authorize only a later, separately bounded Mode A document proposing:

1. the final subject vocabulary;
2. the chosen physical directory strategy;
3. the relationship-record mechanism;
4. exact mapping of the 127 notebooks;
5. duplicate and invalid-artifact dispositions; and
6. reversible migration batches.

Acceptance of `.06` does not itself authorize that successor, exact mapping, a manifest, folder creation, migration, notebook modification, duplicate disposition, invalid-artifact repair, or PIAB work. A separate explicit human authorization is required.

## 16. Human-decision table

| Decision | Status |
|---|---|
| One canonical physical notebook file for an eventually selected canonical artifact | **Already human-directed** |
| Several simultaneous subject memberships per notebook | **Already human-directed** |
| Several curriculum views may reference one canonical notebook | **Already human-directed** |
| Physical path does not imply exclusive intellectual subject identity | **Already human-directed** |
| Curriculum ordering remains separate from physical storage | **Already human-directed** |
| No course sequence is selected at this stage | **Already human-directed** |
| Textbook references are approximate level and scope anchors only | **Already human-directed** |
| Subject-oriented organization as the provisional basis for canonical physical storage | **Already human-directed** |
| Final controlled subject vocabulary | Pending human decision |
| Which terms remain broad and which remain specialized | Pending human decision |
| Whether any subject terms become physical folders | Pending human decision |
| Administrative storage strategy | Pending human decision |
| Directory-depth and nesting strategy | Pending human decision |
| Final folder names and hierarchy | Pending human decision |
| Relationship-record mechanism | Pending human decision |
| Curriculum-view mechanism | Pending human decision |
| Authority for subject, prerequisite, application, and pedagogical-emphasis records | Pending human decision |
| Treatment of interdisciplinary notebooks when several homes are plausible | Pending human decision |
| Treatment of exploratory and historical artifacts | Pending human decision |
| Exact- and near-duplicate handling | Pending human decision |
| Invalid-notebook and saved-error handling | Pending human decision |
| Whether exact mapping of all 127 notebooks is authorized as the next task | Pending human decision |

Human review options are **accept**, **revise**, **reject**, or **defer**. Acceptance does not authorize a successor. This Mode A task stops for explicit human acceptance.