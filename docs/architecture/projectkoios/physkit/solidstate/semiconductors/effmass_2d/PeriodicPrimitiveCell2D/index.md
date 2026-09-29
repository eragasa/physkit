# `PeriodicPrimitiveCell2D`

`PeriodicPrimitiveCell2D` is an immutable DataObject defined in
`projectkoios.physkit.solidstate.semiconductors.effmass_2d.cell`.

It owns a $2\times2$ physical primitive-basis matrix whose columns are direct
vectors and a coherent physical `UnitSystem`. It derives the cell area, metric
tensor, and reciprocal basis $B=2\pi A^{-\mathsf T}$. It rejects singular,
nonfinite, incorrectly shaped, dimensionless, or unit-inconsistent inputs.
