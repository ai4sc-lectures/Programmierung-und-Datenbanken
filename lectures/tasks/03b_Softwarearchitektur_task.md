# Task: 03b_Softwarearchitektur

| Field | Value |
|-------|-------|
| **New file** | `../03b_Softwarearchitektur.qmdx` |
| **Source file** | `../oldx/02a_Softwarearchitektur.qmdx` |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S03 |
| **Status** | REFRAMED |

> Open `../oldx/02a_Softwarearchitektur.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
