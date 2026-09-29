"""Verification of the quantum-model root base."""

from abc import ABC

from projectkoios.physkit.qm.models.base import BaseQuantumModel


def test_is_nominal_abstract_model_root() -> None:
    assert issubclass(BaseQuantumModel, ABC)
