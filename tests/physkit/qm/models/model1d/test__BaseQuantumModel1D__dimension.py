"""Verification of one-dimensional quantum-model ownership."""

from physkit.qm.models.base import BaseQuantumModel
from physkit.qm.models.model1d import BaseQuantumModel1D


def test_directly_inherits_quantum_model_and_declares_dimension() -> None:
    assert BaseQuantumModel1D.__bases__[0] is BaseQuantumModel
    assert BaseQuantumModel1D.dimension == 1
