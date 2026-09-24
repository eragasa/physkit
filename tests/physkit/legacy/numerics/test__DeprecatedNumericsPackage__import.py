"""Deprecation verification for the retained numerics package."""

import importlib
import sys

import pytest

pytestmark = pytest.mark.deprecated


def test_warns_and_exposes_deprecated_marker() -> None:
    sys.modules.pop("physkit.legacy.numerics", None)

    with pytest.warns(
        DeprecationWarning,
        match=r"physkit\.legacy\.numerics is deprecated",
    ):
        module = importlib.import_module("physkit.legacy.numerics")

    assert module.__deprecated__ is True
