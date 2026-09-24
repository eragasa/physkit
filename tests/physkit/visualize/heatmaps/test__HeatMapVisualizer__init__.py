"""Verification of ``HeatMapVisualizer`` construction."""

import numpy as np
import pytest

from physkit.visualize.heatmaps import HeatMapVisualizer


def test_owns_binary64_matrix_and_symmetric_limit() -> None:
    source = np.array([[2.0, 0.0], [-1.0, 0.5]], dtype=np.float32)
    visualizer = HeatMapVisualizer(source)
    source[:] = 99.0

    np.testing.assert_array_equal(
        visualizer.values,
        [[2.0, 0.0], [-1.0, 0.5]],
    )
    assert visualizer.values.dtype == np.dtype(np.float64)
    assert visualizer.values.flags.owndata
    assert visualizer.color_limit == 2.0


@pytest.mark.parametrize(
    "invalid",
    [
        [True, False],
        [1.0, 2.0],
        np.zeros((1, 1, 1)),
        np.zeros((0, 2)),
        [[1.0, np.nan]],
        [[1.0 + 2.0j]],
        [["1", "2"]],
        [[1.0], [2.0, 3.0]],
    ],
)
def test_rejects_invalid_matrix_values(invalid: object) -> None:
    with pytest.raises((TypeError, ValueError)):
        HeatMapVisualizer(invalid)  # type: ignore[arg-type]
