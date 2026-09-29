# `projectkoios.physkit.solidstate.bloch1d.cosinepotential`

This package owns the one-dimensional bare-electron Bloch model with
$V(x)=V_0\cos(2\pi x/a)$.

`CosinePotentialBloch1D` is an immutable actionized DataObject. Its band solve
retains the model, Bloch wave-number grid, finite-difference point count, and
requested band count. It reuses the maintained free-electron Hamiltonian, adds
the represented diagonal potential, and returns ordered energy bands.

The package does not own generic PBC mechanics, empirical semiconductor
parameters, density-of-states policy, finite-temperature occupation, or
chemical-potential solving.
