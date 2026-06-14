# Icons And Brand Assets

## Purpose

Use this reference when a deck needs:

- iconography for stat cards, callouts, labels, or section headers
- domain-specific symbols for BIM, embodied carbon, IFC, or scenario comparison
- more visual polish without inventing new assets

The canonical icon root is:

- `_extensions/ai4sc-style/assets/icons`

All icons are SVGs sourced from [Lucide](https://lucide.dev) and should
usually be referenced from there.

**If an icon you need is not in the set:** download the SVG from
lucide.dev, place it in `_extensions/ai4sc-style/assets/icons/`, and
patch the stroke attributes to match the house style:

```bash
sed -i '' \
  's/stroke-width="2"/stroke-width="1.5"/g; \
   s/stroke-linecap="round"/stroke-linecap="square"/g; \
   s/stroke-linejoin="round"/stroke-linejoin="miter"/g' \
  _extensions/ai4sc-style/assets/icons/<name>.svg
```

## General Guidance

- Prefer existing icons over inventing emoji, Unicode symbols, or ad hoc
  decorative shapes.
- Use icons to clarify meaning, not just to decorate empty space.
- Pair icons with short labels in most scientific slides; icon-only usage
  is better for repeated UI-like patterns.
- Keep icon sizing restrained. In most text contexts, start around
  `0.9em` to `1.2em`. In cards or section labels, start around
  `16px` to `28px`.
- Match icon color to the semantic role of the surrounding text:
  - `var(--ink)` for neutral/default
  - `var(--signal-blue)` for action or primary highlight
  - `var(--signal-red)` for warning/error/destructive meaning
  - `var(--signal-yellow)` for caution/highlight
  - `var(--moss-700)` or moss palette for sustainability/carbon benefit
- Avoid mixing many different icon styles on the same slide. One family
  and one semantic color system is usually enough.

## Icons

All SVG files live in `_extensions/ai4sc-style/assets/icons/`.

### Status and Feedback

- `check-circle.svg` — validated results, completed steps, success
- `check.svg` — compact lists, confirmations, “included” bullets
- `x.svg` — exclusion, removal, “not supported”
- `alert-triangle.svg` — risk, caution, uncertainty, assumptions
- `info.svg` — background context, definitions, interpretive notes
- `loader.svg` — process/runtime states only, not decorative
- `thumbs-up.svg` — pro, advantage, positive argument, benefit
- `thumbs-down.svg` — con, disadvantage, limitation
- `shield.svg` — security, protection, trust, robustness

### Navigation and Structure

- `arrow-right.svg` — flow, progression, implication, next step
- `arrow-left-right.svg` — bidirectional relationship, comparison
- `chevron-right.svg` — compact inline navigation, hierarchy cues
- `chevron-down.svg` — drill-down, expansion, “see below”
- `grid.svg` — system overviews, component matrices
- `layers.svg` — stacks, system layers, abstraction hierarchy
- `git-branch.svg` — branching, taxonomy, decision tree, versions
- `share-2.svg` — graph structure, network topology
- `link.svg` — reference, hyperlink, dependency, cross-reference
- `refresh-cw.svg` — cycle, iteration, feedback loop, algorithm step
- `menu.svg` — interface navigation or dashboard chrome only

### Files, Data, and Delivery

- `file.svg` — documents, artifacts, outputs, report files
- `file-text.svg` — papers, publications, specifications
- `folder.svg` — repositories, collections, datasets
- `database.svg` — persistent store, structured data source
- `table.svg` — tabular data, structured results, comparison matrix
- `archive.svg` — storage, historical records, preserved versions
- `download.svg` — exported artifacts, deliverables, retrieval
- `search.svg` — discovery, inspection, retrieval, analysis pipelines
- `settings.svg` — configuration, parameters, tooling setup
- `plus.svg` — addition, append, create
- `clock.svg` — runtime, latency, timing, process duration
- `calendar.svg` — schedule, timeline, deadline, milestone

### Charts and Results

- `chart-bar.svg` — categorical comparisons, benchmark results
- `chart-line.svg` — trends, time series, training curves
- `chart-pie.svg` — proportions, class distributions, share breakdown
- `trending-up.svg` — growth, improvement, KPI lift, directional gain

### People and Learning

- `users.svg` — team, collaboration, audience, multi-stakeholder
- `user-plus.svg` — onboarding, adoption, new-user participation
- `graduation-cap.svg` — learning objective, course outcome
- `brain.svg` — AI, cognition, ML concept, reasoning process
- `pencil.svg` — exercise, student activity, annotation
- `eye.svg` — observation, visibility, monitoring, inspection

### Academic and Rhetoric

- `lightbulb.svg` — idea, insight, creative proposal, contribution
- `book-open.svg` — definition, textbook reference, foundational concept
- `clipboard-list.svg` — requirement, specification, research question
- `quote.svg` — citation, attributed claim, direct quotation
- `help-circle.svg` — open question, unknown, research gap, exercise
- `star.svg` — key point, takeaway, highlight, important result
- `target.svg` — goal, objective, research aim, evaluation criterion

### Concept Markers (first-mention annotation)

Use these icons to mark the **first appearance** of a concept in a section.
Do not annotate every occurrence — only the introductory instance per section.

Declare the lecture's primary symbols once at the top of the source file (e.g.
as a comment or frontmatter note) so readers can see the symbol set at a glance.

Shortcode syntax: `{{< ai4sc-icon name >}}`

| Shortcode | Concept | When to use |
| --------- | ------- | ----------- |
| `variable` | Variable | First mention of a named value or binding |
| `braces` | Datatype | First mention of a type or representation |
| `box` | Object / Entity | First mention of a class or domain entity |
| `arrow-left-right` | Relationship | First mention of an association or reference |
| `square-function` | Function | First mention of a function or method |
| `workflow` | Algorithm / Cycle | First mention of an algorithm or the agentic cycle |
| `clipboard-list` | Requirement | First mention of a requirement or specification |
| `test-tube` | Test / Verification | First mention of a test, check, or review step |
| `list-tree` | Data Structure | First mention of a collection or file format |
| `database` | Database | First mention of a database concept |

### Science and Computing

- `microscope.svg` — lab, empirical research, experiment
- `flask-conical.svg` — example, worked case, experimental setup
- `atom.svg` — physics, chemistry, fundamental science
- `cpu.svg` — computing hardware, inference, processing
- `code.svg` — source code, implementation, programming concept
- `globe.svg` — web, internet, global deployment, geographic scope

### Sustainability and Built Environment

- `leaf.svg` — sustainability, emissions reduction, green outcomes
- `building.svg` — buildings, AEC context, built environment

### Domain-Specific AEC

- `domain/bim-stack.svg` — BIM workflows, layered model systems
- `domain/ifc-cube.svg` — IFC workflows, geometry exchange
- `domain/embodied-carbon.svg` — LCA, GWP, carbon accounting
- `domain/scenario-fork.svg` — scenario comparison, design alternatives

## Recommended Patterns

### Icon Plus Label

Good default for scientific slides:

```html
<span style="display:inline-flex;align-items:center;gap:8px;">
  <img src="_extensions/ai4sc-style/assets/icons/info.svg" alt="" style="width:18px;height:18px;">
  <span>Context</span>
</span>
```

Use this for:

- eyebrow labels
- card headers
- callout titles
- compact metadata rows

### Stat Card Accent

```html
<div style="display:flex;align-items:center;gap:10px;">
  <img src="_extensions/ai4sc-style/assets/icons/trending-up.svg" alt="" style="width:22px;height:22px;">
  <div>
    <div style="font-size:10px;letter-spacing:.08em;text-transform:uppercase;">Improvement</div>
    <div style="font-size:28px;font-weight:700;">+18%</div>
  </div>
</div>
```

Best for:

- KPI summaries
- measured deltas
- before/after comparisons

### Domain Header

```html
<div style="display:inline-flex;align-items:center;gap:10px;">
  <img src="_extensions/ai4sc-style/assets/icons/domain/ifc-cube.svg" alt="" style="width:24px;height:24px;">
  <span>IFC Inference Pipeline</span>
</div>
```

Best for:

- section headers
- pipeline slides
- methodology overviews

### Sustainability Highlight

```html
<span style="display:inline-flex;align-items:center;gap:6px;color:var(--moss-700);">
  <img src="_extensions/ai4sc-style/assets/icons/leaf.svg" alt="" style="width:16px;height:16px;">
  <span>Carbon reduction scenario</span>
</span>
```

Best for:

- embodied-carbon findings
- greener-option emphasis
- positive environmental results

## When Not To Use Icons

- Do not add icons to every bullet.
- Do not mix many unrelated icons on a dense scientific slide.
- Do not use interface/navigation icons like `menu.svg` or `settings.svg`
  unless the slide is actually about tooling or UI.
- Do not use domain icons if a plain heading or figure caption is already clearer.

## Asset Selection Heuristic

When choosing between several icons:

1. prefer the most semantically specific icon
2. prefer domain icons for BIM/IFC/carbon/scenario topics
3. otherwise prefer neutral/general icons over overly “app-like” ones
4. if none clearly fit, skip the icon rather than forcing one
