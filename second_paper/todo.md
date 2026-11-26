# Paper two: derivations to-do

Our working list. One item at a time, in order unless an item is blocked. Each item records its goal, what counts as done, and what we have found so far.

**Required geometry:** self-consistent co-expansion (see `../AGENTS.md`). **Source of gravity:** `2 rho/(1 + gamma^2)` from the action (item 1); rest mass per absolute volume is not by itself the source.
**Code:** `physics/symbolic/function_generators/paper_two/`, exported only from its `__init__.py`; symbols from `physics/symbolic/variables.py` as overridable defaults, never numeric defaults in symbolic functions.
**Write-ups:** sections in `sections/`; paper one is `../iop/main.tex` (edit in place).

Status: `[ ]` not started, `[~]` in progress, `[x]` done, `[!]` result conflicts with observation.
**Notebook:** `notebooks/paper_two_notes.ipynb` is how results are shown to the author; keep it in step with this file (its "Where we are" cell mirrors the section below).

---

## GEOMETRY CHANGE (2026-11-26): co-expansion along the flow

The author chose co-expansion along the direction of the flow only (as in SR, lengths change only along the motion), so that paper one claims no departure from GR that experiment does not support. Result (module `flow_geometry`, 15/15; notebook section 0): exterior exactly Schwarzschild; flow rule beta^2 = 2Gm(R)/(c^2 R) = Hamiltonian constraint of the Einstein equations on flat absolute slices (and the Friedmann equation); inclined space = Flamm's paraboloid; signature (+,+,+,+) with every interval a sum of squares; field equations are Einstein's. Paper one (`iop/main.tex`) rewritten to it; old version `iop/main_v7_isotropic_coexpansion.tex`.

**Consequence for this list:** items 1-9 below were written for isotropic co-expansion and are now history (they explain why the direction matters: the 4% SEP violation, the moving-star obstruction).

**Plan under the new geometry (2026-11-26), in proposed order:**
- `[x]` **A1. The flow obeys Newton** (done 2026-11-26, module `newtonian_flow` 9/9, notebook 0b, paper §3.3: zero-energy flow + mass carried by the flow => all Einstein equations for dust; Newton's acceleration, vacuum, Hubble flow follow; static matter needs pressure). Show that a flow of flat absolute space with zero energy (beta^2 = 2Gm/(c^2 R)) and Newtonian acceleration (dW/dT + W.grad W = -Gm/R^2) gives the spherical Einstein equations exactly (dust: Lemaitre-Tolman; vacuum: Schwarzschild). Goal: spherical GR derived from absolute time + flowing Euclidean space, not imported.
- `[~]` **A2. A field equation for y** (equation derived 2026-11-26, module `y_field` 6/6, notebook 0c, paper §3.4: spherical y' = beta gamma with the same m as A1; Flamm in vacuum; quadratic in the weak field. NEXT: solve numerically for two masses, axisymmetric). On the static slice the space is a graph y(x) in Euclidean R^3 x y. Its scalar curvature is 2 sigma_2 of the second fundamental form (Gauss), and GR's constraint on that slice says R = 16 pi G rho/c^2. So: sigma_2(II[y]) = 8 pi G rho/c^2, with II_ij = d_i d_j y/sqrt(1 + |grad y|^2). Check: point mass gives Flamm; then solve for two masses (the inclined space of several bodies, which the conformally flat Brill-Lindquist metric could not provide).
- `[x]` **B. Absolute time inside matter** (done 2026-11-26, module `absolute_time_matter` 6/6, numerics `functions/paper_two/absolute_time.py` 3/3, notebook 0d, paper §3.3: flat slices for any static body, N = sqrt(AB), d ln N/dR = 4 pi G R B (eps+p)/c^4, flow still the escape speed, offset -dy/sqrt(A); 1.39 M_sun neutron star N_c = 0.67). For a star with pressure, flat slices need a lapse N = sqrt(-g_tt g_RR) != 1; derive N from the enthalpy (d ln N/dR = 4 pi G R (eps + p) g_RR/c^4) and read it in the y picture.
- `[ ]` **C. Several bodies' "now".** Do two bodies admit flat absolute slices (test at 1PN/2PN)? Is the author's surface-simultaneity rule consistent with it?
- `[ ]` **D. Rotation.** Kerr in Doran's flat-slice form: co-expansion along a rotating flow, frame dragging as the flow's vorticity, the (+,+,+,+) form.
- `[ ]` **E. Cosmology.** Co-expansion along the Hubble flow; cosmological redshift as co-expansion; same Hamiltonian constraint (Friedmann).
- `[ ]` **F. Collapse with an outward flow.** The outward chart covers the time reverse of a black-hole interior; how does collapse look with space flowing outward (Oppenheimer-Snyder in flow form)?

Earlier open items (kept):
- `[ ]` the slicing of absolute time for several bodies (how bodies' "now" joins; author's candidate: surfaces simultaneous);
- `[ ]` a dynamics of `y` of its own, beyond the inclination of space (the long-term 4+0 goal);
- `[ ]` slicing for collapse (the outward flow covers the time reverse of a black-hole interior);
- `[ ]` the co-expansion form of an expanding universe;
- `[ ]` rewrite the Medium article (`../medium_article.md`) and the video to the new geometry.

---

## Where we are (updated 2026-11-25, evening)

**Equivalence principle, status:**
- `[x]` Weak equivalence principle: every body falls the same way, because all matter co-moves along `y` (from the geometry).
- `[x]` Strong equivalence principle at first order: `M_g = m_i = M + E_g/(2c^2)` for a body in equilibrium; eta_N = 0, consistent with lunar laser ranging.
- `[x]` Interiors with the full source and pressure (module `stellar_structure`, 13/13; numerics `physics/functions/paper_two/stellar.py`, 9/9; notebook section 10).
- `[!]` **Strong-field equivalence principle: violated.** `E - M c^2 = int gamma^2 (eps + 3p)(gamma - 1)^2/(1 + gamma^2) d^3x >= 0` (exact; second order, ~u^2/2). For the 1.4378 M_sun pulsar of PSR J0337+1715, `M/E - 1 = -0.040` (Gamma = 2) to `-0.047` (Gamma = 2.5), against the bound `(0.5 +- 1.8) x 10^-6`: excluded by ~2 x 10^4, *if the inertial mass is the energy E*.

**Why:** in the class "one field F(gamma), harmonic outside matter, quadratic gradient energy, matter on the co-expansion geometry", the masses agree exactly only for `F = ln gamma` (exponential metric `gamma = e^u`). Co-expansion's measured-radius rule makes `psi = gamma - 1/gamma` harmonic instead; the two differ first at u^3.

**Decision needed from the author (blocks most other items):**
- **(A, chosen)** keep the measured-radius rule; item 3 must then give a moving star inertial mass M (not E) to 1e-6;
- (B, set aside: its shadow fits EHT worse than GR) make ln gamma the harmonic field: same co-expansion metric form, co-motion along y, PPN gamma = beta = 1, exact SEP; the flow rule changes at u^3 (`beta^2 = 1 - e^{-2u}` instead of `2u/gamma`);
- (C) a field action outside the class (several fields, non-quadratic, tensor): part of item 3.

**Decision (author, 2026-11-25 19:23): back to A.** The author's test for B was that it must match the strong-field data *better* than GR. It does not: B's shadow is +4.6% larger than GR's, but both EHT measurements of Sgr A* sit below GR (delta = -0.08 +- 0.09 VLTI, -0.04 (+0.09/-0.10) Keck) and M87* gives delta = -0.01 +- 0.17. GR (and A, whose photon sphere, shadow and ISCO equal GR's) predict delta = 0, closer to the data. The ISCO is not measured independently of spin, so it does not decide. **B is set aside; A is the working option:** the time-dependent sector (item 3) must give a moving star inertial mass M, not E, to 1e-6.

History of the decision: 19:17 the author chose to pursue B with A as the fallback.
Superseded:  Under B the rule "the flow is set by the measured radius" (gamma - 1/gamma = 2u) is replaced by "co-expansion compounds": ln gamma is harmonic, gamma = e^u, superposition is multiplicative (gamma = prod e^{u_i}), and the source of gravity is energy (dust: rho/gamma; fluid: gamma^2 (eps + 3p)). First look: photon sphere R = 3.297M, ISCO R = 6.338M, shadow b = 5.437M (+4.6% vs GR; EHT Sgr A*: delta = -0.08 +- 0.09 VLTI, -0.04 (+0.09/-0.10) Keck), throat R_min = eM at r = M (R -> infinity as r -> 0; no horizon). To do next: rebuild the B geometry in the package and re-run every test of paper one (2PN orbits, deflection, ringdown, interiors, several masses).

**Other findings from the interiors:** pressure gravitates (`eps + 3p`); hydrostatics reduces to `h = gamma/gamma_s`; passive mass = active mass exactly; virial `E_field = 3 int gamma^2 p`; all stars horizonless; Gamma = 2 sequence has no maximum mass up to its end (h_c ~ 2.9), stability unchecked.

**Biggest risk, not yet addressed:** item 3 (time-dependent equations: binary-pulsar decay, gravitational waves).

---

## 1. `[~]` Action and matter coupling

**Goal:** one action from which the field equation and the motion of bodies both follow, with bodies moving along the co-expansion geometry `ds^2 = -c^2 dt^2/gamma^2 + gamma^2 |dx|^2`. That motion is co-motion along `y`, and it is what gives the equivalence principle, so it is not negotiable. The definition of mass is: if the equations require a different gravitational source than rest mass per absolute volume, we follow the equations.

**Done when:** the action is written down; its variation gives the field equation and geodesic motion; the point-mass solution `gamma = u + sqrt(1 + u^2)` is recovered; PPN gamma = beta = 1; and the Nordtvedt parameter eta_N is computed and compared with lunar laser ranging (|eta_N| ~ 1e-4).

**Found so far (2026-11-25, checked with sympy):**
- **The field term is fixed.** The point-mass solution needs `psi = gamma - 1/gamma` to be harmonic outside matter, so the field term of the action must be `|grad psi|^2` (up to a constant). Any other choice changes the vacuum solution.
- **Ruled out: a gravitational charge equal to rest mass.** Making a body's gravitational energy exactly linear in psi (so that its source is exactly rest mass per absolute volume) means bodies no longer follow the co-expansion geometry: `-g00 = 1 - 2U + U^2`, beta_PPN = 1/2, perihelion advance 7/6 of GR. Fixing it would need gamma_PPN = 3/4, which Cassini excludes.
- **What co-motion along y gives instead.** With bodies on the co-expansion geodesics (static energy `m c^2 / gamma`), the source of the field equation is `2 rho / (1 + gamma^2)`, because `d(1/gamma)/dpsi = -1/(1 + gamma^2)`:
  `lap(gamma - 1/gamma) = -(8 pi G / c^2) * 2 rho / (1 + gamma^2)`.
  Outside matter nothing changes: the point-mass solution, exact superposition of point masses, and all PPN results stand. Inside matter the source is reduced by `2/(1 + gamma^2)`, which in the weak field is `rho (1 + Phi/c^2)`: a body's gravitational mass is `M + 2 E_g / c^2` (E_g its Newtonian binding energy, negative), not its rest mass.

- **Falling is relative co-motion (author's requirement, 2026-11-25).** Matter of the Earth co-moves along `y`; a body at rest at `R > R_Earth` does not, which is why it appears to fall to the surface. In the geometry, the acceleration of a non-co-moving body relative to co-moving (static) matter is `a = c^2 gamma'/gamma^2 = 2GM / (r^2 (1 + gamma^2)) = GM / (R^2 (1 - GM/(c^2 R)))` (checked; Newton in the weak field; GR's static-observer value is `GM / (R^2 sqrt(1 - 2GM/(c^2 R)))`, equal at first order). The factor `2/(1 + gamma^2)` is the same one that appears in the field's source: both are `-d(1/gamma)/dpsi`. The action must distinguish co-moving matter from free bodies and give the fall as their relative co-motion.

**Action found (2026-11-25; module `co_expansion_action`, 8/8 checks):**
`S = -(c^4/32 pi G) int |grad psi|^2 d^3x dt - sum m c^2 int sqrt(1/gamma^2 - gamma^2 v^2/c^2) dt`.
- Variation gives the field equation with source `sigma = 2 rho/(1 + gamma^2)` (rho = rest mass per absolute volume), free bodies on the co-expansion geodesics, and the fall `a = 2GM/(r^2 (1 + gamma^2))` of a non-co-moving body relative to co-moving matter.
- **Strong equivalence principle holds at first order.** A moving particle's weight in the source is `m (1 + Phi/c^2 + 3v^2/(2c^2))`, its energy `m c^2 + m Phi + m v^2/2`. For a bound body: `M_g = M + (2E_g + 3T)/c^2`, `m_i = M + (E_g + T)/c^2` (field energy -E_g included). In equilibrium (virial 2T + E_g = 0) both are `M + E_g/(2c^2)`, as in GR: eta_N = 0. This matches eta_N = 4 beta - gamma - 3 = 0.
- **Correction:** an earlier budget (same day) used an unsupported static dust ball (T = 0), which is not in equilibrium, and wrongly gave eta_N = 1 and "the field energy must be a source". That is withdrawn; paper one §6.2 has been corrected.
- A source of exactly rho is excluded (it needs a static clock rate 1 - psi/2: beta_PPN = 1/2, perihelion 7/6 of GR).

**Next steps, in order** (order changed 2026-11-25: the interior comes first because the strong-field test is built on it):
1. `[x]` **Interiors with the full source** and pressure: done (see "Where we are"). Source `2 gamma^3 (eps + 3p)/(1 + gamma^2)`, `h = gamma/gamma_s`, horizonless, no maximum mass found for Gamma = 2. Open: stability of the sequence.
2. `[!]` **Strong-field equivalence principle**: computed; violated by ~4% for neutron stars (white dwarfs ~1e-10), excluded by PSR J0337+1715 as it stands. Author chose A (B set aside, 2026-11-25): the fix must come from the time-dependent sector, item 3, which is now the next item.
3. **Write-up:** update `sections/field_equation.tex` and `sections/compact_objects.tex` to the action and source (paper one §3.3 and §6.2 already updated).

---

## 2. `[ ]` Horizonless surfaces against observations

**Goal:** confront the horizonless endpoint of collapse (`sections/compact_objects.tex`) with the observational arguments against surfaces around black-hole candidates.
**Done when:** the relevant published limits (Sgr A* / M87* accretion luminosity, any echo searches) are collected with citations, and the model's surface redshift and surface emission are compared with them quantitatively.
**Notes:** the surface lies at `R = GM/c^2 + sqrt((GM/c^2)^2 + a^2)`, redshift `z = u + sqrt(1 + u^2) - 1`; the photon sphere and shadow are GR's.

## 3. `[~]` Time-dependent field equations (tensor sector) — NEXT (option A)

**First results (2026-11-25, module `time_dependent`, 6/6; notebook section 11):**
- Matter metric, covariant: `g = gamma^2 eta + (gamma^2 - 1/gamma^2) u u`, u = absolute frame. Option A needs m_i = M != E, impossible in any Lorentz/diffeomorphism-invariant completion (P = E V), so the completion must keep this preferred frame and still give alpha_1 ~ alpha_2 ~ 0 at first order.
- Unit-lapse foliation action `sqrt(h)[K_ij K^ij - lambda K^2 + xi R]` (paper one's flow form, metric only): GR's PG solution at lambda = xi = 1; co-expansion forces lambda = 1 at first order, then the momentum constraint fails at O(M^(5/2)) (residual 4 sqrt2 (M/r)^(5/2)) for every xi. **A field beyond the metric is required** (psi, i.e. y).
- That field's effective stress at leading order is a negative-energy scalar's (rho = p_r = -g^2/8 pi G, p_t = -p_r): ghost-like.
- **Author (2026-11-25 19:51): negative energy is acceptable in this geometry.** Free fall is the co-expanding surface (a fixed temporal surface moving outward with the Earth) meeting a body that does not co-move. Working reading: the negative energy is the Newtonian field energy (-g^2/8 pi G is exactly Newton's field-energy density), and it is harmless if psi is *not a wave*: psi is set instantaneously on each absolute-time slice (an elliptic constraint, like Newton's potential and GR's conformal mode). Then there is no negative-energy radiation and no scalar radiation in binaries; only tensor waves propagate.
- Consequence to fix: with psi instantaneous and no flow response to moving matter (g_0i = 0 in the absolute frame), PPN alpha_1 = -8 (gauge-independent, given gamma_PPN = 1), against |alpha_1| < ~1e-4 (lunar laser ranging). **Next: the flow (shift) equation for moving sources** — it must give GR's gravitomagnetism at first order (alpha_1 = alpha_2 = 0, Gravity Probe B), and then the inertial mass of a moving star (target m_i = M).
- `[x]` **Flow response at first order (2026-11-25, module `flow_response`, 9/9; notebook 11b).** Since lambda = 1 is forced, the flow obeys the linearised momentum constraint: `w = g_0i = -4V + (1/2) grad(dchi/dt) = -(7/2)V - (1/2)W`. Verified identically for arbitrary moving matter. Static sector's g_00 equals GR's through 1PN (psi source weights); with the flow response all PPN parameters equal GR's (alpha_1 = alpha_2 = alpha_3 = zeta_i = xi = 0); frame dragging w = -2 J x r/r^3 = GR (GP-B, LAGEOS); first-order inertial mass = energy.
- **Author (2026-11-25 20:06) on the slicing:** around one uniform spherical body absolute time is constant on spheres R = const; how one body's "now" relates to another's (Earth/Moon) is unresolved; candidate (assumption, not fact): body surfaces are simultaneous. Note: that fixes one constant per body (the seeds of item 8); the radial tilt of "now" is a separate question.
- `[x]` **Static slicing (lapse 1/gamma) — module `static_foliation`, 4/4; notebook 11c.** Preferred-slicing action for static fields: `sqrt(h) N [R + alpha a_i a^i]`. Co-expansion is an **exact vacuum solution at alpha = 2** (GR at alpha = 0). But the lapse equation with matter is `(1 - alpha/2) lap phi = 4 pi G rho`: at alpha = 2 matter drops out, so the matter coupling must come from psi's equation. Next: combine; then redo the flow response (11b assumed the linearised momentum constraint) and the inertial mass in this slicing.
- `[x]` **Combined theory, linear order (2026-11-25, module `combined_theory`, 7/7; notebook 11d).** Static slicing; metric from psi + flow + tensor waves (N = 1/gamma(psi), h = gamma^2 (delta + h^TT), shift free); action `(1/16 pi G_b) int sqrt(h) N [K_ij K^ij - lambda K^2 + R + alpha a^2] - (c^4/32 pi G) int |grad psi|^2 + S_m`. Coefficients fixed: alpha = 2 (static part on the ansatz is -4 lap ln gamma + (alpha-2)|grad ln gamma|^2 for any gamma: boundary term iff alpha = 2, so static sector = psi's); lambda = 1 (flow equation lap(dzeta/dt) = 4 pi G_b div J = time derivative of psi's equation + continuity: psi instantaneous, no scalar waves; otherwise c_s^2 = (G_b/G)(1-lambda)/(1-3 lambda)); G_b = G (consistency); xi = 1 (GW speed). Linear consequences: div w = 3 dU/dt, w^T = -4 V^T, i.e. 11b's flow response is derived.
- `[x]` **Moving star at second order (2026-11-25, module `moving_star`, 5/5; notebook 11e).** O(V^2) Lagrangian `L_2[W] = int (1/2)(sqrt(h)/N)(eps+p)|W|^2 + (1/16 pi G) sqrt(h) N (K.K - K^2)`, W = V + shift, m_i = 2 L_2/V^2 with W -> V far away; reduced to radial F, H. GR exterior: uniform motion F = 1 exact (boost invariance). **Co-expansion exterior: F = 1 is not a solution (residual 2M^2/3r^2); the longitudinal flow is fixed only at O(M^2), where co-expansion departs from GR; far-field modes F ~ r^2, 1/r only. A body cannot move uniformly relative to a distant absolute frame: its frame moves with it (or the inertia diverges).** Matches the author's note that absolute time is defined around each body; the inertial-mass test (PSR J0337) cannot be posed until the inter-body rule (item 8) is known.
- `[ ]` **Next:** (1) the rule connecting different bodies' absolute frames (item 8 merged here): a body moving relative to another body's frame, e.g. the Moon in the Earth's; (2) then the inertial mass and PSR J0337; (3) constraint consistency beyond linear order.
- `[~]` Superseded: **Next: the combined theory at second order.** (a) constraint consistency beyond linear order, and whether the flow form's O(M^(5/2)) failure is absent in the static slicing; (b) inertial mass of a moving neutron star (target M; PSR J0337+1715). One nonlinear flow equation must (a) remove the O(M^(5/2)) momentum-constraint failure of the static flow, and (b) give a moving neutron star inertial mass M rather than E (PSR J0337+1715). Also settle which slicing is absolute time (flow form T vs static t): the first-order results do not depend on it. Next: write metric + psi on the absolute slicing, check the sign of the psi kinetic energy, its stability, whether psi radiates (must not, beyond GR's quadrupole), and the inertial mass of a moving star.


**Goal:** field equations for moving sources whose static limit is item 1's equation.
**Done when:** the equations are written, the static co-expansion geometry is an exact solution, and radiation is tensor (two polarizations) with the quadrupole formula at leading order (binary-pulsar decay).
**Lead:** read through the Einstein equations, the co-expansion exterior has `rho ~ p_r ~ -p_t ~ -g^2/(8 pi G)` at leading order, the stress of a negative-kinetic scalar. First test: GR + such a field built from `y`; is the co-expansion geometry an exact solution or only leading-order?
**Depends on:** 1.

## 4. `[ ]` Realistic neutron stars

**Goal:** hydrostatic equilibrium with a nuclear equation of state; mass-radius curves; compare with NICER and with measured masses.
**Done when:** mass-radius curves for at least two standard equations of state, compared with GR and with data.
**Notes:** *outdated:* "gravitational mass = baryonic mass (about 10% more than GR)" came from the old mass definition; with the source `2 rho/(1 + gamma^2)` the gravitational mass includes binding (first order: `M + E_g/(2c^2)`, as in GR). Redo after item 1, step 1. no Buchdahl limit for incompressible matter; check the dominant energy condition. Code: `compact_objects.uniform_star` is the incompressible starting point.

## 5. `[ ]` Cosmic co-expansion

**Goal:** the co-expansion form of an expanding universe (FLRW), and what "Earth expands with the universe" means there.
**Done when:** the cosmological metric under co-expansion is derived, and the drift of G is computed against the lunar-laser-ranging bound `dot G / G = (7.1 +- 7.6) x 10^-14 / yr`.

## 6. `[ ]` Rotation from the field equation

**Goal:** the gravitomagnetic field (Lense-Thirring) from the model, not imported from GR.
**Done when:** the non-gradient component `a_mu` follows from the model's equations and reproduces Gravity Probe B (37.2 +- 7.2 mas/yr) at first order.
**Depends on:** 3.

## 7. `[ ]` Ringdown properly

**Goal:** quasinormal modes from the model's own perturbation equations, including spin, replacing the eikonal estimate (`tau x 2/sqrt3`).
**Done when:** l = 2 frequencies and damping times computed and compared with GWTC-3 (delta f_220, delta tau_220).
**Depends on:** 3 (and 6 for spin).

## 8. `[ ]` Several masses: the direction of the flow

**Goal:** the field equation fixes `|grad y|` for any static configuration; the direction of `grad y` (the eikonal divides and their free constants) is still undetermined.
**Done when:** a rule fixing it follows from the dynamics (items 1/3), or it is shown to be unobservable.

## 9. `[ ]` Time of a body at rest; clocks as internal motion

**Goal:** older items 1-2 of `../further_investigation.md`: define the time of a body at rest from the change of everything else (ephemeris time), and derive the clock rate `1/gamma` from a clock's internal motion.
**Done when:** both derivations reproduce `c d tau = dx / sin psi` and `dt_U = d tau / gamma`, and any departure is checked against the clock bounds.

---

## Done

- `[x]` Co-expansion postulate, self-consistent gamma, exact metric, 1PN = GR, 2PN differences (`co_expansion`, `sections/co_expansion.tex`, paper one §3).
- `[x]` Absolute frame reconciled with the outward flow (paper one §3.2-3.4).
- `[x]` Static field equation and exact superposition (`co_expansion_field`, `sections/field_equation.tex`, paper one §3.3).
- `[x]` Action, source inside matter, fall as relative co-motion, the weak equivalence principle, and the strong equivalence principle at first order (item 1; paper one §3.3, §6.2). The strong-field version is still open (item 1, step 2).
- `[x]` Interactive notes notebook `notebooks/paper_two_notes.ipynb` (2026-11-25); all six check suites pass. Check calls must pass `rtol`, `atol`, `tol` and `n` explicitly (the shared helper's defaults are symbols).
- `[x]` Compact objects: superseded by the full-source interiors (`stellar_structure`, `functions/paper_two/stellar.py`, notebook section 10); `sections/compact_objects.tex` still describes the leading-order version.
