"""Verification of ``Piab1D`` model ownership."""

from physkit.qm.models.model1d import BaseQuantumModel1D
from physkit.qm.piab1d.base import Piab1D


def test_directly_inherits_base_quantum_model_1d() -> None:
    assert Piab1D.__bases__ == (BaseQuantumModel1D,)
    assert Piab1D.dimension == 1
