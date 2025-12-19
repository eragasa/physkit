# src/physkit/units/_protocols.py
# Author: Eugene Joseph M. Ragasa
"""
Internal protocols for physkit unit quantities.

These protocols enforce API shape without inheritance.
They are intended for tests, static analysis, and tooling.
"""

from typing import Protocol, runtime_checkable
from enum import IntEnum


@runtime_checkable
class QuantityProtocol(Protocol):
  """
  Structural interface for a physkit physical quantity.

  A conforming quantity must:
  - define a nested Units(IntEnum)
  - provide convert(from_, to)
  - be stateless
  """

  class Units(IntEnum):
    ...

  @staticmethod
  def convert(*, from_, to):
    ...

