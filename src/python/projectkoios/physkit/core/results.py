"""Nominal base for immutable computational results."""

from projectkoios.physkit.core.data import DataObject


class ResultsObject(DataObject):
    """Identify an immutable, correlated result returned by a computation."""
