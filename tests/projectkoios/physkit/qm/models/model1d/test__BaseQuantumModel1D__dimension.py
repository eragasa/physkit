"""Verification of one-dimensional quantum-model ownership."""

from projectkoios.physkit.qm.models.base import BaseQuantumModel
from projectkoios.physkit.qm.models.model1d import BaseQuantumModel1D


def test_directly_inherits_quantum_model_and_declares_dimension() -> None:
    assert BaseQuantumModel1D.__bases__[0] is BaseQuantumModel
    assert BaseQuantumModel1D.dimension == 1
