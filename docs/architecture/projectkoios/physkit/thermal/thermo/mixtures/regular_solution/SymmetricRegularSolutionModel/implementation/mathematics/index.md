# Mathematics

For component-B mole fraction $x$, interaction parameter $\Omega$, absolute
temperature $T$, and molar gas constant $R_g$, the implementation evaluates

$$
\Delta H_{\mathrm{mix}}=\Omega x(1-x),
$$

$$
\Delta S_{\mathrm{mix}}=-R_g[x\ln x+(1-x)\ln(1-x)],
$$

and $\Delta G_{\mathrm{mix}}=\Delta H_{\mathrm{mix}}-T\Delta S_{\mathrm{mix}}$.
The endpoint limits are evaluated as zero without taking $\ln 0$.

The maintained [lecture note](../../../../../../../../../../lecture-notes/thermodynamics/mixtures/symmetric-regular-solution/index.md)
discusses symmetry, local curvature, and the boundary between mixing curves and
phase-coexistence analysis.

## Navigation

- [Implementation](../index.md)
