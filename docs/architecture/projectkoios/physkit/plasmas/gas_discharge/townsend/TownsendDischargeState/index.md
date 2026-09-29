# `TownsendDischargeState`

## Responsibility

`TownsendDischargeState` is an immutable DataObject containing primary current,
first Townsend coefficient, gap length, and secondary-emission coefficient. It
owns the intrinsic avalanche gain and feedback factor.

## Contract

Every field is a nonnegative finite built-in float. Current uses amperes, the
Townsend coefficient uses reciprocal metres, gap length uses metres, and the
secondary-emission coefficient is dimensionless.

The derived values are

$$
M=\exp(\!\alpha d),
\qquad
r=\gamma_e(M-1).
$$

Gain overflow produces positive infinity.

## Local mapping

- Code: `src/python/projectkoios/physkit/plasmas/gas_discharge/townsend.py::TownsendDischargeState`
- Tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendDischargeState__init.py`
- Property tests: `tests/projectkoios/physkit/plasmas/gas_discharge/townsend/test__TownsendDischargeState__derived_properties.py`

## Navigation

- [Module](../index.md)
