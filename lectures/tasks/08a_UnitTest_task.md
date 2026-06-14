# Task: 08a_UnitTest

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../08a_UnitTest.qmdx` |
| **Source file** | `../oldx/06b_UnitTest.qmdx` |
| **Block** | Block 4 — Verification & Quality |
| **Session** | S08 |
| **Status** | EXPANDED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../08a_UnitTest.qmdx`

---

### 08a_UnitTest

**Block**: Block 4 — Verification & Quality | **Session**: S08
**Status**: EXPANDED | **Primary symbols**: 🔍 📋
**Source file**: `../oldx/06b_UnitTest.qmdx`

#### Summary: Unit Tests

Introduces unit testing as systematic error detection. Expanded with test-driven
prompting (TDP): write tests before prompting the AI so the test suite is the
acceptance criterion. Environmental monitoring threshold function as the worked
example.

#### Main topics

- Why tests matter; functional, limit, and data type tests; test structure; coverage
- **[ADDED]** Test-Driven Prompting: write tests before you prompt
- **[ADDED]** Using the test suite to evaluate AI output
- **[ADDED]** Environmental threshold function worked example (5 tests → AI generates
  → at least 1 fails → diagnose → iterate)

#### Key takeaways

- Writing tests before prompting forces precise behavior specification — the prompt
  becomes better as a result.
- A failing test on AI code is success: you found the error before production.
- Test coverage reveals which behaviors the AI did not implement.

#### Change Notes

**Content to ADD**:
- "Test-Driven Prompting" section (~4 slides): (1) Start from requirements, (2) Write
  tests that operationalize requirements, (3) Prompt with tests as acceptance
  criterion, (4) AI generates, (5) Run tests, (6) If fail, diagnose and reprompt.
- Environmental threshold example (~5 slides): requirement "classify soil
  contamination as Clean/Monitor/Critical." Write 5 tests: normal cases (3) +
  boundary cases (2). AI generates `classify_contamination()`. At least one test
  fails — diagnose and iterate.
- Code coverage section (~2 slides): line coverage and branch coverage; untested
  branches in AI code are invisible risks.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Tests catch bugs" → "Tests are the specification; writing them before prompting
  makes AI output measurable."

**Agentic workflow integration**:
- TDP maps directly onto the agentic cycle: tests = requirements (prompt step);
  AI generates (generate step); test runner = verify step; failing tests → iterate.

**Symbols to add**: 🔍 on testing strategy slides; 📋 on requirement → test slides.

**Cross-references**:
- → `04a_Anforderungen` (S04): requirements are the source of tests
- → `01c_AgentischesProgrammieren` (S01): "verify" step formalised here
- → `08b_CodeReview` (S08): code review follows testing; both are verification
