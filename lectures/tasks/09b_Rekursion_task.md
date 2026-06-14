# Task: 09b_Rekursion

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../09b_Rekursion.qmdx` |
| **Source file** | `../oldx/04b_Rekursion.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S09 |
| **Status** | MOVED from Block 3 + REFRAMED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../09b_Rekursion.qmdx`

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
