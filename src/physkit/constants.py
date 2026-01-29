# physkit/constants.py
# Eugene Joseph M. Ragasa 2025-2026

r"""
Physical constants containers (SI and CGS/Gaussian).

Design goals
------------
- Minimal and explicit: no unit algebra, no parsing, no dependencies.
- Constants are provided as simple immutable dataclass containers.
- Intended for direct numerical work and reproducible pedagogy.
- A structural Protocol defines the minimum attribute set expected by downstream code.

Important caveat about "CGS"
----------------------------
`ConstantsCGS` below is specifically **Gaussian CGS (esu)** for charge.
In Gaussian CGS, $\varepsilon_0$ is not used as a dimensional constant in the
formulas (Coulomb's law is written without $\varepsilon_0$). We include `eps0`
only to satisfy a uniform structural interface; it is set to `1.0` and should
be treated as a **placeholder**, not as an SI-like permittivity.

Units summary
-------------
ConstantsSI:
- a0   [m]
- q    [C]
- k_B  [J/K]
- eps0 [F/m]
- me0  [kg]
- N_A  [1/mol]
- R_g  [J/(mol K)]
- h    [J s]
- hbar [J s]
- m_u  [kg]   atomic mass constant (u, dalton)
- m_u_u [kg]  standard uncertainty for m_u

ConstantsCGS (Gaussian/esu):
- a0   [cm]
- q    [statC] (esu)
- k_B  [erg/K]
- eps0 [dimensionless placeholder (=1.0)]
- me0  [g]
- N_A  [1/mol]
- R_g  [erg/(mol K)]
- h    [erg s]
- hbar [erg s]
- m_u  [g]
- m_u_u [g]
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable
from dataclasses import dataclass
import math


# -----------------------------------------------------------------------------
# Protocol (structural interface)
# -----------------------------------------------------------------------------
@runtime_checkable
class PhysicalConstantsProtocol(Protocol):
  r"""
  Structural type for a "constants container".

  Purpose
  -------
  Downstream code may depend on a small set of named constants without tying
  itself to a specific container class. This Protocol defines that minimal
  attribute set.

  Runtime behavior
  ---------------
  - `@runtime_checkable` enables `isinstance(obj, PhysicalConstantsProtocol)`.
  - This checks only that the attributes exist (structural check).
  - It does NOT validate numeric values, units, or dimensional consistency.

  Required attributes
  -------------------
  All attributes are required to exist on the container object.

  Notes on eps0
  -------------
  `eps0` is an SI concept. In Gaussian CGS it is not used in the same way.
  If you use a CGS container, treat `eps0` as a placeholder unless your
  formula set is explicitly written to use it.
  """

  a0: float     # Bohr radius
  q: float      # elementary charge
  k_B: float    # Boltzmann constant
  eps0: float   # vacuum permittivity (SI; placeholder in Gaussian CGS)
  me0: float    # electron rest mass
  N_A: float    # Avogadro constant
  R_g: float    # molar gas constant
  h: float      # Planck constant
  hbar: float   # reduced Planck constant
  m_u: float    # atomic mass constant (u, dalton)
  m_u_u: float  # standard uncertainty of m_u (same units as m_u)


# -----------------------------------------------------------------------------
# SI constants
# -----------------------------------------------------------------------------
@dataclass(frozen=True)
class ConstantsSI:
    r"""
    Physical constants in SI units.

    Policy
    ------
    - This container stores numerical values in SI base/derived units.
    - Some constants are exact by SI definition (e.g., q, k_B, N_A, h).
      Others are experimentally determined (e.g., eps0, me0, a0).
    - Values are intended to be stable references for computation.

    Attribute units
    ---------------
    a0   [m]
    q    [C]
    k_B  [J/K]
    eps0 [F/m]
    me0  [kg]
    N_A  [1/mol]
    R_g  [J/(mol K)]
    h    [J s]
    hbar [J s]
    m_u  [kg]
    m_u_u [kg]
    """
    a0: float   = 5.29177210903e-11   # m, Bohr radius
    q: float    = 1.602176634e-19     # C
    k_B: float  = 1.380649e-23        # J/K
    eps0: float = 8.854187812e-12     # F/m
    me0: float  = 9.1093837015e-31    # kg
    N_A: float  = 6.02214076e23       # 1/mol
    R_g: float  = 8.314462618         # J/(mol K)
    h: float    = 6.62607015e-34      # J s
    hbar: float = h / (2.0 * math.pi) # J s
    m_u: float  = 1.660_539_068_92e-27   # kg
    m_u_u: float = 0.000_000_000_52e-27  # kg

# -----------------------------------------------------------------------------
# CGS (Gaussian / esu) constants
# -----------------------------------------------------------------------------
@dataclass(frozen=True)
class ConstantsCGS:
    r"""
    Physical constants in Gaussian CGS (esu) units.

    Scope
    -----
    This container is for computations written consistently in Gaussian CGS.
    It is NOT intended to be mixed with SI formulas unless you explicitly
    convert units and rewrite electromagnetic relations appropriately.

    eps0 warning
    ------------
    In Gaussian CGS, $\varepsilon_0$ is not a dimensional constant in the
    Maxwell/Coulomb relations. We keep `eps0 = 1.0` as a placeholder ONLY
    to satisfy `PhysicalConstantsProtocol`. Do not interpret it as an SI-like
    permittivity.

    Attribute units
    ---------------
    a0   [cm]
    q    [statC] (esu)
    k_B  [erg/K]
    eps0 [dimensionless placeholder (=1.0)]
    me0  [g]
    N_A  [1/mol]
    R_g  [erg/(mol K)]
    h    [erg s]
    hbar [erg s]
    m_u  [g]
    m_u_u [g]
    """
    a0: float   = 5.29177210903e-9       # cm, Bohr radius (1 m = 100 cm)
    q: float    = 4.80320471e-10         # statC (esu)
    k_B: float  = 1.380649e-16           # erg/K  (1 J = 1e7 erg)
    eps0: float = 1.0
    me0: float  = 9.1093837015e-28       # g
    N_A: float  = 6.02214076e23          # 1/mol
    R_g: float  = 8.314462618e7          # erg/(mol K)
    h: float    = 6.62607015e-27         # erg s
    hbar: float = h / (2.0 * math.pi)    # erg s
    m_u: float  = 1.660_539_068_92e-24   # g
    m_u_u: float = 0.000_000_000_52e-24  # g
