# Testing

The class-owned tests verify:

- normalized unit-cube midplane evaluation;
- homogeneous-Dirichlet boundary zeros;
- `X`, `Y`, and `Z` plane-normal mappings;
- analytical integrated plane density;
- physical-coordinate unit conversion;
- physical eigenfunction-amplitude and integrated-density units;
- complete-plane zeros at fixed-axis nodes; and
- rejection of a fixed coordinate outside the box.

These checks establish software and numerical agreement with the documented
separable-box equations. They do not constitute independent scientific
validation.

## Evidence mapping

- `tests/projectkoios/physkit/qm/piab3d/tise/analytical/eigenfunctions/test__Piab3DAnalyticalEigenfunction__evaluate_plane_slice.py`
- `tests/projectkoios/physkit/qm/piab3d/tise/analytical/eigenfunctions/test__Piab3DAnalyticalEigenfunctionPlaneSlice__init.py`
- `tests/projectkoios/physkit/qm/piab3d/tise/analytical/eigenfunctions/test__Piab3DPlaneNormal__members.py`

## Navigation

- [Implementation](../index.md)
