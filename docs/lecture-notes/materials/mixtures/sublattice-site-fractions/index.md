# Site-fraction composition on multiple sublattices

## Scope

A bulk mole-fraction vector does not identify which crystallographic site class
a constituent occupies. A sublattice representation assigns a separate
composition vector to each declared site class. This note defines finite
site-fraction bookkeeping only; it does not provide thermodynamic energies or
equilibrium occupancies.

## Sublattice state

Let $s$ identify a sublattice with allowed species set $\mathcal A_s$. If
$n_i^{(s)}\geq0$ sites are assigned to species $i$ and
$N_s=\sum_i n_i^{(s)}>0$, then

$$
y_i^{(s)}=\frac{n_i^{(s)}}{N_s},
\qquad
\sum_{i\in\mathcal A_s}y_i^{(s)}=1.
$$

Each sublattice is normalized independently. For $S$ sublattices, the complete
composition lies in a product of $S$ simplices rather than one global simplex.

## Formula-unit multiplicity

Let $a_s>0$ be the represented number of sites on sublattice $s$ per formula
unit. The amount of constituent $i$ per formula unit is

$$
N_i^{\mathrm{fu}}=\sum_s a_sy_i^{(s)},
$$

where the sum includes only sublattices on which $i$ is allowed. Species shared
by multiple sublattices accumulate in deterministic sublattice order.

## Explicit pseudocomponent exclusion

Vacancies or other pseudocomponents may be represented as ordinary identifiers
in a site-fraction vector. Whether they participate in an overall normalized
constituent composition is a model choice, not a universal rule. For an
explicit exclusion set $\mathcal E$,

$$
X_i=\frac{N_i^{\mathrm{fu}}}
{\sum_{j\notin\mathcal E}N_j^{\mathrm{fu}}},
\qquad i\notin\mathcal E.
$$

The exclusion set is retained in the software result's request context.

## Numerical contract

Input fraction vectors must be finite, nonnegative, aligned with the declared
species order, and normalized to one within an absolute tolerance of
$10^{-12}$ with zero relative tolerance. The implementation does not silently
renormalize supplied fractions. Count normalization is a separate explicit
action.

## Evidence boundary

The maintained tests verify normalization, indexing, multiplicity-weighted
aggregation, and explicit exclusions. They do not establish a real crystal
structure, validate vacancy concentrations, or implement CALPHAD equilibrium.
Such claims require separately identified structural and thermodynamic evidence.
