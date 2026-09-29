# Complex plane waves

## Generic representation

A complex plane wave in $d$ spatial dimensions is

$$
u(\mathbf r,t)=A\exp\left[i\left(\mathbf k\cdot\mathbf r-
\omega t+\phi\right)\right].$$

Here $A\geq0$ is the dimensionless amplitude, $\mathbf k$ is the angular wave
vector, $\omega$ is the angular frequency, and $\phi$ is a phase offset in
radians. The phase must be dimensionless, so $\mathbf k$ has inverse-length
units and $\omega$ has inverse-time units.

The magnitude is constant:

$$|u(\mathbf r,t)|=A.$$

Its real and imaginary parts oscillate in quadrature. Positive $\omega$ with
the selected sign convention advances constant-phase surfaces along
$\mathbf k$.

## One dimension

In one dimension,

$$u(x,t)=A\exp[i(kx-\omega t+\phi)],$$

and the wavelength for nonzero $k$ is $\lambda=2\pi/|k|$. The maintained model
accepts physical positions and time and converts compatible units before
forming the phase.

## Two-dimensional periodic sampling

On an endpoint-excluded rectangular grid with lengths $L_x$ and $L_y$, exactly
periodic angular wave-vector components have the form

$$k_x=\frac{2\pi n_x}{L_x},\qquad
k_y=\frac{2\pi n_y}{L_y},$$

for integers $n_x$ and $n_y$. Such a sampled plane wave occupies one discrete
Fourier mode, subject to the FFT indexing convention. A wave vector between
discrete modes produces spectral leakage rather than one exact peak.

## Interpretation boundary

The mathematical representation alone does not determine a dispersion relation
$\omega(\mathbf k)$. It also does not determine whether the field represents a
quantum amplitude, electromagnetic field, acoustic field, elastic displacement,
or another quantity. Those meanings require domain-specific state spaces,
normalization, units, governing equations, and boundary conditions.

The maintained models therefore use a unitless complex field and make no
quantum normalization or physical-wave validation claim.
