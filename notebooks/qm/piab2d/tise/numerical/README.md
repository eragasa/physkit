# PIAB2D numerical prototypes

- [`oblique-periodic-boundary-prototype.ipynb`](oblique-periodic-boundary-prototype.ipynb)
  preserves the former `notebooks/solidstate/piab2d_pbc.ipynb` byte-for-byte.
- [`generalized-oblique-coordinate-prototype.ipynb`](generalized-oblique-coordinate-prototype.ipynb)
  preserves the former `notebooks/scratch/generalized_piab2d.ipynb`
  byte-for-byte.

The artifact is preserved for more than its current implementation. Its
scientific and pedagogical intent is a PIAB2D treatment combining periodic
boundaries, oblique lattice geometry, coordinate transformation, spectral
solution, and physical-space probability-density plots. That intended model and
its graph sequence remain valuable even though the executed solver path does not
yet realize the complete periodic-boundary contract.

The current code constructs centered finite-difference operators without active
seam couplings and maps a parameter-space grid through an oblique direct basis.
The unused periodic helper does not by itself establish periodic boundary
behavior. This implementation finding qualifies the artifact; it does not erase
its intended content.

The preserved goals include:

- metric-aware differentiation in oblique coordinates;
- a two-dimensional free-particle eigenproblem;
- physical-coordinate mapping of represented states; and
- probability-density visualization on a parallelogram.

The generalized prototype adds derivation of the metric tensor, a mixed-
derivative curvilinear Laplacian, reciprocal-basis construction, plane-wave
energies, real-space reconstruction, and both physical-space and reciprocal-
space plots. It also contains repeated experimental routes and a saved error.
Those layers are preserved because they document distinct numerical ideas and
presentation attempts, not because every route is correct.

The two prototypes are related but not interchangeable. One expresses an
intended periodic-boundary PIAB2D path; the other explores both bounded
curvilinear finite differences and periodic reciprocal-space plane waves. A
future consolidation must first identify each route's state space, boundary
condition, endpoint convention, basis normalization, and error source.

These are preserved exploratory prototypes, not maintained or validated
laboratories. They must not be cited as evidence of a periodic or generalized
PIAB2D solver until the boundary conditions, endpoint treatment, spacing, mixed
derivative, state normalization, and independent numerical checks are corrected
explicitly.
