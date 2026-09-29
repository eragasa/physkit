# `Piab2D`

## Responsibility

`Piab2D` is an immutable DataObject representing a particle of selected mass on
`[0, length_x] × [0, length_y]` with homogeneous Dirichlet boundaries. The
selected `UnitSystem` supplies coherent length, mass, action, and energy units.

Construction is keyword-only. Each numerical parameter must be a finite
positive built-in float. The model owns no state enumeration or solution
algorithm.

## Local mapping

- Code: `src/python/projectkoios/physkit/qm/piab2d/base.py::Piab2D`
- Construction tests: `tests/projectkoios/physkit/qm/piab2d/base/test__Piab2D__init.py`
- Quantity tests: `tests/projectkoios/physkit/qm/piab2d/base/test__Piab2D__quantities.py`

## Navigation

- [Module](../index.md)
