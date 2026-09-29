# Finite-level occupations and spatial density

## Single-particle level inventory

Consider a finite inventory of normalized single-particle orbitals $\psi_n(x)$
with energies $E_n$. The inventory is a representation choice. Results depend
on whether enough levels have been retained for the selected thermal scale and
expected particle number.

No degeneracy is implicit in the formulas below. Each represented level accepts
one modeled fermion. A spin or other degeneracy factor must be declared and
applied consistently to both occupation sums and spatial density.

## Fermi–Dirac occupations

For chemical potential $\mu$ and positive thermal energy $k_B T$, the expected
occupation of level $n$ is

$$
f_n=\frac{1}{\exp\!\left((E_n-\mu)/(k_B T)\right)+1}.
$$

For a target expected occupation $N$, the finite-level chemical potential solves

$$
\sum_n f_n=N.
$$

The sum increases monotonically with $\mu$, so a bracketed bisection method can
solve the finite equation deterministically. Numerically stable evaluation uses
an exponentially decaying form for positive arguments rather than evaluating a
potentially overflowing exponential directly.

## Occupation-weighted spatial density

The independent-particle spatial number density represented by the occupied
orbitals is

$$
\rho(x)=\sum_n f_n|\psi_n(x)|^2.
$$

If each orbital is normalized on the box, then

$$
\int \rho(x)\,dx=\sum_n f_n=N.
$$

Therefore $\rho(x)$ is a number density, not a probability density normalized to
one. When $N>0$, the corresponding normalized position density for a particle
sampled from the modeled population is

$$
p(x)=\frac{\rho(x)}{N}.
$$

## Distinction from a canonical single-particle distribution

[Canonical probabilities on finite PIAB1D levels](piab1d__canonical_probabilities.md)
sum to one and describe the mutually exclusive level of one modeled particle.
Fermi–Dirac occupations instead solve an expected particle-number equation and
each lie between zero and one. They are not interchangeable and therefore have
separate computational laboratories.

The
[computational laboratory](../../../../notebooks/qm/piab1d/piab1d__fermions.ipynb)
uses the extracted finite-level analysis APIs to reproduce the continuous and
discrete occupation presentation and spatial-density visualization with
explicit units and checks.

## Exercises

1. Show that $\sum_n f_n$ is monotone in $\mu$.
2. Verify the spatial-density integral from orbital normalization.
3. Identify the additional factor required for a declared twofold spin
   degeneracy.
4. Explain why truncating the level inventory can bias a high-temperature
   chemical-potential solution.
