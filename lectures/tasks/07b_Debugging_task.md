# Task: 07b_Debugging

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../07b_Debugging.qmdx` |
| **Source file** | `../oldx/06c_Debugging.qmdx` |
| **Block** | Block 4 — Verification & Quality |
| **Session** | S07 |
| **Status** | REFRAMED |

## Instructions

1. Read `../lecture_skill/SKILL.md` — follow its conventions for layout, icons, Quarto syntax, and slide structure throughout.
2. Read the source file(s):
   - `../oldx/06c_Debugging.qmdx`
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../07b_Debugging.qmdx`

---

### 07b_Debugging

**Block**: Block 4 — Verification & Quality | **Session**: S07
**Status**: REFRAMED | **Primary symbols**: 🔍
**Source file**: `../oldx/06c_Debugging.qmdx`

#### Summary: Debugging

Debugging techniques reframed around AI code. Opens with "200 lines of AI code,
wrong output." Introduces a 5-step AI debugging strategy. VS Code debugger walkthrough
expanded to cover multi-function AI modules.

#### Main topics

- `print()`, `logging`; graphical debugger; Jupyter in VS Code
- **[ADDED]** 5-step AI debugging strategy
- **[ADDED]** Multi-function AI module debugger walkthrough

#### Key takeaways

- Debugging AI code: reproduce → isolate → hypothesize → inspect → fix → re-verify.
- The graphical debugger is more powerful than `print()` for multi-function AI modules.
- Static reasoning alone is insufficient — execution observation is required.

#### Change Notes

**Content to ADD**:
- Opening scenario (~1 slide): "200 lines of AI code. Wrong output. No exception.
  Where do you start?"
- 5-step AI debugging strategy (~5 slides): (1) Reproduce with minimal input,
  (2) Isolate failing function with a unit test, (3) Hypothesize which assumption is
  wrong, (4) Inspect execution state with debugger, (5) Fix and re-verify.
- Multi-function module walkthrough (~4 slides): set breakpoint at entry, step through
  calls, inspect state at each level.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here are debugging tools" → "Here is a systematic strategy for debugging AI code;
  these tools implement the strategy."

**Agentic workflow integration**:
- Debugging is the "verify" step applied at execution level.

**Symbols to add**: 🔍 on every debugging strategy slide.

**Cross-references**:
- → `07a_Exceptions` (S07): exceptions are the starting point for debugging
- → `08a_UnitTest` (S08): isolating with a unit test is step 2 of the strategy
