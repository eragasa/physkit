# physkit/units/temperature.py
# Author: Eugene Joseph M. Ragasa
"""
Temperature units and conversions.

Implementation is intentionally minimal and explicit.

- Canonical base unit: kelvin (K)
- Explicit affine conversions (scale + offset)
- Stateless, vectorizable
- No unit algebra
- No parsing
- Explicit
"""

from enum import IntEnum


class Temperature:
  """
  Temperature quantity.

  Canonical base unit: K (kelvin)
  """

  class Units(IntEnum):
    # Absolute
    K  = 0

    # SI-adjacent
    C  = 1    # degree Celsius
    mK = 2

    # Imperial / legacy
    F  = 3    # degree Fahrenheit
    R  = 4    # degree Rankine

  # ------------------------------------------------------------------
  # Conversion parameters
  #
  # T[K] = scale * T[unit] + offset
  # ------------------------------------------------------------------

  _SCALE_TO_K = (
    1.0,        # K
    1.0,        # C
    1.0e-3,     # mK
    5.0 / 9.0,  # F
    5.0 / 9.0,  # R
  )

  _OFFSET_TO_K = (
    0.0,        # K
    273.15,     # C → K
    0.0,        # mK
    459.67 * 5.0 / 9.0,  # F → K
    0.0,        # R → K
  )

  @staticmethod
  def convert(*, from_, to: "Temperature.Units"):
    """
    Convert temperature.

    Parameters
    ----------
    from_ : [value, unit_from]
      value : float or numpy.ndarray
      unit_from : Temperature.Units
    to : Temperature.Units

    Returns
    -------
    float or numpy.ndarray
    """
    value, unit_from = from_

    # Convert to canonical (K)
    value_k = (
      value * Temperature._SCALE_TO_K[int(unit_from)]
      + Temperature._OFFSET_TO_K[int(unit_from)]
    )

    # Convert from canonical
    return (
      value_k - Temperature._OFFSET_TO_K[int(to)]
    ) / Temperature._SCALE_TO_K[int(to)]

  # ------------------------------------------------------------------
  # Explicit base helpers
  # ------------------------------------------------------------------
  @staticmethod
  def to_canonical(value, unit: "Temperature.Units"):
    """Convert to base unit (K)."""
    return (
      value * Temperature._SCALE_TO_K[int(unit)]
      + Temperature._OFFSET_TO_K[int(unit)]
    )

  @staticmethod
  def from_canonical(value_k, unit: "Temperature.Units"):
    """Convert from base unit (K)."""
    return (
      value_k - Temperature._OFFSET_TO_K[int(unit)]
    ) / Temperature._SCALE_TO_K[int(unit)]
