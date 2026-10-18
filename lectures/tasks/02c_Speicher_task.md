# Task: 02c_Speicher

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../02c_Speicher.qmdx` |
| **Source file** | NEW — create `02c_Speicher.qmdx` |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S02 |
| **Status** | NEW (~20 min, 6 slides) |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Create `../02c_Speicher.qmdx` from scratch as a new `.qmdx` lecture file.
3. Use the **Change Notes** below as the complete content specification — they define every section, slide group, and callout to include.
4. Save the finished file to `../02c_Speicher.qmdx`.

---

### 02c_Speicher

**Block**: Block 1 — Computational Foundations | **Session**: S02
**Status**: NEW (~20 min, 6 slides) | **Primary symbols**: □ ⇄
**Source file**: NEW — `02c_Speicher.qmdx`

#### Summary: Memory Model of Variables

The single place where the course explains what a variable is in memory. Builds on
`01c` (memory cells with addresses) and `02b` (variables, types, lists). Students
need no functions and no operators besides `=`. One question carries the deck: after
`auswertung = messwerte` and sorting `auswertung`, is `messwerte` sorted too?

#### Learning goal

Students can explain what happens in memory when Python executes an assignment, and
predict whether a change through one variable affects another.

#### Main topics

- A name exists only in the source code; in the running program it stands for an
  address in memory where the value lies (`id()` shows it)
- Assignment gives the name an address; a new assignment gives it a new address
- `b = a` copies the address, not the value: two names, one address (*Alias*)
- Two kinds of change: new assignment vs. changing the content in place;
  mutable/immutable types (**[RECEIVED from 02b_Datentypen]**)
- Copies (`.copy()`) give independent data

#### Key takeaways

- A variable name stands for an address; the value lives at that address.
- `b = a` shares the address. Changing the content through `b` is visible through `a`.
- Only mutable types (`list`, `dict`, `set`) can change their content; immutable types
  only get new assignments.
- Independent data needs an explicit copy.

#### Change Notes

**Slide sequence** (one running example: `messwerte = [3.2, 1.1, 4.5]`):
1. Hörsaalfrage: `auswertung = messwerte`, then sort `auswertung` — is `messwerte`
   sorted too? (resolved on slide 6)
2. The name in the code is not the memory: `a` exists only in the source code; in the
   running program `a` stands for an address; `id(a)` shows it. Manim animation
   (`manim/variablen.py`, style of `manim/stack_heap.py`): code line → value in a
   memory cell → name table row `a | 0x…` → arrow; `print(a)` follows the address.
3. Assignment: `temperatur = 21.5`, then `temperatur = 23.0` — the name gets a new
   address; the old value is not overwritten. `id()` before and after.
4. `b = a` copies the address, not the value. Define *Alias* here (two names for the
   same address) and why it matters.
5. Two kinds of "change": new assignment (`b = …`) vs. changing the content
   (`b.append(…)`, `b.sort()`); the mutable/immutable table from `02b`.
6. Resolution and copy: yes, `messwerte` is sorted too; `auswertung = messwerte.copy()`
   gets a new address.

**Rules**: every term is defined on the slide where it first appears (Adresse,
Zuweisung, Alias, veränderlich/unveränderlich, Kopie). No interpreter internals
(small-int cache, constants, bytecode). One visual language: name table left, memory
cells with addresses right, as in the cell diagrams of `01c`.

**NOT in this deck** (lives elsewhere): `==`/`is` (`05a`), call stack and frames
(`06a`), mutated arguments and mutable defaults (`06a`), tracebacks (`07a`), stack
overflow and recursion (`09b`).

**Symbols to add**: □ on variable diagrams; ⇄ on shared-address diagrams.

**Cross-references**:
- → `01c_Computerhardware` (S02): memory cells and addresses
- → `02b_Datentypen` (S02): variables, types, lists
- → `05a_Operatoren` (S05): `is` checks for the same address
- → `06a_Funktionen` (S06): arguments share the address (builds on slide 4–5)
