# Finite-difference quantum harmonic oscillator

## Continuum model

The one-dimensional quantum harmonic oscillator has Hamiltonian

$$
\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+\frac12m\omega^2x^2,
$$

where $m>0$ is the particle mass and $\omega>0$ is the angular frequency. Its
continuum stationary energies are

$$
E_n=\hbar\omega\left(n+\frac12\right),
\qquad n=0,1,2,\ldots.
$$

The physical coordinate domain is unbounded.

## Bounded numerical representation

Choose a finite interval $[x_{\min},x_{\max}]$ and a uniform grid including its
endpoints. Homogeneous Dirichlet values are imposed at those computational
boundaries, while interior samples are unknown. At an interior point,

$$
\frac{d^2\psi}{dx^2}(x_i)\approx
\frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}{\Delta x^2}.
$$

The represented Hamiltonian is real, symmetric, and tridiagonal apart from the
diagonal potential. Diagonalization returns Euclidean-normalized eigenvectors.
For the rectangular quadrature convention, continuously normalized samples are
obtained by dividing each column by $\sqrt{\Delta x}$.

## Error sources

Two numerical errors remain distinct:

1. **Domain truncation error** arises because the unbounded oscillator is
   represented on a finite interval with artificial endpoint conditions.
2. **Discretization error** arises because the differential operator is
   replaced by a finite-spacing stencil.

Increasing the point count at fixed bounds addresses only the second source.
Moving the bounds while changing the spacing can affect both. These errors
should not be combined without a declared analysis.

A truncated Hermite-function basis is a different representation. Its dominant
control is basis size and reference-basis choice rather than a coordinate-grid
spacing and finite boundary. Agreement between the two approaches can provide
independent numerical evidence when conventions are aligned.

The
[computational laboratory](../../../../notebooks/qm/qho1d/qho1d__finite_difference.ipynb)
compares low represented energies with the exact spectrum and preserves the
shifted-eigenfunction visualization over the harmonic potential.

## Exercises

1. Derive the tridiagonal kinetic-energy matrix.
2. Check even and odd parity of successive states on a symmetric grid.
3. Design separate interval and spacing refinement studies.
4. Explain why low states converge before states with appreciable boundary
   amplitude.
