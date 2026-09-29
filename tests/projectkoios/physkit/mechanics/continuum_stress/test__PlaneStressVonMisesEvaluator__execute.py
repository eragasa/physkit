"""Tests for plane-stress von Mises equivalent stress."""

import math

import numpy as np
import pytest
from numpy.typing import NDArray

from projectkoios.physkit.mechanics.continuum_stress import (
    PlaneStressVonMisesEvaluator,
)


class TestPlaneStressVonMisesEvaluatorExecute:
    """Verify plane-stress formula, symmetrization, and input contracts."""

    def test__execute__returns_uniaxial_stress_magnitude(self) -> None:
        stress_tensor = np.array([[100.0, 0.0], [0.0, 0.0]], dtype=np.float64)

        result = PlaneStressVonMisesEvaluator().execute(stress_tensor)

        assert result == pytest.approx(100.0, rel=0.0, abs=1e-14)

    def test__execute__returns_pure_shear_equivalent_stress(self) -> None:
        stress_tensor = np.array([[0.0, 25.0], [25.0, 0.0]], dtype=np.float64)

        result = PlaneStressVonMisesEvaluator().execute(stress_tensor)

        assert result == pytest.approx(25.0 * math.sqrt(3.0), rel=1e-15, abs=0.0)

    def test__execute__averages_off_diagonal_pair_without_mutation(self) -> None:
        stress_tensor = np.array([[100.0, 20.0], [30.0, 40.0]], dtype=np.float64)
        before = stress_tensor.copy()

        result = PlaneStressVonMisesEvaluator().execute(stress_tensor)

        expected = math.sqrt(100.0**2 - 100.0 * 40.0 + 40.0**2 + 3.0 * 25.0**2)
        assert result == pytest.approx(expected, rel=1e-15, abs=0.0)
        np.testing.assert_array_equal(stress_tensor, before)

    @pytest.mark.parametrize(
        "stress_tensor",
        [
            np.zeros((2, 2), dtype=np.float32),
            np.zeros((2, 2), dtype=np.int64),
            np.zeros((2, 2), dtype=np.bool_),
        ],
        ids=["float32", "int64", "boolean"],
    )
    def test__execute__rejects_non_float64_array(
        self,
        stress_tensor: NDArray[np.float32] | NDArray[np.int64] | NDArray[np.bool_],
    ) -> None:
        with pytest.raises(TypeError, match="float64 dtype"):
            PlaneStressVonMisesEvaluator().execute(  # type: ignore[arg-type]
                stress_tensor
            )

    @pytest.mark.parametrize(
        "shape",
        [(1,), (2,), (1, 2), (2, 3), (3, 3)],
        ids=[
            "vector-one",
            "vector-two",
            "one-by-two",
            "two-by-three",
            "three-by-three",
        ],
    )
    def test__execute__rejects_wrong_shape(self, shape: tuple[int, ...]) -> None:
        stress_tensor = np.zeros(shape, dtype=np.float64)

        with pytest.raises(ValueError, match=r"shape \(2, 2\)"):
            PlaneStressVonMisesEvaluator().execute(stress_tensor)

    @pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
    def test__execute__rejects_nonfinite_entry(self, value: float) -> None:
        stress_tensor = np.array([[value, 0.0], [0.0, 0.0]], dtype=np.float64)

        with pytest.raises(ValueError, match="only finite values"):
            PlaneStressVonMisesEvaluator().execute(stress_tensor)

    def test__execute__rejects_nonarray_input(self) -> None:
        with pytest.raises(TypeError, match="must be a NumPy array"):
            PlaneStressVonMisesEvaluator().execute(  # type: ignore[arg-type]
                [[1.0, 0.0], [0.0, 0.0]]
            )
