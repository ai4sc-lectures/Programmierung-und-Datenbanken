# Task: 07a_Exceptions

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../07a_Exceptions.qmdx` |
| **Source file** | `../oldx/06a_Exceptions.qmdx` |
| **Block** | Block 4 — Verification & Quality |
| **Session** | S07 |
| **Status** | REFRAMED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../07a_Exceptions.qmdx`

---

### 07a_Exceptions

**Block**: Block 4 — Verification & Quality | **Session**: S07
**Status**: REFRAMED | **Primary symbols**: 🔍
**Source file**: `../oldx/06a_Exceptions.qmdx`

#### Summary: Exceptions

Explains Python exception handling. Opens with "you ran AI code and got TypeError."
Exceptions are reframed as contract violations that reveal incorrect assumptions in
AI-generated code. The call stack trace becomes a diagnostic tool.

#### Main topics

- Error types: lexical, syntactic, semantic; exception handling; custom exceptions
- Exception propagation through the call stack
- **[ADDED]** Exceptions as AI contract violations
- **[ADDED]** Call stack trace as a diagnostic tool; guard clause pattern

#### Key takeaways

- Exceptions reveal that an AI assumption was wrong — they are diagnostic information.
- Reading a traceback means reading the call stack frozen at the moment of failure.
- Guard clauses prevent exceptions by checking preconditions before risky operations.

#### Change Notes

**Content to ADD**:
- Opening scenario (~2 slides): "You ran 200 lines of AI code. TypeError: unsupported
  operand type NoneType + float. Walk through the traceback, identify the faulty
  assumption, add a guard clause."
- Guard clause pattern (~2 slides): "AI often omits precondition checks before risky
  operations (division, attribute access). Add them."
- Call stack as diagnostic (~2 slides): traceback = call stack frozen at failure;
  read top-to-bottom to reveal execution path.

**Content to REMOVE or REDUCE**:
- Reduce debugging content here — `07b_Debugging` (same session) covers it in depth.

**Content to REFRAME**:
- "Exceptions signal errors" → "Exceptions signal that an AI assumption was
  incorrect; the traceback tells you which assumption."

**Agentic workflow integration**:
- "When AI code throws an exception: (1) read traceback, (2) identify failed
  assumption, (3) add guard clause or fix data, (4) reprompt with constraint explicit."

**Symbols to add**: 🔍 on traceback analysis slides.

**Cross-references**:
- → `07b_Debugging` (S07): debugging tools for the same error
- → `08a_UnitTest` (S08): tests catch exception cases before production
