"""Nominal base for immutable computational results."""

from abc import ABC


class ResultsObject(ABC):
    """Identify an immutable, correlated result returned by a computation."""
