# Thermal de Broglie wavelength

## Relation to de Broglie waves

The de Broglie relation assigns wavelength

$$
\lambda=\frac{h}{p}
$$

to a momentum eigenstate with momentum magnitude $p$. A thermal ensemble does
not have one definite momentum, so its thermal wavelength is instead a
statistical normalization scale derived from the momentum distribution.

## Analytical derivation

For one nonrelativistic, structureless particle of mass $m$ in volume $V$, the
translational canonical partition function is

$$
Z_1=\frac{1}{h^3}\int_V d^3x\int_{\mathbb{R}^3}d^3p\,
\exp\!\left(-\beta\frac{p^2}{2m}\right),
\qquad \beta=\frac{1}{k_BT}.
$$

The position integral contributes $V$. The momentum integral separates into
three identical Cartesian Gaussian integrals:

$$
I_p=\int_{-\infty}^{\infty}
\exp\!\left(-\frac{\beta p_x^2}{2m}\right)dp_x
=\sqrt{\frac{2\pi m}{\beta}}
=\sqrt{2\pi m k_BT}.
$$

Therefore,

$$
Z_1=\frac{V}{h^3}(2\pi m k_BT)^{3/2}.
$$

Defining the thermal de Broglie wavelength by $Z_1=V/\lambda_T^3$ gives

$$
\boxed{\lambda_T=\frac{h}{\sqrt{2\pi m k_BT}}}
=\sqrt{\frac{2\pi\hbar^2}{m k_BT}}.
$$

The factor $2\pi$ follows from the Gaussian phase-space normalization. Thus
$\lambda_T$ is related to de Broglie waves through $h/p$, but it is not one
particle's definite wavelength or the literal spatial extent of a wave packet.
Other thermal-wavelength conventions can appear when a different characteristic
momentum is selected; the maintained model uses the canonical
partition-function convention above.

## Computational derivation

The corresponding computational route evaluates the one-dimensional Gaussian
integral numerically. With

$$
u=\frac{p_x}{\sqrt{2mk_BT}},
$$

one obtains

$$
I_p=\sqrt{2mk_BT}\int_{-\infty}^{\infty}e^{-u^2}\,du.
$$

Numerical quadrature supplies the dimensionless Gaussian integral independently
of the package's closed-form wavelength evaluator. The resulting normalization
length is $h/I_p$. Agreement between this route and the analytical evaluator is
a numerical verification of the represented formula.

## Use in statistical mechanics

For number density $n$, the dimensionless parameter

$$
n\lambda_T^3
$$

measures the occupied phase-space density scale. Small or order-one values can
support regime analysis, but the maintained API reports the parameter without
embedding a universal classification threshold.

The [computational laboratory](../../../../notebooks/thermal/statmech/quantum/thermal-de-broglie-wavelength.ipynb)
performs the independent quadrature, checks the $T^{-1/2}$ scaling, evaluates an
illustrative degeneracy parameter, and plots the electron thermal wavelength.
The calculations verify the documented software and mathematics; they do not
constitute material-specific scientific validation.
