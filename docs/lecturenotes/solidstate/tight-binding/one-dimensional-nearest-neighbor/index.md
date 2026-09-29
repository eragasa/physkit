# One-dimensional nearest-neighbor tight binding

## Reduced lattice model

Consider one scalar basis state per site on an infinite one-dimensional integer
lattice. A nearest-neighbor tight-binding operator with onsite energy
$\varepsilon_0$ and positive hopping magnitude $t$ acts as

$$
(H\psi)_r
=\varepsilon_0\psi_r-t\psi_{r-1}-t\psi_{r+1}.
$$

This is a reduced lattice model. Its site labels are integers and do not by
themselves specify physical positions, atomic orbitals, a lattice constant, or a
material.

The corresponding
[computational laboratory](../../../../../notebooks/solidstate/tight-binding/one-dimensional-tight-binding.ipynb)
constructs the operator through `projectkoios.physkit.periodic.lattice`.

## Bloch dispersion

For a dimensionless Bloch phase $k$ per lattice step, substitute

$$
\psi_r=\exp(ikr).
$$

The eigenvalue is

$$
E(k)=\varepsilon_0-2t\cos(k).
$$

The band is centered on $\varepsilon_0$ and has width $4|t|$. If a physical
lattice constant $a$ is supplied by a separate physical-geometry model, the
phase can instead be written as $ka$.

## Finite open-chain level splitting

For $N$ uncoupled identical scalar orbitals, the onsite operator
$\varepsilon_0 I$ has an $N$-fold degenerate level at $\varepsilon_0$. Adding
nearest-neighbor hopping on an open chain gives

$$
H_{\mathrm{open}}
=\varepsilon_0 I
-t\sum_{r=0}^{N-2}
\left(|r\rangle\langle r+1|+|r+1\rangle\langle r|\right).
$$

Its eigenvalues are

$$
E_j=\varepsilon_0-2t\cos\left(\frac{j\pi}{N+1}\right),
\qquad j=1,\ldots,N.
$$

Thus off-diagonal coupling splits the degenerate isolated level into distinct
finite-chain levels. This is a useful bridge to band formation, but an open
chain is not translationally equivalent to the periodic crystal.

A separation-dependent illustrative hopping law such as

$$
t(r)=t_0e^{-\beta(r-r_0)}
$$

predicts collapse back toward the isolated level as $r\to\infty$ when
$t_0>0$ and $\beta>0$. This ansatz is not a universal interatomic law or a
material fit. The maintained periodic hopping model does not currently own
physical separation or this parameterization.

## Finite periodic domain

A finite periodic domain with $N$ sites and zero boundary twist samples

$$
k_m=\frac{2\pi m}{N},
\qquad m=0,1,\ldots,N-1.
$$

Its matrix spectrum is therefore the multiset

$$
\left\{E(k_m)\right\}_{m=0}^{N-1}.
$$

The matrix is finite, while $E(k)$ denotes the continuous dispersion of the
translation-invariant parent model. Increasing $N$ adds sampling points; it does
not change the parent hopping inventory.

## Twisted boundary condition

Let $\phi$ denote an unreduced boundary twist in turns. In centered uniform-link
gauge, each displacement $R$ receives the phase

$$
\exp\left(2\pi i\frac{\phi R}{N}\right).
$$

For the nearest-neighbor model, this shifts the sampled phases to

$$
k_m(\phi)=\frac{2\pi(m+\phi)}{N}.
$$

The finite operator then samples $E[k_m(\phi)]$. Integer shifts of the twist lift
are retained explicitly by the finite-lattice representation even when they
share a quotient representative.

## Representation checks

For the selected real symmetric hopping inventory:

- the $-1$ and $+1$ displacement coefficients are equal;
- the finite matrix is Hermitian;
- its trace is $N\varepsilon_0$; and
- its eigenvalues agree with the sampled dispersion.

These checks verify the represented nearest-neighbor model and its matrix
construction.

## Exercises

1. Derive the dispersion directly from the translation eigenstate.
2. Identify the band minimum and maximum for positive and negative $t$.
3. Show that a full one-turn twist permutes the eigenvalue multiset.
4. Compare the open-chain levels with periodic samples at equal site count.
5. For the illustrative $t(r)$, show how the finite-chain level spread changes
   with separation.
6. Add a real next-nearest-neighbor term and derive the new dispersion.
