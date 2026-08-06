"""Minimal immutable linear-operator interface and scalar scaling.

:class:`LinearOperator` separates software application from any particular
matrix or physical model.  Implementations expose immutable semantic domain
and codomain metadata, shape, dtype, and array application.  The base typing
boundary intentionally uses :class:`object`; it does not establish a general
PhysKit state-space hierarchy.

The only accepted algebraic operation is finite non-Boolean scalar scaling.
The private wrapper preserves the operand's exact domain and codomain, freezes
shape and dtype at construction, and applies the scalar after the operand.
General operator composition, symbolic behavior, units, and quantum operators
are excluded.  Implementations determine state validation; invalid scaling
scalar types raise :class:`TypeError` and nonfinite values raise
:class:`ValueError`.  Execution alone makes no numerical, physical,
pedagogical, or uncertainty claim.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from numbers import Number
from typing import Any

import numpy as np
from numpy.typing import ArrayLike


class LinearOperator(ABC):
    """Abstract linear operator with explicit semantic endpoints.

    Attributes
    ----------
    domain : object
        Immutable semantic metadata describing accepted input states.
    codomain : object
        Immutable semantic metadata describing produced output states.
    shape : tuple[int, int]
        Matrix-like output-by-input dimensions.
    dtype : numpy.dtype
        Canonical operator coefficient dtype.

    Notes
    -----
    The ``object`` annotations are deliberately minimal.  Concrete operators
    may narrow them, but this class introduces no general state-space base
    class or compatibility protocol.  ``@`` delegates to :meth:`apply`.

    See Also
    --------
    physkit.operators.DiscreteLinearOperator1D
        Discrete specialization exposing a CSR matrix.
    """

    @property
    @abstractmethod
    def domain(self) -> object:
        """Return immutable semantic input-state metadata.

        Returns
        -------
        object
            Operator-specific domain metadata.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def codomain(self) -> object:
        """Return immutable semantic output-state metadata.

        Returns
        -------
        object
            Operator-specific codomain metadata.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def shape(self) -> tuple[int, int]:
        """Return output-by-input dimensions.

        Returns
        -------
        tuple[int, int]
            Two nonnegative matrix-like dimensions.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def dtype(self) -> np.dtype:
        """Return the canonical coefficient dtype.

        Returns
        -------
        numpy.dtype
            Operator coefficient dtype.
        """
        raise NotImplementedError

    @abstractmethod
    def apply(self, state: ArrayLike) -> np.ndarray:
        """Apply the operator to one state vector.

        Parameters
        ----------
        state : numpy.typing.ArrayLike
            Operator-specific input vector.

        Returns
        -------
        numpy.ndarray
            New owned result vector.

        Raises
        ------
        TypeError
            If ``state`` has an unsupported semantic type.
        ValueError
            If a correctly typed state violates an operator invariant.
        """
        raise NotImplementedError

    def __matmul__(self, state: ArrayLike) -> np.ndarray:
        """Apply the operator with ``operator @ state`` syntax.

        Parameters
        ----------
        state : numpy.typing.ArrayLike
            Operator-specific input vector.

        Returns
        -------
        numpy.ndarray
            New owned result returned by :meth:`apply`.

        Raises
        ------
        TypeError
            If ``state`` has an unsupported semantic type.
        ValueError
            If a correctly typed state violates an operator invariant.
        """
        return self.apply(state)

    def scaled(self, factor: Number) -> LinearOperator:
        """Return an immutable scalar multiple of this operator.

        Parameters
        ----------
        factor : numbers.Number
            Finite non-Boolean Python/NumPy real or complex scalar.

        Returns
        -------
        LinearOperator
            Private wrapper preserving this operator's exact domain and
            codomain.  Its dtype is ``numpy.result_type(self.dtype, factor)``.

        Raises
        ------
        TypeError
            If ``factor`` is Boolean or not a real/complex scalar.
        ValueError
            If ``factor`` is nonfinite or cannot be finitely canonicalized.

        Notes
        -----
        Scaling stores no applied state and does not define composition.

        Examples
        --------
        ``scaled = operator.scaled(-0.5)`` creates a new operator without
        mutating ``operator``.
        """
        return _ScaledLinearOperator(self, factor)


class _ScaledLinearOperator(LinearOperator):
    """Private immutable scalar wrapper preserving semantic endpoints."""

    __slots__ = (
        "_operand",
        "_factor",
        "_domain",
        "_codomain",
        "_shape",
        "_dtype",
        "_frozen",
    )

    def __init__(self, operand: LinearOperator, factor: Number) -> None:
        if isinstance(factor, (bool, np.bool_)) or not isinstance(factor, Number):
            raise TypeError("factor must be a non-Boolean real or complex scalar.")
        if not np.isfinite(factor):
            raise ValueError("factor must be finite.")

        canonical_factor: float | complex
        if isinstance(factor, (complex, np.complexfloating)):
            canonical_factor = complex(factor)
        else:
            canonical_factor = float(factor)
        if not np.isfinite(canonical_factor):
            raise ValueError("factor must remain finite when canonicalized.")

        object.__setattr__(self, "_operand", operand)
        object.__setattr__(self, "_factor", canonical_factor)
        object.__setattr__(self, "_domain", operand.domain)
        object.__setattr__(self, "_codomain", operand.codomain)
        object.__setattr__(self, "_shape", tuple(operand.shape))
        object.__setattr__(
            self, "_dtype", np.dtype(np.result_type(operand.dtype, canonical_factor))
        )
        object.__setattr__(self, "_frozen", True)

    def __setattr__(self, name: str, value: Any) -> None:
        if getattr(self, "_frozen", False):
            raise AttributeError(f"{type(self).__name__} is immutable.")
        object.__setattr__(self, name, value)

    @property
    def domain(self) -> object:
        """Return the operand's exact domain object."""
        return self._domain

    @property
    def codomain(self) -> object:
        """Return the operand's exact codomain object."""
        return self._codomain

    @property
    def shape(self) -> tuple[int, int]:
        """Return the shape frozen from the operand."""
        return self._shape

    @property
    def dtype(self) -> np.dtype:
        """Return the frozen result dtype of coefficients and factor."""
        return self._dtype

    def apply(self, state: ArrayLike) -> np.ndarray:
        """Apply the operand and multiply its owned result by the factor."""
        applied = self._operand.apply(state)
        output_dtype = np.dtype(np.result_type(self._dtype, applied.dtype))
        return np.array(
            np.asarray(applied, dtype=output_dtype) * self._factor,
            dtype=output_dtype,
            order="C",
            copy=True,
        )
