# Task: 07b_Debugging

| Field | Value |
|-------|-------|
| **New file** | `../07b_Debugging.qmdx` |
| **Source file** | `../oldx/06c_Debugging.qmdx` |
| **Block** | Block 4 — Verification & Quality |
| **Session** | S07 |
| **Status** | REFRAMED |

> Open `../oldx/06c_Debugging.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
