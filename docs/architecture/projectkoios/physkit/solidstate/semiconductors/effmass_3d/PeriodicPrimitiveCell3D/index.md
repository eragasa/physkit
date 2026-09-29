# `PeriodicPrimitiveCell3D`

`PeriodicPrimitiveCell3D` is an immutable DataObject defined in
`projectkoios.physkit.solidstate.semiconductors.effmass_3d.cell`.

It owns a $2\times2$ physical primitive-basis matrix whose columns are direct
vectors and a coherent physical `UnitSystem`. It derives the cell volume, metric
tensor, and reciprocal basis $B=2\pi A^{-\mathsf T}$. It rejects singular,
nonfinite, incorrectly shaped, dimensionless, or unit-inconsistent inputs.
