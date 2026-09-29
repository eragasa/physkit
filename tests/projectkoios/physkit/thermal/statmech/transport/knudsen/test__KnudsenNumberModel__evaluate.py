"""Evaluation tests for ``KnudsenNumberModel``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.statmech.transport.knudsen import (
    KnudsenNumberModel,
)
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestKnudsenNumberModelEvaluate:
    """Verify unit-aware dimensionless mean-free-path ratios."""

    def test__evaluate_converts_lengths_and_returns_unitless_ratios(self) -> None:
        model = KnudsenNumberModel(
            characteristic_length=ScalarQuantity(
                magnitude=1.0,
                unit=PhysicalUnit(expression="millimeter"),
            )
        )
        mean_free_paths = VectorQuantity(
            magnitude=np.array([1.0e-6, 1.0e-3, 1.0], dtype=np.float64),
            unit=PhysicalUnit(expression="meter"),
        )

        evaluation = model.evaluate(mean_free_paths=mean_free_paths)

        assert evaluation.request.model is model
        assert evaluation.request.mean_free_paths is mean_free_paths
        np.testing.assert_allclose(
            evaluation.knudsen_numbers.magnitude,
            np.array([1.0e-3, 1.0, 1.0e3], dtype=np.float64),
            rtol=0.0,
            atol=0.0,
        )
        assert isinstance(evaluation.knudsen_numbers.unit, Unitless)

    def test__evaluate_rejects_nonpositive_mean_free_path(self) -> None:
        model = KnudsenNumberModel(
            characteristic_length=ScalarQuantity(
                magnitude=1.0,
                unit=PhysicalUnit(expression="meter"),
            )
        )

        with pytest.raises(ValueError, match="mean_free_paths must be positive"):
            model.evaluate(
                mean_free_paths=VectorQuantity(
                    magnitude=np.array([0.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="meter"),
                )
            )
