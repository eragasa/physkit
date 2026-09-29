"""Solve tests for ``FermiDiracChemicalPotentialSolver``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.statmech.qm import FermiDiracChemicalPotentialSolver
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestFermiDiracChemicalPotentialSolverSolve:
    """Verify finite-level particle-number inversion."""

    OCCUPATION_TOLERANCE = 1.0e-12

    def test__solve_recovers_symmetric_half_filling(self) -> None:
        unit = PhysicalUnit(expression="electron_volt")
        energies = VectorQuantity(
            magnitude=np.array([0.0, 1.0, 2.0, 3.0], dtype=np.float64),
            unit=unit,
        )
        thermal_energy = ScalarQuantity(magnitude=0.2, unit=unit)
        target_occupation = ScalarQuantity(magnitude=2.0, unit=Unitless())
        solver = FermiDiracChemicalPotentialSolver()

        result = solver.solve(
            energies=energies,
            thermal_energy=thermal_energy,
            target_occupation=target_occupation,
        )

        assert result.request.solver is solver
        assert result.request.energies is energies
        assert result.request.thermal_energy is thermal_energy
        assert result.target_occupation is target_occupation
        assert np.isclose(
            result.chemical_potential.magnitude,
            1.5,
            rtol=0.0,
            atol=1.0e-13,
        )
        assert isinstance(result.occupation_residual.unit, Unitless)
        assert abs(result.occupation_residual.magnitude) <= self.OCCUPATION_TOLERANCE
        assert np.isclose(
            np.sum(result.occupations.magnitude),
            target_occupation.magnitude,
            rtol=0.0,
            atol=self.OCCUPATION_TOLERANCE,
        )

    @pytest.mark.parametrize(
        "target_occupation",
        [0.0, 4.0, -1.0, 5.0],
        ids=["zero", "level-count", "negative", "above-level-count"],
    )
    def test__solve_rejects_unattainable_finite_chemical_potential_targets(
        self,
        target_occupation: float,
    ) -> None:
        unit = PhysicalUnit(expression="joule")

        with pytest.raises(ValueError, match="strictly between zero and level count"):
            FermiDiracChemicalPotentialSolver().solve(
                energies=VectorQuantity(
                    magnitude=np.arange(4, dtype=np.float64),
                    unit=unit,
                ),
                thermal_energy=ScalarQuantity(magnitude=1.0, unit=unit),
                target_occupation=ScalarQuantity(
                    magnitude=target_occupation,
                    unit=Unitless(),
                ),
            )

    def test__solve_rejects_empty_energy_inventory(self) -> None:
        unit = PhysicalUnit(expression="joule")

        with pytest.raises(ValueError, match="energies must be nonempty"):
            FermiDiracChemicalPotentialSolver().solve(
                energies=VectorQuantity(
                    magnitude=np.array([], dtype=np.float64),
                    unit=unit,
                ),
                thermal_energy=ScalarQuantity(magnitude=1.0, unit=unit),
                target_occupation=ScalarQuantity(
                    magnitude=1.0,
                    unit=Unitless(),
                ),
            )

    def test__solve_rejects_physical_target_occupation_units(self) -> None:
        energy_unit = PhysicalUnit(expression="joule")

        with pytest.raises(ValueError, match="target_occupation must be unitless"):
            FermiDiracChemicalPotentialSolver().solve(
                energies=VectorQuantity(
                    magnitude=np.arange(4, dtype=np.float64),
                    unit=energy_unit,
                ),
                thermal_energy=ScalarQuantity(
                    magnitude=1.0,
                    unit=energy_unit,
                ),
                target_occupation=ScalarQuantity(
                    magnitude=2.0,
                    unit=PhysicalUnit(expression="mole"),
                ),
            )
