# Task: 06a_Funktionen

| Field | Value |
|-------|-------|
| **New file** | `../06a_Funktionen.qmdx` |
| **Source file** | `../oldx/04a_Funktionen.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S06 |
| **Status** | REFRAMED |

> Open `../oldx/04a_Funktionen.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
