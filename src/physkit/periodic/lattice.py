# src/physkit/periodic/lattice.py

from __future__ import annotations

import numpy as np


class DirectLattice1D:
    """
    One-dimensional direct Bravais lattice.

    The direct-lattice translation vectors are

    .. math::

        R_n = na,

    where ``a`` is the lattice constant and ``n`` is an integer.

    Parameters
    ----------
    lattice_constant:
        Positive primitive-cell length ``a``.

    Attributes
    ----------
    lattice_constant:
        Primitive-cell length.
    """

    def __init__(
        self,
        lattice_constant: float,
    ) -> None:
        self.lattice_constant: float = float(
            lattice_constant
        )

        self.check_args()

    def check_args(self) -> None:
        """
        Validate the direct-lattice parameters.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the lattice constant is not finite and positive.
        """
        if not np.isfinite(self.lattice_constant):
            raise ValueError(
                "lattice_constant must be finite."
            )

        if self.lattice_constant <= 0.0:
            raise ValueError(
                "lattice_constant must be positive."
            )

    @property
    def primitive_cell_length(self) -> float:
        """
        Return the primitive-cell length.

        Returns
        -------
        float
            Primitive-cell length ``a``.
        """
        return self.lattice_constant

    def translation(
        self,
        cell_index: int,
    ) -> float:
        """
        Return a direct-lattice translation vector.

        Parameters
        ----------
        cell_index:
            Integer cell index ``n``.

        Returns
        -------
        float
            Translation ``R_n = na``.

        Raises
        ------
        TypeError
            If ``cell_index`` is not an integer.
        """
        if not isinstance(
            cell_index,
            (int, np.integer),
        ):
            raise TypeError(
                "cell_index must be an integer."
            )

        return (
            float(cell_index)
            * self.lattice_constant
        )
