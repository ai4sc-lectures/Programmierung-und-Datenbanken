# Lecture Tasks — Execution Guide

Each file here is a self-contained task for redesigning one lecture in the course "Programming and Databases" (civil/environmental engineering, University of Rostock).

## How to execute a task file

1. Read the task file.
2. For `.qmdx` authoring conventions use `../lecture_skill/SKILL.md` and its `references/` files as needed.
3. Write the output to the path in the task's **New file** field.

The skill covers ALL authoring patterns including FRONTMATTER. Do ***NOT*** open completed lecture files in `lectures/` to check frontmatter or patterns — the skill has everything!

## Concept-marker symbols

Task files use shorthand symbols to specify concept markers. **Never put these as emoji in slide content.** Translate them to `{{< ai4sc-icon name >}}` shortcodes (inline at first mention) or `%%div eyebrow` / `%%/div` labels for section headers.

| Shorthand | Shortcode | Concept |
|-----------|-----------|---------|
| □ | `{{< ai4sc-icon variable >}}` | Variable |
| ≡ | `{{< ai4sc-icon braces >}}` | Datatype |
| ○ | `{{< ai4sc-icon box >}}` | Object / Entity |
| ⇄ | `{{< ai4sc-icon arrow-left-right >}}` | Relationship |
| ⚙ | `{{< ai4sc-icon square-function >}}` | Function |
| 🔄 | `{{< ai4sc-icon workflow >}}` | Algorithm / Agentic cycle |
| 📋 | `{{< ai4sc-icon clipboard-list >}}` | Requirement |
| 🔍 | `{{< ai4sc-icon test-tube >}}` | Test / Verification |
| 📂 | `{{< ai4sc-icon list-tree >}}` | Data Structure |
| 🗄 | `{{< ai4sc-icon database >}}` | Database |

Example eyebrow label:
```
%%div eyebrow
{{< ai4sc-icon workflow >}} Agentic Cycle
%%/div
```

Stay inside the `lectures/` directory. Do not search for or open files outside this project.
