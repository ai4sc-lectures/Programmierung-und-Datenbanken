# Task: 04c_Objects — Design Concept View

| Field | Value |
|-------|-------|
| **New file** | `../04c_Objects.qmdx` |
| **Source file** | `../oldx/04c_Objects.qmdx` (first appearance; design concept slides only) |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S04 |
| **Status** | MOVED (design concept view only) |

> Open `../oldx/04c_Objects.qmdx` (first appearance; design concept slides only) as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
