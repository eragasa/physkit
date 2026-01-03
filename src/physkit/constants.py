from typing import Protocol
from dataclasses import dataclass
import math

class PhysicalConstantsProtocol(Protocol):
  """ Structural type for any constant container."""
  a0: float   # length, Bohr radius
  q: float    # charge, elementary charge
  k_B: float  # energy/temperature, Boltzmann constant
  eps0: float # force/length, vacuum permittivity
  me0: float  # mass, electron rest mass
  N_A: float  # per mol, Avogadro constant
  R_g: float  # energy/mol/temperature, gas constant
  h: float    # planck's constant
  hbar: float # reduced planck's constant

@dataclass(frozen=True)
class ConstantsSI:
    """
    Physical constants in SI units.
    """
    a0: float   = 5.29177210903e-11   # m, Bohr radius
    q: float    = 1.602176634e-19     # C, elementary charge
    k_B: float  = 1.380649e-23        # J/K, Boltzmann constant
    eps0: float = 8.854187812e-12     # F/m, vacuum permittivity
    me0: float  = 9.1093837015e-31    # kg, electron rest mass
    N_A: float  = 6.02214076e23       # 1/mol, Avogadro constant
    R_g: float  = 8.314462618         # J/mol/K, gas constant
    h: float    = 6.62607015e-34      # J s, Planck's Constant
    hbar: float = h / (2.0 * math.pi) # J·s, reduced planck's constant

from dataclasses import dataclass

@dataclass(frozen=True)
class ConstantsCGS:
    """
    Physical constants in CGS units.
    """
    a0: float   = 5.29177210903e-9    # cm, Bohr radius
    q: float    = 4.80320471e-10      # statC (esu), elementary charge
    k_B: float  = 1.380649e-16        # erg/K, Boltzmann constant
    eps0: float = 1.0                 # Dimensionless in Gaussian CGS
    me0: float  = 9.1093837015e-28    # g, electron rest mass
    N_A: float  = 6.02214076e23       # 1/mol, Avogadro constant
    R_g: float  = 8.314462618e7       # erg/mol/K, gas constant
    h: float    = 6.62607015e-27      # erg s, planck's constant
    hbar: float = h / (2.0 * math.pi) # erg·s, reduced planck's constant
