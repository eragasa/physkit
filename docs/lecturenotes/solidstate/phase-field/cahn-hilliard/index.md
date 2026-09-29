# Dimensionless periodic Cahn--Hilliard evolution

## Scope

The Cahn--Hilliard equation describes a conserved scalar field driven by
chemical-potential gradients. This note owns a reduced dimensionless model on
uniform periodic one- and two-dimensional domains. It does not map the reduced
variables to a material, infer thermodynamic parameters, or validate a
coarsening law.

## Free energy and chemical potential

For reduced field $c(\mathbf x,t)$, use

$$
F[c]=\int_\Omega\left[\frac14(c^2-1)^2
+\frac\kappa2|\nabla c|^2\right]d\mathbf x,
$$

where $\kappa>0$ is the reduced gradient penalty. The variational derivative is

$$
\mu=\frac{\delta F}{\delta c}=c^3-c-\kappa\nabla^2c.
$$

With constant reduced mobility $M>0$ and flux $\mathbf J=-M\nabla\mu$,
conservation gives

$$
\frac{\partial c}{\partial t}=M\nabla^2\mu.
$$

Periodic boundaries imply that the integral, and therefore the spatial mean,
of $c$ is conserved.

## Spectral representation

For Fourier wave vector $\mathbf k$,

$$
\mathcal F[\nabla^2 c]=-k^2\widehat c,
\qquad
\mathcal F[\nabla^4 c]=k^4\widehat c.
$$

The represented semi-implicit step is

$$
\widehat c^{n+1}=
\frac{\widehat c^n-\Delta t M k^2\widehat{(c^3-c)}^n}
{1+\Delta t M\kappa k^4}.
$$

The nonlinear bulk contribution is explicit; the fourth-order gradient term is
implicit. At $k=0$, numerator and denominator both leave the existing mode
unchanged, providing the discrete conservation mechanism.

## Numerical boundaries

The maintained solver:

- uses uniform endpoint-excluded periodic samples;
- accepts finite unitless fields and positive reduced parameters;
- retains the initial, requested-stride, and final snapshots;
- does not apply de-aliasing to the cubic term;
- does not adapt the time step; and
- does not assert unconditional energy decrease.

The original exploratory chemical-potential helper had the wrong sign on its
spectral gradient term, although that helper was unused by the time-step loop.
The maintained implementation follows the update derived above and omits the
unused inconsistent helper.

## Evidence boundary

Stationary constant solutions and zero-mode conservation provide software and
numerical verification of specific invariants. They do not establish spatial
or temporal convergence, energy stability, late-stage scaling, or scientific
validation for a material system. Those claims require additional separately
designed evidence.
