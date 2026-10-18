# Task: 01c_Computerhardware

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../01c_Computerhardware.qmdx` |
| **Source file** | `../oldx/01c_Computerhardware.qmdx` |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S02 |
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
   - `../01c_Computerhardware.qmdx`

---

### 01c_Computerhardware

**Block**: Block 1 — Computational Foundations | **Session**: S02
**Status**: EXPANDED | **Primary symbols**: □ ≡
**Source file**: `oldx/01c_Computerhardware.qmdx`

#### Summary: Computer Hardware

Structure of computers and how hardware components support data processing.
In the redesign, adds a sequential execution model connecting hardware to Python's
runtime: memory consists of cells with addresses, and the CPU only knows addresses.
Stack/heap is NOT taught here (it needs functions and recursion); it lives in
`06a_Funktionen` and `09b_Rekursion`.

#### Main topics

- Computer types; CPU, GPU, RAM, storage, motherboard
- Buses, instruction pointer, registers, memory cells
- Storage hierarchy: registers, cache, RAM, SSD/HDD
- Binary representation of integers and floats
- **[ADDED]** Sequential execution model: instruction pointer advancing through memory
- **[MOVED to 09b_Rekursion]** Stack and heap slides with the Manim videos
  (`manim_stack_heap`, `manim_call_stack`; both use the recursion s(n))

#### Key takeaways

- Every instruction the CPU executes comes from a memory address; execution is
  sequential by default.
- The memory hierarchy explains performance differences across programs.
- Memory is a sequence of cells with addresses; a variable name in the code stands for
  an address in the running program (developed further in `02c_Speicher`).

#### Change Notes

**Content to ADD**:
- Sequential execution model (~3 slides): instruction pointer advancing, registers
  holding intermediate values, memory-cell diagram annotated with □ symbols for
  variables. Connect to "how Python code becomes machine instructions."

**Content to REMOVE or REDUCE**:
- MOVE "Zwei Speicherregionen im RAM" and "Der Stack wächst mit jedem Aufruf" (slides,
  `%%book`, Manim videos) to `09b_Rekursion`. Leave one sentence: "→ `02c_Speicher`".

**Content to REFRAME**:
- Binary representation → "this is what □ (a variable) looks like in hardware" —
  motivates data types in `02b_Datentypen`.

**Agentic workflow integration**: none specific (the stack-overflow callout moves to
`09b_Rekursion` together with the stack slides).

**Symbols to add**: □ on memory-cell diagram; ≡ on binary representation slide.

**Cross-references**:
- → `02c_Speicher` (S02): name in the code → address in memory
- → `02b_Datentypen` (S02): data types as memory representations
- → `09b_Rekursion` (S09): stack/heap slides and videos moved there
