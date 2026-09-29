from __future__ import annotations

import numpy as np
import pytest

from projectkoios.physkit.numerics.linear_algebra.volume import (
    normalized_column_volume,
)


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test__normalized_column_volume__returns_unit_for_scaled_orthogonal_columns(
    scale: float,
) -> None:
    matrix = scale * np.eye(3)

    assert normalized_column_volume(matrix) == 1.0


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
def test__normalized_column_volume__preserves_scaled_near_collinear_volume(
    scale: float,
) -> None:
    offset = 2.0e-8
    matrix = scale * np.array(
        [
            [1.0, 1.0, 0.0],
            [0.0, offset, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    expected = offset / np.sqrt(1.0 + offset * offset)

    assert normalized_column_volume(matrix) == pytest.approx(
        expected,
        rel=1.0e-15,
        abs=0.0,
    )


def test__normalized_column_volume__returns_zero_for_zero_column() -> None:
    matrix = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )

    assert normalized_column_volume(matrix) == 0.0


@pytest.mark.parametrize(
    "matrix",
    [
        np.ones((2, 3)),
        np.empty((0, 0)),
        np.array([[1.0, np.inf], [0.0, 1.0]]),
    ],
)
def test__normalized_column_volume__rejects_invalid_matrix(
    matrix: np.ndarray,
) -> None:
    with pytest.raises(ValueError):
        normalized_column_volume(matrix)
