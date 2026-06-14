# Task: 09b_Rekursion

| Field | Value |
|-------|-------|
| **New file** | `../09b_Rekursion.qmdx` |
| **Source file** | `../oldx/04b_Rekursion.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S09 |
| **Status** | MOVED from Block 3 + REFRAMED |

> Open `../oldx/04b_Rekursion.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 09b_Rekursion

**Block**: Block 5 — Problem Classes | **Session**: S09
**Status**: MOVED from Block 3 + REFRAMED | **Primary symbols**: 🔄
**Source file**: `../oldx/04b_Rekursion.qmdx`

#### Summary: Recursive Functions

Moved to Block 5 and reframed as a divide-and-conquer strategy, not a Python
language feature. Stack/heap content is removed — that is now in `02b_Speicher`
(S02). Engineering examples from BIM hierarchy traversal and spatial subdivision
replace the canonical factorial.

#### Main topics

- Recursion as divide-and-conquer; recursive functions; base case and recursive case
- Preventing infinite recursion
- **[REMOVED]** Stack/heap content → moved to S02
- **[ADDED]** BIM hierarchy traversal; spatial subdivision; recursion vs iteration

#### Key takeaways

- Recursion is a strategy for problems that decompose into smaller same-type instances.
- BIM models and spatial trees are natural recursive structures in civil engineering.
- Students already understand the call stack from `02b_Speicher` (S02).

#### Change Notes

**Content to ADD**:
- Divide-and-conquer framing (~2 slides): recursion is a strategy; problems that
  decompose into smaller same-type problems are candidates.
- BIM hierarchy traversal (~3 slides): Building → Floors → Rooms → Elements; each
  level delegates to the same function. AI generates; students verify base case and
  recursive step.
- Spatial subdivision example (~2 slides): quadtree for geographic data.
- Recursion vs iteration comparison (~2 slides): when each is appropriate; stack depth
  constraints.

**Content to REMOVE or REDUCE**:
- REMOVE stack/heap content: now in `02b_Speicher` (S02). Only reference:
  "You already understand the call stack from Session 02."
- REDUCE factorial example: keep as minimal intro; engineering examples are primary.

**Content to REFRAME**:
- "Recursion is how Python handles self-reference" → "Recursion is a divide-and-
  conquer strategy for hierarchical engineering data."

**Agentic workflow integration**:
- "When AI generates a recursive function: verify base case, trace first two recursive
  calls, check stack depth for expected input size."

**Symbols to add**: 🔄 on divide-and-conquer diagram.

**Cross-references**:
- → `02b_Speicher` (S02): call stack explained there — reference, don't repeat
- → `09a_Algorithmen` (S09): recursion as a divide-and-conquer algorithm strategy
