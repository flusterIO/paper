# Paper two: derivations to-do

Our working list. One item at a time, in order unless an item is blocked. Each item records its goal, what counts as done, and what we have found so far.

**Required geometry:** self-consistent co-expansion (see `../AGENTS.md`). **Mass:** being re-derived in item 1 (rest mass per absolute volume is not consistent with motion along the co-expansion geometry).
**Code:** `physics/symbolic/function_generators/paper_two/`, exported only from its `__init__.py`; symbols from `physics/symbolic/variables.py` as overridable defaults, never numeric defaults in symbolic functions.
**Write-ups:** sections in `sections/`; paper one is `../iop/main.tex` (edit in place).

Status: `[ ]` not started, `[~]` in progress, `[x]` done.

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

**Action written and tested (2026-11-25; module `co_expansion_action`, 9/9 checks):**
`S = -(c^4/32 pi G) int |grad psi|^2 d^3x dt - sum m c^2 int sqrt(1/gamma^2 - gamma^2 v^2/c^2) dt`.
- Its variation gives `lap psi = -(8 pi G/c^2) * 2 rho/(1 + gamma^2)`, free bodies on the co-expansion geodesics, and the fall `a = 2GM/(r^2 (1 + gamma^2))` relative to co-moving matter.
- **It fails the strong equivalence principle.** For a uniform ball (weak field): gravitational mass `M + 2E_g/c^2`, field energy `-E_g`, total energy `M + E_g/c^2`, so `m_g/m_i = 1 + E_g/(M c^2)` and eta_N = 1. Lunar laser ranging requires |eta_N| ~ 1e-4.
- **The missing piece is exact:** the gravitational source is short by the field's own energy. Adding the field energy to the source gives gravitational mass = total energy, eta_N = 0 (checked). The co-expansion geometry already has this structure in GR terms (its exterior source is `~ -g^2/(8 pi G)`, the field energy).

**Next steps, in order:**
1. **Let the field's energy source psi.** Write the field equation with source `2 rho/(1 + gamma^2)` plus the field energy density, and find the map `gamma(field)` for which the point-mass solution is still `gamma = u + sqrt(1 + u^2)` (so PPN and the exact metric are unchanged). Derive it from an action.
2. **Recompute the mass budget** with that action: confirm `m_g = m_i` (eta_N = 0) at first order, then estimate the next order for neutron stars (PSR J0337+1715, Delta ~ 1e-6).
3. **Interiors.** Redo the uniform star (`compact_objects`) with the final source; check whether the no-Buchdahl result survives.
4. **Write-up.** Update `sections/field_equation.tex`, `sections/compact_objects.tex` and paper one (§3.3, §6.2): the source of gravity is the total energy (rest mass + binding + field), not rest mass per absolute volume.

---

## 2. `[ ]` Horizonless surfaces against observations

**Goal:** confront the horizonless endpoint of collapse (`sections/compact_objects.tex`) with the observational arguments against surfaces around black-hole candidates.
**Done when:** the relevant published limits (Sgr A* / M87* accretion luminosity, any echo searches) are collected with citations, and the model's surface redshift and surface emission are compared with them quantitatively.
**Notes:** the surface lies at `R = GM/c^2 + sqrt((GM/c^2)^2 + a^2)`, redshift `z = u + sqrt(1 + u^2) - 1`; the photon sphere and shadow are GR's.

## 3. `[ ]` Time-dependent field equations (tensor sector)

**Goal:** field equations for moving sources whose static limit is item 1's equation.
**Done when:** the equations are written, the static co-expansion geometry is an exact solution, and radiation is tensor (two polarizations) with the quadrupole formula at leading order (binary-pulsar decay).
**Lead:** read through the Einstein equations, the co-expansion exterior has `rho ~ p_r ~ -p_t ~ -g^2/(8 pi G)` at leading order, the stress of a negative-kinetic scalar. First test: GR + such a field built from `y`; is the co-expansion geometry an exact solution or only leading-order?
**Depends on:** 1.

## 4. `[ ]` Realistic neutron stars

**Goal:** hydrostatic equilibrium with a nuclear equation of state; mass-radius curves; compare with NICER and with measured masses.
**Done when:** mass-radius curves for at least two standard equations of state, compared with GR and with data.
**Notes:** gravitational mass = baryonic mass here (about 10% more than GR for a given star); no Buchdahl limit for incompressible matter; check the dominant energy condition. Code: `compact_objects.uniform_star` is the incompressible starting point.

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
- `[~]` Definition of mass and its strong-equivalence-principle requirement (paper one §6.2): being revised in item 1.
- `[x]` Compact objects: no Buchdahl limit, horizonless endpoint (`compact_objects`, `sections/compact_objects.tex`).
