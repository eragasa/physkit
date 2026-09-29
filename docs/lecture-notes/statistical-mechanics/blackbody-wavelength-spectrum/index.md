# Blackbody spectral energy density per wavelength

## Represented quantity

Let $u_\lambda(\lambda,T)$ denote equilibrium electromagnetic energy per volume
per wavelength at wavelength $\lambda>0$ and absolute temperature $T>0$. Its SI
dimensions are joules per cubic metre per metre, equivalently joules per fourth
power of metre.

This quantity is not spectral radiance and is not emitted surface flux. Those
quantities require additional angular or geometric relations.

## Planck distribution

The wavelength-domain Planck distribution is

$$
u_\lambda(\lambda,T)=
\frac{8\pi hc}{\lambda^5}
\frac{1}{\exp(x)-1},
\qquad
x=\frac{hc}{\lambda k_BT}.
$$

The dimensionless value $x$ determines which asymptotic approximation is
appropriate.

## Short-wavelength limit

When $x\gg1$, one has $\exp(x)-1\approx\exp(x)$. Therefore,

$$
u_\lambda(\lambda,T)
\approx
\frac{8\pi hc}{\lambda^5}\exp(-x),
$$

which is the Wien approximation to the spectrum. It is distinct from Wien's
displacement law, which concerns the location of the spectral maximum.

## Long-wavelength limit

When $x\ll1$, the expansion $\exp(x)-1=x+O(x^2)$ gives

$$
u_\lambda(\lambda,T)
\approx
\frac{8\pi hc}{\lambda^5}\frac{1}{x}
=
\frac{8\pi k_BT}{\lambda^4},
$$

the Rayleigh--Jeans approximation. Its divergence as $\lambda\rightarrow0$
shows that it must not be extended into the short-wavelength regime.

## Computational use

The maintained model evaluates Planck's expression using an algebraically
stable denominator and returns all three densities in an explicit compatible
unit. The [computational laboratory](../../../../notebooks/thermal/statmech/radiation/blackbody-wavelength-spectrum.ipynb)
checks the two dimensionless approximation regimes and plots exact spectra for
several temperatures.

The represented curves describe an ideal equilibrium radiation field. They do
not incorporate wavelength-dependent material emissivity and do not constitute
validation for a real radiating body.
