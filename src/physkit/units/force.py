# physkit/units/force.py
# Author: Eugene Joseph M. Ragasa
"""
Force units and conversions

Implementation is intentionally minimal and explicity

- Canonical base unit: newton (N)
"""
from enum import IntEnum

class Force:
  """
  Force quantity.

  Canonical unit: newton (N)
  """

  class Units(IntEnum):
    # SI
    N    = 0
    kN   = 1
    MN   = 2

    # CGS
    dyn  = 3   # dyne

    # Imperial / USCS (absolute force)
    lbf  = 4   # pound-force

  _TO_N = (
    1.0,              # N
    1.0e3,            # kN
    1.0e6,            # MN
    1.0e-5,           # dyne (1 dyn = 1e-5 N)
    4.4482216152605,  # lbf
  )

  # ------------------------------------------------------------------
  # Core conversion
  # ------------------------------------------------------------------
  @staticmethod
  def convert(*, from_, to: "Force.Units"):
    """
    Convert force values between units.
    """
    value, unit_from = from_

    value_N = Force._to_canonical(value, unit_from)
    return Force._from_canonical(value_N, to)

  # ------------------------------------------------------------------
  # Internal canonical helpers
  # ------------------------------------------------------------------
  @staticmethod
  def _to_canonical(value, unit: "Force.Units"):
    """Convert value to canonical unit (N)."""
    return value * Force._TO_N[int(unit)]

  @staticmethod
  def _from_canonical(value_N, unit: "Force.Units"):
    """Convert value from canonical unit (N)."""
    return value_N / Force._TO_N[int(unit)]

