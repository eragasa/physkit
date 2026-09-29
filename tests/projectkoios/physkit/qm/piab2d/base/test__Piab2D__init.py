"""Tests for two-dimensional particle-in-a-box model construction."""

import math

import numpy as np
import pytest

from projectkoios.physkit.qm.models.model2d import BaseQuantumModel2D
from projectkoios.physkit.qm.piab2d.base import Piab2D
from projectkoios.physkit.units import UnitSystem


class TestPiab2DInit:
    """Verify model ownership and intrinsic scalar invariants."""

    LENGTH_X = 2.0
    LENGTH_Y = 3.0
    PARTICLE_MASS = 4.0

    def test__init__retains_selected_model_scale(self) -> None:
        model = Piab2D(
            length_x=self.LENGTH_X,
            length_y=self.LENGTH_Y,
            mass=self.PARTICLE_MASS,
            unit_system=UnitSystem.NONDIMENSIONAL,
        )

        assert isinstance(model, BaseQuantumModel2D)
        assert model.dimension == 2
        assert model.length_x == self.LENGTH_X
        assert model.length_y == self.LENGTH_Y
        assert model.mass == self.PARTICLE_MASS
        assert model.unit_system is UnitSystem.NONDIMENSIONAL

    def test__init__rejects_boolean_length(self) -> None:
        invalid_length = True
        with pytest.raises(TypeError, match="length_x must be a built-in float"):
            Piab2D(
                length_x=invalid_length,  # type: ignore[arg-type]
                length_y=self.LENGTH_Y,
                mass=self.PARTICLE_MASS,
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_numpy_scalar_mass(self) -> None:
        invalid_mass = np.float64(self.PARTICLE_MASS)
        with pytest.raises(TypeError, match="mass must be a built-in float"):
            Piab2D(
                length_x=self.LENGTH_X,
                length_y=self.LENGTH_Y,
                mass=invalid_mass,  # type: ignore[arg-type]
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_nonpositive_length(self) -> None:
        nonpositive_length = 0.0
        with pytest.raises(ValueError, match="length_y must be finite and positive"):
            Piab2D(
                length_x=self.LENGTH_X,
                length_y=nonpositive_length,
                mass=self.PARTICLE_MASS,
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_nonfinite_mass(self) -> None:
        nonfinite_mass = math.inf
        with pytest.raises(ValueError, match="mass must be finite and positive"):
            Piab2D(
                length_x=self.LENGTH_X,
                length_y=self.LENGTH_Y,
                mass=nonfinite_mass,
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_non_unit_system(self) -> None:
        invalid_unit_system = "nondimensional"
        with pytest.raises(TypeError, match="unit_system must be UnitSystem"):
            Piab2D(
                length_x=self.LENGTH_X,
                length_y=self.LENGTH_Y,
                mass=self.PARTICLE_MASS,
                unit_system=invalid_unit_system,  # type: ignore[arg-type]
            )
