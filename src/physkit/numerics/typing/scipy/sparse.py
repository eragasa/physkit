"""SciPy sparse-array and sparse-matrix type aliases."""

from __future__ import annotations

from scipy import sparse


type SparseMatrix = sparse.spmatrix | sparse.sparray
