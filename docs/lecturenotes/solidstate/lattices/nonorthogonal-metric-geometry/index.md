# Nonorthogonal lattice metric geometry

**Prerequisite:** [Direct and reciprocal lattice bases](../direct-and-reciprocal/index.md)

This lesson develops constant metric geometry for two- and three-dimensional
Bravais-lattice bases. The basis vectors and all derived numerical arrays use
one consistent illustrative length convention. No crystal, material parameter,
or constitutive response is inferred from the examples.

## Fractional and Cartesian coordinates

Collect the linearly independent direct primitive vectors as columns of

$$
A=\begin{bmatrix}\mathbf a_1&\cdots&\mathbf a_d\end{bmatrix},
\qquad d\in\{2,3\}.
$$

A fractional-coordinate vector $\mathbf s$ maps to the Cartesian vector

$$
\mathbf r=A\mathbf s.
$$

The squared Cartesian distance between two fractional coordinates is therefore

$$
\lVert \Delta\mathbf r\rVert^2
=\Delta\mathbf s^{\mathsf T}g\,\Delta\mathbf s,
\qquad
g=A^{\mathsf T}A.
$$

The symmetric positive-definite matrix $g$ is the covariant geometric metric.
Its determinant recovers the fundamental-region measure,

$$
\Omega=\sqrt{\det g}=|\det A|.
$$

This metric records geometry only. It is not an effective-mass, strain,
dielectric, or other constitutive tensor.

## Reciprocal metric

The reciprocal primitive basis is

$$
B=2\pi A^{-\mathsf T},
\qquad
A^{\mathsf T}B=2\pi I.
$$

Consequently,

$$
B^{\mathsf T}B=(2\pi)^2g^{-1}.
$$

For an integer reciprocal mode $\mathbf n$, the plane wave
$\exp(i2\pi\mathbf n\cdot\mathbf s)$ has Cartesian reciprocal vector
$\mathbf G=B\mathbf n$ and

$$
|\mathbf G|^2
=(2\pi\mathbf n)^{\mathsf T}g^{-1}(2\pi\mathbf n).
$$

For reduced Bloch coordinates $\mathbf q$, the Cartesian Bloch vector is
$\mathbf k=B\mathbf q$. The shifted free kinetic factor becomes

$$
|\mathbf G+\mathbf k|^2
=\bigl(2\pi(\mathbf n+\mathbf q)\bigr)^{\mathsf T}
 g^{-1}
 \bigl(2\pi(\mathbf n+\mathbf q)\bigr).
$$

This identity relates fractional-coordinate and Cartesian descriptions; it does
not by itself define a Hamiltonian coefficient, particle mass, or energy unit.

## Constant-metric Laplacian

Because a Bravais-lattice basis is constant in space, the Cartesian Laplacian in
fractional coordinates is

$$
\nabla^2=g^{ij}\,\partial_i\partial_j,
$$

where $g^{ij}$ are entries of $g^{-1}$. In two dimensions,

$$
\nabla^2
=g^{11}\partial_1^2
+2g^{12}\partial_1\partial_2
+g^{22}\partial_2^2.
$$

An off-diagonal inverse-metric entry therefore produces a mixed derivative.
This constant-basis expression is not the general curvilinear
Laplace--Beltrami operator, whose metric can vary with position and whose
volume factor belongs inside a divergence.

## Nearest periodic image

Two fractional displacements that differ by an integer vector describe the same
periodic separation. The nearest image solves

$$
\mathbf n_*=
\underset{\mathbf n\in\mathbb Z^d}{\operatorname{argmin}}
\;\lVert A(\Delta\mathbf s-\mathbf n)\rVert.
$$

For an orthogonal basis this can be resolved component by component away from
half-cell ties. For a skewed basis, independently rounding each fractional
component need not minimize Cartesian distance.

`NearestLatticeImageResolver` uses componentwise rounding only to obtain an
initial Cartesian radius $r$. If $\sigma_{\min}$ is the smallest singular value
of $A$, every candidate that can improve the initial image obeys

$$
\lVert\Delta\mathbf s-\mathbf n\rVert_2
\leq \frac{r}{\sigma_{\min}}.
$$

The resulting integer bounding box is finite and complete, so the resolver does
not depend on an assumed nearest-neighbor shell. Very ill-conditioned bases can
produce a large box and correspondingly higher runtime.

## Interpretation and limitations

The metric, reciprocal basis, and nearest-image calculation are exact statements
about one represented constant basis up to floating-point rounding. The package
requires the metric and its inverse to remain finite in binary64. The examples
are not a convergence study, do not select a physical unit, and do not establish
a real material, an effective-mass model, scientific validation, uncertainty
quantification, or pedagogical validation.

The [computational laboratory](../../../../../notebooks/solidstate/lattices/nonorthogonal-metric-geometry.ipynb)
checks the 2D and 3D identities, displays a skew-cell nearest-image example, and
compares metric and Cartesian Bloch kinetic factors.

## Exercises

1. Show that the metric is diagonal when the direct basis is orthogonal.
2. Derive $B^{\mathsf T}B=(2\pi)^2g^{-1}$ from the duality relation.
3. Find a skew two-dimensional basis for which componentwise fractional
   rounding does not return the nearest Cartesian image.
4. Starting from $\mathbf r=A\mathbf s$, derive the constant-metric Laplacian.
5. Explain why replacing a geometric metric by an effective-mass tensor would
   change the physical model rather than merely the coordinates.
6. Estimate how the smallest singular value affects the candidate count of an
   exact nearest-image search.

## References

- N. W. Ashcroft and N. D. Mermin, *Solid State Physics*, Holt, Rinehart and
  Winston (1976), chapters 4--8.
- M. P. Marder, *Condensed Matter Physics*, 2nd ed., Wiley (2010), chapters
  3--4.
