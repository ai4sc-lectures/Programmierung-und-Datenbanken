# Visuals

## Resource File Organization

Keep lecture assets under named subdirectories:

```text
data/<LECTURE_FILE_NAME>/
  ├── patches1.json          # Cached Plotly figures
  ├── training_curve1.json   # Training dynamics
  └── architecture_comp.json # Model comparisons

images/<LECTURE_FILE_NAME>/
  ├── mj_title.mp4           # Background video for title slide
  ├── mj_concept.png         # Midjourney conceptual images
  └── example_screenshot.png # Case study screenshots
```

The `{lecture_file_name}` directory name should match the `.qmdx` source file.
Add the data directory to `resources:` in frontmatter so Quarto copies it:

```yaml
resources:
  - data/{lecture_file_name}
```

## Visualization Hierarchy

Choose visual types by their pedagogical role, not by aesthetics:

1. **Motivational** — conceptual Midjourney images that create atmosphere or
   frame the problem; used in title, section openers, Hörsaalfrage slides
2. **Operational** — step-by-step diagrams or animations that show *how*
   something works (convolution sliding window, pipeline flow)
3. **Analytical** — training curves, loss landscapes, benchmark comparisons;
   used to support a claim with evidence
4. **Comparative** — architecture diagrams or side-by-side layouts that let
   students contrast approaches

Prefer analytical and operational visuals on content slides. Reserve
motivational visuals for openers and transitions. Do not use motivational
images as evidence.

## Standard Figures

Use plain Quarto image syntax for normal scientific figures:

```md
![](images/figure.svg){fig-align="center"}
```

Helpful attributes seen locally:

- `fig-align="center"`
- `height="400px"`
- class-based styling such as `{class="midjourney"}`

## Midjourney Images

Use Midjourney assets in the established ways:

- right-hand support image in `%%col`
- framed image via heading attributes `colR`, `capR`, `imgR`
- final/title atmospherics

Do not let Midjourney images replace actual evidence on analytical slides.

## QR Codes and Linked Images

Standard Quarto Markdown works:

```md
[![https://example.org](images/qrcode.png)](https://example.org)
```

This is a recurring house pattern for course logistics, platform links, documentation access, and other resource slides.

Typical use:

- screenshot or platform image in one column
- QR code or clickable image in the other column
- optional URL shown in the image alt text or surrounding context

Use it when a slide should direct the audience to:

- course material
- documentation
- signup pages
- external demos or videos

## Bottom-of-Slide Reference Strips

Place 1 to 3 lightweight references at the bottom of a slide in gray,
separate from the main content. Use the `%%slide_ref` shortcut:

```md
%%slide_ref @Jafariasi Jafariasi, J.; Krause, N.; Spyridis, P.; Ploennigs, J.: Efficient Concrete Crack Diagnosis, Structural Concrete, 2025
%%slide_ref @Krause Krause, N.; Ploennigs, J.: Digital twins for green roofs, EENVIRO, 2025
```

Consecutive lines on the same slide stack into one block automatically. The
text after the citekey is the shortened slide label — intentionally briefer
than the full BibTeX entry. Citekeys are injected as hidden citations so the
same sources appear in the final `%%references` bibliography.

Use this pattern when:

- 1 to 3 references should stay visible on the slide itself
- you want provenance on the visual slide, not only in the bibliography
- the references are supportive context rather than the main slide content

For the macro syntax and expansion detail see the `%%slide_ref` entry in
[quarto-authoring-and-shortcuts.md](quarto-authoring-and-shortcuts.md).
