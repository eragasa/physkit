# One-dimensional cosine-potential Bloch bands

The model adds one prescribed periodic Fourier component to the bare
free-electron Hamiltonian:

$$
H=-\frac{\hbar^2}{2m_e}\frac{d^2}{dx^2}
+V_0\cos\left(\frac{2\pi x}{a}\right).
$$

The reference-cell state satisfies

$$
\psi(x+a)=e^{ika}\psi(x).
$$

The generic endpoint-excluded grid and seam phases are owned by `pbc1d`; the
cosine model owns the potential and band solve.

## Free-electron limit

At $V_0=0$, the represented Hamiltonian is exactly the maintained
free-electron finite-difference Hamiltonian. The continuum reference branches
are

$$
E_n(k)=\frac{\hbar^2}{2m_e}
\left(k+\frac{2\pi n}{a}\right)^2.
$$

This exact reduction is a software-verification requirement.

## First gap

The cosine potential has reciprocal components at $G=\pm2\pi/a$. At the first
zone boundary it couples the degenerate free-electron modes. In the weak
potential limit, the first gap approaches

$$
\Delta E\approx |V_0|.
$$

A represented finite-difference calculation additionally carries grid error.
The potential effect and discretization error must remain distinct.

Changing $V_0$ to $-V_0$ translates the cosine by half a cell, so the complete
spectrum is unchanged. The spectra at $k=-\pi/a$ and $k=\pi/a$ also agree.

## Evidence boundary

The maintained tests verify the represented free-electron limit, Brillouin-zone
endpoint agreement, weak-potential first-gap behavior, and amplitude-sign
invariance. These checks establish the idealized software and numerical model,
not a material-specific semiconductor gap.

Density-of-states and finite-temperature analyses retained in exploratory
notebooks require separate sampling, normalization, occupation, and chemical-
potential contracts.

See the [computational laboratory](../../../../../notebooks/solidstate/bloch1d/cosinepotential/cosine-potential-bands.ipynb).
