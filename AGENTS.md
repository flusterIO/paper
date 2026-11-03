# Shared writing guidance

## Project

- This folder contains a research manuscript on a proposed relationship among time, gravitation, cosmic expansion, and a fourth density-like spatial coordinate. The working LaTeX manuscript is `main.tex`; references are in `citations.bib`; figures and their sources are under `diagrams/`.
- The goal is to develop a submission-ready paper during November 2026. Treat November 30, 2026 as the working deadline unless the author sets another date.
- The target journal is not yet specified. Do not assume the included Springer Nature template determines the eventual venue or its requirements.

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
