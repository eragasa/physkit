# physkit/surface_source/types.py
# Eugene Joseph M. Ragasa, 2026

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class DiskSourceParams:
    """
    Geometry + emission parameters for a finite emitting disk.

    h: source plane z=-h to substrate plane z=0 separation
    a: disk radius
    n: cosine-power exponent for emission intensity about +z normal
    """
    h: float
    a: float
    n: float = 1.0

    @property
    def valid_range(self) -> Optional[Tuple[float, float]]:
        return None

