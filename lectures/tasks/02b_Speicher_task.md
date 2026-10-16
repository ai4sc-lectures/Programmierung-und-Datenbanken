# Task: 02b_Speicher

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../02b_Speicher.qmdx` |
| **Source file** | NEW — create `02b_Speicher.qmdx` |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S02 |
| **Status** | NEW (~20 min, ~15 slides) |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Create `../02b_Speicher.qmdx` from scratch as a new `.qmdx` lecture file.
3. Use the **Change Notes** below as the complete content specification — they define every section, slide group, and callout to include.
4. Save the finished file to `../02b_Speicher.qmdx`.

---

### 02b_Speicher

**Block**: Block 1 — Computational Foundations | **Session**: S02
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: □ ≡ ⇄
**Source file**: NEW — create `02b_Speicher.qmdx`

#### Summary: Memory Model

New lecture covering the Python memory model at the level relevant for engineering
programmers. Variables are named references to memory cells, not boxes containing
values. The stack/heap distinction is covered visually. Engineering motivation: AI
code often makes incorrect assumptions about object identity and mutability —
understanding the memory model is required to debug them.

#### Main topics

- Variables as names bound to memory addresses
- Value types vs reference types in Python
- Aliasing and mutation: when two names point to the same object
- Stack memory: function call frames, local variable lifetime
- Heap memory: object lifetime, garbage collection
- Visual diagrams of each concept
- Why the memory model matters for debugging AI-generated code

#### Key takeaways

- In Python, assignment binds a name to an object; it does not copy the object.
- Mutable objects shared via references cause surprising side effects in AI-generated
  code.
- Understanding the stack prevents confusion when reading exception tracebacks.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–3: Variables as references — `id()`, assignment binds a name, diagram of
  name → object → value
- Slides 4–5: Value vs reference semantics — immutable (int, str, tuple) vs mutable
  (list, dict, object)
- Slides 6–7: Aliasing example: `a = [1,2,3]; b = a; b.append(4)` — why `a` is now
  `[1,2,3,4]`; diagram
- Slides 8–10: Call stack — each function call creates a frame; local variables live
  in the frame; frame destroyed on return; visual stack growing and shrinking
- Slides 11–12: Heap — objects live in heap; references from stack point into heap;
  garbage collection reclaims unreachable objects
- Slides 13–14: Engineering implications — common AI mistakes: mutation of input
  lists, returning mutable defaults, unintended aliasing in object graphs
- Slide 15: Connection to debugging — reading a traceback = reading the call stack

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "When AI generates a function taking a list as input, check: does it modify the
  list in place or return a new list? The answer determines whether the caller's data
  is safe."

**Symbols to add**: □ on every variable diagram; ≡ on type annotation slides;
⇄ on aliasing/reference diagrams.

**Cross-references**:
- → `02a_Computerhardware` (S02): execution model motivates this
- → `02c_Datentypen` (S02): data types as memory representations connects here
- → `09b_Rekursion` (S09): recursion revisited with call stack already understood
