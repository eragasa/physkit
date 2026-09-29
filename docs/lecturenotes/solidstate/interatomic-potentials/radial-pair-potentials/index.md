# Lennard--Jones and Morse radial pair potentials

## Scope

A radial pair potential assigns energy $V(r)$ to the separation $r>0$ of two
represented particles. The signed radial force is

$$
F_r(r)=-\frac{dV}{dr},
$$

where positive force is repulsive and negative force is attractive. These
models omit many-body, angular, electronic, environmental, and quantum effects.

A radial formula alone also does not define an atomistic structure or a force
field. Chemical-species identities, pair-to-parameter selection, atom
identifiers, positions, boundary conditions, and interaction enumeration are
separate contracts. The maintained potential parameters are therefore
species-agnostic; callers must not infer material applicability from the class
name or an illustrative parameter set.

## Lennard--Jones 12-6 model

The Lennard--Jones form is

$$
V_{\mathrm{LJ}}(r)=4\epsilon
\left[(\sigma/r)^{12}-(\sigma/r)^6\right],
$$

with $\epsilon>0$ and $\sigma>0$. Its force is

$$
F_{\mathrm{LJ}}(r)=\frac{24\epsilon}{r}
\left[2(\sigma/r)^{12}-(\sigma/r)^6\right].
$$

The zero crossing occurs at $r=\sigma$. The equilibrium distance, energy, and
curvature are

$$
r_0=2^{1/6}\sigma,\qquad
V(r_0)=-\epsilon,\qquad
V''(r_0)=\frac{72\epsilon}{r_0^2}.
$$

The attractive tail approaches zero algebraically as $-r^{-6}$.

## Morse model

The shifted Morse form is

$$
V_{\mathrm M}(r)=D[(1-e^{-a(r-r_e)})^2-1],
$$

with $D>0$, $a>0$, and $r_e>0$. Differentiation gives

$$
F_{\mathrm M}(r)
=-2aD(1-e^{-a(r-r_e)})e^{-a(r-r_e)}.
$$

Therefore the force is positive for $r<r_e$, zero at $r_e$, and negative for
$r>r_e$. The minimum and curvature are

$$
V(r_e)=-D,\qquad V''(r_e)=2Da^2.
$$

The attractive tail approaches zero exponentially.

## Local curvature matching

Choosing

$$
D=\epsilon,\qquad r_e=r_0,\qquad a=6/r_0
$$

matches well depth, equilibrium distance, and second derivative because
$2D(6/r_0)^2=72\epsilon/r_0^2$. This is a local mathematical comparison, not a
material fit. The potentials remain different away from equilibrium.

## Numerical verification

The force can be checked independently with centered differentiation of sampled
energies. This test must compare the signed analytical force with $-dV/dr$;
using $+dV/dr$ reverses attraction and repulsion. Unit compatibility is checked
before evaluation, and all outputs retain requested physical units.

## Evidence boundary

Analytical characteristic values and finite-difference agreement establish
software and numerical verification of the represented formulas. They do not
validate either model for a material, temperature, phase, pressure, or
simulation purpose. Such use requires identified parameter provenance and
independent scientific validation.
