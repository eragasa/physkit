
@dataclass(frozen=True)
class Species:
    """
    Physical species metadata for Hertz–Knudsen modeling.
    """
    name: str
    molar_mass: float #g/mol
    density: float    #g/cm^3 (solid film density, for thickness rate)

    @property
    def m_kg(self) -> float:
        """Molecular/atomic mass in kg."""
        return self.molar_mass_kg_per_mol / NA