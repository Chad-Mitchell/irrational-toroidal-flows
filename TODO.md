# TODO.md for Irrational Toroidal Flows Conjecture Repo

**Version:** v2.0 (Updated November 11, 2025)  
**Status:** Active – Prioritizing whitepaper v2 for arXiv submission; Pareto 80/20 focus (80% on core polish, 20% on exploratory extensions).  
**Goals:** Expand v1 (3-page sketch) to 15-20 pages for comprehensive, falsifiable probe of emergent sync from chaos via irrational flows. Regime-smart hybrids, higher-genus integrations, and broader generalizations for apps (AI detuning, neurotherapies, fluids). Ship v2 to repo/arXiv by week's end; invite forks/disproofs.

## 1. Whitepaper v2 Integration & Polish (80% Effort – Main Body Focus)
- **Core Sections (Build on v1 Abstract, Eq 1, Figure 1, Probe Hits Table, Disproof Log, App Hint, Refs):**
  - Refine abstract: Emphasize ≥20% synergy lift (MI gain > additive) via irrational ω ergodic fills; add regime-dependent toggles (weak K<1.2 irrational ~70% dominance for superadditive MI; strong/quantum rational for 1700-4000% variance boosts).
  - Expand Eq 1 derivations: Sketch ξ = |avg e^{iθ}| metric (0=chaos, 1=lock); fixed pt ξ* ≈ √μ stability proof; incorporate noise η and spatial stalls (v=5 golden at 0.005% entropy nudge).
  - Update/Merge Tables: Combine v1 probe hits (e.g., 48% phase sync irr lift, 171% flux density, 0.35 quantum ent depth) with repo test table (regime rows: weak +77% irr, strong +17% rat) and higher-genus addendum (~80% irr in weak with orientable transversals). Add multi-metrics for variability (address 8% MI-only dips).
  - Visuals: Retain Figure 1 (dense irr/golden traj sync 0.94 vs rat 0.72); add Poincaré sections, higher-dim paths from repo.
  - Falsifiability: Strengthen disproof log (irr holds ∞ units vs rat <50; rational prunes >20% lifts in weak niches); add clauses for new extensions (e.g., homotopy obstructions >20% prunes in genus/quantum).

- **Regime Change Extensions:**
  - Formalize hybrid selector: Decision tree/threshold (K>1.2 → rational for variance; else irr for +15-25% MI transitional synergies). Add pseudocode; tie to v1 μ crank (e.g., μ=2.5 +24.67% irr drop).

- **Higher-Genus Extensions (Incorporate higher_genus_extensions.md):**
  - Section 4: Generalize to genus h≥2 (hyperbolic manifolds, negative Euler char); integrate Katok conjecture disproof (2006: obstructions in homotopy classes lacking transversals due to alternating intersections/index contradictions).
  - Mechanisms: Irr flows yield denser ergodic mixing for +15-25% MI in weak/noisy (avoid blocks via orientable classes); hybrid to rat for strong/quantum.
  - Addendum Table: Merge with core (e.g., weak +77-102% irr sync; quantum damped +25% hybrid).
  - Refs: Add [10,12,6] Katok sources; 2025 diffeology (Iglesias-Zemmour on T_α quotients R/(Z+αZ), homotopy ~Z+αZ for arithmetic α like √2+1).
  - Gaps: High-dim probes (HCP/FlyWire data); PR for nilflow ties.

- **New Section 5: Non-Commutative and Quantum Extensions (Bullet 2 Generalization):**
  - ~5 pages: Build on diffeology for noncommutative tori (arithmetic α for entanglement depths >0.35; damped +25% lifts in quantum to avoid subadditive edges).
  - Mechanisms: Tiling spaces as coverings over irr tori; bridges to quantum regimes (QuTiP sims for non-exact magnetic flows echoing Katok spheres).
  - Updated Rows: Quantum: Hybrid +25% via tiling; falsify if homotopy obstructions >20%.
  - Stubs: Extend sympy diffeological probe for ergodic densities in noncomm sims (target low ~0.1-0.2 for dense mixing).
  - Apps: Quantum entropy (0.35→0.5); 25%+ AI detuning via noncomm bridges.
  - Refs: 2025 Iglesias-Zemmour; add [9,7,19,12] for noncomm geometry/tiling.

## 2. Appendices for Exploratory Extensions (20% Effort – Prospective Scouts)
- **Appendix A: Nilmanifolds and Higher-Step Nilflows (Bullet 1 – 2-3 pages):**
  - Introduce nilpotent Lie groups (e.g., Heisenberg) for slow chaos avoidance; smooth time-changes induce mixing in irr nilflows (step ≥2).
  - Potential: +10-20% sync in high-dim noisy (refine ~70/30 splits for neural PDEs); Lyapunov bounds for probs gap.
  - Stub: Sympy proxy for nilflow densities (extend diffeological; test 171% flux in nonlinear Schrödinger PDE stability).
  - Refs: [0,5,6] ergodic averages on higher-step nilmanifolds; anisotropic Banach spaces.
  - Falsify: Mixing sets prune >20% lifts → limit to abelian.
  - Language: "Preliminary estimates suggest...; refine via PRs."

- **Appendix B: Infinite-Dimensional Generalizations (Bullet 3 – 2-3 pages):**
  - Extend to Hilbert/Banach manifolds for PDE flows (e.g., Hamiltonian PDEs with integrable geodesics; commuting flows on infinite Grassmannians).
  - Potential: Irr ratios for emergent structure in diffusion models/Ricci flows; +25% overfitting cuts in AI via geometric gradients.
  - Stub: Symplectic for vakonomic systems; target entropy boosts (0.35→0.5) in wild dynamics.
  - Refs: [20,21,22,24,29] infinite-dim ergodic theory/PDEs.
  - Falsify: If infinite-dim prunes >20% in sims, scope to finite.
  - Language: "Future directions; calls for PRs on gaps."

## 3. Simulations & Code Expansions (/sims/ Folder)
- Extend hybrid Kuramoto-torus (numpy/scipy) with diffeology (sympy arithmetic α) and genus proxies (hyperbolic metrics via scipy geodesics).
- Add QuTiP for quantum/noncomm (entanglement depths; damped +25%).
- Run Ensembles: Vary K, h=2-5, noise; log MI lifts/sync ξ (e.g., ergodic_density <0.15 → +102% weak irr).
- Validation: Pull HCP/FlyWire (if accessible); address variability with multi-metrics.
- New Stubs: Nilflow densities; infinite-dim PDE proxies (e.g., nonlinear Schrödinger for fluxes).

## 4. Validation & Gaps
- Disproof Avoids: Test homotopy classes (orientable only for lifts); hybrid recovery if blocks.
- Debates: Open GitHub issues (e.g., "Obstruction Gaps in Nilflows", "Infinite-Dim Prunes").
- Societal Value: Expand v1 app hint (20% rhythm gain in networks/swarmalators) with examples (AI 25%+ detuning, fusion/eng 10-30%→30-50% gains via extensions).

## 5. Roadmap & Milestones
- **Immediate (Tomorrow):** Draft Section 5/appendices; run sim stubs; merge tables/figs; polish eqs/log.
- **Near-Term (Week's End):** v2 PDF/repo push; arXiv submission (math.DS/nlin.CD; abstract: "Generalizing irr toroidal flows for emergent sync, with hybrids and higher-genus/quantum/infinite-dim probes").
- **Long-Term:** v3 promotions (appendices to sections on feedback); ports to AI/eng/social; collabs (@strogatz, @peyre, @kontorovich).
- **Contribs:** Update CONTRIBUTING.md; PR sims/disproofs.

**Notes:** Stay falsifiable/regime-aware; use "preliminary" for unvalidated claims. Total ~15-20 pages – lean but visionary. If sim snags, debug jointly. Torque for 10x gains! 🌊
