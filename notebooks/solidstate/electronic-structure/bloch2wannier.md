---
title: "From Bloch States to Wannier Functions"
subtitle: "Companion Lecture Notes on Gauge, Localization, and Operator Reconstruction"
artifact_status: "Exploratory companion to the accepted notebook; not canonical or supported"
source_notebook: "bloch2wannier.ipynb"
---

# From Bloch States to Wannier Functions

## Scope

These notes accompany the exploratory notebook of the same name. They organize its finite-dimensional construction into a lecture sequence; they do not replace the executable calculations. The model is a one-dimensional, two-orbital, periodic tight-binding system treated with NumPy linear algebra and a discrete Fourier transform.

The central distinction is between an operator, a matrix representation, a retained subspace, and a basis chosen inside that subspace. Bloch eigenvector phases change the basis and the shapes of individual Wannier functions, even when the band projector is unchanged.

## Learning objectives

After working through the notebook and these notes, a reader should be able to:

1. construct the finite periodic real-space Hamiltonian used in the notebook;
2. block-diagonalize it into Bloch fibers with a discrete Fourier transform;
3. distinguish Bloch eigenvectors from gauge-invariant band projectors;
4. explain how momentum-dependent phases alter the Wannier basis;
5. construct translated Wannier functions for one isolated band;
6. verify orthonormality, translation covariance, and retained-projector equality;
7. reconstruct the retained dispersion from the Wannier Hamiltonian; and
8. state why independently constructed retained spaces require an explicit alignment before their matrices are compared.

## 1. Finite periodic state space

For $N$ unit cells with orbitals $A$ and $B$ in every cell,

$$
\mathcal H_{\mathrm{real}}=\mathbb C^N\otimes\mathbb C^2,
\qquad \dim \mathcal H_{\mathrm{real}}=2N.
$$

The basis vectors $|R,A\rangle$ and $|R,B\rangle$, with $R=0,\ldots,N-1$, are orthonormal. Cell labels are periodic: additions to $R$ are taken modulo $N$. This is a finite representation of a periodic model, not a statement about the geometry of material orbitals.

## 2. Real-space tight-binding Hamiltonian

The notebook uses an SSH-like two-orbital Hamiltonian,

$$
\begin{aligned}
\hat H={}&\sum_R \Delta\bigl(|R,A\rangle\langle R,A|-|R,B\rangle\langle R,B|\bigr)\\
&+\sum_R\left[t_1|R,A\rangle\langle R,B|
+t_2|R+1,A\rangle\langle R,B|+\mathrm{h.c.}\right].
\end{aligned}
$$

Here $t_1$ is the intracell hopping, $t_2$ is the intercell hopping, and $\pm\Delta$ are onsite energies. The matrix assembled in the notebook is Hermitian by construction and checked numerically. That check establishes internal software consistency; it does not validate this Hamiltonian for a particular material.

## 3. Translation symmetry and Bloch fibers

The allowed discrete momenta and Fourier matrix are

$$
k_j=\frac{2\pi j}{Na},
\qquad
F_{kR}=\frac{1}{\sqrt N}e^{-ikRa}.
$$

With $\mathcal F=F\otimes I_2$, the transformed matrix is

$$
H_k^{\mathrm{full}}=\mathcal F H_{\mathrm{real}}\mathcal F^\dagger.
$$

Translation symmetry makes this matrix block diagonal, with one $2\times2$ fiber per sampled momentum. Under the notebook's Fourier and hopping conventions,

$$
H(k)=
\begin{pmatrix}
\Delta & t_1+t_2e^{-ika}\\
t_1+t_2e^{ika} & -\Delta
\end{pmatrix}.
$$

The notebook checks unitarity of $F$, equality of every transformed block with this analytic fiber, and vanishing of all off-fiber blocks.

## 4. Bloch eigenstates and retained-band projectors

At every momentum,

$$
H(k)|u_{nk}\rangle=E_n(k)|u_{nk}\rangle.
$$

The construction retains the lower eigenvalue and its normalized eigenvector $|u_k\rangle$. The associated rank-one projector is

$$
P(k)=|u_k\rangle\langle u_k|.
$$

An eigenvector is a frame vector; the projector identifies the one-dimensional retained subspace. This distinction matters because the eigenvector is not unique.

## 5. Gauge freedom

For one isolated band, a momentum-dependent $U(1)$ phase changes the frame,

$$
|u_k\rangle\longmapsto e^{i\phi(k)}|u_k\rangle,
$$

but cancels from the projector:

$$
e^{i\phi(k)}|u_k\rangle\langle u_k|e^{-i\phi(k)}=P(k).
$$

The notebook applies a reproducible irregular phase field and verifies projector invariance. Thus the retained subspace is unchanged although the basis used to represent it is different.

## 6. Open-chain parallel transport

A smoother sampled frame is produced sequentially. If $|u_{k_j}\rangle$ has already been fixed, the phase of $|u_{k_{j+1}}\rangle$ is chosen so that

$$
\langle u_{k_j}|u_{k_{j+1}}\rangle
$$

is real and positive. This removes neighboring overlap phases along the ordered momentum samples.

**Important boundary:** this is open-chain parallel transport. It does not enforce closure between the final and initial momentum samples. The remaining closure phase must be handled explicitly before making a periodic-gauge or Berry-phase claim.

## 7. Wannier construction

Define a full Bloch state by

$$
|\psi_k\rangle=|k\rangle\otimes|u_k\rangle.
$$

For translation label $R_0$, the notebook constructs

$$
|w_{R_0}\rangle=\frac{1}{\sqrt N}\sum_k e^{-ikR_0a}|\psi_k\rangle,
$$

or, in the real-space orbital basis,

$$
\langle R,\alpha|w_{R_0}\rangle
=\frac1N\sum_k e^{ik(R-R_0)a}u_\alpha(k).
$$

The cell probability is

$$
p_{R_0}(R)=\sum_\alpha|\langle R,\alpha|w_{R_0}\rangle|^2.
$$

Different phase frames produce different real-space shapes for individual Wannier functions, even though they span the same retained subspace.

## 8. Consistency checks for the Wannier basis

Collect the translated Wannier functions as columns of a $2N\times N$ matrix $W$. The notebook checks three properties:

1. **Orthonormality:** $W^\dagger W=I_N$.
2. **Translation covariance:** translating a Wannier state by one cell advances its center label by one.
3. **Projector equality:** $WW^\dagger$ equals the projector constructed from the retained full Bloch states.

These checks establish consistency among the finite representations. They do not claim completeness outside the retained band.

## 9. Exploratory localization diagnostic

For a center label $R_0$, the notebook uses minimum-image displacements $x_R$ on the finite ring and computes

$$
\Omega_{R_0}=\sum_R p_{R_0}(R)x_R^2
-\left(\sum_R p_{R_0}(R)x_R\right)^2.
$$

This makes the random and parallel-transport frames easy to compare in the finite example.

**Important boundary:** $\Omega_{R_0}$ is an exploratory minimum-image quadratic spread. It is not a periodic-position functional and is not the Marzari--Vanderbilt spread. A smaller value in this example is therefore not a maximal-localization result.

## 10. Hamiltonian in Wannier coordinates

The retained Hamiltonian matrix is

$$
H_{RR'}=\langle w_R|\hat H|w_{R'}\rangle,
\qquad
H_W=W^\dagger H_{\mathrm{real}}W.
$$

Translation symmetry makes $H_W$ circulant. Its row indexed by an origin cell supplies hopping amplitudes as a function of displacement. The retained dispersion is reconstructed by

$$
E(k)=\sum_{\Delta R}e^{ik\Delta Ra}H(\Delta R).
$$

The notebook compares this reconstruction with the original lower-band eigenvalues at every sampled momentum.

## 11. The special single-band result

Although the Wannier functions depend on the $U(1)$ phase, for one isolated band

$$
H_{RR'}=\frac1N\sum_k e^{ik(R-R')a}E(k)
$$

contains only the band energy. The phase cancels. In the notebook's single-band experiment, the random-gauge and parallel-transport Wannier Hamiltonians are therefore elementwise equal to numerical precision.

If $S=W_{\mathrm{smooth}}^\dagger W_{\mathrm{random}}$, then the basis change is nontrivial, but

$$
H_{\mathrm{random}}=S^\dagger H_{\mathrm{smooth}}S,
\qquad
[H_{\mathrm{smooth}},S]=0
$$

within the checked tolerance.

**Important boundary:** this experiment cannot demonstrate a nonzero Wannier-Hamiltonian coordinate difference. A composite retained subspace with momentum-dependent $U(M)$ mixing would be needed for that different example, and such a redesign is deferred.

## 12. Motivation for retained-space alignment

Suppose pristine and doped calculations independently produce retained operators $\hat H_b^{(P)}$ and $\hat H_d^{(P)}$. Their numerical matrices are not automatically expressed in identified coordinates. A comparison requires an explicit unitary map

$$
\hat U_d:\mathcal H_b^{(P)}\longrightarrow\mathcal H_d^{(P)},
$$

before defining

$$
\Delta\hat H_d^{(P)}
=\hat U_d^\dagger\hat H_d^{(P)}\hat U_d-\hat H_b^{(P)}.
$$

**Important boundary:** the notebook motivates this expression but does not construct two different retained spaces, produce $\hat U_d$, or validate a pristine--dopant subtraction procedure.

## 13. Representation map

The lecture can be summarized by

$$
\mathcal H_{\mathrm{real}}
\xrightarrow{\mathcal F}
\bigoplus_k\mathcal H(k)
\xrightarrow{P(k)}
\bigoplus_k\mathcal H^{(P)}(k)
\xrightarrow{\text{gauge}}
\{|u_k\rangle\}
\xrightarrow{\text{Fourier transform}}
\{|w_R\rangle\}.
$$

The projector is gauge invariant. Bloch frame vectors and individual Wannier functions are gauge dependent. In this one-band construction, the retained Wannier Hamiltonian is nevertheless fixed by the dispersion.

## 14. Suggested lecture flow

1. Draw the two-orbital periodic basis and assemble the real-space matrix.
2. Derive the analytic $2\times2$ Bloch Hamiltonian and compare it with the transformed matrix.
3. Diagonalize each fiber and contrast vectors with projectors.
4. Apply a phase field and inspect projector invariance.
5. Introduce open-chain parallel transport and discuss the unresolved closure phase.
6. Fourier transform both frames into Wannier functions and compare their probability distributions.
7. Check the Wannier basis and reconstruct the band.
8. Explain why the single-band Hamiltonian matrix is phase invariant.
9. End with the retained-space alignment question and its explicit non-result in this notebook.

## Preserved limitations

These notes preserve the notebook's four principal limitations:

1. The open-chain parallel-transport gauge does not enforce periodic momentum closure.
2. The minimum-image quadratic spread is exploratory, not a periodic-position or Marzari--Vanderbilt localization functional.
3. The single-band $U(1)$ experiment cannot demonstrate a nonzero Wannier-Hamiltonian coordinate difference; multiband redesign is deferred.
4. The pristine--dopant discussion is motivation only and does not construct or validate retained-space alignment.

## Further work requiring separate authorization

Periodic-gauge closure, Zak phase, a robust periodic spread functional, composite-band $U(M)$ transformations, entangled-band subspace selection, Marzari--Vanderbilt localization, imported electronic-structure data, comparison with Wannier90, or formal PhysKit capability status are outside this artifact's scope.
