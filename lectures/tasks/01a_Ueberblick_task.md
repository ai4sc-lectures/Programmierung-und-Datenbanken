# Task: 01a_Ueberblick

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../01a_Ueberblick.qmdx` |
| **Source file** | `../oldx/01a_Ueberblick.qmdx` (filename unchanged) |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S01 |
| **Status** | REFRAMED |

## Instructions

1. Read `../lecture_skill/SKILL.md` — follow its conventions for layout, icons, Quarto syntax, and slide structure throughout.
2. Read the source file(s):
   - `../oldx/01a_Ueberblick.qmdx`
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../01a_Ueberblick.qmdx`

---

### 01a_Ueberblick

**Block**: Block 1 — Computational Foundations | **Session**: S01
**Status**: REFRAMED | **Primary symbols**: ≡ 🔄
**Source file**: `../oldx/01a_Ueberblick.qmdx` (filename unchanged)

#### Summary: Overview

Course introduction reframed around AI-enabled engineering. The learning goals shift
from "learn to write code" to "learn to read, verify, and modify AI-generated code."
The symbol legend and agentic cycle are introduced here so they can be referenced
throughout the course.

#### Main topics

- Course goals, topics, and organization
- Lecture and exercise workflow
- The role of AI tools in this course and in engineering practice
- Application areas: CAD, structural engineering, GIS, facility management
- Symbol legend and agentic cycle overview

#### Key takeaways

- Active competencies: read, modify, and verify AI-generated code.
- Python is the primary language because of its AI ecosystem and engineering tool coverage.
- The agentic workflow (prompt → generate → understand → verify → iterate) applies to
  every programming task in this course.

#### Change Notes

**Content to ADD**:
- Course framing around AI-enabled engineering (~3 slides): restate goals as "read AI
  code, modify for the engineering requirement, verify quality." Include a one-slide
  diagram of the full agentic cycle.
- Symbol legend slide: introduce □ ≡ ○ ⇄ ⚙ 🔄 📋 🔍 📂 🗄 with SVG icon references;
  explain these markers appear throughout the course to label "what kind of thing
  we are talking about."

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "AI is a helper" → "AI generates code; the engineer is the architect and verifier."

**Agentic workflow integration**:
- Open with the cycle diagram (prompt → generate → understand → verify → iterate)
  as a one-slide visual. Tell students they will practice each step starting here.

**Symbols to add**: ≡ on data-types slide; 🔄 on agentic cycle diagram.

**Cross-references**:
- → `01c_AgentischesProgrammieren` (S01): mechanics of the workflow introduced visually here
- → `03a_Wissenspyramide` (S03): pyramid levels map to course block structure
