"""Deprecation verification for the retained quantum package."""

import importlib
import sys

import pytest

pytestmark = pytest.mark.deprecated


def test_warns_and_exposes_deprecated_marker() -> None:
    sys.modules.pop("physkit.legacy.qm", None)

    with pytest.warns(
        DeprecationWarning,
        match=r"physkit\.legacy\.qm is deprecated",
    ):
        module = importlib.import_module("physkit.legacy.qm")

    assert module.__deprecated__ is True
