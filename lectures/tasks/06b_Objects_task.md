# Task: 06b_Objects — Implementation View

| Field | Value |
|-------|-------|
| **New file** | `../06b_Objects.qmdx` |
| **Source file** | `../oldx/04c_Objects.qmdx` (second appearance; implementation slides only) |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S06 |
| **Status** | REFRAMED (implementation view) |

> Open `../oldx/04c_Objects.qmdx` (second appearance; implementation slides only) as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
