# Lecture Book Output Patterns

This file covers *when* and *why* to use dual-output authoring — where the
same `.qmdx` source serves both reveal.js slides and written documentation.
For macro syntax and expansion details, see
[quarto-authoring-and-shortcuts.md](quarto-authoring-and-shortcuts.md).

This pattern is common in lecture decks but not every scientific presentation
needs it. Default to slides-only unless the deck explicitly needs to double
as written teaching material.

## Deciding Whether To Write For Dual Output

Use dual output when:

- the deck is a lecture that students will revisit as written notes
- slides are intentionally sparse and the explanation lives in spoken words,
  meaning the printed version would be incomplete without added prose
- the same source is published to both a course website and a talk

Stay slides-only when:

- the presentation is a conference talk or scientific seminar
- the deck is self-contained and will not be reused as documentation
- adding book prose would force you to duplicate content rather than
  complement it

## Opening Book Block

The first `%%book` block at the top of the file (before any section headings)
sets the visual and thematic tone for the written/page output. The standard
shape is a full-width band image followed by a pull quote:

```md
%%book

![](images/{lecture_file_name}/mj_title_band.jpg)

> Pull quote that frames the lecture topic or poses its central question.
>
> — Attribution (person, source, year)

%%/book
```

The band image is typically a wide-crop Midjourney asset (landscape ratio,
no caption needed here). The pull quote should create intellectual tension or
curiosity — it is not a summary. This block is invisible in slides output.

## Core Split Pattern

The fundamental building block is alternating `%%book` and `%%slides` blocks
around each section. The most common shape for a dual-output section:

```md
%%# Section Title

%%book
### TL;DR

Two to four sentences that summarise what the slides cover. Written for
a reader who will not attend the talk.
%%/book

%%slides
## Key visual slide
- Bullet one
- Bullet two
%%/slides+book

Extended explanation, definitions, or worked examples for written output.
%%/book
```

`%%#` keeps the section heading synchronized across both outputs. The
`%%book` TL;DR before the slides gives written readers orientation before the
detail. `%%/slides+book` is the compact transition between blocks.

## Heading Strategy

Choose between plain headings and the `%%#` family based on whether the
heading should exist in both outputs:

| Situation | Use |
| --- | --- |
| Slide title only, no book section | `##` or `%%slidetitle` |
| Section exists in both, slides are primary | `%%#` or `%%##` |
| Within-slide emphasis or local label | `###` / `####` (plain) |
| Subsection that book output should carry deeper | `%%##` / `%%###` |

Rule of thumb: plain `###` and `####` inside slides are visual structure, not
semantic headings. Use `%%###` only when the line is genuinely a new topic
that the book output should index as a subheading.

For expansion details (what each `%%#` variant emits), see the
"Dual-Output Headings" section in
[quarto-authoring-and-shortcuts.md](quarto-authoring-and-shortcuts.md).

## Column Strategy

Use `%%scol` as the default column macro in lecture decks. It automatically
generates a `%%slides` column layout *and* a `%%book` linearised version from
one source block:

```md
%%scol 40 60
Key concept or question
%%sep
![](images/figure.png)
%%/scol
```

Use bare `%%col` only when:

- the layout is already inside a `%%slides` block (wrapping would be
  redundant)
- the book linearisation would produce unreadable output and you want manual
  control over the book version

For the full expansion, see the `%%scol` section in
[quarto-authoring-and-shortcuts.md](quarto-authoring-and-shortcuts.md).

## Common Book-Side Prose Patterns

### TL;DR Block

Place a brief summary immediately after each `%%#` section opener so written
readers get orientation before the slide sequence:

```md
%%# Methodik

%%book
### TL;DR

Diese Lektion erklärt ...
%%/book
```

### Narrative Bridge

Connect two slide sequences in book output without adding a slide:

```md
%%/slides+book
The previous section established X. The next section builds on this by
introducing Y.
%%/book+slides
```

### Extended Definition

A callout on the slide, full prose in the book:

```md
%%slides
%%note Definition: Maschinelles Lernen
Maschinelles Lernen ist ...
%%/note
%%/slides+book
Maschinelles Lernen (ML) bezeichnet Verfahren, bei denen ...
%%/book
```

### Figure With Caption Prose

A figure on the slide is often not self-explanatory in written output. Add
interpretation in book mode:

```md
%%slides
![](images/figure.png){height="420px"}
%%/slides+book
*Abbildung: ...* The figure shows that ...
%%/book
```
