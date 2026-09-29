# Spectral time evolution in a one-dimensional box

## Stationary basis

Let $\psi_n(x)$ be normalized stationary particle-in-a-box eigenfunctions with
energies $E_n$. A state represented in a finite analytical basis is

$$
\Psi(x,0)=\sum_{n=1}^{N}c_n(0)\psi_n(x),
$$

where the coefficients satisfy

$$
\sum_{n=1}^{N}|c_n(0)|^2=1.
$$

The finite basis is an explicit representation choice. Modes outside the basis
have zero represented coefficient.

## Exact spectral propagation

Each stationary coefficient acquires its exact phase,

$$
c_n(t)=c_n(0)\exp\left(-\frac{iE_nt}{\hbar}\right),
$$

so

$$
\Psi(x,t)=
\sum_{n=1}^{N}
c_n(0)
\exp\left(-\frac{iE_nt}{\hbar}\right)
\psi_n(x).
$$

No time-stepping discretization is used. The represented time evolution is exact
within the selected finite continuum eigenbasis.

## Conserved quantities

Because every phase has unit magnitude,

$$
\sum_n|c_n(t)|^2=
\sum_n|c_n(0)|^2=1.
$$

The energy expectation is also constant:

$$
\langle E\rangle
=
\sum_n |c_n(0)|^2E_n.
$$

A numerical laboratory can check both spectral norm and the coordinate-space
normalization

$$
\int_0^L|\Psi(x,t)|^2\,dx=1.
$$

## Two-mode interference

For a superposition of modes $n=1$ and $n=2$, the probability density contains
an interference term whose relative phase evolves at

$$
\omega_{21}=\frac{E_2-E_1}{\hbar}.
$$

The corresponding beat period is

$$
T_{\mathrm{beat}}
=
\frac{2\pi\hbar}{E_2-E_1}.
$$

After one beat period, the relative phase returns and the probability density is
restored. The full wavefunction may differ by a physically irrelevant global
phase.

The
[computational laboratory](../../../../notebooks/qm/piab1d/piab1d__time_evolution.ipynb)
propagates a phase-shifted equal superposition of the first two modes and checks
norm, energy, and density recurrence.

## Exercises

1. Derive conservation of spectral norm directly from the phase factors.
2. Show that the energy expectation has no time dependence.
3. Compare global-phase recurrence with probability-density recurrence.
4. Explain why projecting an arbitrary initial function introduces a separate
   basis-truncation question.
