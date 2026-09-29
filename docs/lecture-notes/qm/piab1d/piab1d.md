# One-dimensional particle-in-a-box spectrum

## Model

The one-dimensional particle in a box represents a particle of mass $m$ on the
closed interval $[0,L]$. The stationary wavefunction satisfies homogeneous
Dirichlet boundary conditions,

$$
\psi(0)=\psi(L)=0,
$$

and the time-independent Schrödinger equation

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi.
$$

The corresponding
[computational laboratory](../../../../notebooks/qm/piab1d/piab1d.ipynb)
compares the continuum solution with a finite-difference representation.

## Boundary-condition derivation

For positive energy, define

$$
k^2=\frac{2mE}{\hbar^2}.
$$

The interior equation becomes

$$
\frac{d^2\psi}{dx^2}+k^2\psi=0,
$$

with general solution

$$
\psi(x)=A\sin(kx)+B\cos(kx).
$$

The left boundary condition gives $B=0$. The right boundary condition then
requires

$$
A\sin(kL)=0.
$$

A nonzero state therefore has

$$
k_n=\frac{n\pi}{L},
\qquad n=1,2,3,\ldots.
$$

Normalizing each selected sine mode determines its remaining amplitude. The
laboratory verifies the resulting eigenvalue equation and normalization using
symbolic algebra without introducing a second symbolic model API.

## Continuum solution

The normalized continuum eigenfunctions are

$$
\psi_n(x)=\sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right),
\qquad n=1,2,3,\ldots,
$$

with energies

$$
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

The quantum number $n$ orders the modes by increasing energy. Higher modes have
shorter wavelengths and therefore require finer numerical grids.

## Grid and active state space

A full grid includes both boundary points so that the geometric interval and
Dirichlet data remain explicit. The boundary values are prescribed rather than
unknown degrees of freedom. The matrix operator therefore acts only on the
interior samples. If there are $N$ interior points, the active numerical state
space has dimension $N$ even though the full coordinate grid has $N+2$ points.

This distinction separates the continuous differential operator, its boundary
conditions, and one finite matrix representation. Restoring zero boundary
values for plotting is an embedding of the active vector into the full grid;
it does not add degrees of freedom to the eigenproblem.

## Finite-difference representation

Let $N$ be the number of interior points and

$$
h=\frac{L}{N+1}
$$

be the uniform spacing. The second-order central-difference approximation is

$$
\frac{d^2\psi}{dx^2}\bigg|_{x_j}
\approx
\frac{\psi_{j-1}-2\psi_j+\psi_{j+1}}{h^2}.
$$

Applying the Dirichlet boundary conditions gives an $N\times N$ real symmetric
tridiagonal Hamiltonian. Its exact represented eigenvalues are

$$
E_n^{(h)}=
\frac{2\hbar^2}{mh^2}
\sin^2\left(\frac{n\pi}{2(N+1)}\right),
\qquad n=1,\ldots,N.
$$

These matrix eigenvalues differ from the continuum energies because the matrix
represents a discrete approximation to the differential operator. Comparing a
numerical eigensolver with $E_n^{(h)}$ checks solution of the represented matrix;
comparing $E_n^{(h)}$ with $E_n$ measures continuum-discretization error.

## Wavefunction normalization

A continuum wavefunction obeys

$$
\int_0^L |\psi(x)|^2\,dx=1.
$$

A matrix eigensolver instead returns a vector $v$ satisfying

$$
\sum_{j=1}^{N}|v_j|^2=1.
$$

For a uniform grid, sampled continuum values are compared with the eigensolver
vector through

$$
v_j\approx\sqrt{h}\,\psi(x_j).
$$

Either sign of a real eigenvector represents the same state, so a numerical
comparison must align the sign before comparing components.

## Exercises

1. Expand $E_n^{(h)}$ for small $h$ and identify the leading energy error.
2. Explain why a fixed grid represents low-energy modes more accurately than
   high-energy modes.
3. Verify the orthogonality of two sampled sine modes.
4. Derive the $L^{-2}$ energy scaling from the continuum formula.
