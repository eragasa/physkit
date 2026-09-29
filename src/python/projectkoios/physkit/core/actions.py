"""Typed request-to-response action boundaries for data objects."""

from typing import Protocol

from projectkoios.physkit.core.data import DataObject


class DataObjectActionizer[RequestT: DataObject, ResponseT: DataObject](Protocol):
    """Describe an ActionObject that maps one request to one response."""

    def action(self, *, request: RequestT) -> ResponseT:
        """Return the response produced from ``request``."""
        ...


class ActionizedDataObject[RequestT: DataObject, ResponseT: DataObject](DataObject):
    """Provide typed mechanical dispatch from a façade to its ActionObject."""

    __slots__ = ()

    actionizer: DataObjectActionizer[RequestT, ResponseT]

    def _respond(self, *, request: RequestT) -> ResponseT:
        """Delegate one complete request to the configured ActionObject."""
        return self.actionizer.action(request=request)
