# Task: 04c_Objects — Design Concept View

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../04c_Objects.qmdx` |
| **Source file** | `../oldx/04c_Objects.qmdx` (first appearance; design concept slides only) |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S04 |
| **Status** | MOVED (design concept view only) |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../04c_Objects.qmdx`

---

### 04c_Objects — Design Concept View

**Block**: Block 2 — Computational Engineering | **Session**: S04
**Status**: MOVED (design concept view only) | **Primary symbols**: ○ ⇄ 📋
**Source file**: `../oldx/04c_Objects.qmdx` (first appearance; design concept slides only)

> `04c_Objects.qmdx` appears in TWO sessions. This entry covers the design concept
> view in S04. The Python implementation view is in Session 06.

#### Summary: Object Design (Conceptual View)

Uses `04c_Objects` to present OO thinking as a decomposition strategy, not a Python
feature. Students identify entities in an engineering domain, define attributes and
responsibilities, and express relationships using UML class diagrams — before any
Python syntax. "Design before you prompt."

#### Main topics

- OO design as domain decomposition
- Classes as named structures with attributes and responsibilities
- Associations, aggregation, composition
- Worked example: BIM element hierarchy (Building → Floor → Room → Window)
- **[ADDED]** UML class diagram as the design artifact for an AI prompt

#### Key takeaways

- Classes are design units before they are Python constructs.
- A UML class diagram is the specification you give to an AI; the AI generates the
  Python class; the engineer verifies against the diagram.
- Object relationships must be explicit in the design or the AI will invent them.

#### Change Notes

**Content to ADD**:
- Framing as design concept (~2 slides): "We are not learning Python syntax yet.
  We are learning to think in objects."
- "Design before you prompt" section (~3 slides): UML class diagram → structured
  prompt → AI generates Python class → verify against diagram.
- Connect to UML notation introduced in `03c_Softwareentwurf` (S03).

**Content to REMOVE or REDUCE**:
- For this view: REDUCE Python syntax slides to near zero — move to S06 implementation
  view. Keep only conceptual slides: entities, attributes, relationships, UML.

**Content to REFRAME**:
- "Here is how Python classes work" → "Here is how we decompose a domain into named
  structures before any code is written."

**Agentic workflow integration**:
- UML diagram = "prompt" step for object design: diagram → AI generates → verify
  class matches diagram.

**Symbols to add**: ○ on class/entity symbols; ⇄ on relationship arrows;
📋 on "design before prompt" slide.

**Cross-references**:
- → `03c_Softwareentwurf` (S03): UML notation introduced there
- → `04c_Objects` implementation view (S06): Python syntax for same concepts
- → `08a_UnitTest` (S08): tests verify implemented class matches design
