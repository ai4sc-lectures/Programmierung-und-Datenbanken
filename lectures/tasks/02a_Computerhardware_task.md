# Task: 02a_Computerhardware

| Field | Value |
|-------|-------|
| **New file** | `../02a_Computerhardware.qmdx` |
| **Source file** | `../oldx/01c_Computerhardware.qmdx` |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S02 |
| **Status** | EXPANDED |

> Open `../oldx/01c_Computerhardware.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 02a_Computerhardware

**Block**: Block 1 — Computational Foundations | **Session**: S02
**Status**: EXPANDED | **Primary symbols**: □ ≡
**Source file**: `../oldx/01c_Computerhardware.qmdx`

#### Summary: Computer Hardware

Structure of computers and how hardware components support data processing.
In the redesign, receives stack/heap content migrated from `09b_Rekursion` and adds
a sequential execution model connecting hardware to Python's runtime — essential for
understanding AI-generated code that causes unexpected memory behavior.

#### Main topics

- Computer types; CPU, GPU, RAM, storage, motherboard
- Buses, instruction pointer, registers, memory cells
- Storage hierarchy: registers, cache, RAM, SSD/HDD
- Binary representation of integers and floats
- **[ADDED]** Sequential execution model: instruction pointer advancing through memory
- **[RECEIVED from 04b_Rekursion]** Stack and heap memory concepts

#### Key takeaways

- Every instruction the CPU executes comes from a memory address; execution is
  sequential by default.
- The memory hierarchy explains performance differences across programs.
- Stack and heap are two memory regions with different lifetimes — essential for
  understanding recursion and object references (developed further in `02b_Speicher`).

#### Change Notes

**Content to ADD**:
- Sequential execution model (~3 slides): instruction pointer advancing, registers
  holding intermediate values, memory-cell diagram annotated with □ symbols for
  variables. Connect to "how Python code becomes machine instructions."
- Stack and heap content (RECEIVED from `09b_Rekursion`): keep the visual from that
  file; reframe here as "two memory regions, not a Python feature."

**Content to REMOVE or REDUCE**: None. Stack/heap joins existing hardware content here.

**Content to REFRAME**:
- Binary representation → "this is what □ (a variable) looks like in hardware" —
  motivates data types in `02c_Datentypen`.

**Agentic workflow integration**:
- Callout: "When AI generates deep recursion, it may not know your system's stack
  size. Understanding the execution model helps you recognize and fix stack overflows."

**Symbols to add**: □ on memory-cell diagram; ≡ on binary representation slide.

**Cross-references**:
- → `02b_Speicher` (S02): detailed memory model follows
- → `02c_Datentypen` (S02): data types as memory representations
- → `09b_Rekursion` (S09): REMOVE stack/heap there — content now lives here
