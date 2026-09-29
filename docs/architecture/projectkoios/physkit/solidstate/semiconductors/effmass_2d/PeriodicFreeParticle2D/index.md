# `PeriodicFreeParticle2D`

`PeriodicFreeParticle2D` is an immutable actionized DataObject defined in
`projectkoios.physkit.solidstate.semiconductors.effmass_2d.model`.

Its `evaluate_modes(...)` façade accepts explicit integer reciprocal indices
and one Cartesian Bloch wave vector. The actionizer returns a retained request,
physical wave vectors, and effective-mass kinetic energies in deterministic
request order. The model requires the primitive cell and effective-mass tensor
to use the same physical unit system.

The implementation is an exact reciprocal-space reference model. It does not
own Brillouin-zone path policy, mode cutoffs, electronic occupation, material
parameters, or a DFT calculation.
