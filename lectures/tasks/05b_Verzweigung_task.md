# Task: 05b_Verzweigung

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../05b_Verzweigung.qmdx` |
| **Source file** | `../oldx/03a_Verzweigung.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S05 |
| **Status** | REFRAMED |

## Instructions

1. Follow the `.qmdx` conventions in `CLAUDE.md` (auto-loaded — do not read any other files).
2. The **Summary**, **Main topics**, and **Key takeaways** sections below describe the existing content — do not open the source file.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../05b_Verzweigung.qmdx`

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
