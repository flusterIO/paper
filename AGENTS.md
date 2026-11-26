# Shared writing guidance

## Project

> The version that we're currently working on is contained within the `./iop` directory. Use the bibliography, `main.tex` and other associted files from that directory.

- This folder contains a research manuscript on a proposed relationship among time, gravitation, cosmic expansion, and a fourth density-like spatial coordinate. The working LaTeX manuscript is `main.tex`; references are in `citations.bib`; figures and their sources are under `diagrams/`.
- The goal is to develop a submission-ready paper during November 2026. Treat November 30, 2026 as the working deadline unless the author sets another date.
- The target journal is not yet specified. Do not assume the included Springer Nature template determines the eventual venue or its requirements.

### REQUIRED GEOMETRY: co-expansion along the flow (since 2026-11-26)

This is a fundamental, permanent part of the model. Every new derivation, section, notebook, video script and code path must use it.

- **Co-expansion along the flow is the source of the equivalence principle.** Matter at rest relative to a mass moves through the outward-flowing space and co-expands as a moving body does in special relativity: lengths ALONG the flow scale by the Lorentz factor `gamma` of the flow, clocks run at `1/gamma`, and lengths ACROSS the flow are unchanged (exponents -1, +1, 0, the same as SR). It is the same for all matter. A body released at rest no longer co-moves along `y` with the matter around it and falls relative to it.
- **Signature (+,+,+,+): write every interval as a sum of squares.** Static observer: `c^2 dt^2/gamma^2 = c^2 dtau^2 + gamma^2 dR^2 + R^2 dOmega^2`. Absolute frame: `c^2 dT^2 = c^2 dtau^2 + |dx - W dT|^2` on FLAT absolute slices, `W = beta c R-hat` outward. SR: `(c dtau)^2 = (c dt_U)^2 + dx^2`. Do not write Lorentzian forms except to identify a result with GR.
- **The flow is set by the measured radius** `R` (on flat absolute slices the absolute radius equals the measured radius): `beta^2 = 2GM/(c^2 R)`, `gamma = 1/sqrt(1 - 2GM/(c^2 R))`. With enclosed mass, `beta^2 = 2Gm(R)/(c^2 R)` is the Hamiltonian constraint of the Einstein equations on flat slices (and the Friedmann equation for the Hubble flow).
- **Inclined space = Flamm's paraboloid:** `dy/dR = beta gamma`, `y = 2 sqrt(2M(R - 2M))`; synchronization offset `c(dT - dt) = -beta gamma^2 dR = -gamma dy`.
- **Field equations are Einstein's**, written on the slices of absolute time. The geometry of an isolated mass is exactly Schwarzschild; every GR prediction holds (SEP/PSR J0337, binary pulsars, GW170817, shadow, ISCO 6M, deflection 4M/b + 15pi/4 (M/b)^2). Earth: proper radius exceeds measured radius by ~GM/(3c^2) = 1.5 mm (uniform body).
- **Do NOT reintroduce co-expansion in every direction** (`ds^2 = -dt^2/gamma^2 + gamma^2|dx|^2`, `gamma = u + sqrt(1+u^2)`): it departs from GR at second order and its neutron stars violate the strong equivalence principle by ~4%, excluded by PSR J0337+1715 by ~2e4. That version is kept only as history (`iop/main_v7_isotropic_coexpansion.tex`, Zenodo v7; paper-two modules `co_expansion`, `stellar_structure`, ...).
- **Code:** `physics.symbolic.function_generators.paper_two.flow_geometry` (`check_flow_geometry`, 15 checks).

**Paper one (`iop/main.tex`) uses co-expansion along the flow since 2026-11-26.** The text submitted to Physica Scripta on 2026-11-24 (`iop/main_as_submitted.tex`) used the same outward Painleve-Gullstrand slices (flat, unit lapse) and is consistent with this geometry; the 2026-11-25 version with co-expansion in every direction (`iop/main_v7_isotropic_coexpansion.tex`) is superseded.

### Git

- Write all commits as if you're one of the following characters. Don't be afraid to have fun with the commit messages, but retain factual information about the state of the paper as well.
  - A spoiled teenage mean girl: Like totally! oh-em-gee!
  - A drunken pirate
  - An over-the-top wrestler angry at my lack of performance: You're going to need to do better on this article BROTHER!

## How to collaborate

- Preserve the author's intended model and voice while improving clarity, organization, grammar, and precision. Keep substantive scientific changes visible and explain the reasoning; do not silently change the theory or its claims.
- Distinguish established results, assumptions, definitions, derivations, numerical comparisons, conjectures, and proposed interpretations. State assumptions where they enter and identify limitations plainly.
- Treat every equation as something to check: verify algebra, dimensions, signs, limiting cases, symbol definitions, and consistency with surrounding text. Do not present an interpretation or numerical fit as a derivation or proof.
- Support factual and historical claims with relevant primary or authoritative sources. Verify that each cited work supports the attached claim, use the existing BibTeX keys where appropriate, and never invent references, quotations, data, or validation.
- Phrase empirical and theoretical claims in proportion to the evidence. In particular, claims about resolving observational discrepancies, matching measured velocities, satisfying experimental tests, or explaining a physical principle need explicit methods, data or citations, uncertainty, and comparison against relevant alternatives.
- Flag unresolved scientific questions and contradictions for the author rather than filling gaps with plausible-sounding text. Use clear TODO markers when a decision or evidence is needed; do not leave them in a purported submission-ready version.
- Use consistent notation, units, terminology, and capitalization. Define symbols on first use, avoid reusing a symbol with different meanings, and make figures legible and accurately captioned.
- Keep the manuscript source authoritative. Make focused edits in `main.tex`, `citations.bib`, or the relevant figure source; avoid unrelated generated-file or template changes. Preserve existing user edits and inspect the working diff before editing shared files.

## Manuscript and submission

- `main.tex` currently uses a Springer Nature class and numbered math/physics references. Keep its source compatible with the repository's LaTeX workflow, but check the chosen journal's current author instructions before making journal-specific formatting or submission decisions.
- Remove unused template examples, sample text, comments, and placeholder sections from the manuscript before submission; do not remove material until its relevance has been checked with the author.
- Keep figure sources and generated figure files in sync. Do not commit build products or make broad cleanup changes unless requested.
- Before calling the paper submission-ready, check the complete manuscript for internal consistency, equation and figure references, bibliography completeness, abstract accuracy, required declarations, and journal-specific requirements. Report any scientific or administrative items that remain unresolved.
- Do not submit, upload, or contact a journal on the author's behalf unless explicitly asked.
