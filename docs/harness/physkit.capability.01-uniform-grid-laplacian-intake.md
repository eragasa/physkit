# Uniform one-dimensional grid and Laplacian capability intake

**Status:** Proposed for human scope review

**Task:** `FOUNDATIONS-FD1`

**Inspection revision:** `46e313afb3dbccd320968c16df7f72b77a76774a`

**Authority:** Descriptive and advisory intake only; not a capability contract

## 1. Purpose, scope, and non-decisions

This intake inventories existing PhysKit representations related to uniform one-dimensional grids, active degrees of freedom, boundary data, discrete states, and finite-difference second derivatives. It prepares alternatives for a human capability-scope decision.

It does **not** select a capability boundary, survivor implementation, public API, matrix storage, sign convention, canonical notebook, evidence criterion, lifecycle state, or support claim. It does not accept a contract or authorize implementation. PIAB, Hamiltonians, eigensolvers, and Poisson solvers remain outside the proposed initial boundary.

The inspection was static. Notebooks were parsed but not executed; dependencies were not installed. Saved notebook outputs are historical observations, not current execution evidence.

## 2. Inspection method and relevant-path inventory

### 2.1 Required paths inspected

- `src/physkit/discretization/grid_1d.py`
- `src/physkit/core/grids.py`
- `src/physkit/core/state.py`
- `src/physkit/core/operator.py`
- `src/physkit/numerics/finite_difference.py`
- `src/physkit/numerics/differentiation/laplacian.py`
- `src/physkit/math/operators/continuous1d.py`
- `src/physkit/math/operators/discrete1d.py`
- `tests/physkit/discretization/test_ActiveSetType1D.py`
- `tests/physkit/discretization/test_Grid1D.py`
- `notebooks/basic/01_discretization_1d.ipynb`
- `notebooks/core/grids/cartesian-axis.ipynb`
- `notebooks/core/grids/cartesian-grid-1d.ipynb`
- `notebooks/numerics/differentiation/finite-difference-laplacian-1d.ipynb`
- `notebooks/scratch/discretization/grid_1d_conventions.ipynb`

### 2.2 Additional directly relevant paths inspected

These paths were inspected only to resolve imports, tests, or competing consumers:

- `src/physkit/core/boundaries.py`
- `src/physkit/core/coordinates.py` (empty)
- `src/physkit/math/operators/base.py`
- `src/physkit/math/operators/__init__.py`
- `src/physkit/discretization/__init__.py` (empty)
- `src/physkit/numerics/__init__.py` (empty)
- `src/physkit/numerics/differentiation/__init__.py`
- `src/physkit/core/__init__.py` (empty)
- `tests/physkit/core/test_CartesianAxis.py`
- `tests/physkit/core/test_CartesianGrid1D.py`
- `notebooks/basic/grid_1d.py`
- `notebooks/basic/test_Grid1D.py`
- `src/physkit/qm/well1d.py`
- `src/physkit/qm/solver1d.py`
- `src/physkit/qm/models/piab.py`

Repository-wide static reference searches also identified PIAB/QM notebooks and visualization/solver consumers. Their physics behavior was not analyzed because PIAB and solver work are prohibited.

## 3. Existing representations

No row below designates a canonical survivor.

### 3.1 Grid, active-set, state, and boundary representations

| Exact path | Objects and meaning | Numerical representation and dependencies | Consumers, tests, and notebooks | Observed condition; advisory classification |
|---|---|---|---|---|
| `src/physkit/discretization/grid_1d.py` | `ActiveSetType1D`; frozen `Grid1D(a,b,N,active_type)`. The grid is explicitly closed and uniform; active types select all, interior, one-sided, or boundary indices. | `np.linspace(a,b,N)`, `dx=(b-a)/(N-1)`, index arrays, and `x_active=x[indices]`; NumPy and standard-library dataclass/enum only. | Direct tests in `tests/physkit/discretization/test_ActiveSetType1D.py` and `test_Grid1D.py`; scratch notebook describes its extraction. Few committed source consumers were found outside tests. | Internally coherent for a closed reference grid and potentially reusable, but it combines coordinate-grid definition with active-set policy. It permits `N=2`, for which `INTERIOR` is empty, and has no boundary-data object. Arrays are regenerated and mutable. Not exported by the empty package `__init__.py`.
| `src/physkit/core/grids.py` | `CartesianAxis`, `CartesianGrid1D`, and `ActiveSet1D` plus 2D/3D grids. Axis supports endpoint-inclusive or endpoint-excluded sampling. ActiveSet accepts arbitrary unique valid indices. | NumPy arrays; axis stores `length`, `delta`, and `values`; grid stores axis object, shape, size, delta. Active set stores `int64` indices and derived coordinates. | Used by grid notebooks, visualization, `qm/solver1d.py`, and several QM notebooks. Tests exist for axis and CartesianGrid1D, but no direct ActiveSet1D test was found. | Broad and potentially reusable, but committed tests and notebooks disagree with the implementation. Tests expect `L`, `d`, read-only values, `x_min/x_max`, `x_axis`, array-valued `grid.x`, `Lx`, and `dx`; implementation exposes `length`, `delta`, constructor `x_lower/x_upper`, axis-valued `grid.x`, and writable values. Some notebooks follow the implementation while others use missing aliases. This is a competing grid representation, not an accepted API.
| `src/physkit/core/state.py` | A second `Grid1D(x)` that represents interior samples only, plus `Wavefunction1D`. Boundaries are implicit in physics rather than stored. | Dense NumPy coordinate/value arrays; `dx` inferred from consecutive interior coordinates; discrete weighted normalization and inner product. | Used by `core/operator.py` and `qm/well1d.py`. No direct tests found in the inspected test inventory. | Competing, QM-coupled representation. It does not store `[a,b]`, endpoint coordinates, boundary values, or full-grid size; one interior point cannot define `dx`. Duplicate module header/imports are present. Potentially useful historical design evidence, but unsuitable as an unqualified general grid without human decisions.
| `src/physkit/core/boundaries.py` | General `BoundaryCondition` hierarchy, `AxisBoundaryConditions`, and `DirichletBoundaryCondition`, among others. A BC stores a mathematical constraint; axis pairing associates lower/upper conditions. | Typed Python objects with complex scalar values and finite-value validation; no grid indices or operator construction. | Used by the misplaced `Piab1D` content currently in `numerics/differentiation/laplacian.py` and other model code. | Conceptually separates boundary data from grid/active state and may be reusable. The proposed intake uses only homogeneous Dirichlet values; whether this hierarchy belongs in the first contract is a protected scope/API decision.
| `notebooks/basic/grid_1d.py` | Notebook-local `GridType1D` and `Grid1D` covering closed, left/right closed, open/interior, and midpoint grids. | NumPy arrays with spacing dependent on grid type. | Local `notebooks/basic/test_Grid1D.py`; related basic and scratch notebooks. | Exploratory competing implementation. It treats `OPEN` and `INTERIOR` identically, uses a different meaning of `N`, and is not package code.

### 3.2 Operator and Laplacian representations

| Exact path | Objects and mathematical meaning | Numerical representation and dependencies | Consumers/tests/notebooks | Observed condition; advisory classification |
|---|---|---|---|---|
| `src/physkit/core/operator.py` | `LinearOperator1D`, an abstract operator acting on `Wavefunction1D` tied to the interior-only `core.state.Grid1D`. | Lazy dense NumPy matrix; application returns a new `Wavefunction1D`; grid compatibility uses object identity. | `qm/well1d.py`; `math/operators/base.py` appears to duplicate this file. | Potentially reusable abstract idea, but tightly coupled to the competing QM state and dense matrices. No direct tests were found. It does not represent boundary restriction separately.
| `src/physkit/numerics/finite_difference.py` | `Laplacian1D`, intended to build the homogeneous-Dirichlet second derivative on interior unknowns. | SciPy CSR tridiagonal matrix with `(-2,1,1)/dx^2`; intended active slice `1:N-1`. | Imported by `qm/solver1d.py`. | Structurally close to the proposed operator, but currently broken against committed code: imports nonexistent `physkit.core.bc`, `BoundaryCondition`, and `DirichletBC`; expects `CartesianGrid1D.Nx`, array-valued `.x`, and `.dx`, which the current grid implementation does not expose. The module comment names `finitedifference.py`, differing from its path. Potentially reusable only after human scope/API decisions and later authorized repair.
| `src/physkit/numerics/differentiation/laplacian.py` | Despite its path, it defines `Piab1D`, a particle-in-a-box physical model, not a Laplacian. | Model scalars and boundary-condition objects; no grid or matrix. It imports nonexistent `physkit.core.constants`. | `numerics/differentiation/__init__.py` and several notebooks import missing `FiniteDifferenceLaplacian1D` from this path. | Broken/misplaced competing content. The promised class is absent, so current imports cannot be satisfied. PIAB content is explicitly parked and outside this task.
| `src/physkit/numerics/differentiation/__init__.py` | Re-exports `FiniteDifferenceLaplacian1D`. | Import-only module. | Used indirectly by notebook imports. | Broken because the exported symbol is absent from `laplacian.py`.
| `src/physkit/math/operators/continuous1d.py` | `ContinuousOperator1D` and symbolic `PoissonOperator1D`; intended continuous symbolic differentiation. | SymPy expressions. | No direct tests found. | Import-time defect: default arguments use undefined name `x`. It is Poisson-oriented and outside the proposed initial Laplacian boundary except as evidence that continuous and discrete operators are conflated in the repository.
| `src/physkit/math/operators/discrete1d.py` | Content duplicates `continuous1d.py`; it also defines `ContinuousOperator1D` and symbolic `PoissonOperator1D`, not a discrete operator. | SymPy, not a matrix representation. | `notebooks/math_poisson1d.ipynb` contains a separate notebook-local `DiscreteOperator1D`. | Broken/competing: undefined default `x`, wrong conceptual content for its filename, and no discrete Laplacian.
| `src/physkit/math/operators/base.py` and `math/operators/__init__.py` | `base.py` duplicates the dense `LinearOperator1D`; package init re-exports it. | Dense NumPy matrix and state coupling. | Package import surface. | Broken import: `base.py` imports nonexistent `.state`. This is a competing operator base, not an accepted public interface.
| `src/physkit/qm/well1d.py` | `InfiniteSquareWellHamiltonian1D` constructs dense `D2` on interior-only coordinates and multiplies by `-hbar²/(2m)`. | Dense NumPy tridiagonal matrix. | QM well model and reconstruction helpers. | Demonstrates a working-looking local stencil pattern but conflates D2 with a Hamiltonian workflow and depends on the interior-only grid. PIAB/Hamiltonian use is prohibited and not proposed for inclusion.
| `src/physkit/qm/solver1d.py` | Intended sparse Schrödinger solver consuming `finite_difference.Laplacian1D`. | SciPy sparse matrices/eigensolver. | QM solver consumers. | Contains stale/nonexistent BC imports and grid API assumptions, plus unresolved internal attribute names. It is excluded from the candidate boundary and cited only as a consumer conflict.

### 3.3 Tests

| Path | Coverage | Observed limitation |
|---|---|---|
| `tests/physkit/discretization/test_ActiveSetType1D.py` | Enum membership and uniqueness. | Does not validate mathematical semantics beyond existence/identity.
| `tests/physkit/discretization/test_Grid1D.py` | Closed coordinates, length, spacing, all active-index modes, active coordinates, invalid bounds/N, and `N=2` empty interior/boundary. | Supports the discretization implementation but explicitly accepts an empty interior at `N=2`, unlike the proposed `N>=3` boundary. No immutability, type, finite-bound, BC, state, or operator tests.
| `tests/physkit/core/test_CartesianAxis.py` | Intended constructor, endpoint conventions, validation, dtype, immutability, and repr behavior. | Substantially stale relative to implementation: expects aliases/properties and read-only arrays not present, and different error messages.
| `tests/physkit/core/test_CartesianGrid1D.py` | Intended grid attributes, endpoint conventions, shape/size, validation, dtype, immutability, and repr. | Substantially stale: constructor and attribute names do not match current implementation. This test/source disagreement prevents any support inference.
| `notebooks/basic/test_Grid1D.py` | Notebook-local checks for six sampling conventions. | Not package tests; tests the competing notebook-local implementation.

No committed direct test for `ActiveSet1D` or either proposed Laplacian implementation was found in the inspected inventory.

### 3.4 Notebook representations

| Path | Current content and use | Problems or classification |
|---|---|---|
| `notebooks/basic/01_discretization_1d.ipynb` | Explores left/right-closed, open interior, midpoint, and closed grids; ends with a notebook-local class sketch. | Exploratory and competing. One code cell calculates `dx = x[1]-x[0]` after defining uppercase `X`, and the class properties are indented inside `__post_init__`, so the sketch does not expose the intended properties. No saved error output appears, but most cells have historical execution counts.
| `notebooks/core/grids/cartesian-axis.ipynb` | Separates continuous interval, coordinate samples, endpoint conventions, resolution, and sampled fields using `CartesianAxis`. | Pedagogically relevant and relatively clear, but it refers to `axis.L` while implementation stores `length`. Saved outputs without errors do not establish current executability.
| `notebooks/core/grids/cartesian-grid-1d.ipynb` | Uses `CartesianGrid1D` and `ActiveSet1D`; distinguishes full state, interior state, boundary values, restriction, and embedding. | Strong conceptual evidence for separation. It is not canonical. It contains assertions tailored to `sin(pi x)` and homogeneous zero boundaries, and it has no accepted API/evidence status.
| `notebooks/numerics/differentiation/finite-difference-laplacian-1d.ipynb` | Presents the centered stencil, active interior, sparse matrix, application to `sin(pi x)`, convergence, and storage comparison. | Imports missing `FiniteDifferenceLaplacian1D`; current source at that path is unrelated PIAB content. It states sparse storage is “canonical,” but canonical storage is a protected undecided choice. Saved successful-looking outputs are stale relative to current source and are not validation.
| `notebooks/scratch/discretization/grid_1d_conventions.ipynb` | Records cleanup/migration claims, closed-grid active subsets, and package-like checks. | Scratch/exploratory. It imports `grid_1d` as a local module rather than `physkit.discretization.grid_1d`, duplicates open-interval material, and contains historical “done” claims that do not establish current authority.

## 4. Conceptual decomposition

The proposed subject requires these objects to remain distinct:

1. **Continuous domain:** $\Omega=[a,b]$, a set of real coordinates with endpoints and length $L=b-a$.
2. **Continuous scalar state space:** functions $u:\Omega\rightarrow\mathbb F$ with a stated regularity and boundary-condition domain where relevant.
3. **Coordinate sampling:** the rule $x_i=a+ih$ and the convention that determines $h$.
4. **Full grid samples:** $\mathbf x=(x_0,\ldots,x_{N-1})$ and, separately, full sampled values $\mathbf u=(u(x_0),\ldots,u(x_{N-1}))$.
5. **Active degrees of freedom:** an index set $\mathcal I_A$ selecting unknown components; for the proposed interior case, $\{1,\ldots,N-2\}$.
6. **Boundary data:** prescribed values associated with endpoint locations, here provisionally $u(a)=u(b)=0$; these are constraints, not automatically active unknowns.
7. **Discrete state vector:** $\mathbf u_A\in\mathbb F^{N-2}$, distinct from coordinates and from the full sampled-value vector.
8. **Discrete operator matrix:** $\mathbf D_2\in\mathbb R^{(N-2)\times(N-2)}$, a representation of an accepted finite-difference rule on the accepted active state.
9. **Operator application:** $\mathbf v_A=\mathbf D_2\mathbf u_A$, distinct from matrix construction and from reconstruction of full boundary-inclusive values.
10. **Numerical error:** a measured discrepancy under a stated norm, reference derivative, grid sequence, and mode; it is not a physical interpretation or automatically UQ.
11. **Physical interpretation:** a later model-specific meaning assigned to $u$, $\Omega$, or $-\mathbf D_2$; none is needed to define this mathematical/numerical capability.

### Existing conflations

- `discretization.Grid1D` combines a closed coordinate grid with active-set policy through an enum.
- `core.state.Grid1D` calls interior coordinates a grid while omitting the containing domain and boundary data.
- `Wavefunction1D` and `LinearOperator1D` bind general-looking state/operator names to a QM-oriented interior representation.
- `qm/well1d.py` constructs $\mathbf D_2$ only inside a Hamiltonian implementation, joining numerical and physical operators.
- `finite_difference.Laplacian1D` derives active coordinates and BC behavior internally rather than consuming separately accepted grid, active-set, and boundary representations.
- The differentiation notebook labels sparse storage canonical and couples grid, active set, operator, and evidence before those protected choices are accepted.
- The continuous/discrete operator modules duplicate symbolic Poisson content and do not preserve their stated conceptual distinction.

## 5. Candidate bounded capability alternatives

### 5.1 Proposed mathematical boundary for human assessment

The requested candidate boundary is coherent as a bounded homogeneous-Dirichlet finite-difference foundation if humans accept all of these choices:

- a closed uniform grid on $[a,b]$ containing both endpoints;
- $N\geq3$;
- $h=(b-a)/(N-1)$;
- active indices $1,\ldots,N-2$;
- boundary data $u(a)=u(b)=0$;
- active vector dimension $N-2$;
- $\mathbf D_2=h^{-2}\operatorname{tridiag}(1,-2,1)$;
- explicit distinction between $\mathbf D_2$ and $-\mathbf D_2$; and
- exclusion of Hamiltonians, eigensolvers, PIAB, and Poisson solvers.

This intake does not accept any item in that list.

### 5.2 Contract-structure options

**Option 1 — One integrated contract.** One contract governs closed-grid coordinates, active/boundary semantics, discrete states, and the homogeneous-Dirichlet $\mathbf D_2$. This gives one learner-facing story and one integration target, but risks making a reusable grid interface depend on one BC/operator use and may conceal separable evidence obligations.

**Option 2 — Two ordered contracts.** Contract 1 governs the uniform closed grid, full samples, active indices, boundary data, restriction, and embedding. Contract 2 depends on Contract 1 and governs $\mathbf D_2$, its sign, representation, application, and numerical evidence. This makes the dependency explicit, permits grid reuse without implying a Laplacian, and isolates API/evidence decisions. It requires two human contract checkpoints and careful prevention of premature API selection.

**Option 3 — Narrower operator-focused alternative.** Define only a homogeneous-Dirichlet second-derivative constructor from explicit scalar inputs `(a,b,N)` or `(h,N_active)`, returning a matrix and documented index convention, without accepting a general public grid/state object. This reduces initial API surface but leaves current grid/active-state duplication unresolved and weakens the pedagogical library reconstruction.

### 5.3 Advisory recommendation

**Advisory recommendation: two ordered capability contracts**, beginning with a narrowly bounded grid/active/boundary representation and followed only after acceptance by a homogeneous-Dirichlet second-derivative contract. The reasons are:

- the repository already conflates at least three meanings of `Grid1D`;
- grid sampling and active-state semantics are prerequisites to interpreting matrix shape and application;
- a grid contract can be verified without choosing a matrix storage format or Laplacian sign;
- the operator contract can then cite exact accepted coordinate, active-index, and boundary semantics;
- correction or replacement of the broken Laplacian modules need not silently redefine the grid; and
- pedagogical comparison can still present the two accepted capabilities in one later notebook if humans choose Path A.

This is advice only. A human must select one integrated contract, two ordered contracts, or a narrower alternative.

## 6. Possible three-stage pedagogical artifact

No notebook path or canonical role is selected.

### Stage 1 — Explicit construction

- define $[a,b]$, $N$, and $h=(b-a)/(N-1)$;
- create full coordinates and active indices explicitly;
- record homogeneous endpoint data separately;
- sample a function on the full grid and restrict it to the active vector;
- build $h^{-2}\operatorname{tridiag}(1,-2,1)$ directly using visible NumPy/SciPy operations;
- apply the matrix and reconstruct full output only with an explicit boundary convention; and
- expose arrays, shapes, indexing, matrix entries, and sign without PhysKit calls.

### Stage 2 — Proposed PhysKit reconstruction

- construct the same domain, grid, active indices, boundary data, state, and operator through a **proposed, not accepted** library interface;
- compare full coordinates, spacing, active indices, boundary values, state and matrix shapes, matrix entries, and applied results against Stage 1; and
- state that agreement is bounded numerical/software evidence, not API acceptance or validation.

### Stage 3 — Exploration

For multiple $N$ and mode numbers $n$, use

$$
u_n(x)=\sin\!\left(\frac{n\pi(x-a)}{b-a}\right),
\qquad
u_n''(x)=-\left(\frac{n\pi}{b-a}\right)^2u_n(x).
$$

Compare the discrete and analytical second derivatives on active points; plot error versus $h$ and $n$; examine observed second-order behavior where resolved; and explain truncation and resolution degradation for larger mode number. This would not by itself establish physical or pedagogical validation.

## 7. Artifact-path applicability assessment

Artifact path remains unresolved pending a human-accepted contract.

| Path | Advisory assessment | What would be omitted or lost |
|---|---|---|
| **A — library plus notebook** | Best fit to the stated reusable and pedagogical goals, if humans accept both axes. It supports explicit construction, library reconstruction, and exploration. | Nothing expected from the proposed normal pattern, but it creates the largest implementation/evidence obligation and requires an accepted public interface and notebook role.
| **B — notebook only** | Feasible for exploration or bounded pedagogy without library extraction. | No reusable PhysKit API, source implementation, or library reconstruction; existing source fragmentation remains unresolved. Selection would not imply Candidate or any lifecycle state.
| **C — library plus notebook exception** | Feasible if a reusable interface is wanted but a notebook is unsuitable and an adequate alternative is accepted. | Loses the requested explicit/library/exploration notebook sequence and weakens direct learner comparison; an alternative must still explain the library behavior.
| **D — neither library nor notebook** | Narrowest and least aligned with the stated goals; possible only with separate accepted rationales for omitting both axes. | Loses reusable library functionality and the notebook pedagogy; leaves only an alternative representation with tightly limited claims.

**Advisory expectation: Path A**, not a selection. The human-accepted contract must independently decide `reusable_library_interface` and `notebook_artifact`.

## 8. Evidence-obligation options

These are proposals for later human disposition, not accepted applicability or criteria.

| Evidence class | Proposed applicability/options | Possible methods and limitations |
|---|---|---|
| Software verification | Likely required for any public grid or operator interface. | Constructor validation; coordinate/spacing/index invariants; dtype/shape; boundary/state compatibility; dense/sparse behavior if selected; matrix entries; application; error behavior; regression against accepted examples. Tests must follow an accepted API and cannot choose it.
| Numerical verification | Likely required because the capability makes a finite-difference accuracy claim. | Exact stencil-entry checks; manufactured sine modes; independent direct construction; convergence over accepted grids; observed order; mode-resolution studies; accepted norms and tolerances. Shared implementation errors and asymptotic-range selection remain limitations.
| Physical validation | Applicability unresolved. | If claims remain purely mathematical/numerical and make no real-system adequacy claim, humans might accept a scoped non-applicability rationale. If later used to claim adequacy for a physical model/regime, model-specific validation is required. Correct differentiation is not physical validation.
| Pedagogical validation | Likely required if a student-facing notebook is proposed for support. | Instructor review against accepted learning objectives, learner walkthrough/observation, accessibility and prerequisite review, or other accepted evaluation. Execution and visual quality are insufficient.
| Uncertainty quantification | Applicability and depth unresolved. | Potentially characterize floating-point effects, parameter/input uncertainty, or propagated uncertainty only if the accepted use makes such claims. Grid convergence and truncation-error analysis are **numerical verification/error analysis**, not automatically UQ. A deterministic exact-input demonstration may support a human rationale for limited or deferred UQ, but no automatic Not applicable label is justified.

No class is labeled Not applicable by this intake. Humans must accept applicability, methods, references, criteria, adequacy, and claim boundaries.

## 9. Human decisions required

The following decisions remain open and must not be inferred from this intake:

1. **Capability boundary:** accept the proposed foundation, revise it, choose a narrower alternative, or defer.
2. **Contract structure:** one integrated contract or two ordered contracts.
3. **State definitions:** exact continuous scalar state and full/active discrete state meanings.
4. **Closed-grid convention:** whether endpoint-inclusive uniform sampling with $h=(b-a)/(N-1)$ is the initial accepted convention.
5. **Active-DOF semantics:** whether active indices are an independent object, a grid policy, or BC-derived, and whether arbitrary active sets are in scope.
6. **Boundary-condition scope:** homogeneous Dirichlet at both endpoints only, and the exact boundary-data representation.
7. **Laplacian sign:** public meaning of $\mathbf D_2$ versus $-\mathbf D_2$ and naming that prevents confusion.
8. **Matrix representation:** dense, sparse, both, or an abstract operator; no storage choice is accepted.
9. **Public API shape:** names, constructors, properties, validation, mutability, exports, and compatibility policy.
10. **Canonical notebook role:** whether a notebook is required, its role, and later its exact path; none is selected here.
11. **Artifact path:** A, B, C, or D through separate library/notebook applicability decisions.
12. **Evidence applicability:** disposition and depth for each of the five classes, including accepted references and criteria.
13. **Exact contract path:** one path or two ordered paths, subject to Mode A review.
14. **Next authorization:** whether capability-contract drafting should be authorized after scope acceptance.

## 10. Human capability-scope checkpoint

The parent requests one of: **accept scope for contract proposal, revise, reject, or defer**. An affirmative decision must state the selected capability boundary and whether one or two contract proposals may be drafted. Contract acceptance, implementation, evidence production, notebook creation/modification, PIAB, lifecycle work, and successor work remain blocked.
