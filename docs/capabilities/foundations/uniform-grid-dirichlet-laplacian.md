# Uniform-grid homogeneous-Dirichlet 1D Laplacian capability contract

**Status:** Human-accepted capability contract

**Task:** `FOUNDATIONS-FD1`

**Contract revision:** 3

**Accepted source revision:** `5766b281bfea890cc522cf651f36bd93c0493cbb`

**Accepted artifact path:** Path A — library plus notebook

## 1. Authority, preflight, and acceptance status

This is the sole material contract path assigned to the capability architect by the human-authorized `FOUNDATIONS-FD1` instance of `PHYSKIT-CAPABILITY-DEVELOPMENT`. Startup preflight reconciled `AGENTS.md`, `.pi/active-state.json` state revision 15, `.pi/tasks/foundations-fd1.md`, the reusable chain template, repository `https://github.com/eragasa/physkit`, branch `main`, starting revision `1ce0e53afe435cba8551875166ff5fc34bd68945`, `origin`, the complete working tree, the HC02 REMAND, exact ownership, prohibited paths, evidence obligations, the stop condition, and denial of successor authorization. The unrelated untracked `package-lock.json` was not inspected.

The human explicitly accepted contract revision 3 exactly as represented at `5766b281bfea890cc522cf651f36bd93c0493cbb`. Acceptance covers the integrated Path A boundary, public names and APIs, mathematical and numerical conventions, criteria and tolerances, documentation and notebook requirements, M1 clean-surface direction, and all five evidence dispositions. It does not authorize implementation, source or test changes, evidence production or acceptance, Sphinx or notebook creation or execution, adapters, migration, legacy repair, lifecycle or support status, PIAB, or successor work.

The accepted general `LinearOperator.domain -> object` and `LinearOperator.codomain -> object` annotations are a minimal typing boundary for this capability only. They establish no general PhysKit state-space hierarchy. `FiniteDifferenceLaplacian1D` must narrow both properties to `HomogeneousDirichletStateSpace1D`; any general state-space abstraction, protocol, generic type system, or composition framework requires a separate future contract.

Observed repository facts remain those in `docs/harness/physkit.capability.01-uniform-grid-laplacian-intake.md`: competing grid and operator representations exist; the closest sparse Laplacian is inconsistent with committed imports and grid attributes; and a differentiation notebook imports an absent class. Those facts do not select a survivor. The read-only technical reference `eragasa/ksdft2effmass@355df16a7ca4071b70bc844a00ba21949af7c7c6` informs only proportional documentation, exception semantics, Sphinx organization, synchronization, and VVUQ distinctions.

## 2. Learner purpose, audience, and intended use

This accepted capability contract serves learners and instructors in introductory computational physics and PhysKit developers needing a small, inspectable finite-difference foundation. A learner should be able to:

1. distinguish an interval, immutable grid geometry, a homogeneous-Dirichlet state space, active degrees of freedom, a discrete state, and an operator matrix;
2. derive the centered three-point second-derivative stencil;
3. inspect its sparse and dense forms and its sign;
4. apply the same operator to owned real or complex active states; and
5. measure consistency and observed second-order convergence without confusing numerical verification with physical validation or uncertainty quantification.

Intended use is deterministic teaching, examples, small inspections, and reuse as a numerical building block. It is not assurance that a later physical model is adequate.

## 3. Integrated discrete-first boundary

The capability is one integrated but internally layered contract: immutable closed uniform-grid geometry; a separate immutable homogeneous-Dirichlet state space containing that grid; a general linear-operator interface and discrete one-dimensional specialization with explicit domain and codomain; and a centered finite-difference representation of $+d^2/dx^2$.

The following remain distinct: the continuous target $D_2:u\mapsto u''$ with domain $H^2(a,b)\cap H_0^1(a,b)$ and codomain $L^2(a,b)$; grid coordinates; the active state; prescribed zero endpoints; the approximation rule; its CSR matrix; the software operator; an independent analytical oracle; and any later physical operator. The continuous statement explains the target for smooth references but creates no continuous or symbolic public API.

## 4. Physical-model boundary, assumptions, and claim limits

No physical system is modeled. Coordinates may be dimensional or dimensionless but use one caller-owned length convention. State values may be real or complex and retain caller-owned meaning. If coordinates carry length, operator output carries state-value per length squared.

Assumptions are a finite interval, uniform spacing, both endpoints included, exactly homogeneous Dirichlet endpoint values, and sufficient smoothness only for truncation or convergence claims. Excluded claims include Hamiltonian adequacy, experimental observables, material systems, nonsmooth continuum fidelity, high-frequency resolution, and physical validation.

## 5. Exact mathematics and numerical representation

Let

$$
[a,b]\subset\mathbb R,\quad b>a,\quad N\in\mathbb Z,\quad N\ge 3,
$$

$$
h=\frac{b-a}{N-1},\qquad x_i=a+ih,\quad i=0,\ldots,N-1,
$$

and

$$
\mathcal I_A=\{1,\ldots,N-2\},\qquad \mathbf x_A=(x_i)_{i\in\mathcal I_A}.
$$

The state-space convention is

$$
u_0=u(a)=0,\qquad u_{N-1}=u(b)=0,\qquad
V_h=\mathbb F^{N-2},\quad \mathbb F\in\{\mathbb R,\mathbb C\}.
$$

For a full sampled vector $\mathbf v=(v_0,\ldots,v_{N-1})^{\mathsf T}$ and an active vector $\mathbf u_A=(u_1,\ldots,u_{N-2})^{\mathsf T}$, restriction and embedding are exactly

$$
R_h\mathbf v=(v_1,\ldots,v_{N-2})^{\mathsf T},
$$

$$
E_h\mathbf u_A=(0,u_1,\ldots,u_{N-2},0)^{\mathsf T}.
$$

Restriction is a projection and therefore does not validate or alter the discarded endpoint entries. Embedding supplies exact zeros. The discrete operator is

$$
\mathbf D_{2,h}=\frac{1}{h^2}\operatorname{tridiag}(1,-2,1)
\in\mathbb R^{(N-2)\times(N-2)},
$$

with

$$
(\mathbf D_{2,h}\mathbf u_A)_i
=\frac{u_{i-1}-2u_i+u_{i+1}}{h^2},\qquad i\in\mathcal I_A,
$$

where omitted endpoint terms are zero. The continuous second-derivative target is

$$
D_2u=\frac{d^2u}{dx^2}=u''.
$$

The sign is $+d^2/dx^2$: the matrix is real symmetric negative definite. For sufficient smoothness, the local truncation error is $O(h^2)$.

On a general interval $[a,b]$, the sine reference family and its exact second derivative are

$$
u_n(x)=\sin\!\left(\frac{n\pi(x-a)}{b-a}\right),\qquad
u_n''(x)=-\left(\frac{n\pi}{b-a}\right)^2u_n(x),\qquad n\in\{1,2\}.
$$

The verification criteria then specialize this family to $[a,b]=[0,1]$, where $u_n(x)=\sin(n\pi x)$ and $u_n''(x)=-(n\pi)^2u_n(x)$.

For an active vector $\mathbf v$, define the exact weighted discrete norm, relative error, and observed order by

$$
\|\mathbf v\|_{2,h}=\left(h\sum_{i=1}^{N-2}|v_i|^2\right)^{1/2},
$$

$$
e_{n,N}=
\frac{\|\mathbf D_{2,h}\mathbf u_{n,A}-\mathbf u''_{n,A}\|_{2,h}}
{\|\mathbf u''_{n,A}\|_{2,h}},
$$

$$
p_{n;N_c,N_f}=
\frac{\log\!\left(e_{n,N_c}/e_{n,N_f}\right)}
{\log\!\left(h_{N_c}/h_{N_f}\right)},
\qquad h_N=\frac{1}{N-1}.
$$

The bounded claim uses $N=17,33,65,129$: $e_{n,N}$ must decrease monotonically on every refinement, and the accepted final-refinement orders are explicitly $p_{n;33,65}$ and $p_{n;65,129}$, each in $[1.90,2.10]$ for $n=1,2$. This claim is limited to these modes, interval, grids, norm, binary64 behavior, and boundary convention.

## 6. Architecture and semantic identity

The hierarchy remains:

```text
LinearOperator
└── DiscreteLinearOperator1D
    └── FiniteDifferenceLaplacian1D
```

`UniformGrid1D` is geometry only. `HomogeneousDirichletStateSpace1D` contains a grid and owns the boundary, active-index, active-coordinate, dimension, restriction, embedding, and real/complex vector-interpretation semantics. General `LinearOperator` owns immutable semantic state-space metadata for its domain and codomain, without requiring those state spaces to use homogeneous-Dirichlet semantics; it also owns shape, dtype, application, and scalar scaling. No additional public general state-space class is accepted. `DiscreteLinearOperator1D` adds the canonical finite matrix. This capability's concrete `FiniteDifferenceLaplacian1D` is constructed from one `HomogeneousDirichletStateSpace1D` and returns that same immutable concrete state space as both domain and codomain.

A state space's canonical semantic identity is the exact value tuple

```text
(
  "HomogeneousDirichletStateSpace1D",
  ("UniformGrid1D", float(a), float(b), int(num_points), "closed-endpoint-inclusive"),
  "active-interior-indices-1-through-N-minus-2",
  ("homogeneous-dirichlet", 0.0, 0.0),
  "real-or-complex-active-vectors",
)
```

It therefore includes grid geometry, endpoint inclusion, active-index convention, homogeneous boundary convention, and admitted real/complex interpretation. Domain/codomain compatibility is exact equality of this semantic identity, not object identity, shape alone, or approximate coordinate equality. This identity is representation compatibility, not cross-grid physical equivalence.

All accepted grid, state-space, operator, and scaled-operator objects are observably immutable after successful construction: their public properties do not permit reassignment; returned arrays and matrices do not alias mutable internal storage; and behavior cannot change through caller-held inputs. This is a behavioral requirement and does **not** prescribe a frozen dataclass or any particular implementation mechanism.

## 7. Accepted modules, public imports, and exact APIs

The accepted public imports are:

```python
from physkit.discretization import UniformGrid1D, HomogeneousDirichletStateSpace1D
from physkit.operators import (
    LinearOperator,
    DiscreteLinearOperator1D,
    FiniteDifferenceLaplacian1D,
)
```

Accepted defining modules are `physkit.discretization.grid_1d`, `physkit.discretization.state_space_1d`, `physkit.operators.base`, `physkit.operators.discrete_1d`, and `physkit.operators.finite_difference_1d`. Package `__init__.py` files must re-export exactly these names.

```python
class UniformGrid1D:
    def __init__(self, a: Real, b: Real, num_points: Integral) -> None: ...

    @property
    def a(self) -> float: ...
    @property
    def b(self) -> float: ...
    @property
    def num_points(self) -> int: ...
    @property
    def length(self) -> float: ...
    @property
    def spacing(self) -> float: ...
    @property
    def coordinates(self) -> numpy.ndarray: ...


class HomogeneousDirichletStateSpace1D:
    def __init__(self, grid: UniformGrid1D) -> None: ...

    @property
    def grid(self) -> UniformGrid1D: ...
    @property
    def boundary_values(self) -> tuple[float, float]: ...
    @property
    def active_indices(self) -> numpy.ndarray: ...
    @property
    def active_coordinates(self) -> numpy.ndarray: ...
    @property
    def dimension(self) -> int: ...
    @property
    def semantic_identity(self) -> tuple: ...

    def restrict(self, full_state: ArrayLike) -> numpy.ndarray: ...
    def embed(self, active_state: ArrayLike) -> numpy.ndarray: ...


class LinearOperator(abc.ABC):
    @property
    @abc.abstractmethod
    def domain(self) -> object: ...
    @property
    @abc.abstractmethod
    def codomain(self) -> object: ...
    @property
    @abc.abstractmethod
    def shape(self) -> tuple[int, int]: ...
    @property
    @abc.abstractmethod
    def dtype(self) -> numpy.dtype: ...

    @abc.abstractmethod
    def apply(self, state: ArrayLike) -> numpy.ndarray: ...

    def __matmul__(self, state: ArrayLike) -> numpy.ndarray: ...
    def scaled(self, factor: Number) -> LinearOperator: ...


class DiscreteLinearOperator1D(LinearOperator, abc.ABC):
    @property
    @abc.abstractmethod
    def matrix(self) -> scipy.sparse.csr_matrix: ...

    def to_dense(self) -> numpy.ndarray: ...


class FiniteDifferenceLaplacian1D(DiscreteLinearOperator1D):
    def __init__(self, state_space: HomogeneousDirichletStateSpace1D) -> None: ...

    @property
    def domain(self) -> HomogeneousDirichletStateSpace1D: ...
    @property
    def codomain(self) -> HomogeneousDirichletStateSpace1D: ...
```

At the general `LinearOperator` level, the `object` annotation deliberately avoids introducing another public state-space base class. The returned `domain` and `codomain` objects nevertheless contractually represent observably immutable semantic state-space metadata suitable for exact compatibility decisions; they are not merely shapes or grids. The concrete Laplacian annotations narrow both properties to `HomogeneousDirichletStateSpace1D`. These exact modules, signatures, properties, and names are accepted contract requirements.

## 8. Construction, ownership, dtype, and exceptions

`UniformGrid1D` validates finite non-Boolean Python/NumPy real `a,b`, finite `b>a`, and non-Boolean Python/NumPy integral `num_points>=3`; it stores built-in `float`, `float`, and `int`. It owns only geometry. `coordinates` returns a defensive C-contiguous `float64` copy. It has no boundary, active-index, restriction, or embedding API.

`HomogeneousDirichletStateSpace1D` requires a `UniformGrid1D`; its grid is immutable, its boundaries are `(0.0,0.0)`, its active indices are exactly `np.arange(1,N-1)`, its active coordinates are the corresponding grid coordinates, and `dimension == N-2`. Array properties return defensive copies (`float64` coordinates and platform-integer indices).

`restrict` requires a finite, numeric, one-dimensional vector of shape `(N,)`; `embed` requires shape `(N-2,)`. Both reject Boolean, object, string, ragged, nonfinite, and wrong-rank inputs. Both return new owned C-contiguous `float64` arrays for real inputs and `complex128` arrays for complex inputs. Neither mutates nor retains caller storage. `restrict` discards endpoints without requiring zero; `embed` inserts exact zeros of the result dtype.

`FiniteDifferenceLaplacian1D` eagerly validates its state space and builds exactly one owned canonical `float64` CSR matrix. `domain is state_space` and `codomain is state_space` are permitted, but public compatibility depends on semantic identity; `shape == (state_space.dimension,state_space.dimension)` and `dtype == np.dtype(np.float64)`. `matrix` returns a defensive CSR copy with no reachable retained storage. `to_dense()` returns a new owned C-contiguous `float64` array. `apply` and `@` require a valid domain active vector and return a new owned C-contiguous `float64` result for real input or `complex128` result for complex input. The real stencil acts independently on real and imaginary parts; no conjugation or wavefunction meaning is introduced.

`scaled` accepts one finite non-Boolean Python/NumPy real or complex scalar. It eagerly canonicalizes the factor to built-in `float` or `complex`, retains only a private reference to the immutable operand, freezes `shape` and `dtype`, and stores no applied state. The result preserves the operand's exact `domain` and `codomain`; its semantic compatibility is unchanged. Its dtype is `np.result_type(operand.dtype,factor)`, constrained here to `float64` or `complex128`, and application returns a new owned array of `np.result_type(wrapper.dtype,canonical_state.dtype)`.

Wrong semantic types raise `TypeError`; correctly typed values violating invariants raise `ValueError`. No silent conversion of numeric strings, clipping, reshaping, boundary correction, real truncation, coordinate remapping, approximate identity, or recovery is allowed. Hashing, serialization, mutable updates, and custom public exceptions are not accepted.

## 9. Canonical CSR and the $N=3$ edge case

The eager matrix has one construction rule:

```python
M = state_space.dimension
h = state_space.grid.spacing
main = -2.0 * np.ones(M, dtype=np.float64)
diagonals = [main]
offsets = [0]
if M > 1:
    off = np.ones(M - 1, dtype=np.float64)
    diagonals.extend((off, off))
    offsets.extend((-1, 1))
D2 = scipy.sparse.diags(diagonals, offsets, shape=(M, M), format="csr")
D2 /= h**2
D2.sum_duplicates()
D2.sort_indices()
D2.eliminate_zeros()
```

For $N=3$, $M=1$ and the exact result is the `1 x 1` CSR matrix $[-2/h^2]`; no invalid off-diagonal is created. The retained matrix has sorted indices and no explicit zeros. Dense form is derived only from retained CSR. Public sparse and dense forms are defensive copies.

## 10. Scaling retained; composition deferred

Scalar scaling is part of the accepted initial public API and must preserve exact domain and codomain as specified above. A future quantum kinetic-energy operator could use or scale a `FiniteDifferenceLaplacian1D` by $-\hbar^2/(2m)$; it must not inherit from the Laplacian.

There is **no public `compose` method in the initial API**, no composed-wrapper public name, and no initial composition acceptance criterion, test requirement, evidence claim, or notebook requirement. General operator composition is informative future work only. A later contract may propose domain/codomain compatibility and application ordering without retroactively changing this API. `QuantumKineticEnergy1D`, masses, $\hbar$, units, Hamiltonians, eigensolvers, and all related evidence remain deferred.

## 11. Equation authority and source documentation

Every maintained first-party accepted module must have a NumPy-style module docstring stating purpose; represented objects; mathematical/numerical scope; assumptions; invariants; sign, endpoint, boundary, dtype, shape, ownership, and exception conventions; exclusions; neighboring-module relationships; and separate VVUQ claim boundaries. Every public class, property, and method must document applicable `Parameters`, `Attributes`, `Returns`, `Raises`, `Notes`, `Examples`, and `See Also`. Nontrivial private numerical policy receives concise responsibility/invariant comments.

After implementation, `docs/concepts/uniform-grid-dirichlet-laplacian.md` is the maintained pedagogical equation surface. It must store these exact ten equation categories as ten distinct equations under ten stable, unique MyST labels, using the exact Section 5 formulas:

1. `(ugdl-grid-spacing)` — grid spacing $h=(b-a)/(N-1)$;
2. `(ugdl-uniform-coordinates)` — uniform coordinates $x_i=a+ih$;
3. `(ugdl-homogeneous-dirichlet-active-state-space)` — homogeneous-Dirichlet active state space, including zero endpoints and $V_h=\mathbb F^{N-2}$;
4. `(ugdl-continuous-second-derivative)` — continuous second derivative $D_2u=u''$;
5. `(ugdl-centered-stencil)` — centered componentwise stencil action;
6. `(ugdl-matrix-representation)` — tridiagonal matrix representation $\mathbf D_{2,h}$;
7. `(ugdl-sine-reference-family)` — general-interval sine reference family and analytical derivative;
8. `(ugdl-weighted-norm)` — weighted discrete norm $\|\cdot\|_{2,h}$;
9. `(ugdl-relative-numerical-error)` — relative numerical error $e_{n,N}$; and
10. `(ugdl-observed-convergence-order)` — observed convergence order $p_{n;N_c,N_f}$.

The interval constraint, active-index/coordinate, restriction, and embedding formulas remain ordinary mathematics but are not substitutes for or additions to these ten required labeled categories. A stable label immediately precedes each MyST `math` directive, for example `(ugdl-grid-spacing)=` followed by `````{math}```. Each required category has its own directive and label; relative error and observed order are not combined. Labels are unique repository-wide and are referenced rather than duplicated where possible. Source docstrings remain authoritative for API behavior; the concept page is authoritative for maintained pedagogical equation presentation; the canonical notebook synchronizes the same symbols/formulas and cites the concept labels; neither surface invents API behavior. Changes to any formula require synchronized source docstrings, concept page, notebook, and applicable tests under the accepted contract.

The initial capability explicitly rejects `EquationSpecification`, `EquationSpec`, any runtime equation registry, equation-decorator infrastructure, class-level LaTeX metadata, a custom equation renderer, a symbolic equation catalog, and tests that compare LaTeX strings. Programmatic equation infrastructure is deferred to a separately scoped human decision. Stable MyST labels and ordinary documentation references are sufficient here.

## 12. MyST/Sphinx documentation and diagram contract

Later implementation is required at exactly these Markdown documentation surfaces, with no parallel RST pages:

- `docs/index.md`;
- `docs/api/operators.md`;
- `docs/concepts/uniform-grid-dirichlet-laplacian.md`;
- `docs/conf.py`; and
- `docs/_static/diagrams/uniform-grid-dirichlet-laplacian.dot`.

The optional documentation dependencies are Sphinx (`sphinx>=8,<10`) and MyST Parser (`myst-parser>=5.1,<6`). `docs/conf.py` must use exactly:

```python
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.graphviz",
]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
root_doc = "index"
myst_enable_extensions = ["dollarmath"]
napoleon_google_docstring = False
napoleon_numpy_docstring = True
exclude_patterns = ["_build"]
```

It must not mock public imports, suppress import warnings, or commit `_build` output. Supporting both configured suffixes does not authorize parallel duplicate RST and Markdown pages: each maintained API or concept subject has one source page, and the pages required by this contract are the Markdown paths above. `docs/index.md` uses a MyST `{toctree}` containing `api/operators` and `concepts/uniform-grid-dirichlet-laplacian`. `docs/api/operators.md` uses MyST `{automodule}`/`{autoclass}` directives and this generated inheritance directive:

````markdown
```{inheritance-diagram} physkit.operators.LinearOperator physkit.operators.DiscreteLinearOperator1D physkit.operators.FiniteDifferenceLaplacian1D
:parts: 1
```
````

The concept page embeds source-controlled DOT with valid MyST syntax:

````markdown
```{graphviz} ../_static/diagrams/uniform-grid-dirichlet-laplacian.dot
```
````

The required build is exactly:

```text
sphinx-build -W --keep-going -b html docs docs/_build/html
```

The accepted package must be installed and importable. Graph rendering requires the Graphviz `dot` executable on `PATH`; Sphinx does not provide it. Missing public imports, MyST warnings, duplicate labels, invalid directives, or missing `dot` fail the warnings-as-errors build.

The conceptual DOT must be valid Graphviz and show:

- `HomogeneousDirichletStateSpace1D` **contains** `UniformGrid1D`;
- operators **act between** labeled `domain` and `codomain` state-space roles;
- solid hollow-triangle inheritance only for `FiniteDifferenceLaplacian1D -> DiscreteLinearOperator1D -> LinearOperator`;
- an internal scaled-operator node with a labeled filled-diamond containment edge to its operand and the same domain/codomain;
- a dashed-box deferred `QuantumKineticEnergy1D` with a dashed `uses/scales` edge to `FiniteDifferenceLaplacian1D`, never inheritance;
- distinct styles and a legend for inheritance, containment, domain/codomain association, and deferred use; and
- a note that implemented Python classes and source docstrings are authoritative.

The generated inheritance diagram and source-controlled conceptual diagram are distinct surfaces. Rendered Graphviz products are not committed.

## 13. Exact accepted criteria

The human accepted the following criteria as contract obligations:

1. Public imports and exact APIs in Section 7 match, including geometry/state-space separation and absence of public composition.
2. Observable immutability, scalar/vector validation, semantic identity, restriction/embed behavior, ownership, exceptions, domain/codomain, and dtype behavior match Sections 6–8.
3. For $N=3,4,8$, CSR shape/format/canonicalization and every dense entry equal an independent direct tridiagonal oracle; $N=3$ is exactly $[-2/h^2]$ and the sign is $+d^2/dx^2$.
4. Real and complex applications equal an independent stencil using `np.testing.assert_allclose` with `rtol=5e-14` and `atol=5e-14 * max(1, ||reference||_inf)`.
5. For the general-interval sine family specialized to $u_n=\sin(n\pi x)$, $n=1,2$, on $[0,1]$ with $N=17,33,65,129$, the Section 5 relative weighted-$L_2$ errors $e_{n,N}$ decrease on every refinement and $p_{n;33,65}$ and $p_{n;65,129}$ each lie in `[1.90, 2.10]`.
6. Real and complex scaling agrees with explicit scalar multiplication under criterion 4 and preserves exact domain and codomain. No composition or kinetic-energy acceptance/test requirement exists.
7. The three notebook stages in Section 14 execute cleanly, contain no saved error output, use the ten exact equations, and Stage 2 matches Stage 1 under criterion 4. Execution is not pedagogical acceptance.
8. Source, tests, Markdown API/concept pages, stable equation labels, diagrams, and notebook agree; the exact Sphinx build passes with public imports and `dot` resolved; no parallel RST page or equation infrastructure exists.
9. All five evidence records contain every Section 16 field, and required or unresolved evidence truthfully blocks handoff as specified.
10. Fresh independent read-only Mode A review has no unresolved material finding; parent verification establishes readiness only, never contract or evidence acceptance.

## 14. Exact three-stage canonical-notebook requirement

`notebooks/numerics/differentiation/uniform-grid-dirichlet-laplacian.ipynb` is the accepted required canonical notebook path.

**Stage 1 — explicit construction without PhysKit.** Define $[a,b]$, $N$, $h$, full coordinates, a separate explicit homogeneous-Dirichlet state-space construction, active indices/coordinates, dimension, zero boundaries, exact restriction and embedding, and real/complex ownership. Construct eager CSR from the visible single diagonal rule, inspect defensive dense form, apply the positive-second-derivative stencil to real and complex vectors, show $N=3$, and use the exact ten labeled concept-page equations without runtime equation machinery.

**Stage 2 — reconstruction with the accepted PhysKit API.** Recreate exactly Stage 1 with both `UniformGrid1D` and `HomogeneousDirichletStateSpace1D`, then construct `FiniteDifferenceLaplacian1D(state_space)`. Compare geometry, state-space semantic identity, active data, restriction/embed results, domain/codomain, CSR/dense matrices, real/complex applications, and scaled-domain/codomain preservation under the accepted criteria. This stage begins only after accepted API implementation. It does not compose operators.

**Stage 3 — exploration.** First state the general-interval family $u_n(x)=\sin(n\pi(x-a)/(b-a))$ and $u_n''=-(n\pi/(b-a))^2u_n$, then specialize to $[0,1]$. Evaluate $n=1,2$ for $N=17,33,65,129`; compute the exact weighted norm, relative errors $e_{n,N}$, and observed-order formula $p_{n;N_c,N_f}$; demonstrate monotonic errors and explicitly report $(33,65)$ and $(65,129)$ orders; plot error against $h$; illustrate higher-mode under-resolution outside the acceptance family; and distinguish truncation from resolution. It states that this is numerical verification/error analysis, not physical validation, pedagogical acceptance, or UQ.

## 15. Independent applicability axes and Path A

The HC01 decision separately selected:

- `reusable_library_interface: required` — the capability is intended as a reusable discrete foundation and future scaling seam, not only an inline demonstration;
- `notebook_artifact: required` — the learning objectives require visible explicit construction, accepted-library reconstruction, and exploration.

Neither axis determines the other. Their one consistent selection is **Path A — library plus notebook**. No omitted axis, omission rationale, or alternative artifact applies. Path A assigns no lifecycle state, canonical acceptance, support claim, or implementation authorization.

## 16. Five-class evidence dispositions

Every row is an accepted obligation or disposition; all observed outcomes remain `not-run`.

| Evidence class | Applicability / accepted non-applicability rationale | Required claim | Producer / responsible role | Exact artifact or evidence-summary path when written | Method / reference | Human-accepted criterion or unresolved criterion | Reviewer | Result state | Observed outcome | Limitations and claim boundary | Unresolved blocks final handoff? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Software verification | Required for the public interface | Implementation conforms to accepted geometry/state-space separation, API, invariants, errors, copies, CSR, real/complex behavior, domain/codomain, and scaling | `physkit.physkit-verification` | `tests/physkit/discretization/test_uniform_grid_1d.py`, `tests/physkit/discretization/test_homogeneous_dirichlet_state_space_1d.py`, `tests/physkit/operators/test_linear_operator.py`, `tests/physkit/operators/test_finite_difference_laplacian_1d.py`; summary `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | Independent arrays; public imports; Sections 6–13 | Accepted criteria 1–4 and 6 | `physkit.physkit-capability-integration-reviewer` | `required-incomplete` | `not-run` | Contract conformance only; no physical/pedagogical adequacy; composition excluded | Yes |
| Numerical verification | Required for approximation/convergence claims | Stencil implements $D_{2,h}$ and meets the bounded second-order claim | `physkit.physkit-verification` | `tests/physkit/operators/test_finite_difference_laplacian_1d.py`; same summary | Direct tridiagonal oracle; exact sine family, weighted norm, relative error, refinement pairs; Sections 5 and 13 | Accepted criteria 3–5 | `physkit.physkit-capability-integration-reviewer` | `required-incomplete` | `not-run` | Limited to accepted interval, modes, grids, norm, binary64, and homogeneous boundaries; not physical validation | Yes |
| Physical validation | `not-applicable-human-accepted-rationale`: no physical-model adequacy claim exists | Only that no physical-validation conclusion is claimed | `physkit.physkit-verification` records the accepted applicability disposition | `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | Sections 4–5 and VVUQ boundary | Human-accepted Not applicable rationale | `physkit.physkit-capability-integration-reviewer` | `not-applicable-human-accepted-rationale` | `not-run` | Any later physical use needs model-specific validation; numerical agreement cannot fill this class | No |
| Pedagogical validation | Required, proportional to one foundational notebook | Human checklist confirms the accepted distinctions/objectives are exposed correctly without material ambiguity | `physkit.physkit-notebook-documentation` prepares material; `physkit.physkit-verification` records; human assesses/accepts | Section 14 notebook; same summary | Human checklist against Section 2, exact three stages, equations, and synchronization; no formal learner study required | Accepted criterion: every objective and stage is correctly explained and no material misconception/accessibility blocker remains; evidence outcome and acceptance remain pending | `physkit.physkit-capability-integration-reviewer`, then human | `required-incomplete` | `not-run` | Checklist does not establish broad educational effectiveness; execution is insufficient | Yes |
| Uncertainty quantification | `not-applicable-human-accepted-rationale`: deterministic exact inputs and no uncertainty distribution/interval claim | Only that no UQ conclusion is claimed | `physkit.physkit-verification` records the accepted applicability disposition | `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | Sections 4–5; absence of uncertainty propagation | Human-accepted Not applicable rationale | `physkit.physkit-capability-integration-reviewer` | `not-applicable-human-accepted-rationale` | `not-run` | Truncation error, convergence, resolution loss, and floating-point behavior remain numerical verification, not UQ | No |

Humans own applicability, criteria, adequacy, physical/pedagogical validation conclusions, and acceptance. Missing, failed, deferred, difficult, unavailable, or unreviewed evidence is not Not applicable.

## 17. Ten-step lightweight VVUQ and synchronization profile

The proportional sequence remains:

1. human-accepted capability contract;
2. bounded implementation with synchronized source docstrings;
3. relevant software-verification tests;
4. relevant numerical-verification tests;
5. MyST/Sphinx API/concept documentation and class diagrams;
6. explicit/library/exploration notebook;
7. one consolidated independent integration review;
8. at most one consolidated deterministic correction pass;
9. parent verification; and
10. human final acceptance.

This wording requires MyST Markdown documentation, not parallel RST pages. It requires no imported external control-plane ceremony, extra checkpoints for deterministic details, new agents/chains/skills/schemas, evidence IDs, checksum catalogs, separate evidence stores, class-per-file test rules, formal learner studies, physical evidence for unmade claims, or UQ evidence for no uncertainty claim. Ordinary tests need clear assertions, not ceremonial per-test evidence records.

## 18. Migration boundary, exclusions, and remaining decisions

Existing paths remain untouched observations. After acceptance, alternatives for a separate decision are: M1, a new clean surface implementing Section 7 while leaving competing representations untouched; M2, separately authorized thin adapters; or M3, later replacement/deprecation only after inventory and compatibility evidence. M1 remains the recommendation because it least conflates semantics, but no migration, adapter, warning, repair, deletion, relocation, or replacement is authorized.

Excluded are nonuniform/multidimensional grids; arbitrary active sets; inhomogeneous Dirichlet, Neumann, Robin, periodic, or ghost rules; higher-order stencils; finite elements; symbolic production support; equation registries/specifications/renderers/catalogs/LaTeX-string tests; general public composition; Poisson solvers; potentials; Hamiltonians; `QuantumKineticEnergy1D`; eigensolvers; PIAB; units/conversion; serialization; GPU/distributed/HPC behavior; performance claims; lifecycle/support/deprecation decisions; and competing-code repair or migration.

The external reference contributes technical documentation and proportional VVUQ distinctions only; PhysKit rejects its harness/CPN model, campaign controls, schemas, persistence, serialization, Rust, HPC, class-per-file, evidence-ID, checksum, ownership-manifest, skill, chain, and agent ceremony.

No protected contract choice remains unresolved for ownership and implementation planning. Evidence outcomes and adequacy, physical- and pedagogical-validation conclusions, lifecycle or support status, migration or repair authorization, PIAB, and successors remain outside this acceptance boundary.

**Implementation gate:** contract acceptance permits only the recorded HC02 resolution and the exact ownership and implementation plan. No production, verification, evidence, notebook, Markdown/Sphinx, dependency, packaging, or CI writer stage begins without separate authorization after plan completion. Adapters, repairs, migrations, lifecycle work, PIAB, and successors remain unauthorized. Successor authorization is `false`.
