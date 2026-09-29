# `ActionizedDataObject`

## Responsibility

`ActionizedDataObject` provides the typed mechanical delegation shared by
domain façades. A concrete façade constructs its complete request and exposes a
domain action such as `evaluate`; the configured ActionObject owns the actual
operation.

## Local mapping

- Code: `src/python/projectkoios/physkit/core/actions.py::ActionizedDataObject`
- Tests: `tests/projectkoios/physkit/core/actions/test__ActionizedDataObject__respond.py`

## Navigation

- [Module](../index.md)
