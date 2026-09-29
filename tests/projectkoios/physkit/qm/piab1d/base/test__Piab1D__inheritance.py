"""Verification of ``Piab1D`` model ownership."""

from projectkoios.physkit.qm.models.model1d import BaseQuantumModel1D
from projectkoios.physkit.qm.piab1d.base import Piab1D


class TestPiab1DInheritance:
    """Own the cohesive evidence in this module."""

    def test_directly_inherits_base_quantum_model_1d(self) -> None:
        assert Piab1D.__bases__ == (BaseQuantumModel1D,)
        assert Piab1D.dimension == 1
