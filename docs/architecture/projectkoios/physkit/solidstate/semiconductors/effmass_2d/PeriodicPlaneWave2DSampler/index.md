# `PeriodicPlaneWave2DSampler`

`PeriodicPlaneWave2DSampler` is an ActionObject defined in
`projectkoios.physkit.solidstate.semiconductors.effmass_2d.wavefunctions`.

It maps dimensionless fractional coordinates through the retained primitive
cell and samples every mode in a `PeriodicFreeParticle2DSpectrum`. Returned
plane waves have normalization $\Omega^{-1/2}$ and therefore inverse-length
units in two dimensions. The result retains its complete request and physical
Cartesian positions.
