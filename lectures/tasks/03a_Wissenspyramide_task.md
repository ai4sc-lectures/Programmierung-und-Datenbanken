# Task: 03a_Wissenspyramide

| Field | Value |
|-------|-------|
| **New file** | `../03a_Wissenspyramide.qmdx` |
| **Source file** | `../oldx/02b_Wissenspyramide.qmdx` |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S03 |
| **Status** | REFRAMED |

> Open `../oldx/02b_Wissenspyramide.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 03a_Wissenspyramide

**Block**: Block 2 — Computational Engineering | **Session**: S03
**Status**: REFRAMED | **Primary symbols**: ⇄ 🔄
**Source file**: `../oldx/02b_Wissenspyramide.qmdx`

#### Summary: Knowledge Pyramid

Introduces the knowledge pyramid as the conceptual backbone of the course. Reframed
so each pyramid level maps to a course block, giving students a mental map of the
course structure. The position of AI in the pyramid is explicitly stated.

#### Main topics

- Pyramid stages: characters, syntax, semantics, data, information, processing,
  knowledge
- Programming language syntax and semantics
- Learning styles and strategies
- **[ADDED]** Pyramid levels → course block mapping diagram
- **[ADDED]** Where AI sits in the pyramid

#### Key takeaways

- Meaning arises from structured interpretation, not from symbols alone.
- The course moves students up the pyramid: data types (Block 1) → system design
  (Block 2) → implementation (Blocks 3–4) → domain problems (Block 5) → persistence
  (Block 6).
- AI operates at the data→information boundary; domain knowledge is the engineer's
  layer.

#### Change Notes

**Content to ADD**:
- Pyramid → block mapping diagram (~2 slides): characters/data → Block 1;
  information/relationships → Block 2; processing/algorithms → Blocks 3–5;
  knowledge/persistence → Block 6.
- "Where AI sits" (~1 slide): AI converts syntax to candidate code (data layer);
  the engineer validates the code implements the correct information model.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here is how meaning arises" → "Here is the map of the course — each block takes
  you one level higher on the pyramid."

**Agentic workflow integration**:
- "The agentic workflow sits at the data→information boundary: your job is to cross
  it by verifying that AI output encodes the correct engineering meaning."

**Symbols to add**: ⇄ on pyramid level transitions; 🔄 on course map diagram.

**Cross-references**:
- → `01a_Ueberblick` (S01): course structure; pyramid gives it conceptual depth
- → `03b_Softwarearchitektur` (S03): architecture is the information layer for software
