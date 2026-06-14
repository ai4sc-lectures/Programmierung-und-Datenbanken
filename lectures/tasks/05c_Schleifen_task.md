# Task: 05c_Schleifen

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../05c_Schleifen.qmdx` |
| **Source file** | `../oldx/03b_Schleifen.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S05 |
| **Status** | REFRAMED |

## Instructions

1. Read `../lecture_skill/SKILL.md` — follow its conventions for layout, icons, Quarto syntax, and slide structure throughout.
2. Read the source file(s):
   - `../oldx/03b_Schleifen.qmdx`
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../05c_Schleifen.qmdx`

---

### 05c_Schleifen

**Block**: Block 3 — Programming Foundations | **Session**: S05
**Status**: REFRAMED | **Primary symbols**: 📂 🔄
**Source file**: `../oldx/03b_Schleifen.qmdx`

#### Summary: Loops

Explains repetition through loops. Motivated by engineering scale ("process 10,000
sensor readings"). Examples are AI-generated code that students trace before running.
Infinite loop detection added as an explicit skill.

#### Main topics

- `for` loops; for-each over sequences and dicts; `while` loops
- Infinite loops, `break`, skipping elements
- **[ADDED]** Trace-table exercise for AI-generated loop
- **[ADDED]** Infinite loop detection strategy

#### Key takeaways

- AI commonly generates off-by-one errors and missing termination conditions —
  trace tables reveal these.
- Loops are motivated by scale: engineering data arrives in large collections.

#### Change Notes

**Content to ADD**:
- Trace-table exercise (~2 slides): AI-generated loop over sensor list; students fill
  in a trace table (iteration / variable values / output) on paper.
- Infinite loop detection (~2 slides): "Signs: no visible termination condition,
  loop variable not modified inside loop, condition never becomes False."
- Scale motivation (~1 slide): "10,000 soil samples, 1M sensor readings, 50,000
  building elements."

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Learn to write loops" → "Learn to read loops: trace iterations, find termination
  condition, check collection type."

**Agentic workflow integration**:
- "When AI generates a loop: (1) identify what it iterates over, (2) trace the first
  two and last iterations, (3) verify it terminates."

**Symbols to add**: 📂 on collection-iteration slides; 🔄 on loop pattern slides.

**Cross-references**:
- → `02c_Datentypen` (S02): collection types introduced there
- → `09a_Algorithmen` (S09): algorithms as structured loop patterns
