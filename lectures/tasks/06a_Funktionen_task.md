# Task: 06a_Funktionen

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../06a_Funktionen.qmdx` |
| **Source file** | `../oldx/04a_Funktionen.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S06 |
| **Status** | REFRAMED |

## Instructions

1. Read `../lecture_skill/SKILL.md` — follow its conventions for layout, icons, Quarto syntax, and slide structure throughout.
2. Read the source file(s):
   - `../oldx/04a_Funktionen.qmdx`
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../06a_Funktionen.qmdx`

---

### 06a_Funktionen

**Block**: Block 3 — Programming Foundations | **Session**: S06
**Status**: REFRAMED | **Primary symbols**: ⚙ 📋
**Source file**: `../oldx/04a_Funktionen.qmdx`

#### Summary: Functions

Introduces functions as reusable building blocks. The function signature is
positioned as a contract: name + parameter types + return type = a promise. "Read
the signature and docstring before reading the implementation" is the primary habit.

#### Main topics

- Function definition, parameters, arguments, default values, return values, scope
- **[ADDED]** Function signature as a contract to verify
- **[ADDED]** "Read docstring → write tests → read implementation" exercise
- **[ADDED]** Mutable default argument callout (common AI error)

#### Key takeaways

- A function signature specifies a promise that can be tested before the
  implementation is read.
- Default mutable arguments in AI-generated functions often hide dangerous aliasing.

#### Change Notes

**Content to ADD**:
- "Signature as contract" framing (~2 slides): `def calculate_area(length: float,
  width: float) -> float:` is a complete specification.
- "Read docstring → write tests → read implementation" exercise (~3 slides): given an
  AI function, read signature + docstring, write two tests, then read implementation
  to check predictions.
- Mutable default callout (~1 slide): `def __init__(self, items=[]):` is a classic
  AI error — explain why.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Learn to write functions" → "Read signatures as contracts; write tests before
  reading implementations."

**Agentic workflow integration**:
- "When AI generates a function: read signature first. Correct inputs? Return type?
  Matches requirement? Write a test. If not, fix signature and reprompt."

**Symbols to add**: ⚙ on function definition slides; 📋 on signature-as-contract.

**Cross-references**:
- → `04c_Objects` design view (S04): methods are functions on objects
- → `08a_UnitTest` (S08): "read signature → write test" is the TDP workflow
