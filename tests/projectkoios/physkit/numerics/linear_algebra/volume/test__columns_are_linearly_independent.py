from __future__ import annotations

import math

import numpy as np
import pytest

from projectkoios.physkit.numerics.linear_algebra.volume import (
    columns_are_linearly_independent,
)


@pytest.mark.parametrize("scale", [1.0e-200, 1.0, 1.0e200])
@pytest.mark.parametrize(
    ("offset", "expected"),
    [(2.0e-8, True), (5.0e-9, False), (0.0, False)],
)
def test__columns_are_linearly_independent__applies_scale_invariant_tolerance(
    scale: float,
    offset: float,
    expected: bool,
) -> None:
    matrix = scale * np.array(
        [
            [1.0, 1.0, 0.0],
            [0.0, offset, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )

    assert (
        columns_are_linearly_independent(
            matrix,
            norm_vol_atol=1.0e-8,
        )
        is expected
    )


@pytest.mark.parametrize("tolerance", [-1.0, math.inf, math.nan])
def test__columns_are_linearly_independent__rejects_invalid_tolerance(
    tolerance: float,
) -> None:
    with pytest.raises(ValueError):
        columns_are_linearly_independent(
            np.eye(3),
            norm_vol_atol=tolerance,
        )
