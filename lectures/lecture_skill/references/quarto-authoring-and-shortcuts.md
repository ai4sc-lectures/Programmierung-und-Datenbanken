# Quarto Authoring And Shortcuts

## Mental Model

Think in three layers:

1. The `ai4sc-style-revealjs` Quarto extension provides the presentation format and bundled runtime assets.
2. `.qmdx` is the compact authoring layer.
3. `ai4sc-preprocess` expands shortcuts into standard fenced-div Quarto markup.

Usually write `.qmdx`, not raw `.qmd`, unless debugging expanded markup.

## Common File Shape

Typical lecture `.qmdx` files look like this:

```md
---
title: "Datenbankentwurf"
image-credit: "Midjourney: A walk in the park, ref. Georges Seurat"
format:
  revealjs:
    title-slide-attributes:
      data-background-video: images/{lecture_file_name}/mj_title.mp4
    output-file: {lecture_file_name}.slide.html
  html:
    output-file: {lecture_file_name}.page.html
  typst:
    output-file: {lecture_file_name}.page.pdf
resources:
  - data/{lecture_file_name}
---

%%book

![](images/{lecture_file_name}/mj_title_band.jpg)

> Pull quote that frames the lecture topic.
>
> — Attribution

%%/book

%%slides

## Hörsaalfrage {background="#FFD966" cols40x60 txtL="Opening question?" capR="Midjourney: ..." imgR="images/{lecture_file_name}/mj_concept.png"}

%%/slides

%%# Main section
%%## Subtopic
...

%%references
%%final
```

Notes:

- `image-credit` is a top-level metadata field consumed by the extension to
  render an image credit line on the title slide.
- The three-format block (`revealjs` + `html` + `typst`) produces slides,
  a scrollable page, and a PDF from the same source. Use the naming pattern
  `{name}.slide.html`, `{name}.page.html`, `{name}.page.pdf` consistently.
- The opening `%%book` block contains a full-width band image and a pull
  quote. This gives the written/page output a visual anchor before the first
  section. Omit in slides-only decks.
- The first `%%slides` block typically holds the opening Hörsaalfrage.
- `resources:` copies the data directory for cached Plotly figures.
- The extension bundles `plotly-loader.js`, `plotly.min.js`,
  `slide-particles.js`, `title-slide.html`, `reveal-before-body.html`,
  `favicon.png`, and `apa.csl` — do not add these manually.
- `%%book`-specific patterns are in
  [lecture-book-output-patterns.md](lecture-book-output-patterns.md).

## Common Frontmatter Conventions

Common fields:

- `footertext`
- `institute-logo`
- `university-logo`
- `format.ai4sc-style-revealjs.title-slide-attributes`
- `format.ai4sc-style-revealjs.css`
- `resources:`
- `bibliography:`

Typical example:

```yaml
footertext: Kompetenz von KI & für KI
institute-logo: _extensions/ai4sc-style/assets/logos/ai4sc-logo-ink.svg
university-logo: _extensions/ai4sc-style/assets/logos/uni_logo2.svg
format:
  ai4sc-style-revealjs:
    css:
      - _extensions/ai4sc-style/themes/color/mineral.css
    title-slide-attributes:
      data-background-video: images/{lecture_file_name}/mj_title.mp4
resources:
  - data/{lecture_file_name}
bibliography: references.bib
```

Replace `{lecture_file_name}` with the actual `.qmdx` filename stem.

Use these extension-level metadata fields intentionally:

- `footertext`
  Short plain-text footer convenience field provided by the extension. Prefer this over
  `format.ai4sc-style-revealjs.footer` unless you explicitly need custom HTML.
- `institute-logo`
  Path to the institute or lab logo shown on the title slide.
- `university-logo`
  Path to the university or umbrella-organization logo shown on the title slide.

## Slide-First Default

The default assumption for this file is presentation-first authoring.

- write the slide version first
- add lecture-style written documentation only when the deck actually needs it
- use [lecture-book-output-patterns.md](lecture-book-output-patterns.md) when the same source should also function as detailed written teaching material

Important:

- there is no `%%slide` macro in `ai4sc-preprocess`
- `%%slides` is available as a reveal-only wrapper when needed
- headings such as `#` and `##` remain the normal slide structure
- the dual-output `%%#` / `%%##` / `%%###` family is most relevant when you intentionally need parallel slide/book structure

## Dual-Output Headings

The `%%#` family writes one heading that expands differently for slides and book output:

| Shortcut | Book output | Slides output |
|---|---|---|
| `%%# Title` | `## Title` | `# Title` + blank slide separator |
| `%%## Title` | `### Title` | `## Title` |
| `%%### Title` | `#### Title` | `## Title` |

The book level is always one deeper than the macro hash count. The slides level is capped at `##` — `%%###` and deeper all produce `## Title` in reveal output, never a sub-heading.

`%%#` additionally appends an uncounted blank slide (`## {visibility="uncounted"}`) inside the reveal block so the section title does not count in the progress bar.

Example:

```md
%%# Methodik
%%## Datenbasis
%%### Vorverarbeitung
```

## Slide-Level Heading Attributes

This repo uses heading attributes with macro-aware extras parsed by
`ai4sc-preprocess`. The layout-shortcut attributes expand the heading into a
two-column slide without writing `%%col` blocks manually:

| Attribute | Meaning |
| --------- | ------- |
| `colR` | Right-column image only — no left text; image fills the right side |
| `cols{L}x{R}` | Two-column split, e.g. `cols40x60` → 40% left, 60% right |
| `txtL="..."` | Text/question shown in the left column |
| `capR="..."` | Midjourney caption shown below the right-column image |
| `imgR="..."` | Path to the right-column image |
| `credit="..."` | Inline image credit on the heading (alternative to `%%credit`) |
| `book` | Heading appears in book/page output only |
| `slides` | Heading appears in slides output only |

Standard Quarto background attributes (`background`, `background-color`,
`background-video`, `background-image`) work normally alongside these.

Example title slide pattern:

```md
# Überblick {colR capR="Midjourney: Application of ML in Construction" imgR="images/00_Grundlagen/mj_application_of_machine_learning_in_construction.png" background="#333"}
```

Example Hörsaalfrage pattern:

```md
## Hörsaalfrage {background="#FFD966" cols40x60 txtL="Wo finden wir ML im Alltag?" capR="Midjourney: Every day life with machine learning" imgR="images/00_Grundlagen/mj_every_day_life_with_machine_learning.png"}
```

Use this pattern when:

- a slide title should define the visual frame of the slide
- a question or section opener needs a strong image-plus-text layout
- you want compact source for a repeated slide archetype instead of manually opening columns and framed image blocks

For image provenance on a slide opener with `background-video` or `background-image`, use either an inline heading attribute or an `h1` companion shortcut:

```md
# The origins {background-video="images/mj_wherewestand.mp4" title="The wanderer" credit="cf. Caspar David Friedrich 'The wanderer' (1818)" .fragment .scramble-auto}
```

Treat `%%credit` as a companion line for the preceding `h1` slide opener when that opener uses `background-video` or `background-image`. It is intended for that paired pattern rather than as a free-floating standalone block elsewhere on the slide.

Custom slide-entry and fragment effects are also available through heading and fragment classes:

- `.scramble-slide` on a slide heading triggers a slide-entry scramble effect without consuming a fragment step
- `data-transition="none"` on the same heading is the recommended pairing when you want the scramble effect to replace, rather than compete with, the built-in reveal transition
- `.fragment .scramble` creates a click-revealed scramble fragment
- `.fragment .scramble-auto` creates a scramble fragment that auto-fires when it is the next hidden fragment on slide entry
- `.fragment .whole-slide .scramble` and `.fragment .whole-slide .scramble-auto` are supported on slide headings for whole-slide fragment-style scramble reveals

Examples:

```md
## Title {.scramble-slide data-transition="none"}

Lorem ipsum
```

```md
::: {.fragment .scramble}
This line will scramble in.
:::
```

```md
::: {.fragment .scramble-auto}
This line scrambles automatically on slide entry.
:::
```

```md
## Whole slide scramble {.fragment .whole-slide .scramble}

Lorem ipsum
```

## Visibility and Sectioning Macros

```md
%%slides
%%/slides
%%book
%%/book
%%slidesep
%%slidetitle <title>
%%references
%%final
%%credit
```

`%%credit` expands to a small slide credit note associated with a preceding
`h1` opener that uses `background-video` or `background-image`. Use it for
artwork, photo, or video provenance that should stay visible on the slide
itself but does not belong in the scholarly bibliography.

`%%slidetitle <title>` emits a reveal-only `## title` wrapped in a
`content-visible when-format="revealjs"` block. Use it when a slide needs a
title that should not appear in book output at all — no book-level heading,
no section entry.

### Combo Macros

Two macros that logically belong on adjacent lines can be joined with `+` to
save a blank line:

```md
%%/book+slides
```

expands to:

```md
%%/book

%%slides
```

Any pair of `%%macro` tokens can be combined this way. The preprocessor
splits them before the main expansion pass.

## Columns

```md
%%col 40 60
Left
%%sep
Right
%%/col
```

- widths are percentages
- `40v` adds vertical centering to that column
- more `%` means deeper nesting

### Slides-Only Columns (`%%scol`)

Use `%%scol` instead of `%%col` when the document renders in both slides and
book/HTML modes:

```md
%%scol 40 60
Left column
%%sep
Right column
%%/scol
```

The preprocessor pre-expands this into a `%%slides` block with a normal
`%%col` layout, followed by a `%%book` block where the segments are appended
sequentially (top to bottom). The column features — `v` suffix, nesting —
work the same as `%%col`.

Example:

```md
%%%%col 30 30 30
%%%%sep
%%%%/col
```

### Vertical Centering with `v`

Example:

```md
%%col 40v 60
Left column content
%%sep
Right column content
%%/col
```

Use it when:

- one column should sit visually centered next to a taller figure or image
- a rubric, prompt, or summary block should align to the middle of the slide
- the slide would otherwise feel top-heavy

### Nested Shortcut Depth

Examples:

```md
%%%%col 30 30 30
%%%%sep
%%%%/col
```

```md
%%%div cta-meta
API · Revit · Grasshopper · CLI
%%%/div
```

Use deeper `%` levels when:

- nesting columns inside an outer column layout
- a styled block lives inside another styled block
- Quarto fenced-div depth would otherwise become noisy to write by hand

Match the same depth for open, separator, and close forms.

## Generic Styled Blocks

```md
%%div eyebrow
Context · ML
%%/div

%%div lead
One sentence that states the takeaway.
%%/div
```

Common classes seen in examples:

- `eyebrow`
- `display`
- `lead`
- `caption`
- `column`
- `stat-grid`
- `stat-card`
- `stat-label`
- `stat-value`
- `stat-delta`
- `comparison-grid`
- `comparison-col`
- `col-label`
- `quote-text`
- `attribution`
- `cta-row`
- `cta-meta`

## Callouts and Semantic Helpers

```md
%%note Definition: Maschinelles Lernen
Definition text.
%%/note

%%warning Achtung
Warning text.
%%/warning

%%tip Merksatz
Tip text.
%%/tip

%%def Embodied carbon
Definition body.
%%/def

%%aside
Ref.: short side reference or annotation
%%/aside
```

### `%%aside` as a Source Pattern

Typical use:

```md
![](images/data_needs.svg){height="400px" fig-align="center"}

%%aside
Ref.: The Future of IoT, IEEE IoT Magazine, 2018
%%/aside
```

Use `%%aside` when:

- a short source note should stay visually separate from the main slide content
- a figure needs a compact provenance line
- a claim or example needs a brief contextual reference without turning into a full bibliography discussion

Prefer `%%aside` for short attribution/context lines and `@citekey` plus `%%references` for formal scholarly citation.

### `%%note` as a Definition Pattern

Typical pattern:

```md
%%note Definition: Maschinelles Lernen
Maschinelles Lernen (ML) ist ...
%%/note
```

Use this when:

- a concept needs a compact formal definition
- terminology should stand out visually from the surrounding teaching flow
- the definition is important, but does not justify a full separate slide

## Speaker Notes

Use standard Quarto/reveal speaker notes when a slide needs presenter-only guidance.

Common pattern:

```md
## Slide title

Visible slide content.

::: {.notes}
This text is only for the presenter view.
Use it for timing, speaking cues, reminders, or extra context.
:::
```

`%%notes` / `%%/notes` also exists in `ai4sc-preprocess`, but standard Quarto note syntax is usually clearer unless you specifically want to stay fully inside the shortcut style.

## References and Endings

### `%%slide_ref`

```md
%%slide_ref @Key Author, A.: Short slide text, Venue, Year.
```

Consecutive lines on the same slide merge into one bottom reference block.
Citekeys are injected as hidden citations so `%%references` picks them up.

For usage guidance and patterns see
[figures-images-and-slide-references.md](figures-images-and-slide-references.md).

### `%%references`

Use:

```md
%%references
```

This expands to a `# Referenzen` heading plus a `::: {#refs}` block so Quarto can print the bibliography.

### `%%final`

Use:

```md
%%final
```

This expands to the standard reveal-only closing slide:

- title `Fragen`
- black background
- a rotating `mj_questionsN.mp4` video chosen from the filename prefix

## Preprocess and Rebuild

Expand `.qmdx` to `.qmd`:

```bash
uv run ai4sc-preprocess your_deck.qmdx
```

Rebuild `.qmd` back to `.qmdx`:

```bash
uv run ai4sc-preprocess --rebuild your_deck.qmd
```

Check that:

- `%%book` and `%%slides` sections are balanced
- slide headings are in the intended level
- columns close correctly
- citations compile into the reference section
- `%%final` is present when the deck should end with a question slide
