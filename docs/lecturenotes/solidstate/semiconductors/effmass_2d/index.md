# Periodic primitive-cell free particle in two dimensions

This two-dimensional model is a methodological review surface for a future
three-dimensional primitive-cell implementation. It tests the geometry, units,
reciprocal indexing, effective-mass convention, Bloch phase, and normalization
that the three-dimensional model will require. It does not represent a
hard-wall particle in a box and does not reproduce an electronic-structure
calculation.

## Metal-unit convention

The maintained laboratory uses the project's `UnitSystem.METAL` convention:

- direct lengths in angstrom;
- particle masses in dalton;
- time in picosecond;
- action in electron-volt picosecond; and
- energy in electron-volt.

These units are practical rather than algebraically coherent. The evaluator
therefore converts the represented compound unit
$$(\mathrm{eV\,ps})^2/(\mathrm{Da\,\mathring A}^2)$$
to electron-volts explicitly. It must not treat the numerical magnitudes as if
that conversion factor were one.

## Direct and reciprocal geometry

Let the columns of $A$ be two physical primitive vectors. Fractional and
Cartesian positions satisfy

$$
\mathbf r=A\boldsymbol\xi.
$$

The reciprocal-basis matrix is

$$
B=2\pi A^{-\mathsf T},
\qquad
A^{\mathsf T}B=2\pi I.
$$

For reciprocal index $\mathbf n\in\mathbb Z^2$ and Cartesian Bloch vector
$\mathbf k$, the represented wave vector is

$$
\mathbf q_{\mathbf n}=\mathbf k+B\mathbf n.
$$

## Cartesian effective mass

The effective-mass tensor $M$ is symmetric positive definite and is expressed
in the Cartesian frame. The mode energy is

$$
E_{\mathbf n}(\mathbf k)
=
\frac{\hbar^2}{2}
\mathbf q_{\mathbf n}^{\mathsf T}M^{-1}\mathbf q_{\mathbf n}.
$$

A simultaneous Cartesian rotation of $A$, $M$, and $\mathbf k$ must leave the
energy invariant. This is a numerical-verification requirement and a review
point for the future three-dimensional implementation.

## Normalized Bloch plane waves

For cell area $\Omega=|\det A|$, the sampled modes are

$$
\psi_{\mathbf n\mathbf k}(\mathbf r)
=
\Omega^{-1/2}\exp(i\mathbf q_{\mathbf n}\cdot\mathbf r).
$$

They obey

$$
\int_\Omega |\psi|^2\,d^2r=1
$$

and the primitive-translation condition

$$
\psi(\mathbf r+\mathbf a_j)
=
\exp(i\mathbf k\cdot\mathbf a_j)\psi(\mathbf r).
$$

The reciprocal contribution produces an integer multiple of $2\pi$ and does
not change the translation phase.

## Evidence boundary

The exact reciprocal model provides software and numerical-verification
oracles for primitive-cell geometry. It is not DFT, does not replace Quantum
ESPRESSO, and does not establish a material-specific band structure. Values in
the laboratory are illustrative unless separately identified as calculated or
literature evidence.

The corresponding
[computational laboratory](../../../../../notebooks/solidstate/semiconductors/effmass_2d/primitive-cell-methodological-review.ipynb)
reviews which conventions can transfer directly to three dimensions and which
must acquire explicit volume, tensor, and indexing tests.
