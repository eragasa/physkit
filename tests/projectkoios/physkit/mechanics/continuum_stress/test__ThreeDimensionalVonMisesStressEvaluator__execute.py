"""Tests for three-dimensional von Mises equivalent stress."""

import math

import numpy as np
import pytest
from numpy.typing import NDArray

from projectkoios.physkit.mechanics.continuum_stress import (
    ThreeDimensionalVonMisesStressEvaluator,
)


class TestThreeDimensionalVonMisesStressEvaluatorExecute:
    """Verify 3D formula, symmetrization, and input contracts."""

    def test__execute__returns_zero_for_hydrostatic_stress(self) -> None:
        stress_tensor = 75.0 * np.eye(3, dtype=np.float64)

        result = ThreeDimensionalVonMisesStressEvaluator().execute(stress_tensor)

        assert result == 0.0

    def test__execute__returns_uniaxial_stress_magnitude(self) -> None:
        stress_tensor = np.diag(np.array([100.0, 0.0, 0.0], dtype=np.float64))

        result = ThreeDimensionalVonMisesStressEvaluator().execute(stress_tensor)

        assert result == pytest.approx(100.0, rel=0.0, abs=1e-14)

    def test__execute__returns_pure_shear_equivalent_stress(self) -> None:
        stress_tensor = np.array(
            [[0.0, 25.0, 0.0], [25.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            dtype=np.float64,
        )

        result = ThreeDimensionalVonMisesStressEvaluator().execute(stress_tensor)

        assert result == pytest.approx(25.0 * math.sqrt(3.0), rel=1e-15, abs=0.0)

    def test__execute__averages_all_off_diagonal_pairs_without_mutation(self) -> None:
        stress_tensor = np.array(
            [[80.0, 10.0, 18.0], [14.0, 20.0, 6.0], [22.0, 8.0, -10.0]],
            dtype=np.float64,
        )
        before = stress_tensor.copy()

        result = ThreeDimensionalVonMisesStressEvaluator().execute(stress_tensor)

        tau_xy = 12.0
        tau_xz = 20.0
        tau_yz = 7.0
        expected = math.sqrt(
            0.5 * ((80.0 - 20.0) ** 2 + (20.0 + 10.0) ** 2 + (-10.0 - 80.0) ** 2)
            + 3.0 * (tau_xy**2 + tau_xz**2 + tau_yz**2)
        )
        assert result == pytest.approx(expected, rel=1e-15, abs=0.0)
        np.testing.assert_array_equal(stress_tensor, before)

    def test__execute__agrees_with_plane_stress_embedding(self) -> None:
        in_plane = np.array([[100.0, 25.0], [25.0, 40.0]], dtype=np.float64)
        stress_tensor = np.zeros((3, 3), dtype=np.float64)
        stress_tensor[:2, :2] = in_plane
        expected = math.sqrt(100.0**2 - 100.0 * 40.0 + 40.0**2 + 3.0 * 25.0**2)

        result = ThreeDimensionalVonMisesStressEvaluator().execute(stress_tensor)

        assert result == pytest.approx(expected, rel=1e-15, abs=0.0)

    @pytest.mark.parametrize(
        "stress_tensor",
        [
            np.zeros((3, 3), dtype=np.float32),
            np.zeros((3, 3), dtype=np.int64),
            np.zeros((3, 3), dtype=np.bool_),
        ],
        ids=["float32", "int64", "boolean"],
    )
    def test__execute__rejects_non_float64_array(
        self,
        stress_tensor: NDArray[np.float32] | NDArray[np.int64] | NDArray[np.bool_],
    ) -> None:
        with pytest.raises(TypeError, match="float64 dtype"):
            ThreeDimensionalVonMisesStressEvaluator().execute(  # type: ignore[arg-type]
                stress_tensor
            )

    @pytest.mark.parametrize(
        "shape",
        [(1,), (3,), (2, 2), (2, 3), (3, 2)],
        ids=[
            "vector-one",
            "vector-three",
            "two-by-two",
            "two-by-three",
            "three-by-two",
        ],
    )
    def test__execute__rejects_wrong_shape(self, shape: tuple[int, ...]) -> None:
        stress_tensor = np.zeros(shape, dtype=np.float64)

        with pytest.raises(ValueError, match=r"shape \(3, 3\)"):
            ThreeDimensionalVonMisesStressEvaluator().execute(stress_tensor)

    @pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
    def test__execute__rejects_nonfinite_entry(self, value: float) -> None:
        stress_tensor = np.array(
            [[value, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            dtype=np.float64,
        )

        with pytest.raises(ValueError, match="only finite values"):
            ThreeDimensionalVonMisesStressEvaluator().execute(stress_tensor)

    def test__execute__rejects_nonarray_input(self) -> None:
        with pytest.raises(TypeError, match="must be a NumPy array"):
            ThreeDimensionalVonMisesStressEvaluator().execute(  # type: ignore[arg-type]
                [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
            )
