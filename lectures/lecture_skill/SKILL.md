---
name: AI4SC_Lecture_Slides
description: Use this skill when creating or editing lecture slide decks, especially for `.qmdx` sources that use `ai4sc-preprocess` shortcuts like `%%book`, `%%slides`, `%%col`, `%%div`, `%%credit`, `%%#`, `%%references`, and `%%final`. It teaches the local authoring model, common slide archetypes, citation patterns, Plotly/code usage, and how to structure dual slide/book output in the house style shown in `examples/*.qmdx`.
---

# Quarto Script Slides

Use this skill for scientific decks in this repository when the source should be a compact `.qmdx` file rather than raw `.qmd`.

Read only the specific reference files needed for the task. The split reference set is intentionally topic-based so you do not need to load everything.

## Purpose

This repository uses a two-layer authoring model:

- `.qmdx` is the compact source format you should usually edit.
- `ai4sc-preprocess` expands `.qmdx` into standard Quarto `.qmd`.
- Quarto then renders reveal.js slides, HTML pages, and optionally PDF/Typst output through the `ai4sc-style-revealjs` extension.
- Python-side helpers come from the installable `ai4sc_style` package.

The goal is not generic reveal.js Markdown. The goal is to produce decks that match the local scientific teaching style:

- concise slide text
- richer explanatory `book` prose when useful
- repeatable column/image layouts
- careful use of Midjourney figures
- code and Plotly only when they genuinely teach something
- proper bibliography and closing slides

## Workflow

Follow this order.

### 1. Inspect before writing

Open the relevant local patterns first:

- [references/quarto-authoring-and-shortcuts.md](references/quarto-authoring-and-shortcuts.md) for source structure, frontmatter, preprocess/rebuild, macro syntax, heading attributes such as `.scramble-slide data-transition="none"`, and reveal/fragment authoring patterns including `.scramble`, `.scramble-auto`, and whole-slide scramble variants
- [references/lecture-book-output-patterns.md](references/lecture-book-output-patterns.md) when the same source should also serve as written lecture documentation via `%%book`/`%%slides` and dual-output headings
- [references/slide-layout-patterns.md](references/slide-layout-patterns.md) for common layout patterns
- [references/figures-images-and-slide-references.md](references/figures-images-and-slide-references.md) for figures, Midjourney, QR patterns, and slide-local references
- [references/icons-and-brand-assets.md](references/icons-and-brand-assets.md) when the slide needs iconography, domain symbols, or brand-aligned visual accents
- [references/plotly-code-and-equations.md](references/plotly-code-and-equations.md) for Plotly, code, equations, and mixed Quarto constructs
- [references/pedagogical-design-patterns.md](references/pedagogical-design-patterns.md) for narrative structure, concept introduction sequence, code pedagogy patterns (A/B/C), agentic verification callouts, and teaching pattern templates
- `src/ai4sc_style/preprocess.py` if you need exact macro behavior
- [_extensions/ai4sc-style/_extension.yml](/Users/jplonnigs/Documents/code/Presentations/2026/template/_extensions/ai4sc-style/_extension.yml) if you need the exact Quarto format defaults and bundled resources
- representative files in `examples/*.qmdx`

Do not invent new macros if an existing pattern already covers the need.

### 2. Design the scientific narrative

Before drafting slides, decide:

- audience level: lecture, seminar, lab meeting, defense, overview talk
- core claim for each slide
- which content belongs on the slide versus in `%%book`
- which visuals are evidence and which are only decorative

Prefer a strong teaching arc:

1. open with a concrete problem or audience question (not a definition)
2. state the problem or concept with enough tension to motivate the solution
3. show evidence, derivation, or example using the concept introduction sequence
4. apply code pedagogy patterns (A/B/C) — choose based on whether the goal is
   skill-building or critical reading of AI-generated code
5. add agentic verification callouts after every concept students will encounter
   in generated code
6. close with references and a question slide

Read [references/pedagogical-design-patterns.md](references/pedagogical-design-patterns.md)
for the full pattern library: opening hook, concept introduction sequence,
architecture comparison, practical example, and progressive skill levels.

### 3. Author in `.qmdx`

Default to `.qmdx` for new or edited decks in this repo.

Use:

- normal Quarto YAML frontmatter
- `%%book` for explanatory print/page-only prose
- `%%slides` for reveal-only framing
- `%%credit` as a companion line for an `h1` slide opener with `background-video` or `background-image` when visible media provenance is needed
- standard headings plus dual-output shortcut headings like `%%#`, `%%##`, `%%###`, and deeper
- `%%col`, `%%sep`, and `%%div` for layout

Important:

- there is no `%%slide` macro in this repo
- the reveal-visible wrapper is `%%slides`
- individual slides are usually created by headings inside the reveal flow
- the `%%#` / `%%##` / `%%###` family can replace normal slide headings when you intentionally need stronger book hierarchy than reveal supports
- use `# ... {background-video="..."}` or `# ... {background-image="..."}` followed immediately by `%%credit ...` for the title-and-credit opener pattern; the inline alternative is `credit="..."` on the heading itself

### 4. Use the local slide archetypes

Prefer the existing house patterns over ad hoc layouts:

- one text block
- two-column text:text
- two-column text:image
- three-column comparison
- Hörsaalfrage prompt slides
- section intro and closing slides

The concrete syntax for each is in [references/slide-layout-patterns.md](references/slide-layout-patterns.md).

### 5. Handle figures, code, and Plotly intentionally

- Use images as evidence, examples, diagrams, or deliberate atmosphere.
- Use Midjourney images mainly in the established right-column/frame patterns, not everywhere.
- Use the bundled SVG icons when they clarify a card, label, callout, or domain concept; do not invent ad hoc iconography first.
- Keep code fragments short and pedagogically motivated.
- Use Plotly when interactivity or a generated figure materially helps.
- When a Plotly figure is static enough for teaching, a saved PNG is often simpler than live rendering.

### 6. Preprocess and verify

When you need to render or inspect the expanded structure:

```bash
uv run ai4sc-preprocess your_deck.qmdx
```

If you edited the full `.qmd` and want the compact source back:

```bash
uv run ai4sc-preprocess --rebuild your_deck.qmd
```

Check that:

- `%%book` and `%%slides` sections are balanced
- slide headings are in the intended level
- columns close correctly
- citations compile into the reference section
- `%%final` is present when the deck should end with a question slide
- the deck frontmatter uses `format.ai4sc-style-revealjs` rather than ad hoc root-level assets
- extension-level frontmatter fields are used consistently when needed:
  `footertext`, `institute-logo`, and `university-logo`

## Authoring Rules

- Prefer existing macros and classes over one-off HTML.
- Keep slides sparse; move extended explanation into `%%book`.
- Use assertion-style or conceptually precise titles, not vague placeholders.
- Treat `%%credit` as part of a preceding `h1` opener that uses `background-video` or `background-image`, not as a free-floating standalone block elsewhere on the slide.
- For scientific decks, figures and equations should support a point, not fill space.
- Use standard Quarto features when they already solve the problem cleanly.
- Use raw HTML only when Quarto plus the shortcuts cannot express the layout.
- Prefer the extension metadata fields `footertext`, `institute-logo`, and `university-logo`
  over custom footer HTML or ad hoc title-slide logo markup.

## When To Read More

Open the specific reference file you need:

- [references/quarto-authoring-and-shortcuts.md](references/quarto-authoring-and-shortcuts.md) for deck structure, frontmatter, preprocess/rebuild, `%%book` vs `%%slides`, heading shortcuts, and the macro inventory
- [references/lecture-book-output-patterns.md](references/lecture-book-output-patterns.md) for the lecture-specific written-documentation pattern built around `%%book`, `%%slides`, and dual-output headings
- [references/slide-layout-patterns.md](references/slide-layout-patterns.md) for slide-template snippets
- [references/figures-images-and-slide-references.md](references/figures-images-and-slide-references.md) for images, Midjourney, QR patterns, and bottom slide references
- [references/icons-and-brand-assets.md](references/icons-and-brand-assets.md) for bundled SVG icons, semantic meanings, concept-marker shortcodes, and usage patterns
- [references/plotly-code-and-equations.md](references/plotly-code-and-equations.md) for Plotly, code-fragment examples, equations, and normal Quarto/reveal constructs
- [references/pedagogical-design-patterns.md](references/pedagogical-design-patterns.md) for narrative arc, concept introduction sequence, code pedagogy patterns (A/B/C), agentic verification callouts, teaching pattern templates, and skill-level assessment structure
