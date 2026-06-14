# Task: 05a_Operatoren

| Field | Value |
|-------|-------|
| **New file** | `../05a_Operatoren.qmdx` |
| **Source file** | `../oldx/03a_Operatoren.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S05 |
| **Status** | REFRAMED |

> Open `../oldx/03a_Operatoren.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
