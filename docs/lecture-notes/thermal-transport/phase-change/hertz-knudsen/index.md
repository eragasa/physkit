# Planar Hertz–Knudsen flux from a three-dimensional gas

## Model and dimensional setting

The maintained model describes a three-dimensional dilute ideal gas incident on
a two-dimensional planar interface. Let the interface normal point along the
$z$ axis. Molecular velocity is
$\mathbf{v}=(v_x,v_y,v_z)\in\mathbb{R}^3$.

At mass $m$ and absolute temperature $T$, the normalized three-dimensional
Maxwell velocity density is

$$
f(\mathbf{v})
=\left(\frac{m}{2\pi k_BT}\right)^{3/2}
\exp\!\left[-\frac{m(v_x^2+v_y^2+v_z^2)}{2k_BT}\right].
$$

## One-way number flux

For gas number density $n$, the number of particles crossing unit interface area
per unit time in the positive normal direction is the positive half-space
velocity moment

$$
J_+
=n\int_{v_z>0}v_z f(\mathbf{v})\,d^3v.
$$

Because the Maxwell density factorizes, the two tangential integrals satisfy

$$
\int_{-\infty}^{\infty}f_x(v_x)\,dv_x
=
\int_{-\infty}^{\infty}f_y(v_y)\,dv_y
=1.
$$

They do not disappear physically; their normalization reduces the remaining
calculation to the positive normal-velocity integral

$$
J_+
=n\int_0^\infty v_z
\sqrt{\frac{m}{2\pi k_BT}}
\exp\!\left(-\frac{mv_z^2}{2k_BT}\right)dv_z.
$$

Evaluating the Gaussian moment gives

$$
J_+=n\sqrt{\frac{k_BT}{2\pi m}}.
$$

Using the ideal-gas relation $P=nk_BT$ yields

$$
\boxed{J_+=\frac{P}{\sqrt{2\pi m k_BT}}}.
$$

The result has dimensions of particles per area per time. A one- or
two-dimensional gas would have different state-space normalization and is not
represented by this model.

## Separate evaporation and condensation

Let $P_{\mathrm{eq}}$ be equilibrium vapor pressure at the interface,
$P_{\mathrm{ambient}}$ the incident ambient partial pressure,
$\alpha_{\mathrm{evap}}$ the evaporation coefficient, and
$\alpha_{\mathrm{cond}}$ the condensation coefficient. The maintained model
defines

$$
J_{\mathrm{evap}}
=\alpha_{\mathrm{evap}}
\frac{P_{\mathrm{eq}}}{\sqrt{2\pi m k_BT}},
$$

$$
J_{\mathrm{cond}}
=\alpha_{\mathrm{cond}}
\frac{P_{\mathrm{ambient}}}{\sqrt{2\pi m k_BT}},
$$

and the signed net flux

$$
J_{\mathrm{net}}=J_{\mathrm{evap}}-J_{\mathrm{cond}}.
$$

The corresponding signed mass flux is $mJ_{\mathrm{net}}$. Negative net flux
represents condensation toward the condensed phase and is not silently clamped
to zero.

## Computational derivation

The [computational laboratory](../../../../../notebooks/thermal/transport/phase-change/hertz-knudsen-net-flux.ipynb)
numerically integrates the positive normal-velocity moment after the two
normalized tangential factors are retained analytically. It compares the result
with the package evaluator, then composes a synthetic Antoine equilibrium
pressure with distinct evaporation and condensation coefficients.

“First principles” in that exercise means direct computation from the stated
classical ideal-gas kinetic-theory assumptions. It is not an electronic-
structure or interacting many-body first-principles calculation. The synthetic
coefficients and pressures are illustrative and do not validate a material or
process.
