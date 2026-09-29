# `TwistGaugeBridgeConstructor` testing

## Strategy

The constructor test uses a three-site nearest-neighbor ring with a quarter-turn
twist. Expected diagonal phases and the transformed quotient-seam matrix are
hand-derived rather than produced by a second call to the constructor.

| Evidence kind | Current result |
| --- | --- |
| Implementation conformance | Supported: exact fiber roles, direction convention, and sparse diagonal values are asserted. |
| Numerical verification | Supported: maximum elementwise absolute comparison with tolerance `1e-15` under NumPy/SciPy on CPython 3.14. |
| Scientific validation | Not evaluated: no independent physical dataset or declared-use validation protocol is tested. |
| Human acceptance | Not evaluated: the test does not represent a human scientific decision. |

## Local mapping

- `tests/projectkoios/physkit/periodic/lattice/gauge_bridges/test__TwistGaugeBridgeConstructor__execute.py::test__execute__matches_diagonal_phases_and_declared_seam_relation`

## Limitations

The fixture covers one one-dimensional domain and one nonzero twist. Separate
result and analyzer tests cover invariant rejection and compatibility gates. No
general physical gauge-invariance claim follows from this finite fixture.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Mathematics](../mathematics/index.md)
