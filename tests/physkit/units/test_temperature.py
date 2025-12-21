# tests/physkit/units/test_temperature.py

import numpy as np
import pytest

from physkit.units import Temperature
from physkit.units._protocols import QuantityProtocol


# ---------------------------------------------------------------------
# API / protocol compliance
# ---------------------------------------------------------------------

@pytest.mark.unit
def test_temperature_conforms_to_quantity_protocol():
  assert isinstance(Temperature, QuantityProtocol)


@pytest.mark.unit
def test_units_is_intenum():
  from enum import IntEnum
  assert issubclass(Temperature.Units, IntEnum)


# ---------------------------------------------------------------------
# Canonical unit sanity
# ---------------------------------------------------------------------

@pytest.mark.unit
def test_canonical_unit_is_kelvin():
  val = Temperature.convert(
    from_=[1.0, Temperature.Units.K],
    to=Temperature.Units.K
  )
  assert val == 1.0


# ---------------------------------------------------------------------
# Known reference conversions (scalar)
# ---------------------------------------------------------------------

@pytest.mark.unit
def test_c_to_k_freezing_point():
  val = Temperature.convert(
    from_=[0.0, Temperature.Units.C],
    to=Temperature.Units.K
  )
  assert abs(val - 273.15) < 1e-12


@pytest.mark.unit
def test_k_to_c_freezing_point():
  val = Temperature.convert(
    from_=[273.15, Temperature.Units.K],
    to=Temperature.Units.C
  )
  assert abs(val - 0.0) < 1e-12


@pytest.mark.unit
def test_f_to_c_freezing_point():
  val = Temperature.convert(
    from_=[32.0, Temperature.Units.F],
    to=Temperature.Units.C
  )
  assert abs(val - 0.0) < 1e-12


@pytest.mark.unit
def test_c_to_f_freezing_point():
  val = Temperature.convert(
    from_=[0.0, Temperature.Units.C],
    to=Temperature.Units.F
  )
  assert abs(val - 32.0) < 1e-12


@pytest.mark.unit
def test_f_to_k_absolute_zero():
  val = Temperature.convert(
    from_=[-459.67, Temperature.Units.F],
    to=Temperature.Units.K
  )
  assert abs(val - 0.0) < 1e-10


@pytest.mark.unit
def test_r_to_k():
  val = Temperature.convert(
    from_=[491.67, Temperature.Units.R],
    to=Temperature.Units.K
  )
  assert abs(val - 273.15) < 1e-10


@pytest.mark.unit
def test_mk_to_k():
  val = Temperature.convert(
    from_=[1000.0, Temperature.Units.mK],
    to=Temperature.Units.K
  )
  assert abs(val - 1.0) < 1e-12


# ---------------------------------------------------------------------
# Round-trip invariants (affine sanity)
# ---------------------------------------------------------------------

@pytest.mark.unit
@pytest.mark.parametrize("unit", list(Temperature.Units))
def test_round_trip_scalar(unit):
  x = 123.456
  y = Temperature.convert(from_=[x, unit], to=Temperature.Units.K)
  z = Temperature.convert(from_=[y, Temperature.Units.K], to=unit)
  assert abs(z - x) < 1e-12


# ---------------------------------------------------------------------
# Vectorization behavior
# ---------------------------------------------------------------------

@pytest.mark.unit
def test_vectorized_conversion_c_to_k():
  arr = np.array([-40.0, 0.0, 100.0])
  out = Temperature.convert(
    from_=[arr, Temperature.Units.C],
    to=Temperature.Units.K
  )
  assert isinstance(out, np.ndarray)
  assert np.allclose(out, arr + 273.15)


@pytest.mark.unit
def test_vectorized_conversion_f_to_c():
  arr = np.array([-40.0, 32.0, 212.0])
  out = Temperature.convert(
    from_=[arr, Temperature.Units.F],
    to=Temperature.Units.C
  )
  assert isinstance(out, np.ndarray)
  assert np.allclose(out, (arr - 32.0) * (5.0 / 9.0))


# ---------------------------------------------------------------------
# Consistency between absolute scales
# ---------------------------------------------------------------------

@pytest.mark.unit
def test_k_and_r_affine_consistency():
  k = 300.0
  r = Temperature.convert(from_=[k, Temperature.Units.K], to=Temperature.Units.R)
  k2 = Temperature.convert(from_=[r, Temperature.Units.R], to=Temperature.Units.K)
  assert abs(k2 - k) < 1e-12


# ---------------------------------------------------------------------
# Error behavior (minimal but explicit)
# ---------------------------------------------------------------------

@pytest.mark.unit
def test_invalid_unit_raises():
  class FakeUnit:
    pass

  with pytest.raises(Exception):
    Temperature.convert(from_=[1.0, FakeUnit()], to=Temperature.Units.K)
