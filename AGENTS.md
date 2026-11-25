# Shared writing guidance

## Project

> The version that we're currently working on is contained within the `./iop` directory. Use the bibliography, `main.tex` and other associted files from that directory.

- This folder contains a research manuscript on a proposed relationship among time, gravitation, cosmic expansion, and a fourth density-like spatial coordinate. The working LaTeX manuscript is `main.tex`; references are in `citations.bib`; figures and their sources are under `diagrams/`.
- The goal is to develop a submission-ready paper during November 2026. Treat November 30, 2026 as the working deadline unless the author sets another date.
- The target journal is not yet specified. Do not assume the included Springer Nature template determines the eventual venue or its requirements.

### REQUIRED GEOMETRY: self-consistent co-expansion

This is a fundamental, permanent part of the model. Every new derivation, section, notebook, video script and code path must use it.

- **Co-expansion is the source of the equivalence principle.** All matter co-expands with the change in `y`: every material length scales by the local Lorentz factor `gamma`, and every clock runs at the coordinate density `1/gamma`. Measured with co-expanding rulers and clocks, `ds^2 = -c^2 dt^2 / gamma^2 + gamma^2 |dx|^2` in the absolute (co-moving) coordinates `x`.
- **The flow is set by the co-expanded (measured) radius** `R = gamma r`: `beta^2 = 2GM/(c^2 R)`. With `u = GM/(c^2 r)` this gives `gamma^2 - 2 u gamma - 1 = 0`, i.e. `gamma = u + sqrt(1 + u^2)`. (Using the absolute radius instead gives a perihelion advance 4/3 of GR and is ruled out.)
- **Exact form in the areal radius** (`G = c = 1`): `ds^2 = -(1 - 2M/R) dt^2 + (R - M)^2/(R - 2M)^2 dR^2 + R^2 dOmega^2`. `R = 2M` is the absolute centre `r = 0`.
- **It is meant to differ from GR.** It matches GR at first post-Newtonian order (PPN gamma = beta = 1). It differs at second order and in the ringdown. Report the differences; do not tune them away.
- **Code:** `physics.symbolic.function_generators.paper_two.co_expansion` (`check_co_expansion`). Paper-two section draft: `second_paper/sections/co_expansion.tex`.

**Paper one (`iop/main.tex`) has included co-expansion since 2026-11-25.** The text submitted to Physica Scripta on 2026-11-24, which did not, is kept in `iop/main_as_submitted.tex`. Its absolute slices were the outward Painlevé–Gullstrand slices, flat in the areal radius with no co-expansion; co-expansion keeps that flow, its unit lapse and the synchronization offset exactly and adds the angular factor, so the submitted text is the construction with co-expansion removed. Do not copy constructions from `main_as_submitted.tex` into new work without applying co-expansion.

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
