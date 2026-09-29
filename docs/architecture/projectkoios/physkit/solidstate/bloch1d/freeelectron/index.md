# `projectkoios.physkit.solidstate.bloch1d.freeelectron`

This package owns the one-dimensional bare free-electron Bloch representation.

- `BlochPrimitiveCell1D` owns one oriented physical reference-cell length and
  its reciprocal basis.
- `FreeElectronBloch1D` evaluates the exact folded modes
  $q_n=k+2\pi n/a$ using the bare electron mass.
- `FreeElectronBloch1DWavefunctionSampler` samples exact cell-normalized Bloch
  modes.
- `FreeElectronBloch1DFiniteDifferenceHamiltonianConstructor` combines the
  physical free-electron coefficient with the independently owned `pbc1d`
  Laplacian.

The package uses the selected physical unit system and performs compound-unit
conversion explicitly. It does not own an effective semiconductor mass,
crystal potential, interacting-electron model, or DFT calculation.
