"""Evaluation tests for ``CanonicalLevelProbabilityModel``."""

import numpy as np
import pytest

from projectkoios.physkit.thermal.statmech.qm import CanonicalLevelProbabilityModel
from projectkoios.physkit.units import (
    PhysicalUnit,
    ScalarQuantity,
    Unitless,
    VectorQuantity,
)


class TestCanonicalLevelProbabilityModelEvaluate:
    """Verify stable normalized finite-level canonical probabilities."""

    @staticmethod
    def _model(
        *,
        thermal_energy: float,
        unit: PhysicalUnit,
    ) -> CanonicalLevelProbabilityModel:
        return CanonicalLevelProbabilityModel(
            thermal_energy=ScalarQuantity(
                magnitude=thermal_energy,
                unit=unit,
            )
        )

    def test__evaluate_is_normalized_and_invariant_under_energy_shift(self) -> None:
        unit = PhysicalUnit(expression="electron_volt")
        model = self._model(thermal_energy=0.5, unit=unit)
        base_energies = VectorQuantity(
            magnitude=np.array([0.0, 1.0, 2.0], dtype=np.float64),
            unit=unit,
        )
        shifted_energies = VectorQuantity(
            magnitude=np.array([1000.0, 1001.0, 1002.0], dtype=np.float64),
            unit=unit,
        )

        base = model.evaluate(energies=base_energies)
        shifted = model.evaluate(energies=shifted_energies)

        assert base.request.model is model
        assert base.request.energies is base_energies
        assert isinstance(base.probabilities.unit, Unitless)
        assert np.isclose(
            np.sum(base.probabilities.magnitude),
            1.0,
            rtol=0.0,
            atol=2e-16,
        )
        np.testing.assert_allclose(
            base.probabilities.magnitude,
            shifted.probabilities.magnitude,
            rtol=0.0,
            atol=0.0,
        )
        assert np.all(
            base.probabilities.magnitude[:-1] > base.probabilities.magnitude[1:]
        )

    def test__evaluate_rejects_empty_level_inventory(self) -> None:
        unit = PhysicalUnit(expression="joule")
        model = self._model(thermal_energy=1.0, unit=unit)

        with pytest.raises(ValueError, match="energies must be nonempty"):
            model.evaluate(
                energies=VectorQuantity(
                    magnitude=np.array([], dtype=np.float64),
                    unit=unit,
                )
            )

    def test__evaluate_rejects_mismatched_energy_unit(self) -> None:
        model = self._model(
            thermal_energy=1.0,
            unit=PhysicalUnit(expression="joule"),
        )

        with pytest.raises(ValueError, match="must use the thermal-energy unit"):
            model.evaluate(
                energies=VectorQuantity(
                    magnitude=np.array([0.0, 1.0], dtype=np.float64),
                    unit=PhysicalUnit(expression="electron_volt"),
                )
            )
