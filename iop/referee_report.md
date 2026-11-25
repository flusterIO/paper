# Mock referee report and edit plan

Reviewed: `main.pdf` built 2026-11-23 (43 pp, biber build). Reviewer: a fresh agent with no knowledge of the project, asked to act as a Physica Scripta referee and to read the whole manuscript.

**Verdict: reject in present form; a shorter, refocused resubmission could be considered.**

This file has two parts:
1. **Triage and edit plan.** Claude's working checklist for editing main.tex, with line ranges as of this build.
2. **The full referee report**, verbatim.

---

# Part 1: Triage and edit plan

## Verification of key claims

| ID | Claim | Status |
|---|---|---|
| M9 | Sec 3.5 compares the escape speed with the circular speed | **CONFIRMED.** In `rc_results.npz`, `v_pap / v_newt = 1.4142` at every radius. The g0 fits use `v_newt` (the circular speed) and stand. Bullets 1–2 of Sec 3.5 are wrong. |
| M4 | p_y = (3p−ε)/2 is fine-tuning | Fair. This is a wording change. |
| M6 | Sec 4.7 calls the annual test "direct" although the model predicts SR | Fair. Reword as bounds on future y-dynamics. |
| M6b | "A length along the motion as γ^{n∥}" | Fair. RMS `b` is a transformation coefficient, not a rod length. Reword. |
| M10 | Abstract quotes 0.158 without the 5% floor; Υ systematics (~20%) and H0 dependence not stated | Fair. Add the floor, the Υ systematic and the H0 value. |
| M11 | The static-slice constraint applied to dust FLRW | Plausible. Check Table 2's last row and Sec 2.5.4's third bullet. |
| M2 | The base metric in 2.4.4–2.4.5 is Schwarzschild, while 2.5.3/2.10 use a flat base: double counting | Plausible. **Verify before editing**; may need one clarifying paragraph. |
| M3 | A flat non-compact y gives no 4D gravity without localization | Fair. Needs a statement of the cylinder condition and κ5 ↔ G, plus citations. |
| M7 | Missing literature | Fair. Each new reference must be verified by search before it is added. |
| minor 3 | Fig 1 hypotenuse label has a spurious τ | Check the figure source. |
| minor 10 | "previously derived 1/R profile" with no antecedent | Check. |
| minor 22 | MM/KT citations | Already corrected this session (Schiller 2006; Tobar 2010). |

## Decisions for Andrew (do NOT edit without his call)

- **D1, M1: "time is not a separate dimension."** The reviewer argues the 5D metric still contains a timelike coordinate. This is a core claim of the theory.
  - Options: (a) keep it, adding a paragraph that addresses causal structure; (b) soften it to "time is not an independent geometric dimension at the level of ℝ³ + y"; (c) drop it from the title and abstract.
- **D2, M5(c): outward flow.** Outward flow is a fundamental convention of the model, which stays. The reviewer says the abstract presents it as an observation even though the inward PG chart describes the same spacetime.
  - Option: present it as the model's postulate (the absolute frame is the outward-flow frame) rather than as an observable fact. The physics is unchanged.
- **D3: Section 3 (Hypothesis M).** The reviewer recommends removing it into a separate paper.
  - Milgrom 1999 (Phys Lett A 253, 273) derives a0 ≈ cH/2π from a de Sitter–Unruh horizon argument, which is close to Hypothesis M. **Verify this; it affects any novelty claim.**
- **D4: Sec 1.1 "Lighthouse & Clock-Tower."** The reviewer recommends deletion: the notation is undefined and nothing later uses it.
- **D5: target length.** The reviewer suggests 16–20 pages; the earlier target was 25–30.

## Edit plan (in order; line ranges from the current main.tex)

### Phase A: correctness (no meaning changes needed beyond the fix)
- [ ] **A1 (M9)** Sec 3.5, ~L1896–1906. Compare v_obs with the Newtonian baryonic circular speed `v_newt`, not βc.
  - The new ratio (v_obs/v_newt)² is 2× the old one: 1.78 at 5.3 kpc, rising to about 3.4 beyond 17 kpc. Recompute it.
  - Note that the enclosed-mass spherical formula is approximate for a disc.
- [ ] **A2 (M10)** Abstract and Sec 3.6: state the 5% floor beside 0.158, the H0 used, and the ~20% Υ systematic. Drop "the sample confirms its value".
- [ ] **A3 (M4)** Abstract and Sec 2.4.5 (~L1150–1190): describe p_y as a fine-tuning condition. Reword Eqs. 48–49 ("G44 measured").
- [ ] **A4 (M6)** Sec 4.7, ~L2240–2255: change "direct experimental test" to bounds that any future y-dynamics must satisfy. Restate the n∥ dictionary as transformation coefficients.
- [ ] **A5 (M11)** Table 2's last row and Sec 2.5.4: restrict the static-slice claim to de Sitter, or point to Eq. 160.
- [ ] **A6** Minor items 7, 8, 10, 11, 14, 15, 18, 19, 26: wording and local fixes.

### Phase B: cuts (largest page savings first)
- [ ] **B1** Appendix A, L2279–3327 (9 pp): cut to ≤1 p; keep the results and cite MTW/Hartle. Delete A.1.1 (spatial-geodesic orbit equation). ~8 pp
- [ ] **B2** Sec 2.4.5, L585–1190 (5 pp): keep the reduction summary, Eqs. 61, 66, 70 and 97, and the Cassini conclusion. Cite the standard KK reduction. Drop the flux, exterior log solution and weak-field example. ~3 pp
- [ ] **B3** Discussion 4.1–4.5, L1947–2231 (4 pp): reduce to ~1 p, since it repeats Section 2. ~3.5 pp
- [ ] **B4** Sec 2.2, L172–364: condense to the dt = 0 Lorentz transform and γ² = 1 + (βγ)². ~1.7 pp
- [ ] **B5** Tolman VII inside Sec 2.6.1 (~L1431–1643): cut to 3 lines or move to the appendix. ~1.5 pp
- [ ] **B6** Sec 2.4.1–2.4.2, L430–539: keep only the line element; fix the circular Eq. 22 ↔ 38 reference. ~1.2 pp
- [ ] **B7** Secs 2.8–2.9, L1705–1753: one sentence each. ~1 p
- [ ] **B8** Sec 2.7, L1644–1704: condense; delete "What this does not give". ~1 p
- [ ] **B9** Sec 1.1, L69–123: delete if D4 = yes. ~1 p
- [ ] **B10** Sec 2.4.4, L573–584: delete (superseded). ~0.3 p
- [ ] **B11** Remove most of the ~40 boxed equations (IOP style).
- [ ] **B12** Sec 3, L1847–1938: remove if D3 = split. ~2.7 pp

### Phase C: positioning
- [ ] **C1 (M7)** Add a related-work paragraph to the Introduction: Euclidean relativity (Montanus, Almeida, Gersten, Epstein); neo-Lorentzian views (Bell, Brown, Selleri); the river model; induced-matter theory. Verify every reference.
- [ ] **C2 (M3)** State the cylinder condition and κ5 ↔ G; cite brane and induced-matter localization.
- [ ] **C3 (M12)** Add classic citations: Tolman 1939, Oppenheimer–Volkoff 1939, Schwarzschild 1916 (interior), Buchdahl 1959, Hartle 1967.
- [ ] **C4 (M2)** One paragraph fixing the base metric: flat base in the embedding picture, Schwarzschild base in the KK reduction. Say how the two relate.
- [ ] **C5** Rewrite the abstract to ~150–200 words around the structural result: the synchronization offset equals the Flamm height.
- [ ] **C6** Keywords: replace "inflation"; switch to the Physica Scripta template and remove the placeholders. Deposit the code on Zenodo with a DOI.

### Rules while editing
- Backup before every phase: `$HOME/main.tex.before_<phase>`.
- Preserve CRLF. Use binary-safe, exactly-once replacements.
- After each phase:
  - rebuild with the stub;
  - check that refs, labels and cites resolve;
  - check for duplicate labels;
  - update `major_edits.md`.
- Keep `\label`s of any cut material that are referenced elsewhere, or update the references.
- Do not touch the D-items without Andrew's decision.

---

# Part 2: Full referee report (verbatim)

**Manuscript:** "Absolute Time in Higher-Dimensional Geometry: Classically Simultaneous Relativity via an Unwrapped Kaluza–Klein Dimension"
**Journal:** Physica Scripta
**Length:** 43 pages, 300 numbered equations, 1 figure, 3 tables, 1 appendix. I read the whole manuscript, including Appendix A and the references.

## 1. Summary

The author reinterprets special relativity and spherically symmetric gravity in terms of an extra non-compact spatial coordinate *y*. The Lorentz factor is written as the slope of *y*, γ = √(1+(∂ₓy)²). The term γβx/c in the Lorentz transformation is read as a displacement along *y*. This gives a preferred-frame ("absolute time") reading in which every inertial observer can recover the time τ of a distinguished frame S (Sec. 2.3).

In gravity, the absolute slices are the flat slices of the Painlevé–Gullstrand (PG) metric, taken with the flow pointing outward. The height *y* is the Flamm embedding of the static slice. The synchronization offset between the static and flow slicings is −γ dy (Eq. 33).

A 5D Kaluza–Klein reading follows, with G₄₄ = Φ² and A_μ = ∂_μy. The diagonal sector reduces to Brans–Dicke with ω_BD = 0. Agreement with Cassini then requires a fine-tuned stress p_y = (3p−ε)/2 along *y* (Eq. 97). The A_μ sector is pure gauge, except for a non-gradient part, which is identified with gravitomagnetism (Sec. 2.7).

Using GR's static field equations, the paper re-derives a series of results: the Schwarzschild lapse (Sec. 2.6), the TOV equation, the interior Schwarzschild solution and the Buchdahl bound, a Tolman VII interior, the Lense–Thirring precession, and Schwarzschild orbits (Appendix A). It writes the Hamiltonian constraint on flat slices as ⅔θ² − σσ = 16πGρ, which covers both the exterior of a mass and FLRW.

Section 3 adds a separate, assumed modified-inertia law ("Hypothesis M"), which is MOND with a₀ = κ′cH₀. Fitted to 153 SPARC galaxies, it gives κ′ ≈ 0.16–0.19, near 1/2π.

The author states openly that everything developed so far is equivalent to GR. Departures would have to come from sectors that have not yet been developed.

## 2. Recommendation: Reject in the present form (a substantially shorter, refocused manuscript could be considered as a new submission)

By the author's own account (Secs. 2.10.4, 2.11 "Status", 4.6, 4.8), every developed result is GR or SR written in different variables. Most of the GR content is imported, not derived: the Hamiltonian constraint, the static vacuum equations and the TOV equations.

What remains is an interpretation. It amounts to a neo-Lorentzian absolute-simultaneity reading of the Mansouri–Sexl type, combined with a time-reversed river model. That reading is known in essence, and the manuscript does not engage the closest literature: "Euclidean relativity", Epstein diagrams, and Lorentzian pedagogy. The extra-dimensional sector adds no physics. The diagonal part is either excluded (ω_BD = 0) or fine-tuned away (Eq. 97). The off-diagonal part is pure gauge. Section 3 is MOND with a value of a₀ that Milgrom noted in 1983, and it is not connected to the geometry (Sec. 3.7 says so).

On top of this, the manuscript has three serious problems:

- an undefined, non-standard formalism in Sec. 1.1;
- a physics error in the Milky Way comparison (Sec. 3.5), where escape speed is compared with circular speed;
- extreme redundancy: about half the pages repeat material or reproduce textbook derivations.

Many individual calculations are correct (I checked many; see Sec. 7). The candid "what is and is not established" paragraphs are unusual and welcome.

A typical Physica Scripta referee would see a long, idiosyncratic reformulation with no new prediction, and editors would probably reject it after review. A more lenient referee might ask for major revision. If so, the revision would have to be a different, much shorter paper (about 15–20 pages) that:

- frames itself explicitly as an interpretation or reformulation;
- positions itself against the literature named below;
- drops or splits off Section 3.

## 3. Major concerns

**M1. "Time is not a separate dimension" is not supported by the construction (abstract; Sec. 2 opening; Eqs. 6–7; Sec. 2.3 last paragraph; Sec. 4.1).**
- Eq. 7 only converts seconds to metres (c = 1). That is units, not the removal of a dimension.
- The absolute time τ stays an independent coordinate in Sec. 2.3: events are labelled (x, τ).
- The invariant the author writes at the end of Sec. 2.3, x_U² − w_U² = x² − w² with w = cτ, is Lorentzian. The Euclidean triangle (Fig. 1; Δx_U² = Δx² + Δy_U²) holds only on Δτ = 0.
- From Sec. 2.4 on, the metric is g_μν dx^μ dx^ν + G₄₄dy², with a 4D Lorentzian g_μν that includes time, plus *y*. That is 4+1 dimensions, so time is a dimension of the construction.
- The suggestion in Sec. 4.1 of a "4+0 metric, relying on τ alone" cannot reproduce light cones or causal structure without further structure. This is a known obstruction in Euclidean-relativity programmes.

*Fix:* drop the claim from the title, abstract and Sec. 2, or show explicitly how causal structure arises without a timelike coordinate.

**M2. The coordinate *y* has three incompatible meanings, and the KK sector double-counts the spatial curvature (Secs. 2.3, 2.4.3–2.4.5, 2.5.3).**
- In Sec. 2.3, y_U(x) = γβx is an *observer-dependent* function on ℝ³. Each observer has its own graph.
- In Sec. 2.4, *y* is a *coordinate* of a 5D manifold.
- In Secs. 2.5.3 and 2.10, *y*(R) is the Flamm height of an embedded slice in *flat* ℝ⁴ (base metric δ_ij, G₄₄ = 1, Eq. 105).
- Sec. 2.4.4–2.4.5 instead takes the base g_μν to *already be Schwarzschild* (Eqs. 50, 82). If the induced metric of the graph y(R) is then built on that base, as in Eq. 105, the radial component is γ² + G₄₄β²γ² ≠ γ². The spatial curvature is counted twice.

The paper needs one 5D metric with a stated base. It must say whether gravity lives in the embedding (flat base) or in g_μν (curved base), and use that choice throughout.

**M3. A non-compact ("unwrapped") flat extra dimension does not by itself give 4D gravity (Secs. 1, 2.4.5).**
- With a flat, non-compact *y* and matter not localized in *y*, the 4D Newton constant obtained by integrating over *y* diverges, and the static force law becomes 1/r³. Torsion-balance tests exclude flat extra dimensions above roughly 50 μm.
- The paper silently uses κ₅T⁽⁵⁾ as if κ₅ = 8πG, and imposes ∂_y = 0 (Eq. 54, the "cylinder sector", a term never defined).
- Existing approaches handle this with brane localization (Randall–Sundrum II, DGP) or with the cylinder condition of induced-matter theory.

*Fix:* state how 4D gravity and the relation between κ₅ and G arise, and cite the relevant work.

**M4. The extra-dimensional scalar sector is either excluded or fine-tuned (Sec. 2.4.5, Eq. 97; abstract).**
- I checked the reduction. Eqs. 55–60, 61, 63, 64, 66 and 70 are correct.
- The ω_BD = 0 identification is correct. Standard KK reduction gives ω = 0, so γ_PPN = ½, which is excluded by Cassini.
- Agreement therefore needs p_y = (3p−ε)/2, which is −ε/2 (a tension) for dust. This exactly cancels the scalar source. No action, equation of state or microphysics supplies this stress; it is introduced only to switch the sector off.
- The abstract presents this as a result ("agreement… requires a stress"). Fine-tuning would be the more accurate word.

The same applies to Eqs. 48–49. What Cassini measures is the spatial metric, i.e. the product G₄₄(dy/dR)². The author admits in Sec. 2.4.3 that rescaling *y* absorbs G₄₄. So "G₄₄ is measured by these tests" restates the convention for *y*.

*Fix:* present Eq. 97 as a fine-tuning condition, discuss whether any physical mechanism could supply it, and remove Eqs. 48–49 or reword them.

**M5. Existence of the absolute foliation, and the physical status of the "outward flow" (Secs. 2.3 "Gravitational case", 2.3 "What is and is not established", 2.10, 4.6, 4.7).**

(a) *Existence.* Flat slices are shown only for spherical vacuum, marginally bound dust, FLRW and first order in J. Generic spacetimes (N-body systems, the Solar System inside a galaxy inside FLRW) have no intrinsically flat foliation. One slicing function cannot remove six curvature components. So the central claim, a single absolute time over ℝ³ in the real Universe, rests on a foliation that is not shown to exist where it matters.

(b) *Horizons.* The outward PG chart is singular on future horizons. It covers the white-hole region, not the interior of a black hole formed by collapse, so the absolute time fails for black holes. The statement "space flows outward from every mass" is then false for black holes formed by collapse. Sec. 2.10.1 limits the claim to "exterior or ordinary stars", but the abstract does not.

(c) *Direction.* The outward direction is a convention ("the inward form is its time reverse and describes the same spacetime", Sec. 2.10.3). Yet the abstract states "space flows outward from every mass, in the same direction as the Hubble flow" as physics.

(d) *Which frame applies locally?* The paper takes the absolute frame to be the CMB frame on large scales and the local outward flow near masses. At Earth this would combine the CMB velocity (370 km s⁻¹), the solar flow at 1 AU (about 42 km s⁻¹) and Earth's own flow (11.2 km s⁻¹). The rule for composing them is not given. The β² addition in Sec. 3.1 holds only for Schwarzschild–de Sitter. Yet Sec. 4.7 uses the 370 km s⁻¹ CMB velocity alone to estimate the annual modulation.

**M6. The absolute frame is unobservable by construction, so Sec. 4.7 overclaims.**
- Secs. 2.3 and 4.6 correctly say α₁ = α₂ = α₃ = 0 and that no local experiment can tell the construction from SR.
- Sec. 4.7 then calls clock and cavity comparisons over the year "the direct experimental test of the absolute-frame reading."
- The construction predicts exactly the SR exponents. Those experiments test Lorentz invariance. A detected departure would falsify this construction as well as SR, not support it.

Separately, Eq. 191 says "a length along the motion as γ^{n∥}" with n∥ = +1 in SR. This assigns the γ of the coordinate transformation (Robertson–Mansouri–Sexl's b) to a physical *length*. In any preferred-frame theory, moving rods are *contracted* by 1/γ in the preferred frame. The γΔx of Sec. 2.3 refers to events that are not simultaneous for U, so it is not a rod length. The dictionary should be stated in terms of transformation coefficients.

*Fix:* say plainly that the reading is empirically equivalent to SR and GR locally, and present Sec. 4.7 as bounds on any future dynamics for *y*.

**M7. Novelty relative to known literature is not established, and key prior work is missing.**
- **Euclidean / "4th spatial coordinate" relativity.** Fig. 1, Eq. 27, and the reading x_U² = x² + y_U² with an extra spatial axis are close to the following. None is cited, and the difference has to be stated:
  - Epstein's diagrams (*Relativity Visualized*, 1985);
  - Newburgh & Phipps (1969);
  - Montanus (Found. Phys. 1991, 1997, 2001);
  - Almeida (2001 onward);
  - Gersten (2003).
- **Neo-Lorentzian and preferred-frame readings.** Mansouri–Sexl, Reichenbach and Malament are cited. Also needed: Bell ("How to teach special relativity"), Brown (*Physical Relativity*), the Lorentz–Poincaré ether literature, and Selleri's absolute synchronization. Eq. 29 is precisely the Mansouri–Sexl transformation with "absolute" synchronization; that is item 1 of the Proposition.
- **River model / PG.** Hamilton & Lisle and Doran are cited. The "time-reversed river" and the reading of redshift as kinematic time dilation relative to the flow are in that literature. The paper's addition, the Flamm height equals the synchronization offset (Eq. 33), is a nice observation but small.
- **FLRW in PG form / Newtonian cosmology.** Milne, McCrea and Lasky–Lun are cited. Gautreau (1984, curvature coordinates in cosmology) and the "cosmological river" literature should be added.
- **Induced-matter theory.** The paper states its difference from Wesson's theory (Sec. 1) but does not compare results. For example, it should say whether Eq. 70 with p_y matches known induced-matter or Brans–Dicke-from-KK results. It does, at the level of standard KK reduction, so the derivation should be cited, not presented as new.
- **MOND and modified inertia.** Milgrom (1994, Ann. Phys.) shows modified inertia must be nonlocal in time. Milgrom (1999, Phys. Lett. A 253, 273) derives a₀ ≈ cH/2π from a de Sitter–Unruh horizon argument, which is essentially Hypothesis M. Famaey & McGaugh (2012, Living Reviews) and Banik & Zhao (2022) review the field. None is cited, and McCulloch is cited only as "contested".

**M8. Section 1.1 is mathematically undefined and should be removed (pp. 2–3, Eqs. 1–5).**
- ℋ, f = ∂_yℋ and **A**(x_i) are never defined. F is "the sum of all forces acting on the point of space". v^(S) = (t, x_μ) with μ = 1…4 has five components, and "velocity" is used for a point.
- Assertion 2, Δt = γd/v, has no stated frame.
- "v′ dilates inversely with coordinate density" is not a statement that can be checked.
- None of this is used later.

A referee will read this section first and judge the paper by it.

**M9. Milky Way comparison uses the escape speed as the orbital speed (Sec. 3.5, p. 24).**
- "v_orbit = βc = √(2GM_enc/R)" is the Newtonian *escape* speed, √2 times the circular speed.
- The quoted numbers confirm this. 241 km s⁻¹ at 5.3 kpc needs M_enc ≈ 3.6×10¹⁰ M☉ with the factor 2. With √(GM/R) it would need about 7×10¹⁰ M☉, more than the adopted total.
- This contradicts the paper's own result v²_local = GM/(R − r_s) ≈ β²c²/2 (Sec. 2.5.5; Eq. 152; Appendix A.2.4).
- All three bullet results in Sec. 3.5 inherit the error: "does not reproduce the curve", the ratio 0.89 → 1.7, and possibly the g₀ fits, if g_N was taken from v_orbit²/R.
- Enclosed-mass spherical formulas are also inappropriate for a disc.

*Fix:* use the Newtonian disc rotation curve of the baryons (as SPARC does), or remove Sec. 3.5.

**M10. Section 3 overstates what the SPARC fit shows (Sec. 3.6, Table 3, abstract).**
- Agreement with 1/2π appears only after adding a 5% velocity floor: 0.189 without it, 0.158 with it. The abstract quotes only the latter, without saying a floor was used.
- κ′ = g₀/(cH₀) scales with the H₀ assumed, apparently 70. The Hubble tension (67 vs 73) shifts κ′ by about ±5%.
- The fixed stellar mass-to-light ratios (0.5/0.7) carry roughly 20% systematic uncertainty on a₀ (McGaugh et al. 2016: g† = 1.20 ± 0.02 ± 0.24). That is larger than the bootstrap interval.
- So "the sample confirms its value" is not supported. The fit recovers the well-known RAR scale.
- χ² = 1935 for 147 dof shows the universal-scale fit is formally rejected; the text notes this.
- The prediction a₀ ∝ H(z) is listed as a falsifier, but existing high-z rotation-curve and baryonic Tully–Fisher studies are not discussed.
- Modified inertia with the acceleration "g" needs a reference frame. Here it would be the absolute frame, which is an interesting link the paper does not make. It also needs nonlocality (Milgrom 1994). Neither is addressed.

**M11. Applying the time-symmetric constraint to FLRW (Sec. 2.5.4, third bullet; Table 2 last row).**
- The relation ⁽³⁾R = 16πGρ/c² requires K_ij = 0 on the slice. That holds for static slices.
- For dust FLRW there is no static slice. The areal-radius (Kodama) slice has K ≠ 0, and its normal observers see a density different from ρ.
- The "cap with L = c/H" static-slice embedding is valid for de Sitter (vacuum energy), not for matter-dominated FLRW.
- The flat-slice statement in Sec. 2.11 (Eq. 160) is the correct one for FLRW.

*Fix:* restrict the claim, or derive it properly.

**M12. Re-derived GR results are presented as checks, but with emphasis and length that suggest more.**
- Section 2.6 calls N = 1/γ "a theorem of the construction". It is the standard GR solution of the static vacuum equations; the Gauss equation for a flat ℝ⁴ embedding just computes the 3-curvature.
- Sec. 2.6.1 (TOV, interior Schwarzschild, Buchdahl), the Tolman VII material, Sec. 2.7 (Lense–Thirring, from the Hartle equation in Schwarzschild exterior), Sec. 2.8 and Appendix A are textbook GR.
- The paper says "consistency checks, not predictions", which is good. But about 15 pages are spent on them.

Classic sources are uncited: Tolman (1939) for Tolman VII and TOV, Oppenheimer–Volkoff (1939), Schwarzschild's interior solution (1916), Buchdahl (1959), and Hartle (1967).

## 4. Minor concerns

1. **Template placeholders (all pages).** "Journal Name", "Journal vv (yyyy) aaaaaa", "Author et al", "dd Month yyyy" and Crossmark appear. Use the proper Physica Scripta template.
2. **Keywords.** "inflation" is irrelevant; nothing on inflation appears. Better choices: Painlevé–Gullstrand, preferred frame, Kaluza–Klein, simultaneity.
3. **Fig. 1 (p. 2).**
   - The hypotenuse label "√(dx_i dx^i) τγ" has a spurious τ. It should be γvτ, which I checked from the two legs.
   - The labels mix dx and dx^(U) notation.
   - The figure adds little beyond Eq. 27.
4. **Sec. 2.1 "Dictionary" is an empty heading.** Table 1 floats above it. Put the table under it.
5. **Circular cross-reference.** Eq. 22 says "As shown in equation 38"; Eq. 38 says "As defined in equation 22".
6. **Forward references in Sec. 2.3.**
   - The "Gravitational case" uses Eq. 155 (Sec. 2.10).
   - "Sign of G₄₄" uses Eqs. 70 and 97 and the four-potential of Sec. 2.5.

   Either move these paragraphs after Sec. 2.10 or bring Sec. 2.10 forward.
7. **Eq. 33 vs Proposition item 3.** The extra factor γ arises because t is the Killing time, not the static observer's proper time. In proper time, N·c(dT−dt) = −dy, which matches item 3 exactly. Say so.
8. **Eq. 37.** "For a normalized radial coordinate g^RR = 1" contradicts the Schwarzschild g^RR = 1 − r_s/R. Γ^R₄₄ is never used.
9. **Eqs. 43–45.** G₄₄^(U) = 1 follows from how dy was defined. "G₄₄^(S)dy² = 0" carries no information, and the conclusion "Newtonian mechanics may remain contained…" does not follow.
10. **p. 12.** "The previously derived 1/R profile": no such derivation precedes it. This looks like a leftover from an earlier version.
11. **p. 13.** "Within the cylinder sector" is undefined. "Cylinder condition" is the standard term; define it.
12. **Units.** Sec. 2.4.5 switches to c = 1, and the rest of the paper is in SI. The relation between κ₅ and G is never stated (see M3).
13. **Nomenclature.** The paper uses "4th spatial coordinate", "fifth dimension", "unwrapped KK dimension" and "density axis" for the same thing. "Unwrapped" is not standard; use "non-compact".
14. **Sec. 2.11, "number of absolute coordinates per measured length".** This phrase is not meaningful. dR/dℓ = N holds only because g_tt g_RR = −1 in Schwarzschild exterior. Say that directly.
15. **Eq. 161.** The Raychaudhuri equation as written (no acceleration term) applies to geodesic flows. With p ≠ 0 the fluid frame is not geodesic.
16. **Sec. 2.7, "What this does not give".** Comparing ω with √δ refers to a "spin dependence of gravity" that appears nowhere else. Remove it. (The numbers do check: 3.4×10⁻¹⁴ s⁻¹, 1.76×10⁻³ s⁻¹, ratio 1.9×10⁻¹¹.)
17. **Sec. 4.1, Ives–Stilwell paragraph.** "A_μ ≈ B_μ … y^(A) < y₀ < y^(B) … local gravitational flux" is unintelligible: A and B are observers, not covectors. Remove it.
18. **Sec. 3.2.** Calling Gm_H/(c²R_H) = ½ an "identity … derived" overstates it. It is the definition of critical density evaluated at c/H. Cite Dicke (1961) together with Sciama.
19. **Sec. 3.4, "The form forced by dimensional analysis".** Nothing is forced. Dimensional analysis leaves p free, and p = ¼ is input from Hypothesis M. Rename the paragraph.
20. **Boxed equations.** Around 40 are boxed, many trivial (Eqs. 8, 11, 13, 16, 35, 44, 45, …). Boxing is not IOP style; remove most.
21. **Eqs. 22–27.** These repeat Eqs. 13–14 and 19. Eq. 26 is a two-line identity.
22. **Mansouri–Sexl test theory.** The sources of the Michelson–Morley bound (β−δ−½ = (−0.6 ± 2.1 ± 1.2)×10⁻¹⁰, attributed to [1, 55]) and the Kennedy–Thorndike bound should be checked against the original papers and cited to the specific result.
23. **Data and code.** A PyPI link is not an archival record. Deposit a versioned release (e.g. on Zenodo with a DOI), and cite SPARC (Lelli et al. 2016) explicitly in the Data Availability statement. It is currently cited only in Sec. 3.6.
24. **Abstract vs Table 3.** The abstract quotes κ′ = 0.158 without mentioning the 5% floor (see M10).
25. **Sec. 2.3, item 5.** Rapidity addition of collinear boosts is standard. One line suffices.
26. **Sec. 2.5.6 / 4.3.** "acts on a body only through its fifth momentum p_y". The notation p_y is already used for the stress along *y* (Eq. 69). Rename one of them.

## 5. Length and structure

The paper is about 2–2.5 times longer than its content warrants. Roughly 20 of 43 pages are either repeated or textbook derivations.

| Material | Pages | Action | Saving |
|---|---|---|---|
| Sec. 1.1 Lighthouse & Clock-Tower, Eqs. 1–5 | 2–3 | Delete (M8) | ~1 p |
| Sec. 2 opening, Eqs. 6–7 | 3 | Two sentences | ~0.4 p |
| Sec. 2.2 + 2.2.1–2.2.2, Eqs. 8–27 | 4–5 | Condense to ~6 lines: Lorentz transform at dt = 0, and γ² = 1+(βγ)² | ~1.7 p |
| Sec. 2.4.1–2.4.2, Eqs. 34–45 | 7–8 | Delete; keep only the line element | ~1.2 p |
| Sec. 2.4.3, Eqs. 46–49 | 8 | Shorten to a paragraph (see M4) | ~0.4 p |
| Sec. 2.4.4, Eq. 50 | 9 | Delete (superseded by 2.4.5) | ~0.3 p |
| Sec. 2.4.5, Eqs. 51–97 | 9–13 | Cite the standard KK reduction; keep Eqs. 61, 66, 70, 97 and the Cassini conclusion; drop Eqs. 73–96 (flux, exterior log solution, weak-field example) | ~3 p |
| Sec. 2.5.5 + 2.6 | 15–17 | Keep, merged. This is the best part | — |
| Sec. 2.6.1 uniform density + Buchdahl | 17–18 | Keep briefly | ~0.3 p |
| Tolman VII, Eqs. 126–142 | 18–19 | Delete or 3 lines in an appendix | ~1.5 p |
| Sec. 2.7 rotation | 19–20 | Condense to ~0.5 p; delete "What this does not give" | ~1 p |
| Sec. 2.8 and 2.9 | 20–21 | Delete; one sentence plus a citation | ~1 p |
| Secs. 4.1–4.5, Eqs. 166–190 | 25–29 | Nearly all repeats Secs. 2.4–2.10 (Eqs. 177–182 ≡ 109; 184–190 ≡ 152–154; 169–171 ≡ 46–47 and A.1.2). Reduce to ~1 page of discussion | ~3.5 p |
| Appendix A | 31–40 | A.1.1 (orbit equation of *spatial* geodesics, Eqs. 200–211) is physically irrelevant: delete. A.1.3–A.3 are textbook Schwarzschild geodesics: replace with a citation (MTW, Hartle) or ≤1 page | ~8 p |
| Sec. 3 | 23–25 | Remove (see below) | ~2.7 p |

**Essential, must stay:**
- Sec. 2.3: the Proposition and Eq. 33, framed against Mansouri–Sexl and Euclidean-relativity work.
- Sec. 2.5.1–2.5.4 (condensed): the pure-gauge A_μ result and the embedding / Hamiltonian-constraint link, Eq. 109.
- Sec. 2.6: lapse from the embedding Hessian, Eqs. 113–120.
- The Buchdahl-as-tilt observation.
- Sec. 2.10: the PG relation and Table 2, fixed per M11.
- Eq. 160 with its shear-balance reading.
- Secs. 4.6–4.7 (corrected per M6), plus an honest limitations section.

With these cuts the paper would be about 16–20 pages, with a clear line of argument.

**Section 3 hurts the paper.** It is logically independent: Sec. 3.7 says it does not follow from the embedding, and μ, the horizon cutoff, g₀ ∝ cH and κ′ are all assumed. Its content (a₀ ≈ cH₀/2π, horizon-based modified inertia, an RAR fit to SPARC) is known. It contains the escape-speed error (M9) and overstates the fit (M10). Including it invites referees to judge the whole paper as MOND-adjacent, and it lengthens an already long paper.

My advice: remove Sec. 3 from this manuscript. Develop it as a separate paper only if the author can derive μ or κ′ from the geometry, or address nonlocality, the frame dependence of "g", the external-field effect, high-z evolution and cluster scales. If none of these is achieved, an astrophysics journal would be the better venue for a carefully done SPARC analysis, and it would need to state its novelty relative to Li et al. (2018) and McGaugh et al. (2016).

## 6. Abstract

**Length.** About 210 words of prose plus eight inline formulas, so roughly 230–250 word-equivalents. That is at or near the usual IOP limit; the author should check the current Physica Scripta guidance.

**Problems.**
- It is equation-heavy: γ = √(1+(∂ₓy)²), ct_U = γcτ − y_U, β² = 2Gm/(c²R), ⅔θ² − σσ = 16πGρ, p_y = (3p−ε)/2, κ′ = 0.158. It reads as a list of results rather than a statement of the problem and the contribution.
- It states as physics two things that are conventions or interpretations: "time is … a ratio of distances" and "space flows outward from every mass".
- "The Sciama identity follows" overstates a definition (minor item 18).
- It presents the p_y condition as a requirement rather than a fine-tuning (M4).
- It quotes κ′ without the 5% floor (M10).
- It spends about a quarter of its length on Hypothesis M, which is unrelated to the title.

**What it does well.** The sentences "these are consistency checks, not predictions" and "predictions that differ from general relativity must come from sectors not yet developed" are honest and should be kept.

**Suggested rewrite (~150 words):** (i) the reformulation; (ii) the main structural result, Eq. 33 and the absolute-slice offset equal to the Flamm height; (iii) that GR and SR are reproduced but not extended, and that the KK scalar sector is Brans–Dicke ω = 0 unless fine-tuned; (iv) what would distinguish the reading.

## 7. Strengths

- **Candour.** The "What is and is not established" paragraphs in Secs. 2.3, 2.6 and 3.7, and the scope statements in Secs. 2.10.4 and 2.11, are exemplary and rare in submissions of this kind.
- **Correct calculations, checked line by line:**
  - Eqs. 8–21 (trivial);
  - the Sec. 2.3 Proposition and the Reichenbach ε = (1−β)/2 with dy = (1−2ε)dℓ;
  - the PG transformation of Eq. 157;
  - the KK reduction (Eqs. 55–70), the exterior scalar solution (Eq. 87) with its weak-field expansion and Eq. 94;
  - the ω_BD = 0 identification and Eq. 97;
  - Eq. 108 and the cap and critical-density cases;
  - the lapse from the embedding (Eqs. 115–120, including the radial component);
  - the TOV form (Eq. 123), the interior Schwarzschild solution, Buchdahl with arccos(1/3) = 70.5°;
  - the Tolman VII algebra, including the maximum 25/24 and Eq. 138;
  - Lense–Thirring (Eqs. 144–148), with the GP-B number (≈ 41 mas yr⁻¹) reproduced;
  - the Earth ω / √δ numbers;
  - shear balance, θ = 3v/(2R) and σσ = 3v²/(2R²), and the Friedmann limit;
  - the Sec. 3.1 ratios (≈ 10⁻⁵ and 3×10⁻⁴; 0.6–1.8 km s⁻¹);
  - Eqs. 164–165;
  - Appendix A (Eqs. 275, 289–291, 299–300);
  - the RMS mapping arithmetic (annual modulation 2.5×10⁻⁷).

  The one physics error I found is M9.
- **Genuinely nice observations**, worth keeping in a shorter paper:
  - the offset between the flat PG slicing and the static slicing equals the Flamm height (Eq. 33);
  - the lapse fixed by the Hessian of the embedding height (Eq. 114), with redshift as the foreshortening cos θ of the slice;
  - the Buchdahl bound as a surface tilt below 70.5°;
  - ⅔θ² − σσ = 16πGρ covering both the shear-balanced flow around a mass and the Friedmann equation.

  These are good teaching material and could suit an educational or foundations venue, provided they are positioned against the river-model and Euclidean-relativity literature.
- **Testing frameworks.** The paper engages correctly with Robertson–Mansouri–Sexl and the PPN α₁, α₂ parameters, and with the condition that any future dynamics for *y* must meet those bounds.
- **Reproducibility.** Code is public, and AI use is declared.
