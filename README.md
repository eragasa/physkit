# physkit
**PhysKit** is an open-source Python library for pedagogically motivated computational physics, designed for undergraduate teaching, exploratory learning, and a gradual path toward research-quality numerical experiments.

The project developed from my classroom experience in the Philippines, where high textbook costs, rising expectations for computational literacy, and subscription-based teaching software create barriers for both students and instructors. These constraints motivated the development of an open and mathematically explicit toolkit.

**Project Stage:** Pre-implementation. The repository currently contains architecture drafts, preliminary design notes, and early notebooks. Development is not full-time; my primary responsibilities involve teaching, preparing lecture materials, and conducting research. PhysKit will grow gradually from these efforts, as lecture notes, research code, and instructional examples evolve into structured, reusable components.

---

## Goals
PhysKit aims to connect three layers of physics education:
- clear conceptual formulations,  
- explicit computational procedures,  
- scalable structures that can extend into research-oriented simulations.
The design emphasizes transparency, reproducibility, and a direct correspondence between mathematical models and executable code.

---

## Planned Core Features
The first functional release is expected to focus on:
- basic mechanics utilities and state representations,  
- simple ODE stepping schemes,  
- unit handling and nondimensionalization tools,  
- minimal visualization helpers for trajectories and scalar fields.
- notebooks illustrating canonical physics problems and computational methods.

These foundational components will support the later expansion into more advanced modules.

---

## Long-Term Vision
The architecture is designed to provide a coherent computational foundation for the full undergraduate physics curriculum, as well as the material commonly reviewed before graduate qualifying examinations. Over time, PhysKit is intended to expand into two complementary layers: **core computational methods** and **physics-domain applications**.

### Computational Methods

- **ODE, PDE, and time-evolution solvers**  
  Numerical tools for wave, diffusion, Poisson, Schrödinger, heat transport, elasticity, and other common equations, using finite-difference, finite-volume, or spectral approaches.

- **Operator-based formulations**  
  A unified framework in which linear and nonlinear operators act on states, supporting applications across quantum mechanics, vibrations, diffusion, and lattice or continuum models.

- **Stochastic and Monte Carlo methods**  
  Random walks, sampling algorithms, statistical ensembles, Markov processes, and uncertainty quantification for modeling noise, fluctuations, and thermodynamic behavior.

### Physics Domains
**Core Physics Sequence**
- PHYS101 — Mechanics  
- PHYS102 — Electromagnetism  
- PHYS103 — Optics  
- PHYS104 — Modern Physics  

These courses provide the curricular backbone around which PhysKit is structured. The long-term goal is to offer computational support across the full undergraduate sequence and the foundational areas reviewed before graduate qualifying exams.

**Computational Domains**

- **Computational mechanics**  
  Newtonian, Lagrangian, and Hamiltonian dynamics; oscillators, central-force systems, rigid-body motion, and phase-space analysis.

- **Electromagnetism and field modeling**  
  Discrete and continuous representations of charges, currents, fields, potentials, and Maxwell-equation–based systems.

- **Quantum mechanics**  
  Schrödinger solvers, operator evolution, few-level models, and basic tools for understanding measurements and state transformations.

- **Statistical mechanics and thermodynamics**  
  Ensembles, fluctuations, transport, materials thermodynamics, and computational approaches relevant to equilibrium and non-equilibrium systems.

- **Solid state and materials computation**  
  Lattice models, tight-binding prototypes, phonons, defects, diffusion processes, energetics, and computational methods used in materials science.

These courses form the curricular backbone for which PhysKit aims to provide computational support and example libraries.
---

## Design Principles

Development is guided by several key principles:

- **Explicit mathematical objects** — states, operators, transformations.  
- **Separation of concerns** — physical definitions, numerical methods, and visualization remain distinct.  
- **Transparent numerical workflows** — intermediate steps and update rules are inspectable.  
- **Pedagogical modularity** — small, self-contained examples scale naturally into larger simulations.  
- **Reproducible, notebook-friendly workflows** — examples are designed to run in environments such as Google Colab with minimal setup (standard Python stack, no proprietary tooling).  
- **Literate-computing integration** — compatible with Quarto, Obsidian, and related tools for combining narrative, mathematics, and code.

More detailed architectural documentation will be added as the project evolves.

---

## Status
- **No functional modules implemented yet**

---

## Contributing

PhysKit is currently in its architectural phase.  
The most valuable contributions at this stage include:
- feedback on structure, naming, and API design,  
- suggestions for module organization,  
- prototype notebooks demonstrating desired patterns,  
- discussion of physics models and numerical approaches.

Once implementation begins, contributors will be able to extend modules, add examples, and help refine documentation.

---

## Background

PhysKit is informed by experience in computational materials science and several decades of work in mathematical and numerical modeling. Teaching responsibilities have included electromagnetism (PHYS 102), modern physics (PHYS 104), solid state physics, computational physics, and related courses. Early materials in the repository will draw from these lecture notes, with new figures and problem sets created as needed.
