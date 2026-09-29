# Kronig--Penney delta-comb dispersion

## Periodic singular potential

Consider a one-dimensional periodic array of Dirac delta barriers with period
$a$. If the dimensional strength multiplying each delta is $\lambda$, then
$\lambda$ has energy-times-length dimensions. In a free region,

$$
q=\frac{\sqrt{2mE}}{\hbar},
\qquad z=qa.
$$

Matching across one period gives

$$
\cos(ka)=\cos z+\frac{m\lambda}{\hbar^2q}\sin z.
$$

Define

$$
P=\frac{m\lambda a}{\hbar^2}.
$$

Then the dimensionless relation is

$$
\cos(ka)=f_P(z)
=\cos z+P\frac{\sin z}{z}.
$$

The maintained model treats $P\geq0$, including the free-particle limit
$P=0$.

## Allowed bands

A real Bloch phase exists exactly where

$$
-1\leq f_P(z)\leq1.
$$

For every allowed $z$, the nonnegative first-zone branch is

$$
ka=\arccos[f_P(z)],
$$

and inversion symmetry supplies the negative branch. Intervals for which
$|f_P(z)|>1$ are forbidden gaps in this idealized model.

Using

$$
E_a=\frac{\hbar^2}{2ma^2},
$$

the reduced energy is

$$
\frac{E}{E_a}=z^2.
$$

## Numerical representation

Directly filtering $f_P(z)$ on a one-dimensional phase grid preserves the exact
allowed-value criterion at each sample. It does not require an arbitrary
residual tolerance on a two-dimensional $(k,E)$ mesh. The sample density still
controls graphical resolution, and exact band edges require root finding for
$f_P(z)=\pm1$.

## Evidence boundary

The resulting curves are calculated bands of the idealized dimensionless
delta-comb model. They are not an electronic-structure calculation or a
validated material band structure. A dimensional application requires an
identified period, mass, delta strength, unit convention, and independent
validation.

The
[computational laboratory](../../../../../../notebooks/solidstate/electronic-structure/kronig-penney/delta-comb-bands.ipynb)
plots the allowed-value condition and symmetric reduced band branches.

## Exercises

1. Derive $P$ from the dimensional matching relation.
2. Show that $P=0$ produces folded free-particle branches.
3. Locate the first roots of $f_P(z)=\pm1$.
4. Compare repulsive and attractive delta-comb conventions as distinct models.
