# Task: 05b_Verzweigung

| Field | Value |
|-------|-------|
| **New file** | `../05b_Verzweigung.qmdx` |
| **Source file** | `../oldx/03a_Verzweigung.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S05 |
| **Status** | REFRAMED |

> Open `../oldx/03a_Verzweigung.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 05b_Verzweigung

**Block**: Block 3 — Programming Foundations | **Session**: S05
**Status**: REFRAMED | **Primary symbols**: 🔍 □
**Source file**: `../oldx/03a_Verzweigung.qmdx`

#### Summary: Branching

Introduces conditional branching. Adds branch-reading strategy: students mentally
walk through AI-generated `if`/`elif`/`else` blocks to identify which branch executes
under which condition. Structural engineering threshold classifier replaces abstract
examples.

#### Main topics

- `if`, `else`, `elif`; nested and multi-way branching
- **[ADDED]** Branch-reading strategy for AI-generated code
- **[ADDED]** AI-generated threshold classifier (structural stress: OK/Warning/Critical)

#### Key takeaways

- For AI-generated branching: identify conditions, trace branches, list missing cases.
- Writing one test per branch is the minimum for verifying conditional logic.

#### Change Notes

**Content to ADD**:
- Branch-reading strategy (~2 slides): "For every `if` block: (1) identify the
  condition, (2) identify branches, (3) list inputs triggering each branch, (4) check
  for missing cases (None, negative values)."
- Threshold-classifier example (~3 slides): AI-generated `classify_stress()` for
  structural stress levels. Students trace each branch, then write one unit test per
  branch.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Write conditional logic" → "Read conditional logic: trace branches, find missing
  cases."

**Agentic workflow integration**:
- "Before accepting AI branching logic: trace every branch manually, check for
  missing cases, write a test for each branch."

**Symbols to add**: 🔍 on branch-reading strategy; □ on Boolean variable slides.

**Cross-references**:
- → `05a_Operatoren` (S05): Boolean operators used in conditions
- → `08a_UnitTest` (S08): "one test per branch" rule formalised there
