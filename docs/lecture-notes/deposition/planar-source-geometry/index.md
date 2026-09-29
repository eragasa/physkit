# Planar deposition geometry from point and disk sources

## Scope

This note derives normalized thickness profiles for idealized sources in three
dimensional space incident on a parallel two-dimensional substrate. It does
not derive an evaporation rate, account for gas-phase collisions, or model
sticking, re-evaporation, shadowing, source depletion, or chamber boundaries.

## Isotropic point source

Place the substrate at $z=0$ and the source at $(0,0,-h)$ with $h>0$. A
substrate point at lateral radius $\ell$ lies a distance

$$
r=(h^2+\ell^2)^{1/2}
$$

from the source. Isotropic transport contributes an inverse-square factor
$r^{-2}$. The projected substrate area contributes

$$
\cos\theta=\frac{h}{r}.
$$

Consequently the local shape is proportional to $h/r^3$. Normalizing by the
on-axis value gives

$$
\frac{d(\ell)}{d(0)}
=\frac{h^3}{(h^2+\ell^2)^{3/2}}
=\left[1+(\ell/h)^2\right]^{-3/2}.
$$

## Finite circular source

Let an emitting disk of radius $a$ occupy the plane $z=-h$. A source point has
polar coordinates $(\rho,\psi)$ and area element
$dA=\rho\,d\rho\,d\psi$. Its squared distance to the substrate point
$(\ell,0,0)$ is

$$
r^2=\ell^2+\rho^2-2\ell\rho\cos\psi+h^2.
$$

Assume source intensity proportional to $\cos^n\phi$, where $n\geq0$ and
$\cos\phi=h/r$. The parallel substrate projection contributes another $h/r$.
Together with inverse-square spreading, the shape is

$$
J_n(\ell)\propto
\int_0^a\int_0^{2\pi}
\frac{h^{n+1}\rho\,d\psi\,d\rho}{r^{n+3}}.
$$

Only the normalized ratio $J_n(\ell)/J_n(0)$ is represented by the maintained
finite-disk API.

## Point-source limits

When $a/h\to0$, an $n=0$ disk approaches the isotropic point-source profile
$[1+(\ell/h)^2]^{-3/2}$. An $n=1$ Lambertian disk instead approaches
$[1+(\ell/h)^2]^{-2}$. Comparing these without matching the source angular law
would conflate source size with emission anisotropy.

## Numerical evaluation

The finite-disk model rescales all lengths by $h$, applies a periodic uniform
azimuthal rule, applies trapezoidal radial integration, and evaluates the
on-axis normalization with the same quadrature. Refinement compares complete
normalized profiles rather than only one point.

## Evidence boundary

Agreement with the closed form and quadrature refinement are software and
numerical verification of the stated idealized mathematics. Predicting film
thickness requires separately justified emission rate, material density,
transport regime, sticking behavior, and apparatus geometry. No such
scientific validation is claimed here.
