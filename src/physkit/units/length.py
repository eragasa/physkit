# physkit/units/length.py
# Eugene Joseph M. Ragasa
"""
Length units and conversions

Implementation is intentionally minimal and explicit.

- Canonical base unit: Pascal (Pa)
- Units represented via fixed lookup table (tuple)
- Stateless, vectorizable
- No unit algebra
- No parsing
- Explicit
"""
from enum import IntEnum

# physkit/units/length.py
#
# Author: Eugene Joseph M. Ragasa
# Affiliation: De La Salle University
#
# Length units and conversions.
# Canonical base unit: meter (m)

from enum import IntEnum


class Length:
  """
  Length quantity.

  Canonical unit: meter (m)
  """

  class Units(IntEnum):
    # SI
    m   = 0
    km  = 1
    cm  = 2
    mm  = 3
    um  = 4
    nm  = 5
    pm  = 7
    A   = 6

    # Imperial / USCS (absolute)
    in_ = 7   # inch (underscore avoids keyword)
    ft  = 8   # foot
    yd  = 9   # yard
    mi  = 10   # mile


  _TO_M = (
    1.0,            # m
    1.0e3,          # km
    1.0e-2,         # cm
    1.0e-3,         # mm
    1.0e-6,         # um
    1.0e-9,         # nm
    1.0e-10,        # pm
    1.0e-10,        # Angstoms
    0.0254,         # inch
    0.3048,         # foot
    0.9144,         # yard
    1609.344,       # mile
  )

  @staticmethod
  def convert(*, from_, to: "Length.Units"):
    """
    Convert length values between units.
    """
    value, unit_from = from_

    value_m = Length._to_canonical(value, unit_from)
    return Length._from_canonical(value_m, to)

  @staticmethod
  def _to_canonical(value, unit: "Length.Units"):
    """Convert value to canonical unit (m)."""
    return value * Length._TO_M[int(unit)]

  @staticmethod
  def _from_canonical(value_m, unit: "Length.Units"):
    """Convert value from canonical unit (m)."""
    return value_m / Length._TO_M[int(unit)]

