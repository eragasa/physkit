# Sampled wavefunction normalization and basis projection

## Weighted sampled representation

Let $\phi_i$ represent a wavefunction shape at sampled coordinates $x_i$, and
let positive quadrature weights $w_i$ approximate integration. Its represented
squared norm is

$$
\|\phi\|_w^2=\sum_i w_i|\phi_i|^2.
$$

For nonzero $\phi$, the normalized samples are

$$
\widetilde{\phi}_i=
\frac{\phi_i}{\sqrt{\sum_jw_j|\phi_j|^2}}.
$$

The quadrature weights are part of the numerical representation. Changing them
changes the discrete inner product and therefore the normalization and
projection coefficients.

## Sampled Gaussian state

A convenient unnormalized shape is

$$
\phi(x)=
\exp\!\left[-\frac{(x-x_0)^2}{2\sigma^2}\right]
\exp(ik_0x),
$$

where $x_0$ is the center, $\sigma>0$ is the width, and $k_0$ is the average
wavenumber parameter. The Gaussian shape does not exactly satisfy homogeneous
Dirichlet boundary conditions unless its boundary values vanish. A finite PIAB
basis therefore approximates both its interior shape and its boundary behavior.

## Weighted basis projection

Let the columns $\psi_{in}$ be sampled basis states that are orthonormal under
the same weights. The expansion coefficients are

$$
c_n=\sum_i w_i\psi_{in}^{*}\widetilde{\phi}_i.
$$

The represented probability associated with basis state $n$ is $|c_n|^2$, and
the probability captured by a finite basis inventory is

$$
P_{\mathrm{represented}}=\sum_{n=1}^{N}|c_n|^2.
$$

A value below one identifies probability outside the represented basis under the
selected sampled inner product. A value close to one does not by itself establish
that coordinate-space reconstruction error is negligible everywhere.

## Symmetry at the box midpoint

For a zero-wavenumber Gaussian centered at $L/2$, reflection symmetry selects
only PIAB eigenfunctions with matching parity. With the standard
$\sin(n\pi x/L)$ basis, alternating coefficients therefore vanish. Moving the
center or adding a plane-wave phase generally removes this selection rule.

The
[computational laboratory](../../../../notebooks/qm/piab1d/piab1d__basis_projection.ipynb)
constructs a midpoint Gaussian, performs weighted normalization and projection,
and visualizes the finite-basis reconstruction and expansion probabilities.

## Exercises

1. Derive the coefficient formula from the sampled weighted inner product.
2. Explain why normalization and projection must use the same weights.
3. Compare represented probability with weighted reconstruction error.
4. Predict which coefficients become nonzero after displacing the Gaussian.
