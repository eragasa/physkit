# Eigenvalue problems

An eigenvalue problem asks for a nonzero vector \(v\) and a scalar \(\lambda\)
such that

\[
A v = \lambda v.
\]

The scalar \(\lambda\) is an **eigenvalue** of \(A\), and \(v\) is a
corresponding **eigenvector**. Multiplying an eigenvector by any nonzero scalar
does not change this relation.

## Characteristic equation

For a finite square matrix, an eigenvalue makes \(A-\lambda I\) singular.
Therefore,

\[
\det(A-\lambda I)=0.
\]

This equation is useful for small analytical examples. Numerical software
normally solves the matrix problem directly instead of constructing the
characteristic polynomial.

## Real-symmetric matrices

When \(A\) is real and symmetric,

\[
A=A^{\mathsf T},
\]

its eigenvalues are real and its eigenvectors can be chosen orthonormal. If the
normalized eigenvectors are the columns of \(V\), then

\[
V^{\mathsf T}V=I,
\qquad
A=V\Lambda V^{\mathsf T},
\]

where \(\Lambda\) is diagonal and contains the eigenvalues.

An eigenvector's sign is arbitrary: both \(v\) and \(-v\) represent the same
eigendirection. Repeated eigenvalues introduce additional freedom because any
orthonormal basis of the repeated eigenspace is valid.

## Checking a computed eigenpair

For a computed pair \((\lambda_i,v_i)\), define the residual

\[
r_i=A v_i-\lambda_i v_i.
\]

A small residual norm shows that the pair satisfies the represented matrix
problem to the stated numerical tolerance. It does not by itself establish that
the matrix is an adequate model of a physical system.

For a complete eigendecomposition, useful checks are

\[
V^{\mathsf T}V\approx I
\]

and

\[
V\Lambda V^{\mathsf T}\approx A.
\]

## Complete and partial spectra

Small dense problems often use a complete eigendecomposition. Large sparse
problems commonly request only a few eigenpairs, such as the lowest eigenvalues.
A partial solver should preserve the sparse representation rather than silently
materializing the full dense matrix.

## Computational exercises

Work through the notebooks in order:

1. [Solve and verify eigenpairs](../../../../../notebooks/foundations/linear-algebra/eigenvalue-problems/01-solve-and-verify-eigenpairs.ipynb)
2. [Check an eigendecomposition](../../../../../notebooks/foundations/linear-algebra/eigenvalue-problems/02-check-an-eigendecomposition.ipynb)
3. [Test eigenvector sign freedom](../../../../../notebooks/foundations/linear-algebra/eigenvalue-problems/03-test-eigenvector-sign-freedom.ipynb)

This chapter covers the linear-algebra problem only. Physical uses—including
quantum Hamiltonians, normal modes, and stability analysis—belong in their
respective application notes and computational laboratories.
