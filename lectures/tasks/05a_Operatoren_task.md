# Task: 05a_Operatoren

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../05a_Operatoren.qmdx` |
| **Source file** | `../oldx/03a_Operatoren.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S05 |
| **Status** | REFRAMED |

## Instructions

1. Read `../lecture_skill/SKILL.md` — follow its conventions for layout, icons, Quarto syntax, and slide structure throughout.
2. Read the source file(s):
   - `../oldx/03a_Operatoren.qmdx`
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../05a_Operatoren.qmdx`

---

### 05a_Operatoren

**Block**: Block 3 — Programming Foundations | **Session**: S05
**Status**: REFRAMED | **Primary symbols**: □ ≡
**Source file**: `../oldx/03a_Operatoren.qmdx`

#### Summary: Operators

Covers Python operators — arithmetic, comparison, logical, bitwise. Examples are
reframed as "AI-generated code to read" rather than "code to write." Operator
precedence is motivated by the need to trace AI expressions before accepting them.

#### Main topics

- Arithmetic, assignment, comparison, identity, membership operators
- Logical and bitwise operators; operator overloading
- **[ADDED]** "Read from AI output" labeling on examples
- **[ADDED]** Trace-this-expression exercise on AI-generated code

#### Key takeaways

- Understanding operator precedence is essential for tracing AI-generated expressions.
- Type mismatches in operator use are a common AI code error.

#### Change Notes

**Content to ADD**:
- "Read from AI output" labels: mark examples as "this is what AI generated — trace
  it before running."
- Trace-this-expression exercise (~2 slides): complex AI-generated expression,
  students evaluate step-by-step on paper before running.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Learn to write expressions" → "Learn to read and trace expressions — then verify
  AI output."

**Agentic workflow integration**:
- "When AI generates `if not x is None and x > 0.0:` — trace before you trust."

**Symbols to add**: □ on variable introduction; ≡ on type-specific operator slides.

**Cross-references**:
- → `02c_Datentypen` (S02): operator behavior depends on type
- → `05b_Verzweigung` (S05): operators in conditional expressions
