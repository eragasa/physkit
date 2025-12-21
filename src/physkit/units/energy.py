# physkit/units/energy.py
# Author: Eugene Joseph M. Ragasa
r"""
Energy units and conversions

Implementation is intentionally minimal and explicit

- Canonical base unit: joule (J)

Notes:
- eV is ubiquitous in solid-state physics.
- This module treats eV as an energy unit: 1 eV = q J, where q is the
  elementary charge in coulombs.

LaTeX docstrings use raw strings to avoid backslash-escape issues.
"""
from enum import IntEnum
import math


class Energy:
    r"""
    Energy quantity.

    Canonical unit: joule (J)

    Mathematical meaning:
    $E \in \mathbb{R}$, and when used as a scale, $E = k_B T$, $E=\hbar\omega$, etc.
    """

    class Units(IntEnum):
        # SI
        J   = 0
        kJ  = 1
        MJ  = 2

        # Solid-state / atomic-scale
        meV = 4
        eV  = 3
        keV = 5

        MeV = 6
        GeV = 7

        # CGS
        erg = 8

        # imperial / uscs
        ft_lbf = 9
        in_lbf = 10

    # ------------------------------------------------------------------
    # Unit scale factors to canonical J
    # ------------------------------------------------------------------
    # Exact SI elementary charge (C). 1 eV = q joules.
    _Q = 1.602176634e-19

    _TO_J = (
      1.0,          # J
      1.0e3,        # kJ
      1.0e6,        # MJ

      1.0e-3*_Q,    # meV
      1.0*_Q,       # eV
      1.0e3*_Q,     # keV

      1.0e6*_Q,     # MeV
      1.0e9*_Q,     # GeV

      1.0e-7,       # erg

      1.3558179483314,     # ft·lbf
      1.3558179483314/12,  # in·lbf
    )

    # ------------------------------------------------------------------
    # Core conversion
    # ------------------------------------------------------------------
    @staticmethod
    def convert(*, from_, to: "Energy.Units"):
        """
        Convert energy values between units.
        """
        value, unit_from = from_

        value_J = Energy._to_canonical(value, unit_from)
        return Energy._from_canonical(value_J, to)

    # ------------------------------------------------------------------
    # Internal canonical helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _to_canonical(value, unit: "Energy.Units"):
        """Convert value to canonical unit (J)."""
        return value * Energy._TO_J[int(unit)]

    @staticmethod
    def _from_canonical(value_J, unit: "Energy.Units"):
        """Convert value from canonical unit (J)."""
        return value_J / Energy._TO_J[int(unit)]
