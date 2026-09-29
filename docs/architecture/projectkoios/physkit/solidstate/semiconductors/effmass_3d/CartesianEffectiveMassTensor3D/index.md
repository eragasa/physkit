# `CartesianEffectiveMassTensor3D`

`CartesianEffectiveMassTensor3D` is an immutable DataObject defined in
`projectkoios.physkit.solidstate.semiconductors.effmass_3d.tensor`.

It owns a symmetric positive-definite $2\times2$ particle-mass tensor expressed
in the physical Cartesian frame. The tensor unit must agree with the selected
physical `UnitSystem`. Exact symmetry is a construction contract; callers that
obtain a tensor through numerical rotation must explicitly restore the intended
symmetric representation before construction.
