# Symmetric binary regular solution

## Model definition

Let $x$ be the mole fraction of component B in a binary mixture. The symmetric
regular-solution model uses a composition-independent molar interaction
parameter $\Omega$ and the ideal configurational entropy.

The molar enthalpy of mixing is

$$
\Delta H_{\mathrm{mix}}=\Omega x(1-x).
$$

The molar entropy of mixing is

$$
\Delta S_{\mathrm{mix}}
=-R_g\left[x\ln x+(1-x)\ln(1-x)\right].
$$

The Gibbs free energy of mixing is therefore

$$
\Delta G_{\mathrm{mix}}
=\Omega x(1-x)
+R_gT\left[x\ln x+(1-x)\ln(1-x)\right].
$$

The continuous pure-component limits at $x=0$ and $x=1$ are zero. Every mixing
quantity is invariant under exchanging the two component labels,
$x\mapsto1-x$.

## Local curvature

The second derivative of the molar Gibbs free energy is

$$
\frac{d^2\Delta G_{\mathrm{mix}}}{dx^2}
=-2\Omega+R_gT\left(\frac{1}{x}+\frac{1}{1-x}\right).
$$

At equimolar composition,

$$
\left.\frac{d^2\Delta G_{\mathrm{mix}}}{dx^2}\right|_{x=1/2}
=-2\Omega+4R_gT.
$$

Negative local curvature indicates instability with respect to infinitesimal
composition fluctuations at that composition. It does not alone determine
coexistence compositions. Those require a separate common-tangent or equivalent
chemical-potential analysis.

## Computational use

The maintained model accepts an explicit molar interaction parameter,
unitless mole fractions, absolute temperature, and requested molar-energy unit.
The [computational laboratory](../../../../../notebooks/thermal/thermo/mixtures/symmetric-regular-solution.ipynb)
checks symmetry, endpoint limits, and equimolar local curvature before plotting
enthalpy, entropy, and Gibbs contributions.

The laboratory parameters are synthetic illustrative values. The resulting
curves are not fitted material data and do not constitute scientific validation
for a real mixture.
