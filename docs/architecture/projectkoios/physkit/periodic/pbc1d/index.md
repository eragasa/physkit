# `projectkoios.physkit.periodic.pbc1d`

This package owns one-dimensional endpoint-excluded periodic grids and
Bloch-twisted finite-difference boundary representations.

- `PeriodicFiniteDifferenceGrid1D` owns point count, oriented physical cell
  length, spacing, and endpoint-excluded positions.
- `BlochPeriodicLaplacian1DConstructor` constructs the centered second
  derivative with conjugate Bloch seam phases and returns an immutable complex
  sparse representation.

This package owns boundary and discretization mechanics. It does not own the
free-electron Hamiltonian, a semiconductor effective mass, a crystal potential,
or band interpretation.
