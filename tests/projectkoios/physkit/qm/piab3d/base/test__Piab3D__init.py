"""Tests for three-dimensional particle-in-a-box model construction."""

import math

import numpy as np
import pytest

from projectkoios.physkit.qm.models.model3d import BaseQuantumModel3D
from projectkoios.physkit.qm.piab3d.base import Piab3D
from projectkoios.physkit.units import UnitSystem


class TestPiab3DInit:
    """Verify model ownership and intrinsic scalar invariants."""

    LENGTH_X = 2.0
    LENGTH_Y = 3.0
    LENGTH_Z = 4.0
    PARTICLE_MASS = 5.0

    def test__init__retains_selected_model_scale(self) -> None:
        model = Piab3D(
            length_x=self.LENGTH_X,
            length_y=self.LENGTH_Y,
            length_z=self.LENGTH_Z,
            mass=self.PARTICLE_MASS,
            unit_system=UnitSystem.NONDIMENSIONAL,
        )

        assert isinstance(model, BaseQuantumModel3D)
        assert model.dimension == 3
        assert model.length_x == self.LENGTH_X
        assert model.length_y == self.LENGTH_Y
        assert model.length_z == self.LENGTH_Z
        assert model.mass == self.PARTICLE_MASS
        assert model.unit_system is UnitSystem.NONDIMENSIONAL

    def test__init__rejects_boolean_length(self) -> None:
        invalid_length = True
        with pytest.raises(TypeError, match="length_z must be a built-in float"):
            Piab3D(
                length_x=self.LENGTH_X,
                length_y=self.LENGTH_Y,
                length_z=invalid_length,  # type: ignore[arg-type]
                mass=self.PARTICLE_MASS,
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_numpy_scalar_mass(self) -> None:
        invalid_mass = np.float64(self.PARTICLE_MASS)
        with pytest.raises(TypeError, match="mass must be a built-in float"):
            Piab3D(
                length_x=self.LENGTH_X,
                length_y=self.LENGTH_Y,
                length_z=self.LENGTH_Z,
                mass=invalid_mass,  # type: ignore[arg-type]
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_nonpositive_length(self) -> None:
        nonpositive_length = 0.0
        with pytest.raises(ValueError, match="length_y must be finite and positive"):
            Piab3D(
                length_x=self.LENGTH_X,
                length_y=nonpositive_length,
                length_z=self.LENGTH_Z,
                mass=self.PARTICLE_MASS,
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_nonfinite_mass(self) -> None:
        nonfinite_mass = math.inf
        with pytest.raises(ValueError, match="mass must be finite and positive"):
            Piab3D(
                length_x=self.LENGTH_X,
                length_y=self.LENGTH_Y,
                length_z=self.LENGTH_Z,
                mass=nonfinite_mass,
                unit_system=UnitSystem.NONDIMENSIONAL,
            )

    def test__init__rejects_non_unit_system(self) -> None:
        invalid_unit_system = "nondimensional"
        with pytest.raises(TypeError, match="unit_system must be UnitSystem"):
            Piab3D(
                length_x=self.LENGTH_X,
                length_y=self.LENGTH_Y,
                length_z=self.LENGTH_Z,
                mass=self.PARTICLE_MASS,
                unit_system=invalid_unit_system,  # type: ignore[arg-type]
            )
