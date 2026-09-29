"""Tests for analytical two-dimensional box solution records."""

import numpy as np
import pytest

from projectkoios.physkit.qm.piab2d.base import Piab2D
from projectkoios.physkit.qm.piab2d.tise.analytical.solution import (
    Piab2DAnalyticalSolution,
)
from projectkoios.physkit.units import Unitless, UnitSystem, VectorQuantity


class TestPiab2DAnalyticalSolutionInit:
    """Verify state inventory, energy correlation, and immutable storage."""

    GROUND_QUANTUM_NUMBER = 1
    SECOND_QUANTUM_NUMBER = 2
    UNIT_LENGTH = 1.0
    UNIT_MASS = 1.0

    @classmethod
    def model(cls) -> Piab2D:
        """Return the shared nondimensional unit-square model."""
        return Piab2D(
            length_x=cls.UNIT_LENGTH,
            length_y=cls.UNIT_LENGTH,
            mass=cls.UNIT_MASS,
            unit_system=UnitSystem.NONDIMENSIONAL,
        )

    @staticmethod
    def energies(*magnitudes: float) -> VectorQuantity:
        """Return nondimensional energy values for one test record."""
        return VectorQuantity(
            magnitude=np.array(magnitudes, dtype=np.float64),
            unit=Unitless(),
        )

    def test__init__retains_immutable_state_inventory(self) -> None:
        quantum_numbers = np.array(
            [
                [self.GROUND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
                [self.GROUND_QUANTUM_NUMBER, self.SECOND_QUANTUM_NUMBER],
            ],
            dtype=np.int64,
        )
        solution = Piab2DAnalyticalSolution(
            model=self.model(),
            quantum_numbers=quantum_numbers,
            energies=self.energies(np.pi**2, 2.5 * np.pi**2),
        )
        mutation_sentinel = 9
        quantum_numbers[0, 0] = mutation_sentinel

        expected_quantum_numbers = np.array(
            [
                [self.GROUND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
                [self.GROUND_QUANTUM_NUMBER, self.SECOND_QUANTUM_NUMBER],
            ],
            dtype=np.int64,
        )
        assert np.array_equal(
            solution.quantum_numbers,
            expected_quantum_numbers,
        )
        assert solution.quantum_numbers.flags.writeable is False

    def test__init__rejects_wrong_quantum_number_shape(self) -> None:
        incorrectly_shaped_quantum_numbers = np.array(
            [self.GROUND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
            dtype=np.int64,
        )
        with pytest.raises(ValueError, match="shape"):
            Piab2DAnalyticalSolution(
                model=self.model(),
                quantum_numbers=incorrectly_shaped_quantum_numbers,
                energies=self.energies(np.pi**2),
            )

    def test__init__rejects_nonpositive_quantum_number(self) -> None:
        nonpositive_quantum_number = 0
        with pytest.raises(ValueError, match="must be positive"):
            Piab2DAnalyticalSolution(
                model=self.model(),
                quantum_numbers=np.array(
                    [[nonpositive_quantum_number, self.GROUND_QUANTUM_NUMBER]],
                    dtype=np.int64,
                ),
                energies=self.energies(np.pi**2),
            )

    def test__init__rejects_duplicate_quantum_number_pair(self) -> None:
        duplicate_pair = [
            self.GROUND_QUANTUM_NUMBER,
            self.GROUND_QUANTUM_NUMBER,
        ]
        with pytest.raises(ValueError, match="must be unique"):
            Piab2DAnalyticalSolution(
                model=self.model(),
                quantum_numbers=np.array(
                    [duplicate_pair, duplicate_pair],
                    dtype=np.int64,
                ),
                energies=self.energies(np.pi**2, np.pi**2),
            )

    def test__init__rejects_energy_shape_mismatch(self) -> None:
        quantum_numbers = np.array(
            [
                [self.GROUND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
                [self.GROUND_QUANTUM_NUMBER, self.SECOND_QUANTUM_NUMBER],
            ],
            dtype=np.int64,
        )
        with pytest.raises(ValueError, match="energies must match"):
            Piab2DAnalyticalSolution(
                model=self.model(),
                quantum_numbers=quantum_numbers,
                energies=self.energies(np.pi**2),
            )

    def test__init__rejects_decreasing_energies(self) -> None:
        descending_energy_pairs = np.array(
            [
                [self.GROUND_QUANTUM_NUMBER, self.SECOND_QUANTUM_NUMBER],
                [self.GROUND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
            ],
            dtype=np.int64,
        )
        with pytest.raises(ValueError, match="energies must be nondecreasing"):
            Piab2DAnalyticalSolution(
                model=self.model(),
                quantum_numbers=descending_energy_pairs,
                energies=self.energies(2.5 * np.pi**2, np.pi**2),
            )

    def test__init__rejects_nonlexicographic_equal_energy_pairs(self) -> None:
        reverse_lexicographic_pairs = np.array(
            [
                [self.SECOND_QUANTUM_NUMBER, self.GROUND_QUANTUM_NUMBER],
                [self.GROUND_QUANTUM_NUMBER, self.SECOND_QUANTUM_NUMBER],
            ],
            dtype=np.int64,
        )
        degenerate_energy = 2.5 * np.pi**2
        with pytest.raises(ValueError, match="lexicographically ordered"):
            Piab2DAnalyticalSolution(
                model=self.model(),
                quantum_numbers=reverse_lexicographic_pairs,
                energies=self.energies(degenerate_energy, degenerate_energy),
            )
