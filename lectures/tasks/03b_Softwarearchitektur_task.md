# Task: 03b_Softwarearchitektur

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../03b_Softwarearchitektur.qmdx` |
| **Source file** | `../oldx/02a_Softwarearchitektur.qmdx` |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S03 |
| **Status** | REFRAMED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../03b_Softwarearchitektur.qmdx`

---

### 03b_Softwarearchitektur

**Block**: Block 2 — Computational Engineering | **Session**: S03
**Status**: REFRAMED | **Primary symbols**: ⇄ 🔄
**Source file**: `../oldx/02a_Softwarearchitektur.qmdx`

#### Summary: Software Architecture

Traces the evolution of software architecture from monolithic to cloud-based systems.
Reframed from "historical survey" to "why architecture must be decided before code" —
preparing students for process models and design tools in `03c_Softwareentwurf`.

#### Main topics

- Historical stages: monolithic, OS/application split, higher-level languages,
  virtualization, internet, cloud
- **[ADDED]** Architecture in the agentic era

#### Key takeaways

- Architecture decisions outlast individual code files — they constrain what AI can
  generate.
- AI generates components; engineers decide the architecture.
- Prompt boundaries are architecture boundaries.

#### Change Notes

**Content to ADD**:
- "Architecture in the Agentic Era" closing section (~2 slides): AI can generate a
  function, a class, or a module — but not the relationships between components.
  That is the architect's job.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "History of software evolution" → "Why architecture precedes code — the evolution
  shows what happens when it doesn't."

**Agentic workflow integration**:
- "The module boundary you define in your prompt is an architecture decision."

**Symbols to add**: ⇄ on component relationship diagrams; 🔄 on agentic era slide.

**Cross-references**:
- → `03a_Wissenspyramide` (S03): information layer of the pyramid = architecture
- → `03c_Softwareentwurf` (S03): process models and UML are the design tools
