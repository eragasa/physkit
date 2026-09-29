# Implementation

The model delegates to `DimensionlessPeriodicCahnHilliard1DSpectralSolver`.
The solver evaluates the nonlinear bulk term explicitly and the fourth-order
gradient term implicitly using NumPy FFTs.

- [Mathematics](mathematics/index.md)
- [References](references/index.md)
- [Testing](testing/index.md)
