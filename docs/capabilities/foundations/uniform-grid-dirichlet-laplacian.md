# Uniform-grid homogeneous-Dirichlet 1D Laplacian capability contract

**Status:** Proposed for human review

**Task:** `FOUNDATIONS-FD1`

**Contract revision:** 2 (corrected proposal; no accepted contract revision exists)

**Artifact path proposal:** Path A — library plus notebook

## 1. Authority, proposal status, and observed facts

This is the sole material contract proposal authorized by the human-accepted `FOUNDATIONS-FD1-HC01` scope. Every public name, signature, criterion, artifact role, and evidence disposition below is a **proposal pending explicit human contract acceptance**. This document does not implement, accept, validate, canonicalize, support, or assign a lifecycle state to the capability.

Observed repository facts at drafting start are recorded in the accepted intake, `docs/harness/physkit.capability.01-uniform-grid-laplacian-intake.md`: PhysKit has competing grid and operator representations; its closest sparse Laplacian implementation is inconsistent with committed imports and grid attributes; and its differentiation notebook imports an absent class. Those observations do not select a survivor.

The read-only technical reference `eragasa/ksdft2effmass@355df16a7ca4071b70bc844a00ba21949af7c7c6` informs only proportional source documentation, exception semantics, Sphinx organization, synchronization, and VVUQ distinctions. Section 25 explicitly rejects its unrelated ceremony.

## 2. Learner purpose, audience, and intended use

The proposed capability is for learners and instructors in introductory computational physics and for PhysKit developers who need a small, inspectable finite-difference foundation. A learner should be able to:

1. distinguish a continuous interval, a closed coordinate grid, prescribed boundary values, active degrees of freedom, a discrete state, and an operator matrix;
2. derive the centered three-point second-derivative stencil;
3. inspect its sparse and dense matrix representations and sign;
4. apply the same operator to real- or complex-valued active states; and
5. measure consistency and observed second-order convergence without confusing numerical verification with physical validation or UQ.

Intended use is deterministic teaching, examples, small inspections, and reuse as a numerical building block. It is not an assurance that any later physical model is adequate.

## 3. Integrated discrete-first capability boundary

The proposal is one integrated but internally layered capability:

1. a uniform closed one-dimensional grid;
2. homogeneous-Dirichlet active-state semantics;
3. a general linear-operator interface and one-dimensional discrete specialization; and
4. a centered finite-difference representation of $d^2/dx^2$.

“Discrete-first” means that the public contract is owned by finite coordinates, vectors, and matrices. A continuous differential expression explains the approximation but does not create a symbolic production API. The following objects are distinct and must be named distinctly in source, tests, Sphinx, and the notebook:

1. the continuous differential operator $D_2:u\mapsto u''$ with domain $H^2(a,b)\cap H_0^1(a,b)$ and codomain $L^2(a,b)$;
2. the closed coordinate grid $(x_0,\ldots,x_{N-1})$;
3. the active discrete state $\mathbf u_A\in\mathbb F^{N-2}$;
4. the prescribed boundary data $u(a)=u(b)=0$, which are not active state components;
5. the centered finite-difference approximation rule for $D_2$;
6. the represented matrix $\mathbf D_{2,h}$ produced by that rule;
7. the software class `FiniteDifferenceLaplacian1D` that owns the representation and application contract;
8. an analytical reference such as the sine-mode second derivative used only as an independent numerical-verification oracle; and
9. a later physical operator such as quantum kinetic energy, which gives a model-specific meaning to a scaled $\mathbf D_{2,h}$.

The continuous domain/codomain statement identifies the mathematical target for smooth reference functions; it does not add a continuous or symbolic public API. Grid and active-state layers remain conceptually distinct inside this one contract.

## 4. Physical-model boundary, assumptions, and claim limit

No physical system is modeled. The interval coordinate may be dimensional or dimensionless, but all coordinates must use one consistent, caller-owned length convention. State values may be real or complex and carry caller-owned meaning. Boundary values are exactly zero. If coordinates carry length, operator output carries state-value per length squared.

The capability assumes a finite interval, uniform spacing, endpoint inclusion, exact homogeneous Dirichlet data, and a sufficiently smooth sampled function only when a truncation-error or convergence statement is made. It makes no claim about Hamiltonians, material systems, experimental observables, continuum-domain fidelity for nonsmooth functions, or high-frequency resolution.

## 5. Mathematical domain, grid, and symbols

Let

$$
[a,b]\subset\mathbb R,\qquad b>a,\qquad N\in\mathbb Z,\quad N\geq3,
$$

with

$$
h=\frac{b-a}{N-1},\qquad x_i=a+ih,\quad i=0,\ldots,N-1.
$$

The full coordinate vector is $\mathbf x=(x_0,\ldots,x_{N-1})$. The active index set and active coordinates are

$$
\mathcal I_A=\{1,\ldots,N-2\},\qquad \mathbf x_A=(x_i)_{i\in\mathcal I_A}.
$$

The endpoints are not active unknowns. This proposal admits no nonuniform, half-open, midpoint, periodic, Neumann, Robin, or arbitrary-active-set convention.

## 6. Boundary and discrete-state semantics

The boundary constraint is

$$
u_0=u(a)=0,\qquad u_{N-1}=u(b)=0.
$$

For $\mathbb F\in\{\mathbb R,\mathbb C\}$, the active state space is

$$
V_h=\mathbb F^{N-2},\qquad
\mathbf u_A=(u_1,\ldots,u_{N-2})^{\mathsf T}.
$$

Restriction maps a full $N$-component sampled vector to components $1{:}N-1$. Embedding maps an active vector to an $N$-component vector by inserting exact zeros at both endpoints. Coordinates, boundary data, full sampled values, and active state values are separate objects even if a convenience method relates them.

## 7. Mathematical operator and sign convention

The discrete operator is

$$
\mathbf D_{2,h}=\frac{1}{h^2}
\operatorname{tridiag}(1,-2,1)\in\mathbb R^{(N-2)\times(N-2)}.
$$

For active index $i$, omitted endpoint terms are zero because of the homogeneous Dirichlet constraint:

$$
(\mathbf D_{2,h}\mathbf u_A)_i
=\frac{u_{i-1}-2u_i+u_{i+1}}{h^2}.
$$

`FiniteDifferenceLaplacian1D` means $+d^2/dx^2$, not $-d^2/dx^2$. Thus $\mathbf D_{2,h}$ is real symmetric and negative definite, with negative eigenvalues. No method or alias named “negative Laplacian” is included.

## 8. Approximation and numerical claim

For a function with sufficient local smoothness, the centered stencil has local truncation error $O(h^2)$ at resolved interior points. The bounded numerical claim is: for fixed resolved sine modes on the specified grid sequence, the active discrete result converges to the analytical second derivative with observed order approximately two under the criteria in Section 21.

This is not a blanket accuracy guarantee. Error depends on smoothness, mode resolution, norm, grid range, and floating-point effects. Convergence is numerical verification, not physical validation or UQ.

## 9. Required architecture and dependency direction

The proposed public hierarchy is equivalent in meaning to:

```text
LinearOperator
└── DiscreteLinearOperator1D
    └── FiniteDifferenceLaplacian1D
```

Dependency direction is general to specific. `LinearOperator` owns shape, scalar dtype, application, scaling, and composition semantics. `DiscreteLinearOperator1D` adds the one-dimensional uniform grid and canonical finite matrix representation. `FiniteDifferenceLaplacian1D` owns only the accepted stencil and homogeneous-Dirichlet meaning.

A continuous or symbolic operator must not be a superclass that determines this API.

## 10. Proposed modules and public import surface

The supported public import surface is proposed as:

```python
from physkit.discretization import UniformGrid1D
from physkit.operators import (
    LinearOperator,
    DiscreteLinearOperator1D,
    FiniteDifferenceLaplacian1D,
)
```

Proposed defining modules are:

- `physkit.discretization.grid_1d.UniformGrid1D`;
- `physkit.operators.base.LinearOperator`;
- `physkit.operators.discrete_1d.DiscreteLinearOperator1D`; and
- `physkit.operators.finite_difference_1d.FiniteDifferenceLaplacian1D`.

Package `__init__.py` files re-export exactly those public names. These paths do not authorize files to be created and do not accept an API until a human accepts this contract.

## 11. Proposed `UniformGrid1D` API

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
    @property
    def active_indices(self) -> numpy.ndarray: ...
    @property
    def active_coordinates(self) -> numpy.ndarray: ...
    @property
    def num_active(self) -> int: ...
    @property
    def boundary_values(self) -> tuple[float, float]: ...

    def restrict(self, full_state: ArrayLike) -> numpy.ndarray: ...
    def embed(self, active_state: ArrayLike) -> numpy.ndarray: ...
```

`a` and `b` accept finite Python/NumPy real scalars except Booleans and are stored as built-in `float`. `num_points` accepts Python/NumPy integer scalars except Booleans and is stored as built-in `int`. Arrays returned by coordinate/index properties are defensive copies with `float64`/platform integer dtype. `boundary_values` is always `(0.0, 0.0)`.

`restrict` requires a finite one-dimensional numeric vector of shape `(num_points,)`; `embed` requires shape `(num_active,)`. Both reject Boolean, object, string, ragged, nonfinite, and wrong-rank inputs. They return owned C-contiguous `float64` for real input and `complex128` for complex input. `restrict` does not require the caller's full boundary entries to be zero because it performs a projection only; `embed` supplies the accepted zero boundary convention.

## 12. Proposed operator APIs and exact signatures

```python
class LinearOperator(abc.ABC):
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
    def compose(self, other: LinearOperator) -> LinearOperator: ...


class DiscreteLinearOperator1D(LinearOperator, abc.ABC):
    @property
    @abc.abstractmethod
    def grid(self) -> UniformGrid1D: ...

    @property
    @abc.abstractmethod
    def matrix(self) -> scipy.sparse.csr_matrix: ...

    def to_dense(self) -> numpy.ndarray: ...


class FiniteDifferenceLaplacian1D(DiscreteLinearOperator1D):
    def __init__(self, grid: UniformGrid1D) -> None: ...
```

All operator instances in this contract are immutable after construction. Construction is eager. `FiniteDifferenceLaplacian1D.__init__` validates the grid, builds one owned canonical `float64` CSR matrix, canonicalizes its indices, removes explicit zeros, and retains that internal matrix for the object's lifetime; no property access or first application triggers matrix construction. `grid` is the supplied validated, immutable grid, `shape == (grid.num_active, grid.num_active)`, and `dtype == np.dtype(np.float64)`. `matrix` returns a defensive CSR copy whose data/index mutations cannot reach the retained matrix. `to_dense()` derives and returns a new owned C-contiguous `float64` dense array on every call. `apply` and `@` never mutate or retain the caller's state and return a new owned C-contiguous array: `float64` for real input and `complex128` for complex input.

`scaled` accepts one finite non-Boolean Python/NumPy real or complex scalar. Wrapper construction is eager: it validates and canonicalizes the factor, computes and freezes `shape` and `dtype`, and retains a private reference to the immutable operand; it does not defer validation or cache an applied state. A real factor is canonicalized to built-in `float`, a complex factor to built-in `complex`. The scaled wrapper's `dtype` is `np.result_type(operand.dtype, factor)`, constrained by this contract to `float64` or `complex128`; any complex factor yields `complex128`. It privately propagates the operand's semantic grid key when one exists. Application returns a new owned C-contiguous array with `np.result_type(wrapper.dtype, canonical_state.dtype)`, likewise `float64` or `complex128`, and never exposes or mutates operand storage.

`compose` requires another `LinearOperator` and compatible inner dimensions. Its wrapper is also constructed eagerly: it validates compatibility, freezes result `shape == (self.shape[0], other.shape[1])` and `dtype == np.result_type(self.dtype, other.dtype)`, and privately retains references to the two immutable operands. It stores no caller state and no lazily materialized product matrix; each application evaluates `self.apply(other.apply(state))` and returns a new owned C-contiguous `float64` or `complex128` result according to `np.result_type(wrapper.dtype, canonical_state.dtype)`. Returned wrapper implementations satisfy `LinearOperator` but are not additional public names in this contract.

For `A.compose(B)`, shape compatibility is necessary. A `DiscreteLinearOperator1D`, and a scaled wrapper derived from it, carries the private canonical semantic key `(grid.a, grid.b, grid.num_points)`, using stored built-in `float`, `float`, and `int` values. If both operands carry semantic grid keys, exact key equality is additionally required; the composed wrapper retains that common key. Same shape on different intervals is rejected with `ValueError`; object identity is irrelevant. Composition for which either operand has no grid metadata uses shape compatibility only and produces no grid-key claim. Application order is `A.compose(B).apply(u) == A.apply(B.apply(u))`.

## 13. Canonical CSR representation and one stencil rule

SciPy CSR is the proposed canonical computational representation. `FiniteDifferenceLaplacian1D` must eagerly construct its canonical matrix exactly once from this one diagonal stencil rule:

```python
M = grid.num_active
main = -2.0 * np.ones(M, dtype=np.float64)
diagonals = [main]
offsets = [0]
if M > 1:
    off = np.ones(M - 1, dtype=np.float64)
    diagonals.extend((off, off))
    offsets.extend((-1, 1))
D2 = scipy.sparse.diags(diagonals, offsets, shape=(M, M), format="csr")
D2 /= grid.spacing**2
D2.sum_duplicates()
D2.sort_indices()
D2.eliminate_zeros()
```

where $M=N-2$. For the required edge case $N=3$, $M=1$: the conditional adds no off-diagonal arrays or invalid offsets and the result is exactly the `1 x 1` CSR matrix $[-2/h^2]$. For $M>1$, the same rule adds the two unit off-diagonals. This is the single stencil source of truth. Dense data must be derived from the retained CSR by `to_dense()`; CSR must not be derived from a separately maintained dense table or loop. Public CSR values are defensive copies with canonical sorted indices and no explicit stored zeros.

## 14. Real and complex state behavior

The grid and matrix are real. Applying the operator to a real active state produces real `float64`; applying it to a complex active state applies the same real stencil independently to real and imaginary parts and produces `complex128`. The class performs no conjugation and does not reinterpret a vector as a wavefunction. Complex support is an algebraic state-space behavior, not a quantum-mechanical claim.

## 15. Invariants, mutability, and equality boundary

Required invariants are:

- finite `a`, `b`, and `b > a`;
- integer `num_points >= 3`;
- endpoint-inclusive spacing and coordinates;
- active indices exactly `np.arange(1, N - 1)`;
- exact zero endpoint embedding;
- square matrix dimension `N-2`;
- entries exactly determined by Section 13 in binary64 arithmetic;
- symmetry, strictly negative diagonal, nonnegative off-diagonal entries, and negative definiteness; and
- no mutation of caller inputs or internal canonical matrix through returned arrays.

Object identity is not a public compatibility rule. Discrete composition uses both shape and exact equality of the canonical semantic grid key `(a, b, num_points)` defined in Section 12; general nondiscrete composition uses shape. This key is representation compatibility, not cross-grid physical equivalence. The contract does not define hashing, serialization, approximate equality, coordinate remapping, or a mutable update protocol.

## 16. Exception taxonomy

Wrong semantic types raise `TypeError`; correctly typed values that violate an invariant raise `ValueError`.

`TypeError` covers Booleans used as numbers, numeric strings, wrong grid/operator classes, nonnumeric vectors, object arrays, and invalid scalar families. `ValueError` covers nonfinite scalars or vector entries, `b <= a`, `num_points < 3`, wrong vector rank or shape, nonfinite scale factors, incompatible composition dimensions, and unequal semantic grid keys for two discrete operands. No silent numeric-string conversion, clipping, reshaping, boundary correction, dtype-to-real truncation, grid remapping, or recovery is permitted. No new public exception class is proposed because the failure states need no structured payload.

## 17. Composition seam and deferred `QuantumKineticEnergy1D`

A future quantum kinetic-energy operator would represent

$$
\mathbf T_h=-\frac{\hbar^2}{2m}\mathbf D_{2,h}.
$$

It must use `FiniteDifferenceLaplacian1D` through `scaled` or contained composition; it must **not** inherit from `FiniteDifferenceLaplacian1D`, because kinetic energy is a scaled physical operator, not a specialized second derivative. `QuantumKineticEnergy1D`, masses, $\hbar$, units, Hamiltonians, eigensolvers, and their evidence are deferred and not accepted here. The seam is verified only as generic scaling/composition behavior.

## 18. Symbolic deferral

SymPy expressions, symbolic differentiation, continuous operator-domain objects, symbolic-to-discrete conversion, and Poisson semantics are excluded. A future symbolic capability may describe $d^2/dx^2$ but must not retroactively determine or silently change this discrete API. Any bridge requires a separate human-accepted contract and compatibility decision.

## 19. Complete NumPy source-documentation standard

Every maintained first-party module proposed here must have a module docstring stating purpose; represented mathematical objects and equations; numerical and dtype/shape scope; assumptions, invariants, sign and boundary conventions; exclusions; neighboring-module relationships; and separate software-, numerical-, physical-validation-, pedagogical-, and UQ claim boundaries where applicable.

Every public class, property, and method must have complete NumPy-style documentation using `Parameters`, `Attributes`, `Returns`, `Raises`, `Notes`, `Examples`, and `See Also` when relevant. It must define symbols, dimensions, coordinate/state roles, units or caller-owned unit conventions, input scalar families, canonicalization, copy/mutability behavior, real/complex behavior, exceptions, and non-goals. Nontrivial private numerical policy and meaningful local state require concise comments explaining responsibility and invariants; mechanical helpers must not receive repetitive prose.

The stencil documentation must state the equation, boundary treatment, shape, dtype, CSR construction, failure modes, second-order scope, and sign. Source docstrings, tests, Sphinx pages, and notebook statements must agree wherever they cover the same contract. Source docstrings own detailed API behavior; Sphinx pages explain and link rather than invent behavior.

## 20. Minimal Sphinx, API/concept pages, and two diagram surfaces

Implementation is proposed later, not authorized now, at exactly these documentation surfaces:

- `docs/conf.py`: minimal configuration listing only `sphinx.ext.autodoc`, `sphinx.ext.napoleon`, `sphinx.ext.inheritance_diagram`, and `sphinx.ext.graphviz`; NumPy docstrings enabled; `exclude_patterns = ["_build"]`; no MyST extension because every Sphinx source proposed here is RST; no mocked public imports or suppressed import warnings;
- `docs/index.rst`: minimal toctree containing the API and concept pages;
- `docs/api/operators.rst`: `automodule`/`autoclass` API surface using the public imports and this exact generated diagram directive:

  ```rst
  .. inheritance-diagram:: physkit.operators.LinearOperator physkit.operators.DiscreteLinearOperator1D physkit.operators.FiniteDifferenceLaplacian1D
     :parts: 1
  ```

- `docs/concepts/uniform-grid-dirichlet-laplacian.rst`: RST mathematical, numerical, sign, boundary, real/complex, composition, and claim-boundary explanation, embedding the conceptual DOT source with `.. graphviz:: ../_static/diagrams/uniform-grid-dirichlet-laplacian.dot`;
- `docs/_static/diagrams/uniform-grid-dirichlet-laplacian.dot`: source-controlled **class-relationship**, not data-flow, diagram. It must use solid hollow-triangle arrows exclusively for `FiniteDifferenceLaplacian1D -> DiscreteLinearOperator1D -> LinearOperator` inheritance; labeled diamond/containment edges from visibly internal scaled/composed wrapper nodes to their `LinearOperator` operands for scaling/composition; and a visibly deferred, dashed-box `QuantumKineticEnergy1D` with a dashed `uses/scales` relation to `FiniteDifferenceLaplacian1D`, never an inheritance edge. A legend must distinguish all three relationship styles.

These are the two distinct diagram surfaces: a generated `inheritance-diagram` and a source-controlled conceptual Sphinx Graphviz class-relationship diagram. The implemented Python classes and their source docstrings are authoritative; generated or conceptual diagrams explain them and must not override them. Generated `docs/_build/` files and rendered Graphviz products must not be committed.

The optional documentation dependency proposal is `sphinx>=8,<10`; MyST is not required. Graph rendering additionally requires the Graphviz `dot` executable as a documented system dependency available on `PATH`; the Python Sphinx dependency does not supply it. The exact required build is:

```text
sphinx-build -W --keep-going -b html docs docs/_build/html
```

The accepted package must be installed/importable in the build environment. With `-W`, no mocked imports, and no suppressed import warnings, any public-module import failure is fatal. The implementation plan must add only the optional documentation dependency and system-requirement documentation needed by this accepted configuration.

## 21. Explicit proposed acceptance criteria

All criteria remain pending human acceptance with this contract:

1. Public imports and every signature/property/method in Sections 10–12 match exactly.
2. Constructor, scalar-family, vector shape/dtype/finiteness, exception, copy, and nonmutation behavior match Sections 11, 15, and 16.
3. For `N = 3, 4, 8`, CSR shape, format, sorted indices, lack of explicit zeros, and every dense entry equal an independent direct tridiagonal construction; the sign is $d^2/dx^2$.
4. Real and complex applications equal independent stencil application using `np.testing.assert_allclose` with `rtol=5e-14` and `atol=5e-14 * max(1, ||reference||_inf)`.
5. For sine modes $n=1,2$ and `N = 17, 33, 65, 129` on `[0,1]`, the relative discrete $L_2$ error against $u_n''=-(n\pi)^2u_n$ decreases on every refinement and each successive observed order from the last three grids lies in `[1.90, 2.10]`.
6. Scaling and composition agree with explicit sequential application under criterion 4; no kinetic-energy subclass is introduced.
7. The three notebook stages satisfy Section 22, execute from a clean environment, contain no saved error output, and Stage 2 matches Stage 1 under criterion 4. Execution alone is not pedagogical acceptance.
8. Source, tests, Sphinx API/concept pages, diagrams, and notebook use the same sign, shapes, names, and claim boundaries; `sphinx-build -W --keep-going -b html docs docs/_build/html` passes with public imports resolved and Graphviz `dot` available.
9. All five evidence records contain every field in Section 24, and required evidence is truthfully completed or blocks final handoff.
10. Fresh independent read-only integration review reports no unresolved material finding; parent verification may establish readiness only, not acceptance or validation.

## 22. Exact three-stage canonical-notebook proposal

`notebooks/numerics/differentiation/uniform-grid-dirichlet-laplacian.ipynb` is proposed as the required canonical notebook path, pending human contract acceptance and later evidence acceptance.

**Stage 1 — explicit construction without PhysKit.** Define `[a,b]`, `N`, `h`, full coordinates, active indices, zero boundary data, full-to-active restriction, and active-to-full embedding. Construct CSR directly from the visible three diagonals, inspect its dense form, apply it to real and complex vectors, and state the sign and shapes.

**Stage 2 — reconstruction with the accepted PhysKit API.** Recreate exactly the Stage 1 grid, state, matrix, dense inspection, restriction/embedding, and real/complex application using `UniformGrid1D` and `FiniteDifferenceLaplacian1D`. Compare coordinates, indices, matrix entries, and results using criterion 4. This stage may begin only after accepted API implementation.

**Stage 3 — exploration.** For sine modes $n=1,2$ and the accepted grid sequence, compare against the analytical second derivative, plot error versus $h$, calculate observed order, show degradation when a higher mode is under-resolved, and explain truncation versus resolution. It must state that these results are numerical verification/error analysis, not physical validation, pedagogical acceptance, or UQ.

## 23. Independent applicability axes and Path A

The human HC01 scope separately selected these proposed contract values:

- `reusable_library_interface: required` — rationale: the capability is intended as a reusable discrete foundation and future composition seam, not only an inline demonstration;
- `notebook_artifact: required` — rationale: the learning objectives require visible explicit construction, library reconstruction, and exploration.

The axes are independent; neither rationale determines the other. Their only consistent selection is **Path A — library plus notebook**. No omission rationale or alternative artifact applies. Path A assigns no lifecycle state, canonical acceptance, support claim, or implementation authorization.

## 24. Five-class evidence-disposition table

Every row is a proposed obligation. `Result state` and `Observed outcome` describe the contract-drafting state, not an evidence conclusion.

| Evidence class | Applicability / proposed non-applicability rationale | Required claim | Producer / responsible role | Exact artifact or evidence-summary path when written | Method / reference | Human-accepted criterion or unresolved criterion | Reviewer | Result state | Observed outcome | Limitations and claim boundary | Unresolved blocks final handoff? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Software verification | Required for the public interface | Implementation satisfies accepted API, invariants, errors, copies, formats, real/complex, scaling, and composition | `physkit.physkit-verification` | Tests under `tests/physkit/discretization/test_uniform_grid_1d.py`, `tests/physkit/operators/test_linear_operator.py`, and `tests/physkit/operators/test_finite_difference_laplacian_1d.py`; summary `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | Independent expected arrays; public-import tests; Sections 10–16 and 21 | Unresolved until human accepts criteria 1–4 and 6 | `physkit.physkit-capability-integration-reviewer` | `required-incomplete` | `not-run` | Shows contract conformance only; no physical or pedagogical adequacy | Yes |
| Numerical verification | Required for approximation and convergence claims | Stencil implements $D_{2,h}$ and exhibits bounded second-order convergence for specified resolved modes | `physkit.physkit-verification` | `tests/physkit/operators/test_finite_difference_laplacian_1d.py`; same verification summary | Direct tridiagonal oracle; manufactured sine modes; refinement and observed order; Section 21 | Unresolved until human accepts criteria 3–5 | `physkit.physkit-capability-integration-reviewer` | `required-incomplete` | `not-run` | Limited to accepted interval, modes, grids, norms, binary64, and homogeneous Dirichlet scope; not physical validation | Yes |
| Physical validation | Proposed `not-applicable-human-accepted-rationale`: no physical-model adequacy claim is made | Only that no physical-validation conclusion is claimed within this mathematical/numerical capability | `physkit.physkit-verification` records disposition; human accepts applicability | `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | Contract Sections 4 and 8; VVUQ classification boundary | Unresolved human acceptance of non-applicability rationale | `physkit.physkit-capability-integration-reviewer` | `unresolved-blocking` | `not-run` | Any later physical intended use requires separate model-specific validation; numerical agreement cannot fill this class | Yes |
| Pedagogical validation | Required, proportional to one foundational notebook | A proportional human checklist review confirms that the notebook correctly exposes the accepted distinctions and learning objectives without material ambiguity | `physkit.physkit-notebook-documentation` prepares notebook/checklist material; `physkit.physkit-verification` records disposition; human performs and accepts the pedagogical review | Notebook in Section 22; assessment summary in `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | Human checklist against Section 2 and the three-stage structure; no formal learner study or walkthrough required | Proposed criterion: human checklist confirms every objective is correctly explained, all three stages are identifiable and correctly interpreted, and no material misconception or accessibility blocker remains; human acceptance unresolved | `physkit.physkit-capability-integration-reviewer`, then human evidence decision | `required-incomplete` | `not-run` | A proportional checklist review does not establish broad educational effectiveness; execution is insufficient | Yes |
| Uncertainty quantification | Proposed `not-applicable-human-accepted-rationale`: exact deterministic inputs and no uncertainty-bearing interval/distribution claim | Only that no UQ conclusion is claimed | `physkit.physkit-verification` records disposition; human accepts applicability | `docs/verification/foundations-uniform-grid-dirichlet-laplacian.md` | Contract Sections 4 and 8; declared absence of uncertainty sources/propagation claims | Unresolved human acceptance of non-applicability rationale | `physkit.physkit-capability-integration-reviewer` | `unresolved-blocking` | `not-run` | Truncation/convergence and deterministic tolerances remain numerical verification, not UQ; later uncertainty claims require a new obligation | Yes |

Humans own applicability, criteria, adequacy, and validation conclusions. Missing, failed, deferred, or unreviewed evidence cannot be relabeled Not applicable.

## 25. Ten-step lightweight VVUQ and synchronization profile

The human-selected proportional execution profile is reproduced in its exact sequence:

1. accepted capability contract;
2. bounded implementation with synchronized source docstrings;
3. relevant software-verification tests;
4. relevant numerical-verification tests;
5. Sphinx API/concept documentation and class diagrams;
6. explicit/library/exploration notebook;
7. one consolidated independent integration review;
8. at most one consolidated deterministic correction pass;
9. parent verification; and
10. human final acceptance.

No additional human checkpoints are required for deterministic implementation details or contract-consistent corrections. This profile does not require new agents, chains, skills, schemas, evidence IDs, checksum catalogs, separate evidence stores, task-ownership manifests beyond the existing task record, one test class per file, one writer per class, repeated review rounds, formal learner studies, physical-validation evidence for unmade claims, or UQ evidence when no uncertainty-bearing claim is made.

This is deliberately lightweight. Ordinary unit tests need clear assertions, not per-test ceremonial evidence records. The proportional human pedagogical checklist review in Section 24 is required, but a formal learner study or walkthrough is not. Retained summary evidence is proportional to the capability claims.

## 26. Explicit rejection of imported external ceremony

The external reference contributes technical documentation, exceptions, Sphinx, synchronization, and proportional VVUQ distinctions only. PhysKit explicitly does **not** import its harness or CPN model; checkpoint, evidence-ID, checksum-catalog, task-ownership-manifest, skill, chain, or agent machinery; serialization or Rust requirements; class-per-file rules; campaign controls; HPC/resource ceremony; workflow base classes; or its project-specific schemas and persistence policies.

No external convention overrides PhysKit authority. No checksum, stable evidence identifier, separate test class per file, Rust mirror, serialized record, campaign ledger, or HPC execution is required by this contract.

## 27. Competing implementations and migration proposals

Existing paths remain observations, not authorized repair targets. After contract acceptance, the implementation plan may present these alternatives for a separate human compatibility decision:

- **Proposal M1, new clean surface:** implement the Section 10 modules and exports; leave all competing legacy representations untouched and document that they are outside this capability.
- **Proposal M2, adapter migration:** implement the accepted surface, then separately authorize thin adapters from compatible legacy grid/Laplacian callers while retaining accepted semantics and emitting no deprecation by default.
- **Proposal M3, later replacement:** after consumer inventory and compatibility evidence, separately propose replacement, deprecation, or removal of specific legacy surfaces.

This contract recommends M1 as the least conflating implementation route, but does not authorize it, migration, adapters, import repair, deprecation warnings, deletion, relocation, or behavioral repair. Current notebooks and QM consumers do not inherit the proposed contract or support status.

## 28. Exclusions, unresolved human decisions, and implementation gate

Excluded are nonuniform or multidimensional grids; arbitrary active sets; inhomogeneous Dirichlet, Neumann, Robin, periodic, or ghost-point rules; higher-order stencils; finite elements; symbolic production support; Poisson solvers; potentials; Hamiltonians; `QuantumKineticEnergy1D`; eigensolvers; PIAB; physical units/conversion; serialization; GPU/distributed/HPC behavior; performance claims; lifecycle/support/deprecation decisions; and repair or migration of competing code.

Unresolved protected decisions are exactly the human disposition of this complete proposal: accept, revise, reject, or defer the proposed public API, criteria/tolerances, Path A artifact roles, documentation surfaces, migration recommendation boundary, and all five evidence dispositions (especially physical-validation and UQ non-applicability rationales). No listed proposal is accepted by its presence here.

**Implementation gate:** stop at `human_contract_acceptance`. Production source, tests/evidence, notebook, Sphinx files, dependencies, packaging, CI, adapters, repairs, and migrations remain unauthorized until explicit human acceptance of this contract and a revised exact ownership and implementation plan. Review, validation, commitment, push, or apparent completeness is not contract acceptance. No successor is authorized.
