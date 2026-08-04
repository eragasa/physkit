# PhysKit Pilot Capability Selection

## 1. Document status and proposed authority

**Status:** Proposed for human review

**Proposed path:**
`docs/harness/physkit.harness.03-pilot-capability-selection.md`

This document is decision support. It compares bounded pilot candidates and
makes one advisory recommendation. It does not select a pilot.

Committing or publishing this proposal does not constitute acceptance. Only a
human may select a pilot and accept, revise, or reject its preliminary boundary.
A later human decision would authorize contract planning only; it would not
accept the capability contract, assign a lifecycle state, select canonical
artifacts, or authorize implementation.

The repository evidence cited here was inspected statically at revision
`c47591d28c9f870a56f567c468ca20530693bdeb`. Tests and notebooks were not run.
Saved notebook outputs and test source are observations, not passing evidence.

## 2. Purpose

The purpose of this proposal is to help a human choose the first bounded PhysKit
capability through which to exercise the reviewed lifecycle pattern:

> pedagogical purpose → physical model → mathematical formulation → explicit
> notebook construction → reusable PhysKit API → shared baseline comparison →
> multi-case exploration and visualization → software and numerical evidence →
> human acceptance

The first exercise should be small enough for close review, yet representative
enough to expose the scientific, pedagogical, API, artifact, evidence, and
human-approval decisions that the lifecycle policy protects.

## 3. Scope and exclusions

This proposal evaluates four narrowly bounded candidates:

1. affine temperature-scale conversion;
2. uniform closed one-dimensional grid with active index selection;
3. homogeneous-Dirichlet finite-difference Laplacian in one dimension;
4. analytical stationary states of the one-dimensional infinite square well.

The comparison uses read-only repository evidence from relevant unmodified
source, test, notebook, and documentation paths, together with:

- `docs/harness/physkit.harness.01-capability-baseline.md`;
- `docs/harness/physkit.harness.02-capability-lifecycle.md`.

This proposal excludes:

- the modified magnetism notebooks and all interpretation of their work;
- complete physics domains, whole subpackages, or general numerical-methods
  programs;
- execution of tests or notebooks;
- repair of source, tests, notebooks, examples, or documentation;
- selection of canonical APIs, implementations, notebooks, references, or
  tolerances;
- a complete pilot capability contract;
- lifecycle classification of any existing material;
- repository-wide cleanup or control-plane infrastructure.

## 4. Selection principles derived from the accepted lifecycle

For this planning step, the human instruction authorizes the reviewed lifecycle
policy as the basis for pilot comparison. The following principles are applied:

1. **Capability before file.** A pilot must be a human-recognizable unit of
   functionality, not a filename, class, notebook, or directory.
2. **Bounded vertical slice.** The pilot should connect pedagogy, explicit
   construction, reusable behavior, comparison, repeated use, and evidence
   without absorbing adjacent domains.
3. **Human authority.** The recommendation may identify decisions but may not
   make protected model, convention, API, artifact, tolerance, evidence, or
   lifecycle decisions.
4. **Two visible stages.** A student-facing pilot should support Stage 1 raw
   construction and Stage 2 PhysKit use without hiding the target computation in
   Stage 1.
5. **Independent evidence.** Software verification, numerical verification,
   physical validation, pedagogical validation, and UQ are separately
   dispositioned. Passing tests or agreement does not cause promotion.
6. **Minimum floors.** A public executable library claim requires software
   verification; numerical-result claims require numerical verification; a
   student-facing capability requires proportional pedagogical validation.
7. **Analytic leverage.** For a first exercise, an analytic or independently
   checkable baseline reduces evidence ambiguity and makes discrepancies easier
   to interpret.
8. **Conflict containment.** Existing conflicts are useful only when they can be
   resolved within the pilot boundary. The pilot must not become a pretext for
   repository-wide consolidation.
9. **Historical neutrality.** Competing representations remain alternatives
   pending human decisions; no representation is declared obsolete here.
10. **Selection is not promotion.** Human selection of a pilot would authorize
    the next contract-planning step, not Candidate, Supported, or any other
    lifecycle state.

## 5. Candidate capabilities

### 5.1 Affine temperature-scale conversion

**Proposed capability name**

Affine conversion among a bounded set of temperature scales through a Kelvin
reference representation.

**Intended learner or user**

Beginning physics learners and PhysKit users who need explicit, vectorized
conversion among K, °C, mK, °F, and °R.

**Pedagogical objective**

Explain why temperature-scale conversion is affine rather than uniformly
multiplicative, distinguish absolute and offset scales, and apply conversions to
scalars and arrays.

**Physical or mathematical scope**

Deterministic affine maps to and from Kelvin. Thermometry, measurement models,
unit algebra, parsing, and empirical temperature realization are excluded.

**Explicit-construction opportunity**

Write each scale-and-offset equation visibly, construct the conversion through
a Kelvin intermediate, and check known points and round trips without PhysKit.

**Possible PhysKit library use**

A public conversion operation could reproduce the baseline points and convert
arrays across several unit pairs. This is a possible use, not an accepted API.

**Possible multi-case visualization**

Plot linear relationships between scales over a declared mathematical range and
compare several unit pairs. Visualization is useful but not central.

**Existing source declarations**

- `src/physkit/units/temperature.py` declares `Temperature`, a nested `Units`
  enum, a Kelvin conversion table, `to_canonical`, `from_canonical`, `convert`,
  and `check_in_range`.
- `src/physkit/units/protocols.py` declares `UnitQuantityProtocol`.
- `src/physkit/units/__init__.py` re-exports `Temperature`.

**Existing tests**

- `tests/physkit/units/test_Temperature.py` contains protocol, signature, shape,
  and K↔C round-trip assertions.
- The inspected test source does not directly cover known points for every
  scale, all conversion branches, or the range behavior.

**Existing notebooks**

- `notebooks/units/units_temperature.ipynb` is a three-code-cell notebook with a
  saved result and no narrative Stage 1.
- Its inspected call uses an older tuple-style API that differs from the current
  source signature.

**Existing documentation**

- `docs/physkit.units.temperature.md` states the affine equations and intended
  behavior, but contains API-name drift and an invalid example using `from=`.

**Competing representations**

The principal conflict is not a second conversion engine but drift among the
current source signature, the source docstring, documentation examples, and the
notebook's older call form. The source also labels `mK` as micro-kelvin while its
factor and documentation indicate millikelvin.

**Dependency depth**

Low: NumPy plus small PhysKit array/type helpers. Neighboring unit-system
containers need not enter the pilot.

**Available analytic or trusted references**

The affine equations are directly checkable. External scale definitions and
reference points would still require human selection; repository documentation
alone is not an accepted authority.

**Expected evidence classifications**

- software verification: Required for a public executable conversion;
- numerical verification: Required for claimed numerical conversions;
- physical validation: potentially Not applicable only for a purely defined
  scale-conversion claim with a human-accepted rationale;
- pedagogical validation: Required if student-facing;
- UQ: potentially Not applicable to the conversion itself, while measurement
  uncertainty remains excluded, subject to human acceptance.

**Major human decisions**

Capability boundary, supported scales, public call semantics, array/return
behavior, below-absolute-zero policy, authoritative definitions, invariants,
tolerances, learning objectives, and artifact roles.

**Explicit exclusions**

General unit algebra, dimensional analysis, string parsing, thermometry,
measurement uncertainty, vapor-pressure validity checking, and repair of all
unit classes.

### 5.2 Uniform closed one-dimensional grid with active index selection

**Proposed capability name**

Uniform closed one-dimensional reference grid with explicit selection of active
degrees of freedom.

**Intended learner or user**

Learners beginning numerical physics and users preparing finite-difference or
boundary-value calculations.

**Pedagogical objective**

Distinguish a continuous interval, the full sampled grid, boundary points,
active degrees of freedom, and restriction/reconstruction operations.

**Physical or mathematical scope**

A finite uniform sampling of `[a,b]` and explicit active indices. No differential
operator, solver, field equation, or physical boundary model is included.

**Explicit-construction opportunity**

Construct coordinates with the spacing formula, enumerate interior and boundary
indices, restrict a full vector, reconstruct a boundary-augmented vector, and
show the associated selection matrix.

**Possible PhysKit library use**

A grid and active-set abstraction could reproduce the explicit coordinates and
indexing for different intervals, resolutions, and active selections. This is a
possible behavior, not an accepted class or API.

**Possible multi-case visualization**

Display active versus boundary samples for several resolutions and selections;
compare full, interior, left/right, and arbitrary active sets.

**Existing source declarations**

- `src/physkit/core/grids.py` declares `CartesianAxis`, `CartesianGrid1D`, and
  `ActiveSet1D`.
- `src/physkit/discretization/grid_1d.py` declares a separate `Grid1D` with
  seven enum-selected active-set conventions.
- `src/physkit/core/state.py` declares another interior-coordinate `Grid1D` used
  by `Wavefunction1D`.
- `src/physkit/visualize/grids.py` contains a grid plotting helper whose expected
  `grid.x` representation differs from current `core.grids` source.

**Existing tests**

- `tests/physkit/core/test_CartesianAxis.py` and
  `tests/physkit/core/test_CartesianGrid1D.py` express substantial constructor,
  spacing, dtype, immutability, and validation expectations, but their names and
  attributes drift from current source.
- `tests/physkit/discretization/test_ActiveSetType1D.py` and
  `tests/physkit/discretization/test_Grid1D.py` cover the enum-based alternative.
- No focused test for `core.grids.ActiveSet1D` was identified by the bounded
  inspection.

**Existing notebooks**

- `notebooks/basic/01_discretization_1d.ipynb` constructs several interval
  conventions directly.
- `notebooks/core/grids/cartesian-grid-1d.ipynb` uses PhysKit objects to explore
  full/interior states, restriction, reconstruction, and visualization.
- `notebooks/core/grids/cartesian-axis.ipynb` explores endpoint and resolution
  choices.
- `notebooks/scratch/discretization/grid_1d_conventions.ipynb` is a competing
  exploratory construction.

**Existing documentation**

No dedicated tracked grid page was identified by the baseline's bounded search.
Source docstrings and notebooks provide partial explanations.

**Competing representations**

At least three incompatible meanings of one-dimensional grid are present:
endpoint-configurable Cartesian axis/grid, closed reference grid coupled to an
enum active set, and interior-coordinate state grid. Names also differ for
bounds, spacing, length, coordinates, and active selection.

**Dependency depth**

Low for a bounded grid: NumPy and basic Python data structures. Downstream
operators and solvers can remain excluded.

**Available analytic or trusted references**

Coordinate and spacing formulas, endpoint membership, index selection, and
restriction/reconstruction identities are independently checkable.

**Expected evidence classifications**

- software verification: Required for a public executable grid API;
- numerical verification: Required for coordinate and indexing claims;
- physical validation: potentially Not applicable for a mathematical sampling
  claim with accepted rationale;
- pedagogical validation: Required if student-facing;
- UQ: potentially Not applicable, without eliminating numerical checks for
  floating-point or discretization semantics.

**Major human decisions**

Grid purpose, endpoint convention, active-set model, names, array mutability,
validation, relationship among existing representations, learning objectives,
and artifact roles.

**Explicit exclusions**

Two- and three-dimensional grids, differential operators, boundary-condition
objects, wavefunction semantics, solvers, mesh refinement, nonuniform grids,
and reconciliation of every downstream consumer.

### 5.3 Homogeneous-Dirichlet finite-difference Laplacian in one dimension

**Proposed capability name**

Sparse centered finite-difference approximation of the one-dimensional second
derivative on a uniform closed grid with homogeneous Dirichlet endpoints.

**Intended learner or user**

Learners who know derivatives and matrices and are beginning numerical
boundary-value problems; users needing a small reusable second-derivative
operator.

**Pedagogical objective**

Derive the centered stencil, map interior unknowns to a tridiagonal matrix,
connect boundary elimination to matrix shape, and observe second-order
convergence for smooth functions.

**Physical or mathematical scope**

The operator `d²/dx²` on a uniform one-dimensional grid with both endpoint
values fixed to zero. No Poisson solver, eigensolver, time evolution, or other
boundary type is included.

**Explicit-construction opportunity**

Derive `(u[i-1] - 2u[i] + u[i+1])/dx²`, build the dense or sparse matrix visibly,
apply it to sampled sine functions, calculate error, and estimate convergence
order without PhysKit.

**Possible PhysKit library use**

A public operator could reproduce the same matrix and active coordinates, then
support repeated resolution, interval, and sine-mode cases. No import path,
class name, or return type is accepted here.

**Possible multi-case visualization**

Plot exact versus discrete second derivatives, error profiles, log-log
convergence, sparse structure, and multiple sine modes or grid resolutions.

**Existing source declarations**

- `src/physkit/numerics/finite_difference.py` declares `Laplacian1D` and the
  intended sparse tridiagonal construction.
- It imports a nonexistent `physkit.core.bc` path and expects grid attributes
  that differ from current `CartesianGrid1D`.
- `src/physkit/numerics/differentiation/__init__.py` exports a
  `FiniteDifferenceLaplacian1D` name not declared by its `laplacian.py` module;
  that module unexpectedly contains a PIAB model instead.
- `src/physkit/core/operator.py` and `src/physkit/math/operators/base.py` contain
  overlapping dense, state-oriented operator abstractions; the latter has a
  broken relative import.

**Existing tests**

No substantive direct Laplacian tests were identified by the bounded search.
The nearest grid tests have source/API drift, and the PIAB-named test file is a
module-skipped stub with pass-only Laplacian classes.

**Existing notebooks**

- `notebooks/numerics/differentiation/finite-difference-laplacian-1d.ipynb`
  contains grid, active-state, sparse-operator, analytic-error, convergence, and
  storage sections.
- It imports the nonexistent advertised class and does not yet separate a fully
  explicit Stage 1 matrix construction from Stage 2 library use.
- Other Poisson, FEM, basic-grid, and scratch notebooks are adjacent material,
  not accepted pilot artifacts.

**Existing documentation**

No dedicated tracked finite-difference operator page was identified by the
baseline's bounded search.

**Competing representations**

The sparse stencil, the notebook-advertised but missing class, dense
wavefunction-coupled operators, duplicated symbolic operator modules, and
several grid conventions overlap without an accepted layering.

**Dependency depth**

Moderate: NumPy, SciPy sparse matrices, one grid/active-set convention that
would require human acceptance, and homogeneous Dirichlet semantics. Broader
operator hierarchies can be excluded.

**Available analytic or trusted references**

For `sin(kπx/L)`, the continuum second derivative and exact discrete
finite-difference eigenvalue are analytically available. These support matrix
invariants and convergence checks without relying on the PhysKit implementation.

**Expected evidence classifications**

- software verification: Required for a public operator;
- numerical verification: Required, including independently built coefficients,
  analytic modes, and refinement behavior;
- physical validation: potentially Not applicable for a purely mathematical
  operator claim with accepted rationale;
- pedagogical validation: Required if student-facing;
- UQ: human disposition required; discretization error belongs to numerical
  verification and must not be mislabeled UQ.

**Major human decisions**

Grid and active-set convention, boundary representation, public import/name,
sparse return contract, minimum grid size, endpoint assumptions, references,
error metric, tolerances, learning objectives, and artifact roles.

**Explicit exclusions**

Neumann, Robin, periodic, and nonhomogeneous boundaries; nonuniform grids;
higher dimensions; Poisson and eigenvalue solvers; PIAB physics; time evolution;
and reconciliation of all operator abstractions.

### 5.4 Analytical stationary states of the one-dimensional infinite square well

**Proposed capability name**

Analytical energy levels and stationary eigenfunctions of a particle in a
one-dimensional infinite square well.

**Intended learner or user**

Introductory quantum-mechanics learners who know wavefunctions, boundary
conditions, and elementary differential equations; users needing a transparent
analytic reference case.

**Pedagogical objective**

Connect the idealized confinement model and zero-boundary wavefunction to
quantized wave numbers, normalized sine eigenfunctions, and the scaling
`E_n ∝ n²/(mL²)`.

**Physical or mathematical scope**

A nonrelativistic particle of positive mass on a finite interval with an
infinite exterior potential and homogeneous Dirichlet endpoint conditions. Only
analytical time-independent stationary states are included.

**Explicit-construction opportunity**

State the model and assumptions, solve the time-independent Schrödinger
equation, impose endpoint conditions, derive wave numbers, normalize the sine
functions, compute energies visibly in Python, and check endpoint,
normalization, orthogonality, and energy-scaling invariants without PhysKit.

**Possible PhysKit library use**

A reusable model-and-analytic-solver behavior could reproduce the shared
baseline, return requested lowest states, evaluate eigenfunctions on user-supplied
coordinates, and support repeated lengths, masses, and quantum numbers. This
does not select the existing class hierarchy or any public API.

**Possible multi-case visualization**

Plot several eigenfunctions and probability densities; compare energy levels;
sweep well length and particle mass; and display the expected `n²`, `L⁻²`, and
`m⁻¹` scaling.

**Existing source declarations**

- `src/physkit/qm/models/piab1d.py` declares a one-dimensional physical model,
  result family, and solver interface.
- `src/physkit/qm/solvers/piab1d/tise.py` declares stationary-state result and
  solver interfaces.
- `src/physkit/qm/solvers/piab1d/tise_analytical.py` declares analytic energies
  and eigenfunction evaluation using the standard closed-form expressions.
- The preferred-looking stack is currently blocked by an `ABC`/`Generic`
  method-resolution-order conflict in its base hierarchy.
- `src/physkit/qm/well1d.py`, `src/physkit/qm/solver1d.py`, and
  `src/physkit/solidstate/piab1d.py` provide older or competing model/numerical
  representations with separate discrepancies.

**Existing tests**

- `tests/physkit/solidstate/test_ParticleInABox1D.py` is explicitly skipped and
  contains no substantive PIAB assertions.
- No focused test relationship for the newer analytic model/result/solver stack
  was identified by the bounded inspection.

**Existing notebooks**

- `notebooks/qm/qm.piab1d.ipynb` contains the richest model, analytic solution,
  grid, boundary, Hamiltonian, eigensolve, normalization, comparison, and
  visualization narrative, but its numerical imports are currently broken.
- `notebooks/qm/qm.piab1d.sym.ipynb` contains a symbolic derivation.
- `notebooks/qm/qm.piab1d.comp.ipynb` and
  `notebooks/qm/qm.piab1d.physkitlib.ipynb` are exact duplicate, abbreviated
  experiments according to the baseline and bounded inspection.
- Other PIAB notebooks are incomplete, retain saved errors, use independent
  local implementations, or cover broader course material.

**Existing documentation**

No dedicated tracked PIAB documentation page was identified by the baseline's
bounded search. Source docstrings and notebook narratives provide partial
material.

**Competing representations**

The newer model/result/solver stack, the dense `well1d` stack, the incomplete
generic sparse solver, the unfinished solid-state representation, symbolic
code, and notebook-local implementations overlap. They differ in units,
constants, grid coupling, naming, solver scope, and separation of model from
method.

**Dependency depth**

Moderate for an analytic-only boundary: NumPy, physical constants or explicit
`hbar`, zero-Dirichlet model semantics, and a usable model/result/solver
interface. SciPy eigensolvers, numerical grids, and finite differences are not
required.

**Available analytic or trusted references**

Closed-form energies and normalized sine eigenfunctions provide a direct
independent baseline. External textbook or primary reference selection remains
a human decision.

**Expected evidence classifications**

- software verification: Required for a public executable model/solver API;
- numerical verification: Required for energy and eigenfunction values,
  normalization, orthogonality, endpoint behavior, and scaling invariants;
- physical validation: potentially Not applicable only if the claim remains an
  idealized mathematical teaching model and does not imply real-system
  adequacy, subject to human acceptance;
- pedagogical validation: Required for a student-facing pilot;
- UQ: human disposition required; likely limited for exact input parameters,
  while parameter sensitivity can be explored without calling it UQ.

**Major human decisions**

Intended learners and objectives; exact infinite-well assumptions; interval,
mass, units, constants, state ordering, sign/phase conventions, and output
semantics; analytic-only boundary; public API; references, invariants,
tolerances; artifact roles; and evidence dispositions.

**Explicit exclusions**

Finite wells, potentials inside the box, numerical finite-difference solving,
time dependence, two- and three-dimensional boxes, spin, interactions,
relativity, real-material adequacy, and consolidation of all legacy PIAB code.

## 6. Comparison criteria

Ratings are qualitative and evidence-backed. They are not maturity scores and
do not assign lifecycle states.

For **opportunity criteria**—pedagogical clarity, raw-code exposure, library
value, multi-case iteration, visualization, reference availability, verification
tractability, and representativeness:

- **Low:** the candidate offers little of the desired property within its bounded
  scope;
- **Moderate:** the property is useful but partial or depends on material human
  decisions;
- **High:** the property is central, visible, and achievable within the proposed
  boundary.

For **burden and risk criteria**—validation burden, dependency depth, competing
implementations, API uncertainty, notebook condition burden, implementation
scope, and refactoring risk:

- **Low:** few dependencies or conflicts are expected within the boundary;
- **Moderate:** bounded resolution work is material but separable;
- **High:** multiple coupled conflicts or substantial scope-control effort are
  expected.

“Notebook condition burden” rates the work needed to obtain a reviewable
notebook, not the notebook's pedagogical worth. “Physical-validation burden” is
Low only where a human could plausibly accept Not applicable for a claim that
does not imply real-system adequacy; this proposal does not accept that
disposition.

## 7. Comparison matrix

### 7.1 Opportunity and tractability

| Criterion | Temperature conversion | 1D grid and active set | 1D Dirichlet Laplacian | Analytical 1D infinite well |
|---|---|---|---|---|
| Pedagogical clarity | Moderate | High | High | High |
| Ability to expose raw code | High | High | High | High |
| Value of later library abstraction | Moderate | High | High | High |
| Suitability for multiple cases | Moderate | High | High | High |
| Visualization value | Low | High | High | High |
| Analytic/independent references | High | High | High | High |
| Software-verification tractability | High | Moderate | Moderate | Moderate |
| Numerical-verification tractability | High | High | High | High |
| Representativeness of future PhysKit work | Low | Moderate | High | High |

### 7.2 Burden and risk

| Criterion | Temperature conversion | 1D grid and active set | 1D Dirichlet Laplacian | Analytical 1D infinite well |
|---|---|---|---|---|
| Physical-validation burden | Low | Low | Low | Low within idealized claim |
| Pedagogical-review burden | Moderate | Moderate | Moderate | Moderate |
| Dependency depth | Low | Low | Moderate | Moderate |
| Competing-implementation burden | Low | High | High | High |
| API uncertainty | Moderate | High | High | High |
| Notebook condition burden | High | Moderate | Moderate | Moderate |
| Implementation scope | Low | Moderate | Moderate | Moderate |
| Repository-wide refactoring risk | Low | High | High | High |

These judgments expose the central tradeoff: temperature conversion is easiest
but tests little of the vertical physics pattern; grid and Laplacian candidates
exercise important foundations but stop before a complete physical model; the
analytical infinite well reaches the full pedagogical-to-physics-to-API path,
provided its boundary remains analytic-only.

## 8. Candidate-specific findings

### 8.1 Temperature conversion

**Strengths**

- smallest implementation and dependency surface;
- direct affine formulas and deterministic reference values;
- existing source, focused test source, notebook, and dedicated documentation;
- conflicts are localized API/documentation drift rather than architectural
  layering.

**Limitations for the first full exercise**

- weak visualization and limited repeated-case scientific exploration;
- does not exercise physical model, state space, operator, or result objects;
- current notebook has no narrative Stage 1 and uses a stale API;
- may test governance mechanics without adequately testing PhysKit's intended
  vertical scientific pattern.

**Overall finding**

A strong later calibration or infrastructure pilot, but less representative as
the first full capability exercise.

### 8.2 Uniform 1D grid and active set

**Strengths**

- clear lesson about discretization, endpoints, active degrees of freedom, and
  restriction/reconstruction;
- low implementation dependencies and strong visual opportunities;
- independently checkable formulas and existing notebook material close to the
  preferred two-stage pattern;
- foundational for many future numerical capabilities.

**Limitations for the first full exercise**

- choosing among three grid meanings is a significant protected API and
  mathematical-convention decision;
- current tests and plotting helper drift from current source;
- lacks a physical model and can become a repository-wide grid reconciliation
  project if boundaries are not enforced.

**Overall finding**

A valuable foundational pilot, but its apparent simplicity hides a high
representation-consolidation risk and it tests only part of the vertical pattern.

### 8.3 Homogeneous-Dirichlet 1D Laplacian

**Strengths**

- compact stencil with transparent matrix construction;
- strong analytic sine-mode and exact discrete-eigenvalue references;
- natural convergence, sparse-structure, resolution, and visualization work;
- existing notebook already contains many desired numerical-verification
  elements;
- representative of reusable numerical PhysKit work.

**Limitations for the first full exercise**

- all advertised library routes have import or API blockers;
- depends on unresolved grid, active-set, and boundary conventions;
- no substantive direct tests were found;
- operator-abstraction overlaps can easily pull in symbolic, state, Poisson,
  eigensolver, and multidimensional refactoring;
- remains a mathematical operator rather than a complete physical capability.

**Overall finding**

The strongest alternative to the recommendation and a good future second
exercise after the grid/operator seam is explicitly bounded by humans.

### 8.4 Analytical 1D infinite-well stationary states

**Strengths**

- one of the smallest complete physics narratives in the repository;
- exact energies and eigenfunctions permit close independent review;
- raw derivation is pedagogically visible and library reuse adds genuine value;
- length, mass, quantum-number, wavefunction, probability-density, and energy
  cases support iteration and visualization;
- an analytic-only boundary avoids grid, finite-difference, sparse-matrix,
  eigensolver, and convergence dependencies;
- existing model/result/solver declarations and multiple notebooks expose the
  governance questions the lifecycle is intended to handle.

**Limitations for the first full exercise**

- the newer analytic stack cannot currently import because of a base-hierarchy
  conflict;
- no substantive focused tests support that stack;
- multiple PIAB representations and notebooks create high canonical-selection
  pressure;
- unit/constants, interval, sign/phase, result, and import-surface decisions
  remain human-owned;
- scope could expand rapidly into numerical PIAB or repository-wide quantum
  cleanup unless explicitly prohibited.

**Overall finding**

Best balance of bounded analytic tractability and end-to-end
representativeness, if and only if the human selects an analytic-only boundary.

## 9. Advisory recommendation

### Advisory recommendation — human selection required

Recommend **analytical stationary states of the one-dimensional infinite square
well** as the first pilot, limited to the preliminary boundary in Section 10.
This is a recommendation only. The capability is not selected, accepted,
classified, or authorized for implementation by this document.

### Why it is appropriately bounded

The proposed pilot stops at a single idealized one-dimensional model and its
closed-form stationary solutions. It excludes numerical eigensolvers,
finite-difference grids, time dependence, higher dimensions, and finite
potentials. The needed mathematics fits in a short derivation and visible Python
implementation, while the reusable behavior remains meaningful.

### Why it is pedagogically meaningful

The capability connects physical assumptions to boundary conditions,
quantization, normalization, energy scaling, eigenfunctions, and probability
density. Learners can see why discrete energies arise rather than treating a
library result as an unexplained number.

### Stage 1 raw construction

Stage 1 can state the infinite-well assumptions and interval, solve the
stationary Schrödinger equation, impose endpoint conditions, derive
`k_n = nπ/L`, normalize `sin(k_n(x-x_lower))`, compute
`E_n = hbar²π²n²/(2mL²)`, implement these expressions directly with NumPy, and
check endpoint, normalization, orthogonality, ordering, and scaling behavior.
The target calculation would not call PhysKit.

### Stage 2 repeated PhysKit use and visualization

Stage 2 could use a human-accepted PhysKit model-and-analytic-solver API to
reproduce the shared baseline, then vary well length, mass, state count, and
evaluation coordinates. It could compare energy ladders, eigenfunctions, and
probability densities and visualize `n²`, `L⁻²`, and `m⁻¹` scaling. These are
expected uses, not accepted API requirements.

### Analytic or independent baseline

The closed-form spectrum and normalized sine eigenfunctions provide the shared
baseline. Endpoint zeros, normalization, orthogonality, energy ratios, and
parameter scaling give independent invariants. Humans must still select
references, numerical representation, comparison method, and tolerances.

### Existing conflicts that must be resolved

Only conflicts necessary for the analytic slice should be addressed later:

- the `ABC`/`Generic` hierarchy that blocks importing the newer PIAB analytic
  stack;
- the bounded relationship among physical model, analytic solver, and result;
- mass, length, `hbar`, and unit-consistency semantics;
- homogeneous Dirichlet boundary representation needed by the model;
- requested-state ordering and eigenfunction evaluation/sign conventions;
- the public import surface for the accepted analytic behavior;
- focused software and numerical evidence for that behavior;
- the role of existing PIAB notebooks relative to a future notebook proposal.

### Broader conflicts explicitly out of scope

The pilot should not reconcile the dense `well1d` numerical stack, generic
sparse solver, solid-state PIAB prototype, all grid/operator abstractions,
finite-difference Laplacians, 2D/3D PIAB, every PIAB notebook, the syntax error in
`piab3d.py`, or repository-wide quantum imports unless a narrowly demonstrated
import seam makes one item unavoidable. No excluded representation is declared
obsolete.

### Why it is preferable to the alternatives

- Compared with temperature conversion, it exercises an actual physical model,
  mathematical solution, result behavior, multi-case exploration, and rich
  visualization.
- Compared with the grid candidate, it reaches a complete learner-facing
  scientific claim without first resolving general discretization semantics.
- Compared with the finite-difference Laplacian, it retains the analytic and
  reusable benefits while avoiding grid, active-set, sparse-matrix, boundary
  elimination, and convergence dependencies in the first exercise.
- Unlike a broader numerical PIAB pilot, the analytic-only slice keeps the first
  lifecycle exercise reviewable while still testing protected physics,
  pedagogy, API, artifact, evidence, and approval decisions.

## 10. Proposed pilot boundary

This is a preliminary boundary for human selection. It is not an accepted
capability contract.

### 10.1 Intended pedagogical purpose

Enable a learner to derive, compute, inspect, and compare the analytical
stationary states of an ideal one-dimensional infinite square well, then use a
reusable PhysKit behavior to explore repeated parameter and state cases.

### 10.2 Intended learner

An introductory undergraduate quantum-mechanics learner who has encountered the
time-independent Schrödinger equation, wavefunctions, boundary conditions, and
basic normalization integrals. The exact prerequisites and learning objectives
remain for human acceptance.

### 10.3 Included physical model

Proposed for review:

- one nonrelativistic particle;
- one finite interval `[x_lower, x_upper]` with positive length;
- positive particle mass;
- zero potential inside and infinite exclusion outside;
- homogeneous Dirichlet wavefunction values at both endpoints;
- time-independent stationary states only.

No model choice in this list is accepted by this proposal.

### 10.4 Included mathematical formulation

Proposed for review:

- the one-dimensional stationary Schrödinger eigenproblem;
- positive integer state labels beginning at one;
- closed-form wave numbers, energies, and real normalized sine eigenfunctions;
- energy ordering, endpoint, normalization, orthogonality, and parameter-scaling
  invariants;
- evaluation of a bounded requested set of states on user-supplied coordinates
  inside the interval.

Phase/sign comparison and numerical quadrature conventions remain human
decisions.

### 10.5 Expected explicit notebook construction

Stage 1 should visibly include:

- model assumptions, state space, interval, units, parameters, and boundaries;
- derivation of quantization and normalization;
- direct NumPy implementation of energies and eigenfunctions;
- intermediate wave numbers and normalization factors;
- independent checks of endpoint values, normalization, orthogonality, energy
  ratios, and scaling;
- plots of states and probability densities.

No PhysKit target calculation should be hidden inside Stage 1.

### 10.6 Expected public-library behavior

Subject to a later human-accepted contract, a PhysKit behavior would be expected
to:

- represent the bounded model inputs explicitly;
- compute a requested positive sequence of analytical stationary-state energies;
- evaluate corresponding eigenfunctions at valid coordinates;
- return inspectable state labels, energies, model context, and evaluated arrays;
- validate declared input and shape constraints;
- behave deterministically for the same explicit inputs.

This list does not select class names, signatures, result containers, import
paths, defaults, units, or exceptions.

### 10.7 Expected multi-case exploration

Stage 2 should be capable of:

- comparing several state indices;
- varying interval length;
- varying positive mass;
- evaluating on several coordinate arrays;
- comparing energies, eigenfunctions, and probability densities;
- visualizing the `n²`, `L⁻²`, and `m⁻¹` relationships.

Finite-difference convergence is excluded from this analytic-only pilot.

### 10.8 Expected verification references

Proposed references and invariants for later human selection include:

- an independently cited derivation of the infinite-square-well spectrum;
- direct Stage 1 formulas separate from the PhysKit implementation;
- endpoint-zero and domain checks;
- normalization and pairwise orthogonality;
- `E_n/E_1 = n²` for fixed mass and length;
- inverse-mass and inverse-square-length energy scaling;
- shape, ordering, finiteness, immutability, and deterministic behavior where
  promised.

No reference, quadrature rule, invariant implementation, or tolerance is
accepted here.

### 10.9 Dependencies that must be resolved

Within the pilot boundary, later planning would need human decisions and bounded
resolution of:

- the importable model/result/solver hierarchy for the analytic slice;
- model parameter and unit-consistency semantics;
- how zero-Dirichlet conditions are represented without importing general
  boundary-condition scope;
- state-number and coordinate validation;
- eigenfunction output orientation and sign/phase comparison;
- public behavior and error contract;
- software, numerical, and pedagogical evidence obligations;
- artifact relationships for the explicit and library stages.

### 10.10 Dependencies treated as external accepted inputs

Subject to human acceptance during contract planning, the pilot may treat as
external inputs rather than new capabilities:

- NumPy array and elementary-function behavior;
- an authoritative human-selected analytic quantum-mechanics reference;
- human-selected values or explicit inputs for `hbar`, mass, and length;
- plotting-library primitives used only for presentation.

Treating an input as external does not confer Supported status on any existing
PhysKit helper or erase the need to verify its use at the pilot boundary.

### 10.11 Work explicitly excluded from the pilot

- numerical finite-difference or other eigensolvers;
- grids, active sets, discrete operators, convergence studies, and sparse
  matrices;
- time-dependent states or superpositions as a promised behavior;
- finite wells, arbitrary potentials, tunneling, scattering, spin,
  interactions, or relativity;
- two- or three-dimensional boxes;
- empirical adequacy for a real quantum well or material;
- general constants, units, boundary, result-container, or serialization
  capabilities;
- resolution, removal, or deprecation of competing PIAB implementations beyond
  the narrow import and contract seam selected by humans;
- broad notebook repair or repository-wide quantum cleanup.

## 11. Risks and deferred work

### 11.1 Scope-expansion risk

The recommended area contains many overlapping source and notebook
representations. A later plan must reject incidental cleanup unless it is
strictly required by the human-selected analytic boundary. Numerical PIAB is a
separate possible future capability.

### 11.2 Apparent-reference simplicity

Closed-form formulas reduce numerical ambiguity but do not eliminate decisions
about units, coordinate domains, quadrature, floating-point comparisons,
eigenfunction sign/phase, array orientation, or authoritative references.

### 11.3 Package import coupling

An unrelated syntax or import defect may affect broad package import behavior.
A later contract must define the bounded import gate and escalate any required
change rather than automatically expanding to repair every quantum module.

### 11.4 Pedagogical evidence

Abundant notebook material does not establish accepted learning objectives or
pedagogical validation. Proportional minimum evidence may be instructor review,
but the responsible humans and method remain unresolved.

### 11.5 Physical-validation claim boundary

The ideal infinite-well solution is not automatically adequate for a real
quantum well. Physical validation may be Not applicable only if humans accept a
strictly idealized teaching claim whose documentation does not imply real-system
adequacy.

### 11.6 Deferred candidate work

- temperature conversion remains a strong small utility/evidence calibration
  candidate;
- the 1D grid remains a foundational representation candidate after humans
  narrow its competing semantics;
- the 1D Dirichlet Laplacian remains a strong numerical candidate after humans
  define the grid/operator seam.

No ordering beyond the single advisory recommendation is proposed.

## 12. Human selection decision

A human must choose one of the following. No choice is made by this document.

### Option A — accept the recommended pilot boundary

Select the analytical one-dimensional infinite-square-well stationary-state
boundary in Section 10 as the subject of the next contract-planning stage,
subject to any human amendments recorded with the decision.

### Option B — select another evaluated candidate

Select temperature conversion, the uniform 1D grid and active set, or the
homogeneous-Dirichlet 1D Laplacian, and identify which preliminary boundary and
comparison findings should guide a revised contract-planning scope.

### Option C — request a narrower or revised candidate

Request changes to a candidate's learner, objective, model, mathematical scope,
library behavior, evidence expectations, dependencies, or exclusions before
selection.

### Option D — defer pilot selection

Make no pilot selection and request additional evidence or review without
implicitly authorizing implementation or lifecycle classification.

There is no agent-decides option. Silence, commit, publication, or merge does
not select a pilot.

## 13. Next step after selection

If a human selects a pilot, the next step is a separate, bounded proposal for
that capability's contract and evidence obligations. That step should begin
from the human-selected boundary and resolve only the protected decisions needed
to state a reviewable contract.

Selection alone must not:

- assign Exploratory, Candidate, Supported, Deprecated, or Historical;
- accept a physical model or mathematical convention;
- accept a public API or canonical notebook;
- define or accept tolerances;
- authorize source, test, notebook, or documentation changes;
- initiate implementation.

If the human requests revision or deferral, no contract-planning or
implementation stage begins.

## 14. Explicit non-decisions

This proposal explicitly does not:

1. select or accept a pilot capability;
2. assign any lifecycle state to a candidate or existing artifact;
3. accept the recommended physical model, mathematical formulation, audience,
   learning objective, API, dependency, evidence disposition, or boundary;
4. select a canonical source declaration, implementation, test, notebook,
   visualization, documentation page, or reference;
5. classify any competing representation as obsolete, deprecated, historical,
   incorrect in total, or suitable for removal;
6. define numerical tolerances, pedagogical acceptance, physical validation, or
   UQ adequacy;
7. authorize implementation, repair, refactoring, notebook execution, or test
   execution;
8. select either modified magnetism notebook or inspect its active human work;
9. update the baseline, lifecycle policy, `README.md`, source, tests, notebooks,
   examples, or existing documentation;
10. define a complete pilot contract, repository-wide cleanup plan, schema,
    record, agent, chain, skill, checkpoint, `.pi/` state, or other control-plane
    infrastructure;
11. begin another planning stage merely because this file is committed or
    published.
