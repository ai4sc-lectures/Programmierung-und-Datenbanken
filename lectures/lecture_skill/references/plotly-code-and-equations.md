# Technical Content

## Plotly

Plotly figures are often used in this repo to illustrate content, explain
concepts, and show worked examples.

### Theme Setup

Always call `load_ai4sc_theme()` at the top of any Python chunk that creates
Plotly figures. It registers the `"ai4sc"` template and sets it as the global
default so figures match the slide color scheme automatically.

```python
from ai4sc_style.plotly_loader import C, load_ai4sc_theme

load_ai4sc_theme()          # mineral (default) — matches the standard slide theme
load_ai4sc_theme("dark")    # for dark-background slides
```

Available themes: `mineral` (default), `dark`, `clay`, `olive`, `slate`,
`warm-bone`. The theme name must match the CSS scheme used in the deck's
frontmatter.

### Semantic Colors

After calling `load_ai4sc_theme()`, the `C` dict exposes every CSS custom
property from the active theme. Use semantic names instead of hard-coded hex:

```python
fig = go.Figure()
fig.add_trace(go.Bar(marker_color=C["signal-blue"]))
fig.add_trace(go.Scatter(line_color=C["signal-red"]))
```

Key semantic names:

| Key | Role |
| --- | ---- |
| `signal-blue` | Primary highlight, action |
| `signal-blue-50` | Muted primary, secondary trace |
| `signal-red` | Warning, error, contrast accent |
| `signal-yellow` | Caution, audience question highlight |
| `carbon` | Dark neutral, text-weight bar |
| `concrete` | Mid neutral |
| `rebar` | Grid lines, axis lines |
| `plaster` | Light neutral |
| `moss-700` | Sustainability, carbon benefit |
| `moss-500` / `moss-300` / `moss-100` | Moss tonal scale |
| `ink` | Main text / tick color |
| `paper` | Figure background |
| `bone` | Plot area background |

Do not hard-code hex values. `C` always resolves to the active theme so
figures stay consistent when the theme changes.

### Slide-Entry Animation

To trigger a count-up animation (bars grow from zero, lines reveal) when the
slide containing the figure becomes active in reveal.js:

```python
from ai4sc_style.plotly_loader import add_slide_animation

fig = px.bar(df, x="category", y="value")
add_slide_animation(fig)                    # 700 ms, cubic-in-out (defaults)
add_slide_animation(fig, duration=400)      # faster
```

`add_slide_animation` sets `layout.meta` flags read by `plotly-loader.js`. It
returns the same figure, so it can be chained. Only use it for figures where
the build-up motion reinforces the teaching point; don't animate every chart.

### Simple Inline Plotly

````md
```{python}
#| echo: false
fig = px.scatter(df, x="x", y="y")
fig.show()
```
````

Use this when normal Quarto rendering is sufficient.

### Caching Pattern

For performance, figures can be generated once, written to JSON, and loaded
client-side on every subsequent render. This is the default approach for
larger decks such as `examples/{lecture_file_name}.qmdx`.

**Preferred: `%%cache_plotly` macro**

Place it immediately after the Python chunk that builds `fig`:

```text
%%cache_plotly "data/{lecture_file_name}/figure.json"
%%cache_plotly "data/{lecture_file_name}/figure.json" 1200x500
%%cache_plotly "data/{lecture_file_name}/figure.json" 900x600 write
```

| Argument | Required | Meaning |
| -------- | -------- | ------- |
| `"path/to/figure.json"` | yes | Path to the JSON file (stem becomes the DOM id) |
| `WIDTHxHEIGHT` | no | Div size in px; defaults to `900x600` |
| `write` | no | Emits a hidden `pio.write_json(fig, ...)` block before the div |

With `write`, the full authored source is just:

````md
```{python}
#| echo: false
fig = px.scatter(...)   # build fig here
```

%%cache_plotly "data/{lecture_file_name}/figure.json" write
````

Without `write`, the JSON must already exist on disk. Use the no-`write`
form when recomputing the figure each render would be too slow.

**Manual equivalent** (use only when `%%cache_plotly` is not available):

````md
```{python}
#| echo: false
pio.write_json(fig, "data/{lecture_file_name}/example.json")
```
````

```html
<div id="plot"></div>
<script type="module">
  await window.PLOTLY_READY;
  await window.renderPlotlyFromJSON("plot", "data/{lecture_file_name}/example.json");
</script>
```

Add the data directory to `resources:` in frontmatter so Quarto copies it:

```yaml
resources:
  - data/{lecture_file_name}
```

`plotly-loader.js` is bundled by the `ai4sc-style-revealjs` extension — do
not add a separate root-level copy.

Practical guidance:

- prefer normal inline Plotly for most scientific teaching figures
- prefer PNG if reproducibility and layout stability matter more than
  interactivity
- prefer the caching pattern when interactivity is genuinely valuable or
  deck build time matters

## Code Fragments

Use standard Quarto code chunks; they are not custom macros.

### Code visibility

Choose the visibility option based on the teaching role of the chunk:

```python
#| echo: true       # Teaching code — show by default
#| echo: false      # Implementation detail — show output only (e.g. plots)
#| code-fold: true  # Optional detail or long block — show on demand
#| error: true      # Demonstrating a failure — code is expected to fail
```

`error: true` is required whenever the chunk intentionally raises an
exception. Without it Quarto aborts the render.

### Other useful chunk options

- `#| include: false` — run silently, no output or code shown (setup chunks)
- `#| output: false` — run and show code, suppress all output
- `#| fig-align: center` — center a figure output
- `#| tags: [remove-cell]` — exclude from all output formats

## Normal Quarto and Raw HTML in `.qmdx`

`.qmdx` in this repo is not macro-only.

It is normal to mix:

- standard Quarto Markdown
- Quarto code chunks
- reveal.js/Quarto fenced divs such as fragments
- occasional raw HTML when needed

Use the shortcuts where they improve repeated local patterns, but keep using
ordinary Quarto constructs when they are the clearest tool.

### Reveal Fragments

```md
::: {.fragment}
Content that should appear later.
:::
```

The local reveal extension also supports scramble-based fragment variants:

```md
::: {.fragment .scramble}
This line will scramble in.
:::
```

```md
::: {.fragment .scramble-auto}
This line will auto-scramble on slide entry if it is the next hidden fragment.
:::
```

For whole-slide fragment reveals, place the classes on the heading instead of
wrapping the body manually:

```md
## Whole slide scramble {.fragment .whole-slide .scramble}

Lorem ipsum
```

### Speaker Notes

```md
::: {.notes}
Presenter-only guidance.
:::
```

## Equations

Use standard dollar-delimited math in this repo.

Preferred forms:

- inline math with `$...$`
- display math with `$$...$$`

Examples:

```md
Der Mittelwert ist $\bar{x}$.
```

```md
$$
\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i
$$
```

Do not switch to bracket-style math delimiters such as `\(...\)` or `\[...\]`
unless explicitly requested.

Use display equations for:

- definitions of metrics or losses
- probability distributions
- derivations worth pausing on

Use inline math for:

- symbols in prose
- short variable references
- light mathematical clarification inside bullets or paragraphs

## Plotly Interactivity Patterns

### Dropdown to switch views

```python
fig.update_layout(updatemenus=[dict(
    type="dropdown",
    buttons=[
        dict(label="View A", method="update", args=[...]),
        dict(label="View B", method="update", args=[...]),
    ],
)])
```

Use when the same dataset has multiple meaningful views (e.g. raw vs.
normalised, linear vs. log scale).

### Hover metadata

```python
fig = px.scatter(df, x="x", y="y",
                 hover_data=["param_count", "accuracy", "inference_time"])
```

Include computed properties students would otherwise have to look up —
makes the figure self-contained for exploration.

### Clickable legend toggle

```python
fig.update_layout(legend=dict(itemclick="toggle"))
```

Use when showing multiple architecture families or training runs that
students should be able to isolate individually.

## ML Device Detection

Standard pattern for lectures with PyTorch code. Use at the top of any
training or inference chunk:

```python
device = torch.device(
    "mps"  if torch.backends.mps.is_available() else
    "cuda" if torch.cuda.is_available()         else
    "cpu"
)
```

Prefer this over hard-coding `"cuda"` — lecture machines vary.

## Code Structure Conventions

### Import order

```python
# Standard library
import sys, os, json, shutil, pickle

# Scientific computing
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# ML frameworks
import torch
import torchvision
```

### Centralized configuration

```python
BATCH_SIZE    = 32
LEARNING_RATE = 1e-3
NUM_EPOCHS    = 100
DEVICE        = device  # from detection pattern above
```

Define constants at the top of each code section; students should be able to
change a single value to explore different settings.

### Variable naming

Include units in names where meaningful: `ms_per_img`, `params_M`,
`loss_train`. Avoid generic names like `result` or `data`.
