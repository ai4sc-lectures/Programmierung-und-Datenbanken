# Task: 02c_Datentypen

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../02c_Datentypen.qmdx` |
| **Source file** | `../oldx/02c_Datentypen.qmdx` (filename unchanged) |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S02 |
| **Status** | MOVED from Block 2 + REFRAMED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../02c_Datentypen.qmdx`

---

### 02c_Datentypen

**Block**: Block 1 — Computational Foundations | **Session**: S02
**Status**: MOVED from Block 2 + REFRAMED | **Primary symbols**: □ ≡ 📂
**Source file**: `../oldx/02c_Datentypen.qmdx` (filename unchanged)

#### Summary: Data Types

Introduces Python variables and data types. Moved to S02 to sit alongside the
hardware and memory content. Reframed: data types are not just "kinds of values"
but memory representations — the way int, float, bool, str are stored in hardware
as described in `02a`.

#### Main topics

- Variables and naming conventions
- Numeric, boolean, textual, binary types
- Sequences, sets, dictionaries; null values
- Mutability vs immutability
- **[ADDED]** Connection to binary representation from `02a`
- **[ADDED]** AI type-inference verification callout

#### Key takeaways

- Data types determine how values are stored in memory and what operations are valid.
- AI-generated code often infers types implicitly — engineers verify the inferred type
  matches the engineering requirement.
- Choosing the wrong type (e.g., `int` instead of `float` for distance) is a
  modeling error, not a style issue.

#### Change Notes

**Content to ADD**:
- Connection to binary representation from `02a` (~2 slides): "An integer is 4 bytes;
  a float is 8 bytes; here is what they look like in memory."
- AI verification callout: "When AI infers a type (e.g., distance as `int`), verify
  the inferred type matches the engineering requirement."

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here are Python's types" → "Here is how engineering values are stored in memory;
  choosing the wrong type is a modeling error."

**Agentic workflow integration**:
- Exercise: given AI-generated code computing wall area as `int`, identify the
  precision error and fix the type annotation.

**Symbols to add**: □ on variable slides; ≡ on type listing slides;
📂 on collection type slides.

**Cross-references**:
- → `02a_Computerhardware` (S02): binary representation already introduced
- → `02b_Speicher` (S02): memory model of variables
- → `05a_Operatoren` (S05): operators act on typed values
