# Von Mises equivalent stress

## Purpose and scope

This note introduces the formulas used by the
[von Mises computational laboratory](../../../../notebooks/mechanics/continuum-mechanics/von-mises-equivalent-stress.ipynb).
Von Mises equivalent stress is a scalar derived from a symmetric Cauchy stress
tensor.

All tensor entries must use one consistent caller-owned stress unit. The
calculated equivalent stress uses that same unit.

## Symmetric stress convention

For numerical input $\boldsymbol{\sigma}$, the package evaluators preserve the
source notebooks' convention of averaging transposed off-diagonal entries:

$$
\tau_{ij}=\frac{\sigma_{ij}+\sigma_{ji}}{2},
\qquad i\ne j.
$$

This deterministic symmetrization is not a tolerance-based compatibility test.
A caller needing rejection of materially asymmetric input must perform that
separate assessment before evaluation.

## Plane stress

Under plane stress, out-of-plane normal and shear stresses are zero. For
in-plane components $\sigma_{xx}$, $\sigma_{yy}$, and $\tau_{xy}$,

$$
\sigma_{\mathrm{vM}}=
\sqrt{
\sigma_{xx}^2-\sigma_{xx}\sigma_{yy}+\sigma_{yy}^2
+3\tau_{xy}^2
}.
$$

`PlaneStressVonMisesEvaluator` accepts the represented $2\times2$ in-plane
matrix and applies this formula.

## Three-dimensional stress

For a three-dimensional symmetric stress tensor,

$$
\sigma_{\mathrm{vM}}=
\sqrt{
\frac{1}{2}\left[
(\sigma_{xx}-\sigma_{yy})^2
+(\sigma_{yy}-\sigma_{zz})^2
+(\sigma_{zz}-\sigma_{xx})^2
\right]
+3\left(\tau_{xy}^2+\tau_{yz}^2+\tau_{xz}^2\right)
}.
$$

`ThreeDimensionalVonMisesStressEvaluator` accepts the represented $3\times3$
matrix and applies this formula after pairwise off-diagonal averaging.

## Limiting cases

- Uniaxial stress of magnitude $s$ gives $\sigma_{\mathrm{vM}}=|s|$.
- Pure shear $\tau$ gives $\sigma_{\mathrm{vM}}=\sqrt{3}|\tau|$.
- Three-dimensional hydrostatic stress $p\mathbf I$ gives
  $\sigma_{\mathrm{vM}}=0$ because its deviatoric component vanishes.
- A plane-stress tensor gives the same result when embedded into a $3\times3$
  tensor with zero out-of-plane components.

## Verification

The package tests verify these algebraic cases and the documented numerical
contract using synthetic tensors.

## Exercises

1. Derive the plane-stress equation from the three-dimensional equation by
   setting out-of-plane components to zero.
2. Show that adding hydrostatic stress leaves the three-dimensional equivalent
   stress unchanged.
3. Compare deterministic symmetrization with a policy that rejects asymmetric
   tensors above a declared tolerance.
