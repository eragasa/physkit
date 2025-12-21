from dataclasses import dataclass

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
