# Task: 08a_UnitTest

| Field | Value |
|-------|-------|
| **New file** | `../08a_UnitTest.qmdx` |
| **Source file** | `../oldx/06b_UnitTest.qmdx` |
| **Block** | Block 4 — Verification & Quality |
| **Session** | S08 |
| **Status** | EXPANDED |

> Open `../oldx/06b_UnitTest.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
