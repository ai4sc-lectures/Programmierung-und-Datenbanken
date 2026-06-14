# Task: 06b_Objects — Implementation View

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../06b_Objects.qmdx` |
| **Source file** | `../oldx/04c_Objects.qmdx` (second appearance; implementation slides only) |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S06 |
| **Status** | REFRAMED (implementation view) |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../06b_Objects.qmdx`

---

### 06b_Objects — Implementation View

**Block**: Block 3 — Programming Foundations | **Session**: S06
**Status**: REFRAMED (implementation view) | **Primary symbols**: ○ ⇄ ⚙
**Source file**: `../oldx/04c_Objects.qmdx` (second appearance; implementation slides only)

> Second appearance of `04c_Objects.qmdx`. Design concept view was in S04.
> This entry covers Python implementation.

#### Summary: Python Classes (Implementation View)

Connects the UML class diagram from S03/S04 to Python syntax. Students who have
already designed a class on paper now see how `class`, `__init__`, `self`, and
methods implement that design. The BIM example from S04 reappears as a complete
Python class.

#### Main topics

- `class`, `__init__`, `self`; instance and class attributes; methods
- References between objects (implementing associations); encapsulation; inheritance
- **[ADDED]** UML from S04 mapped to Python syntax
- **[ADDED]** Common AI OOP mistakes
- **[ADDED]** Code understanding questionnaire

#### Key takeaways

- Python class syntax implements UML design decisions made in S04.
- AI often conflates class and instance attributes, misuses `self`, or ignores
  encapsulation.
- Verifying a class means checking it against its design diagram, not just running it.

#### Change Notes

**Content to ADD**:
- UML → Python mapping (~3 slides): class name → `class Name:`, attribute →
  `self.attr`, method → `def method(self):`, association → instance attribute.
- BIM worked example continuation (~3 slides): `Room` class from S04 UML diagram →
  AI generates Python class → verify each attribute and method against diagram.
- Common AI OOP mistakes (~2 slides): mutable default in `__init__`; missing `self`;
  `cls` used where `self` was intended.
- Code understanding questionnaire (~1 slide): "What does this class model?",
  "Which requirement does it implement?", "What could fail?"

**Content to REMOVE or REDUCE**:
- Design-concept motivation slides already covered in S04 — do not repeat; jump
  directly to Python syntax.

**Content to REFRAME**:
- "Learn to write Python classes" → "Translate your UML design into Python; verify
  the translation is faithful."

**Agentic workflow integration**:
- "Prompt: 'Implement the Room class from this UML diagram.' → verify each attribute
  exists, each method signature matches, encapsulation is respected."

**Symbols to add**: ○ on class/entity slides; ⇄ on association implementation;
⚙ on method definition slides.

**Cross-references**:
- → `04c_Objects` design view (S04): design artifacts used here
- → `06c_Module` (S06): classes organized into modules
- → `08b_CodeReview` (S08): OOP best practices in the review checklist
