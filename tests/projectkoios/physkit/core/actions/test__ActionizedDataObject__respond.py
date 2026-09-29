"""Dispatch tests for ``ActionizedDataObject``."""

from dataclasses import dataclass, field

from projectkoios.physkit.core.actions import ActionizedDataObject
from projectkoios.physkit.core.data import DataObject


@dataclass(frozen=True, slots=True, kw_only=True)
class _ScaleRequest(DataObject):
    value: float
    factor: float


@dataclass(frozen=True, slots=True, kw_only=True)
class _ScaleResponse(DataObject):
    value: float


@dataclass(frozen=True, slots=True)
class _ScaleActionizer:
    def action(self, *, request: _ScaleRequest) -> _ScaleResponse:
        return _ScaleResponse(value=request.value * request.factor)


@dataclass(frozen=True, slots=True, kw_only=True)
class _ScalableValue(ActionizedDataObject[_ScaleRequest, _ScaleResponse]):
    value: float
    actionizer: _ScaleActionizer = field(
        default_factory=_ScaleActionizer,
        repr=False,
        compare=False,
    )

    def scale(self, *, factor: float) -> _ScaleResponse:
        return self._respond(
            request=_ScaleRequest(
                value=self.value,
                factor=factor,
            )
        )


class TestActionizedDataObjectRespond:
    """Verify typed request-to-response delegation through the shared base."""

    def test__respond_delegates_one_complete_request(self) -> None:
        source_value = 3.0
        scale_factor = 4.0
        scalable = _ScalableValue(value=source_value)

        response = scalable.scale(factor=scale_factor)

        assert response == _ScaleResponse(value=source_value * scale_factor)
