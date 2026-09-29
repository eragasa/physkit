# Canonical probabilities on finite PIAB1D levels

## Finite energy inventory

Consider a finite inventory of one-dimensional particle-in-a-box energies
$E_n$. For a box of length $L$ and particle mass $m$,

$$
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2},
\qquad n=1,2,\ldots.
$$

Retaining finitely many levels is a representation choice. The inventory must
include enough high-energy states for the selected thermal scale.

## Canonical probabilities

For one modeled particle at positive thermal energy $k_B T$, the finite-level
canonical probability is

$$
P_n=\frac{\exp[-E_n/(k_B T)]}{Z},
\qquad
Z=\sum_m\exp[-E_m/(k_B T)].
$$

A common energy shift does not alter normalized probabilities. The stable form
used computationally is therefore

$$
P_n=\frac{\exp[-(E_n-E_{\min})/(k_B T)]}
{\sum_m\exp[-(E_m-E_{\min})/(k_B T)]}.
$$

The represented probabilities satisfy

$$
P_n\geq0,
\qquad
\sum_nP_n=1.
$$

## Inventory truncation

The retained high-energy tail must be checked at the selected temperature.
Increasing temperature or box length can increase the number of levels needed
because more energies become thermally accessible. Normalization within a
truncated inventory does not by itself establish that truncation error is
small.

## Distinction from Fermi--Dirac occupations

Canonical probabilities describe mutually exclusive levels of one modeled
particle. Fermi--Dirac values are expected occupations of single-particle
states in a fermion population and require a chemical potential. Their sum is
an expected particle number rather than one. The two normalized objects answer
different questions and must not be interchanged.

The
[computational laboratory](../../../../notebooks/qm/piab1d/piab1d__canonical_probabilities.ipynb)
evaluates a finite PIAB1D inventory, checks normalization and the omitted tail,
and preserves the canonical-probability bar presentation from the exploratory
computational lecture.

## Exercises

1. Show algebraically that a common energy shift leaves $P_n$ unchanged.
2. Explain why increasing $L$ reduces the level spacing.
3. Define a quantitative retained-tail criterion for a chosen calculation.
4. Contrast the normalization of $P_n$ with the sum of Fermi--Dirac
   occupations.
