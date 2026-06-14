# Lectures New Structure Plan — Agentic Programming Redesign

## Overview

This document is the redesign roadmap for the course "Programming and Databases"
(civil/environmental engineering, 1st semester). It describes the new 6-block,
13-session structure and provides Change Notes for each lecture file.

The existing `lectures/lectures_summary.md` is **NOT modified**.
Actual lecture files are edited separately, file by file, using these Change Notes.

**Conceptual thread:** Representation → Decomposition → Implementation → Verification → Scaling
**Pedagogical shift:** "write code from scratch" → **Understand → Modify → Verify AI-generated code**
**Agentic workflow (woven throughout):** prompt → generate → understand → verify → iterate

### Block Overview

| Block | Sessions | Theme | Key Question |
|-------|----------|-------|--------------|
| 1 | S01–S02 | Computational Foundations | What machine are we building for? |
| 2 | S03–S04 | Engineering Approach | What are we building and why? |
| 3 | S05–S06 | Programming Foundations | How does the machine execute our intent? |
| 4 | S07–S08 | Verification & Quality | How do we know the solution is correct? |
| 5 | S09–S11 | Problem Classes | What type of problem am I solving? |
| 6 | S12–S13 | Data Management | How do we persist and scale information? |

### Recurring Symbols

Icons are SVG files from `lectures/_extensions/ai4sc-style/assets/icons/`.
Reference format in `.qmdx`: `{{< ai4sc-icon name >}}` (or equivalent shortcode).

Each lecture declares its **primary symbols** at the top (e.g., `🔍 📋`).
Rules for use:

| Icon | Shortcode | Concept | When to use |
| ---- | --------- | ------- | ----------- |
| ![variable](_extensions/ai4sc-style/assets/icons/variable.svg) | `variable` | Variable | First mention of a named value or binding |
| ![braces](_extensions/ai4sc-style/assets/icons/braces.svg) | `braces` | Datatype | First mention of a type or representation |
| ![box](_extensions/ai4sc-style/assets/icons/box.svg) | `box` | Object / Entity | First mention of a class or domain entity |
| ![arrow-left-right](_extensions/ai4sc-style/assets/icons/arrow-left-right.svg) | `arrow-left-right` | Relationship | First mention of an association or reference |
| ![square-function](_extensions/ai4sc-style/assets/icons/square-function.svg) | `square-function` | Function | First mention of a function or method |
| ![workflow](_extensions/ai4sc-style/assets/icons/workflow.svg) | `workflow` | Algorithm / Cycle | First mention of an algorithm or the agentic cycle |
| ![clipboard-list](_extensions/ai4sc-style/assets/icons/clipboard-list.svg) | `clipboard-list` | Requirement | First mention of a requirement or specification |
| ![test-tube](_extensions/ai4sc-style/assets/icons/test-tube.svg) | `test-tube` | Test / Verification | First mention of a test, check, or review step |
| ![list-tree](_extensions/ai4sc-style/assets/icons/list-tree.svg) | `list-tree` | Data Structure | First mention of a collection or file format |
| ![database](_extensions/ai4sc-style/assets/icons/database.svg) | `database` | Database | First mention of a database concept |

---

## Block 1 — Computational Foundations (Sessions 01–02)

*Key question: What machine are we building for?*

---

### 01a_Ueberblick

**Block**: Block 1 — Computational Foundations | **Session**: S01
**Status**: REFRAMED | **Primary symbols**: ≡ 🔄
**Source file**: `oldx/01a_Ueberblick.qmdx` (filename unchanged)

#### Summary: Overview

Course introduction reframed around AI-enabled engineering. The learning goals shift
from "learn to write code" to "learn to read, verify, and modify AI-generated code."
The symbol legend and agentic cycle are introduced here so they can be referenced
throughout the course.

#### Main topics

- Course goals, topics, and organization
- Lecture and exercise workflow
- The role of AI tools in this course and in engineering practice
- Application areas: CAD, structural engineering, GIS, facility management
- Symbol legend and agentic cycle overview

#### Key takeaways

- Active competencies: read, modify, and verify AI-generated code.
- Python is the primary language because of its AI ecosystem and engineering tool coverage.
- The agentic workflow (prompt → generate → understand → verify → iterate) applies to
  every programming task in this course.

#### Change Notes

**Content to ADD**:
- Course framing around AI-enabled engineering (~3 slides): restate goals as "read AI
  code, modify for the engineering requirement, verify quality." Include a one-slide
  diagram of the full agentic cycle.
- Symbol legend slide: introduce □ ≡ ○ ⇄ ⚙ 🔄 📋 🔍 📂 🗄 with SVG icon references;
  explain these markers appear throughout the course to label "what kind of thing
  we are talking about."

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "AI is a helper" → "AI generates code; the engineer is the architect and verifier."

**Agentic workflow integration**:
- Open with the cycle diagram (prompt → generate → understand → verify → iterate)
  as a one-slide visual. Tell students they will practice each step starting here.

**Symbols to add**: ≡ on data-types slide; 🔄 on agentic cycle diagram.

**Cross-references**:
- → `01c_AgentischesProgrammieren` (S01): mechanics of the workflow introduced visually here
- → `03a_Wissenspyramide` (S03): pyramid levels map to course block structure

---

### 01b_Programmiersprachen

**Block**: Block 1 — Computational Foundations | **Session**: S01
**Status**: REFRAMED | **Primary symbols**: ≡ 🔄
**Source file**: `oldx/01d_Programmiersprachen.qmdx`

#### Summary: Programming Languages

Overview of programming languages and their historical development. A new section
adds Python's position in the AI ecosystem: Python is the lingua franca of LLMs,
data science, and engineering automation — students learn Python because AI
generates Python.

#### Main topics

- Generations of programming languages; machine code → assembly → high-level
- Why new languages emerge; popularity trends
- Python as the primary course language
- **[ADDED]** Python in the AI ecosystem

#### Key takeaways

- Languages differ in abstraction level, usability, and domain fit.
- Python is emphasized because it is the dominant language in LLM training data and
  code output.
- Understanding Python is how you evaluate what the AI generates.

#### Change Notes

**Content to ADD**:
- "Python in the AI Ecosystem" section (~3 slides): Python dominates LLM training
  corpora; most AI-generated engineering code will be Python; language knowledge
  enables verification.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- Language popularity trends → "why Python won in the AI era" — bridge the historical
  chart to current AI tooling.

**Agentic workflow integration**:
- Closing callout: "When you prompt Claude Code or Copilot, you will almost always
  receive Python. Understanding the language is how you evaluate the output."

**Symbols to add**: ≡ on the slide introducing Python types.

**Cross-references**:
- → `01c_Programmiersprachen_ani` (S01): companion notebook using Python
- → `01c_AgentischesProgrammieren` (S01): language knowledge enables code reading

---

### 01c_Programmiersprachen_ani

**Block**: Block 1 — Computational Foundations | **Session**: S01
**Status**: REFRAMED | **Primary symbols**: 🔄
**Source file**: `oldx/01d_Programmiersprachen_ani.ipynb`

#### Summary: Programming Languages Animation

Companion notebook that builds an animated visualization of language popularity.
In the redesign it doubles as the first hands-on encounter with reading someone
else's code: students answer three comprehension questions before executing any cell,
establishing the "understand before run" habit from session one.

#### Main topics

- Download and clean ranking data; load with `pandas`
- Prepare image assets; render animated bar chart race as MP4
- **[ADDED]** "Reading AI-generated code" intro before first executable cell

#### Key takeaways

- The notebook shows a realistic data → visualization workflow.
- Reading unfamiliar code before running it is the primary learning objective here.
- Three comprehension questions scaffold active reading and self-prediction.

#### Change Notes

**Content to ADD**:
- "Reading AI-generated code" intro block (~3 cells before first executable):
  Present the notebook as code an AI handed you. Ask three questions the student
  answers in writing before running: "What does this function return?", "Which line
  downloads the data?", "What happens if the network is unavailable?" Reveal answers
  after execution.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- From "follow along and run cells" → "read first, predict, then verify by running."

**Agentic workflow integration**:
- First practical instance of the "understand → verify" steps of the agentic cycle.

**Symbols to add**: 🔄 on intro block.

**Cross-references**:
- → `01c_AgentischesProgrammieren` (S01): full workflow model that this notebook begins
- → `07b_Debugging` (S07): "read before run" is also the first step of debugging

---

### 01c_AgentischesProgrammieren

**Block**: Block 1 — Computational Foundations | **Session**: S01
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📋 🔍
**Source file**: NEW — create `01c_AgentischesProgrammieren.qmdx`

#### Summary: Agentic Programming

New lecture that introduces the conceptual model and practical workflow for
AI-assisted programming. Explains how LLMs differ from deterministic programs, how
code is generated probabilistically, what the full agentic cycle looks like, and
what the engineer's responsibilities are. Placed in S01 so every subsequent lecture
can reference this foundation.

#### Main topics

- Deterministic programs vs probabilistic LLMs: token prediction
- How AI code generation differs from a database lookup or a compiler
- The agentic workflow cycle: prompt → generate → understand → verify → iterate
- Tool landscape: Claude Code, GitHub Copilot, Cursor
- Effective prompt structure: role / context / task / constraint / output format
- Code reading strategy: signature → docstring → tests → implementation
- Engineering responsibility: the engineer owns the requirement

#### Key takeaways

- LLMs generate plausible code, not guaranteed-correct code — verification is always
  required.
- A well-structured prompt is a form of requirements specification.
- The engineer's role shifts from author to architect, reviewer, and verifier.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slide 1: Title and position ("This is the core workflow for the whole course")
- Slides 2–4: LLM basics — token prediction, training on code corpora, why outputs
  are probabilistic; contrast with a database query (exact retrieval) or a compiler
  (deterministic transformation)
- Slide 5: Agentic cycle diagram — prompt → generate → understand → verify → iterate;
  each node labeled with the skill it requires
- Slides 6–7: Tool landscape — Claude Code (terminal/editor), GitHub Copilot (inline
  suggestion), Cursor (AI-first editor); what each is good for
- Slides 8–10: Prompt structure — worked example building step-by-step: role,
  context, task, constraint ("do not use external libraries"), output format
- Slides 11–12: Code reading strategy — signature and return type first, then
  docstring, then tests, only then implementation
- Slides 13–14: Engineering responsibility — "AI is your junior developer; you are
  the senior engineer who approves the design"
- Slide 15: Preview of how this cycle appears in each course block

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- This lecture defines the agentic cycle — it is the source all other files reference.

**Symbols to add**: 🔄 on cycle diagram; 📋 on prompt structure; 🔍 on code reading.

**Cross-references**:
- → `01a_Ueberblick` (S01): cycle introduced visually there, explained here
- → `04a_Anforderungen` (S04): requirements as the source of a good prompt
- → `08a_UnitTest` (S08): test-driven prompting builds on "verify" step

---

### 02a_Computerhardware

**Block**: Block 1 — Computational Foundations | **Session**: S02
**Status**: EXPANDED | **Primary symbols**: □ ≡
**Source file**: `oldx/01c_Computerhardware.qmdx`

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

---

### 02c_Datentypen

**Block**: Block 1 — Computational Foundations | **Session**: S02
**Status**: MOVED from Block 2 + REFRAMED | **Primary symbols**: □ ≡ 📂
**Source file**: `oldx/02c_Datentypen.qmdx` (filename unchanged)

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

---

## Block 2 — Computational Engineering / Systems Engineering (Sessions 03–04)

*Key question: What are we building and why? (before code)*

---

### 03a_Wissenspyramide

**Block**: Block 2 — Computational Engineering | **Session**: S03
**Status**: REFRAMED | **Primary symbols**: ⇄ 🔄
**Source file**: `oldx/02b_Wissenspyramide.qmdx`

#### Summary: Knowledge Pyramid

Introduces the knowledge pyramid as the conceptual backbone of the course. Reframed
so each pyramid level maps to a course block, giving students a mental map of the
course structure. The position of AI in the pyramid is explicitly stated.

#### Main topics

- Pyramid stages: characters, syntax, semantics, data, information, processing,
  knowledge
- Programming language syntax and semantics
- Learning styles and strategies
- **[ADDED]** Pyramid levels → course block mapping diagram
- **[ADDED]** Where AI sits in the pyramid

#### Key takeaways

- Meaning arises from structured interpretation, not from symbols alone.
- The course moves students up the pyramid: data types (Block 1) → system design
  (Block 2) → implementation (Blocks 3–4) → domain problems (Block 5) → persistence
  (Block 6).
- AI operates at the data→information boundary; domain knowledge is the engineer's
  layer.

#### Change Notes

**Content to ADD**:
- Pyramid → block mapping diagram (~2 slides): characters/data → Block 1;
  information/relationships → Block 2; processing/algorithms → Blocks 3–5;
  knowledge/persistence → Block 6.
- "Where AI sits" (~1 slide): AI converts syntax to candidate code (data layer);
  the engineer validates the code implements the correct information model.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here is how meaning arises" → "Here is the map of the course — each block takes
  you one level higher on the pyramid."

**Agentic workflow integration**:
- "The agentic workflow sits at the data→information boundary: your job is to cross
  it by verifying that AI output encodes the correct engineering meaning."

**Symbols to add**: ⇄ on pyramid level transitions; 🔄 on course map diagram.

**Cross-references**:
- → `01a_Ueberblick` (S01): course structure; pyramid gives it conceptual depth
- → `03b_Softwarearchitektur` (S03): architecture is the information layer for software

---

### 03b_Softwarearchitektur

**Block**: Block 2 — Computational Engineering | **Session**: S03
**Status**: REFRAMED | **Primary symbols**: ⇄ 🔄
**Source file**: `oldx/02a_Softwarearchitektur.qmdx`

#### Summary: Software Architecture

Traces the evolution of software architecture from monolithic to cloud-based systems.
Reframed from "historical survey" to "why architecture must be decided before code" —
preparing students for process models and design tools in `03c_Softwareentwurf`.

#### Main topics

- Historical stages: monolithic, OS/application split, higher-level languages,
  virtualization, internet, cloud
- **[ADDED]** Architecture in the agentic era

#### Key takeaways

- Architecture decisions outlast individual code files — they constrain what AI can
  generate.
- AI generates components; engineers decide the architecture.
- Prompt boundaries are architecture boundaries.

#### Change Notes

**Content to ADD**:
- "Architecture in the Agentic Era" closing section (~2 slides): AI can generate a
  function, a class, or a module — but not the relationships between components.
  That is the architect's job.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "History of software evolution" → "Why architecture precedes code — the evolution
  shows what happens when it doesn't."

**Agentic workflow integration**:
- "The module boundary you define in your prompt is an architecture decision."

**Symbols to add**: ⇄ on component relationship diagrams; 🔄 on agentic era slide.

**Cross-references**:
- → `03a_Wissenspyramide` (S03): information layer of the pyramid = architecture
- → `03c_Softwareentwurf` (S03): process models and UML are the design tools

---

### 03c_Softwareentwurf

**Block**: Block 2 — Computational Engineering | **Session**: S03
**Status**: MOVED from Block 3 + EXPANDED | **Primary symbols**: 📋 ⇄ ⚙ 🔄
**Source file**: `oldx/05a_Softwareentwurf.qmdx`

#### Summary: Software Design

Connects programming to software engineering practice. Moved to S03 — before any
programming content — to establish that design precedes implementation. Substantially
expanded: the agentic dev loop is added as a fourth process model; UML class diagram
notation is introduced here to prepare object design in S04.

#### Main topics

- Software development phases: requirements → design → implementation → test
- Waterfall, V-model, and agile development processes
- **[ADDED]** Agentic dev loop as a fourth process model
- **[ADDED]** UML class diagram notation (prerequisite for S04 `04c_Objects`)
- **[ADDED]** BIM worked example: requirement → UML → AI prompt → verify
- **[REMOVED]** 6 revision slides reviewing OOP/datatypes (not yet taught at this point)

#### Key takeaways

- Good software begins with explicit design before any code is written.
- The agentic loop (prompt → generate → verify → iterate) is a modern process model
  where AI is the implementer.
- UML class diagrams are the language for expressing what you want before you prompt.

#### Change Notes

**Content to ADD**:
- "From Requirements to Code" opening (~5 slides): show the gap between a stakeholder
  need and a line of Python; explain that design closes this gap.
- Agentic dev loop as a process model (~5 slides): prompt = requirements spec;
  generate = implementation sprint; verify = test suite; iterate = next sprint.
  Compare rhythm and risk with waterfall and agile.
- UML class diagrams (~5 slides): class notation, typed attributes, methods with
  signatures, association and inheritance arrows. Enough to draw a simple domain
  model.
- BIM worked example (~3 slides): "A building has rooms. Each room has a name, area,
  and list of windows." → requirement → UML → AI prompt → generated Python code →
  verify against diagram.

**Content to REMOVE or REDUCE**:
- REMOVE 6 revision slides reviewing OOP and data types. These assume knowledge not
  yet covered at this point in the redesigned sequence.

**Content to REFRAME**:
- "Here are the development processes" → "Choose the right process; here is where AI
  fits as a fourth model."

**Agentic workflow integration**:
- The agentic dev loop slide explicitly maps the cycle from `01c_AgentischesProgrammieren`
  onto project management rhythm.

**Symbols to add**: 📋 on requirements slides; ⇄ on UML relationship diagrams;
⚙ on method notation; 🔄 on process model comparison.

**Cross-references**:
- → `03b_Softwarearchitektur` (S03): architecture precedes design; this is the design
  step
- → `04c_Objects` design view (S04): UML introduced here is applied there
- → `04a_Anforderungen` (S04): requirements engineering detail follows

---

### 04a_Anforderungen

**Block**: Block 2 — Computational Engineering | **Session**: S04
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 📋 🔍
**Source file**: NEW — create `04a_Anforderungen.qmdx`

#### Summary: Requirements Engineering

New lecture covering requirements engineering as the foundation for AI-assisted
development. A requirement is the source of a prompt and the source of a test — so
requirements engineering is the prerequisite for both prompting well and verifying
confidently.

#### Main topics

- Functional requirements: what the system must do
- Non-functional requirements: performance, reliability, maintainability
- Constraints: hardware, platform, regulatory
- Stakeholder perspectives
- Quality criteria: measurable acceptance conditions
- User stories: as a [role], I want [action] so that [benefit]
- Requirements as AI prompt specifications
- Requirement → test case traceability

#### Key takeaways

- A requirement is a measurable statement of what the system must do, not how.
- Every functional requirement should generate at least one test case.
- A well-written requirement is the best possible prompt for an AI code generator.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Why requirements matter — "AI satisfies the prompt, not the
  stakeholder. You are the bridge."
- Slides 3–5: Functional vs non-functional requirements; constraints; worked examples
  in sensor monitoring (civil/environmental domain)
- Slides 6–7: Stakeholder perspectives — structural engineer, facility manager,
  regulatory inspector each need different things from the same system
- Slides 8–9: Quality criteria — measurable acceptance conditions: "response < 2s",
  "handles 1M records", "output matches IFC schema"
- Slide 10: User story format — as a [facility manager], I want [sensor alert
  dashboard] so that [I can respond before an SLA breach]
- Slides 11–12: Requirement → prompt — user story converted step-by-step into a
  Claude Code prompt using the structure from `01c_AgentischesProgrammieren`
- Slides 13–14: Requirement → test — same user story converted into a unit test
  (motivates `08a_UnitTest` in S08)
- Slide 15: Traceability triangle: requirement ↔ test ↔ prompt; changing one must
  trigger updating the others

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- Requirements formalize the "prompt" step; unit tests formalize the "verify" step.
  This lecture makes the connection explicit.

**Symbols to add**: 📋 on every requirements slide; 🔍 on test-traceability slides.

**Cross-references**:
- → `01c_AgentischesProgrammieren` (S01): prompt structure applied here
- → `03c_Softwareentwurf` (S03): requirements precede design
- → `04b_Programmablauf` (S04): flowcharts operationalize requirements
- → `08a_UnitTest` (S08): test-driven prompting is the "verify" step

---

### 04b_Programmablauf

**Block**: Block 2 — Computational Engineering | **Session**: S04
**Status**: MOVED from Block 3 + REFRAMED | **Primary symbols**: 📋 ⚙ 🔄
**Source file**: `oldx/05b_Programmablauf.qmdx`

#### Summary: Program Flow

Introduces flowcharts as pre-implementation design artifacts. Reframed: flowcharts
are the blueprint from which a prompt is constructed. "Design the flowchart, then
write the prompt" is the key message.

#### Main topics

- Flowchart symbols: start/end, processing, decision, subroutine
- Function flow and problem decomposition
- Common flowchart errors and interpretation exercises
- **[ADDED]** "Flowcharts as Prompts" — translating a flowchart into an AI prompt

#### Key takeaways

- Flowcharts reveal logic gaps before implementation, when they are cheap to fix.
- A flowchart with clear decision nodes translates directly into a structured prompt.
- Every decision diamond becomes a conditional requirement in the prompt.

#### Change Notes

**Content to ADD**:
- "Flowcharts as Prompts" section (~4 slides): take a concrete flowchart (inspection
  decision procedure) and convert it step-by-step into a Claude Code prompt. Each
  decision diamond → a conditional in the prompt.
- Group exercise reference: exercises directory has a role-based exercise where
  students design a flowchart together before prompting.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Flowcharts visualize code" → "Flowcharts are the design artifact you create before
  writing the prompt."

**Agentic workflow integration**:
- A well-drawn flowchart eliminates ambiguity from the prompt and reduces verify-
  iterate cycles.

**Symbols to add**: 📋 on requirements-to-flowchart slide; ⚙ on function flow;
🔄 on "flowchart to prompt" exercise.

**Cross-references**:
- → `04a_Anforderungen` (S04): requirements generate the flowchart
- → `01c_AgentischesProgrammieren` (S01): prompt structure applied here

---

### 04c_Objects — Design Concept View

**Block**: Block 2 — Computational Engineering | **Session**: S04
**Status**: MOVED (design concept view only) | **Primary symbols**: ○ ⇄ 📋
**Source file**: `oldx/04c_Objects.qmdx` (first appearance; design concept slides only)

> `04c_Objects.qmdx` appears in TWO sessions. This entry covers the design concept
> view in S04. The Python implementation view is in Session 06.

#### Summary: Object Design (Conceptual View)

Uses `04c_Objects` to present OO thinking as a decomposition strategy, not a Python
feature. Students identify entities in an engineering domain, define attributes and
responsibilities, and express relationships using UML class diagrams — before any
Python syntax. "Design before you prompt."

#### Main topics

- OO design as domain decomposition
- Classes as named structures with attributes and responsibilities
- Associations, aggregation, composition
- Worked example: BIM element hierarchy (Building → Floor → Room → Window)
- **[ADDED]** UML class diagram as the design artifact for an AI prompt

#### Key takeaways

- Classes are design units before they are Python constructs.
- A UML class diagram is the specification you give to an AI; the AI generates the
  Python class; the engineer verifies against the diagram.
- Object relationships must be explicit in the design or the AI will invent them.

#### Change Notes

**Content to ADD**:
- Framing as design concept (~2 slides): "We are not learning Python syntax yet.
  We are learning to think in objects."
- "Design before you prompt" section (~3 slides): UML class diagram → structured
  prompt → AI generates Python class → verify against diagram.
- Connect to UML notation introduced in `03c_Softwareentwurf` (S03).

**Content to REMOVE or REDUCE**:
- For this view: REDUCE Python syntax slides to near zero — move to S06 implementation
  view. Keep only conceptual slides: entities, attributes, relationships, UML.

**Content to REFRAME**:
- "Here is how Python classes work" → "Here is how we decompose a domain into named
  structures before any code is written."

**Agentic workflow integration**:
- UML diagram = "prompt" step for object design: diagram → AI generates → verify
  class matches diagram.

**Symbols to add**: ○ on class/entity symbols; ⇄ on relationship arrows;
📋 on "design before prompt" slide.

**Cross-references**:
- → `03c_Softwareentwurf` (S03): UML notation introduced there
- → `04c_Objects` implementation view (S06): Python syntax for same concepts
- → `08a_UnitTest` (S08): tests verify implemented class matches design

---

## Block 3 — Programming Foundations (Sessions 05–06)

*Key question: How does the machine execute our intent?*
*All examples are AI-generated code to read and verify. Programming concepts are
motivated by computational need, not syntax-first.*

---

### 05a_Operatoren

**Block**: Block 3 — Programming Foundations | **Session**: S05
**Status**: REFRAMED | **Primary symbols**: □ ≡
**Source file**: `oldx/03a_Operatoren.qmdx`

#### Summary: Operators

Covers Python operators — arithmetic, comparison, logical, bitwise. Examples are
reframed as "AI-generated code to read" rather than "code to write." Operator
precedence is motivated by the need to trace AI expressions before accepting them.

#### Main topics

- Arithmetic, assignment, comparison, identity, membership operators
- Logical and bitwise operators; operator overloading
- **[ADDED]** "Read from AI output" labeling on examples
- **[ADDED]** Trace-this-expression exercise on AI-generated code

#### Key takeaways

- Understanding operator precedence is essential for tracing AI-generated expressions.
- Type mismatches in operator use are a common AI code error.

#### Change Notes

**Content to ADD**:
- "Read from AI output" labels: mark examples as "this is what AI generated — trace
  it before running."
- Trace-this-expression exercise (~2 slides): complex AI-generated expression,
  students evaluate step-by-step on paper before running.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Learn to write expressions" → "Learn to read and trace expressions — then verify
  AI output."

**Agentic workflow integration**:
- "When AI generates `if not x is None and x > 0.0:` — trace before you trust."

**Symbols to add**: □ on variable introduction; ≡ on type-specific operator slides.

**Cross-references**:
- → `02c_Datentypen` (S02): operator behavior depends on type
- → `05b_Verzweigung` (S05): operators in conditional expressions

---

### 05b_Verzweigung

**Block**: Block 3 — Programming Foundations | **Session**: S05
**Status**: REFRAMED | **Primary symbols**: 🔍 □
**Source file**: `oldx/03a_Verzweigung.qmdx`

#### Summary: Branching

Introduces conditional branching. Adds branch-reading strategy: students mentally
walk through AI-generated `if`/`elif`/`else` blocks to identify which branch executes
under which condition. Structural engineering threshold classifier replaces abstract
examples.

#### Main topics

- `if`, `else`, `elif`; nested and multi-way branching
- **[ADDED]** Branch-reading strategy for AI-generated code
- **[ADDED]** AI-generated threshold classifier (structural stress: OK/Warning/Critical)

#### Key takeaways

- For AI-generated branching: identify conditions, trace branches, list missing cases.
- Writing one test per branch is the minimum for verifying conditional logic.

#### Change Notes

**Content to ADD**:
- Branch-reading strategy (~2 slides): "For every `if` block: (1) identify the
  condition, (2) identify branches, (3) list inputs triggering each branch, (4) check
  for missing cases (None, negative values)."
- Threshold-classifier example (~3 slides): AI-generated `classify_stress()` for
  structural stress levels. Students trace each branch, then write one unit test per
  branch.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Write conditional logic" → "Read conditional logic: trace branches, find missing
  cases."

**Agentic workflow integration**:
- "Before accepting AI branching logic: trace every branch manually, check for
  missing cases, write a test for each branch."

**Symbols to add**: 🔍 on branch-reading strategy; □ on Boolean variable slides.

**Cross-references**:
- → `05a_Operatoren` (S05): Boolean operators used in conditions
- → `08a_UnitTest` (S08): "one test per branch" rule formalised there

---

### 05c_Schleifen

**Block**: Block 3 — Programming Foundations | **Session**: S05
**Status**: REFRAMED | **Primary symbols**: 📂 🔄
**Source file**: `oldx/03b_Schleifen.qmdx`

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

---

### 06a_Funktionen

**Block**: Block 3 — Programming Foundations | **Session**: S06
**Status**: REFRAMED | **Primary symbols**: ⚙ 📋
**Source file**: `oldx/04a_Funktionen.qmdx`

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

---

### 06b_Objects — Implementation View

**Block**: Block 3 — Programming Foundations | **Session**: S06
**Status**: REFRAMED (implementation view) | **Primary symbols**: ○ ⇄ ⚙
**Source file**: `oldx/04c_Objects.qmdx` (second appearance; implementation slides only)

> Second appearance of `04c_Objects.qmdx`. Design concept view was in S04.
> This entry covers Python implementation.

#### Summary: Python Classes (Implementation View)

Connects the UML class diagram from S03/S04 to Python syntax. Students who have
already designed a class on paper now see how `class`, `__init__`, `self`, and
methods implement that design. The BIM example from S04 reappears as a complete
Python class.

#### Main topics

- `class`, `__init__`, `self`; instance and class attributes; methods
- References between objects (implementing associations); encapsulation; inheritance
- **[ADDED]** UML from S04 mapped to Python syntax
- **[ADDED]** Common AI OOP mistakes
- **[ADDED]** Code understanding questionnaire

#### Key takeaways

- Python class syntax implements UML design decisions made in S04.
- AI often conflates class and instance attributes, misuses `self`, or ignores
  encapsulation.
- Verifying a class means checking it against its design diagram, not just running it.

#### Change Notes

**Content to ADD**:
- UML → Python mapping (~3 slides): class name → `class Name:`, attribute →
  `self.attr`, method → `def method(self):`, association → instance attribute.
- BIM worked example continuation (~3 slides): `Room` class from S04 UML diagram →
  AI generates Python class → verify each attribute and method against diagram.
- Common AI OOP mistakes (~2 slides): mutable default in `__init__`; missing `self`;
  `cls` used where `self` was intended.
- Code understanding questionnaire (~1 slide): "What does this class model?",
  "Which requirement does it implement?", "What could fail?"

**Content to REMOVE or REDUCE**:
- Design-concept motivation slides already covered in S04 — do not repeat; jump
  directly to Python syntax.

**Content to REFRAME**:
- "Learn to write Python classes" → "Translate your UML design into Python; verify
  the translation is faithful."

**Agentic workflow integration**:
- "Prompt: 'Implement the Room class from this UML diagram.' → verify each attribute
  exists, each method signature matches, encapsulation is respected."

**Symbols to add**: ○ on class/entity slides; ⇄ on association implementation;
⚙ on method definition slides.

**Cross-references**:
- → `04c_Objects` design view (S04): design artifacts used here
- → `06c_Module` (S06): classes organized into modules
- → `08b_CodeReview` (S08): OOP best practices in the review checklist

---

### 06c_Module

**Block**: Block 3 — Programming Foundations | **Session**: S06
**Status**: REFRAMED | **Primary symbols**: 📂 ⚙
**Source file**: `oldx/07a_Module.qmdx`

#### Summary: Modularization

Explains how Python programs are organized across files, modules, and packages.
Reframed: modules are the granularity at which AI generates code. Understanding the
import system helps students evaluate whether an AI-generated module fits their
project structure.

#### Main topics

- Files, modules, packages; standard library and external packages; `main()` pattern
- **[ADDED]** Modules as the unit of AI code generation
- **[ADDED]** "Prompt for a module" demo

#### Key takeaways

- AI generates code at module granularity — knowing how modules work helps you prompt
  and evaluate AI output.
- Module boundaries are architecture boundaries.

#### Change Notes

**Content to ADD**:
- "Modules as AI generation units" (~2 slides): when you prompt for "a module that
  processes sensor data," the expected output is a `.py` file with a clear interface.
- "Prompt for a module" demo (~2 slides): live prompt → AI generates
  `sensor_processing.py` → students verify the interface matches the requirement.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Organize your code into files" → "Structure your project so AI output lands in the
  right place; module boundaries are architecture boundaries."

**Agentic workflow integration**:
- "When AI generates a module, check: Is the public interface what you specified?
  Are internal helpers private? Does the module import only what it needs?"

**Symbols to add**: 📂 on module structure diagrams; ⚙ on function interface slides.

**Cross-references**:
- → `04c_Objects` impl view (S06): classes organized into modules
- → `08b_CodeReview` (S08): module structure is part of the review checklist

---

## Block 4 — Verification & Quality (Sessions 07–08)

*Key question: How do we know the solution is correct?*

---

### 07a_Exceptions

**Block**: Block 4 — Verification & Quality | **Session**: S07
**Status**: REFRAMED | **Primary symbols**: 🔍
**Source file**: `oldx/06a_Exceptions.qmdx`

#### Summary: Exceptions

Explains Python exception handling. Opens with "you ran AI code and got TypeError."
Exceptions are reframed as contract violations that reveal incorrect assumptions in
AI-generated code. The call stack trace becomes a diagnostic tool.

#### Main topics

- Error types: lexical, syntactic, semantic; exception handling; custom exceptions
- Exception propagation through the call stack
- **[ADDED]** Exceptions as AI contract violations
- **[ADDED]** Call stack trace as a diagnostic tool; guard clause pattern

#### Key takeaways

- Exceptions reveal that an AI assumption was wrong — they are diagnostic information.
- Reading a traceback means reading the call stack frozen at the moment of failure.
- Guard clauses prevent exceptions by checking preconditions before risky operations.

#### Change Notes

**Content to ADD**:
- Opening scenario (~2 slides): "You ran 200 lines of AI code. TypeError: unsupported
  operand type NoneType + float. Walk through the traceback, identify the faulty
  assumption, add a guard clause."
- Guard clause pattern (~2 slides): "AI often omits precondition checks before risky
  operations (division, attribute access). Add them."
- Call stack as diagnostic (~2 slides): traceback = call stack frozen at failure;
  read top-to-bottom to reveal execution path.

**Content to REMOVE or REDUCE**:
- Reduce debugging content here — `07b_Debugging` (same session) covers it in depth.

**Content to REFRAME**:
- "Exceptions signal errors" → "Exceptions signal that an AI assumption was
  incorrect; the traceback tells you which assumption."

**Agentic workflow integration**:
- "When AI code throws an exception: (1) read traceback, (2) identify failed
  assumption, (3) add guard clause or fix data, (4) reprompt with constraint explicit."

**Symbols to add**: 🔍 on traceback analysis slides.

**Cross-references**:
- → `07b_Debugging` (S07): debugging tools for the same error
- → `08a_UnitTest` (S08): tests catch exception cases before production

---

### 07b_Debugging

**Block**: Block 4 — Verification & Quality | **Session**: S07
**Status**: REFRAMED | **Primary symbols**: 🔍
**Source file**: `oldx/06c_Debugging.qmdx`

#### Summary: Debugging

Debugging techniques reframed around AI code. Opens with "200 lines of AI code,
wrong output." Introduces a 5-step AI debugging strategy. VS Code debugger walkthrough
expanded to cover multi-function AI modules.

#### Main topics

- `print()`, `logging`; graphical debugger; Jupyter in VS Code
- **[ADDED]** 5-step AI debugging strategy
- **[ADDED]** Multi-function AI module debugger walkthrough

#### Key takeaways

- Debugging AI code: reproduce → isolate → hypothesize → inspect → fix → re-verify.
- The graphical debugger is more powerful than `print()` for multi-function AI modules.
- Static reasoning alone is insufficient — execution observation is required.

#### Change Notes

**Content to ADD**:
- Opening scenario (~1 slide): "200 lines of AI code. Wrong output. No exception.
  Where do you start?"
- 5-step AI debugging strategy (~5 slides): (1) Reproduce with minimal input,
  (2) Isolate failing function with a unit test, (3) Hypothesize which assumption is
  wrong, (4) Inspect execution state with debugger, (5) Fix and re-verify.
- Multi-function module walkthrough (~4 slides): set breakpoint at entry, step through
  calls, inspect state at each level.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here are debugging tools" → "Here is a systematic strategy for debugging AI code;
  these tools implement the strategy."

**Agentic workflow integration**:
- Debugging is the "verify" step applied at execution level.

**Symbols to add**: 🔍 on every debugging strategy slide.

**Cross-references**:
- → `07a_Exceptions` (S07): exceptions are the starting point for debugging
- → `08a_UnitTest` (S08): isolating with a unit test is step 2 of the strategy

---

### 08a_UnitTest

**Block**: Block 4 — Verification & Quality | **Session**: S08
**Status**: EXPANDED | **Primary symbols**: 🔍 📋
**Source file**: `oldx/06b_UnitTest.qmdx`

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

---

### 08b_CodeReview

**Block**: Block 4 — Verification & Quality | **Session**: S08
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔍 📋 ⇄
**Source file**: NEW — create `08b_CodeReview.qmdx`

#### Summary: Code Review of AI-Generated Code

New lecture introducing code review as the final verification step before accepting
AI-generated code. Three review dimensions: requirement review (does the code do
what was asked?), design review (does it follow the architecture?), and
implementation review (is it correct, safe, maintainable?). An AI-specific
evaluation checklist is the practical output.

#### Main topics

- What code review is; why it is mandatory for AI output
- Requirement review: does the code match functional requirements?
- Design review: does it match the UML design and module structure?
- Implementation review: type safety, error handling, performance
- AI hallucinations and incomplete implementations
- AI evaluation checklist

#### Key takeaways

- Review standard is the requirement and the design — same as for human code.
- Common AI failure modes: hallucinated function calls, missing edge cases, incorrect
  type assumptions, over-engineered solutions.
- A structured checklist reduces cognitive load when reviewing unfamiliar AI code.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Why review AI code — "AI is confident but not always correct."
- Slides 3–4: Requirement review — for each functional requirement: is it
  implemented? Does a test exist? Does it pass?
- Slides 5–6: Design review — module structure matches architecture? Class interfaces
  match UML design?
- Slides 7–9: Implementation review — scan for: hardcoded values, missing type
  annotations, unsafe operations (division without zero-check), mutable defaults,
  missing `return` statements
- Slides 10–11: AI hallucination patterns — calling nonexistent functions, importing
  nonexistent modules, incorrect API usage, unnecessary abstractions
- Slides 12–14: AI evaluation checklist: □ requirement coverage □ design match
  □ type correctness □ edge cases □ error handling □ no hallucinated calls
  □ test suite passes
- Slide 15: Code review is the final "verify" step; if review fails, iterate

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- Code review is the formalized "verify" step. This lecture gives it a checklist
  and a process.

**Symbols to add**: 🔍 on review activity slides; 📋 on checklist slides;
⇄ on design match slides.

**Cross-references**:
- → `08a_UnitTest` (S08): tests are automated part of review; manual review covers
  what tests can't
- → `04a_Anforderungen` (S04): requirements are the review standard
- → `03c_Softwareentwurf` (S03): design is the second review standard

---

## Block 5 — Problem Classes (Sessions 09–11)

*Key question: What type of problem am I solving?*
*Most domain-relevant block. Each session organizes around a real problem class —
algorithms and data structures emerge from the domain, not from abstract CS theory.*

---

### 09a_Algorithmen

**Block**: Block 5 — Problem Classes | **Session**: S09
**Status**: MOVED from Block 3 + REFRAMED | **Primary symbols**: 🔄 📂
**Source file**: `oldx/05c_Algorithmen.qmdx`

#### Summary: Algorithms

Surveys algorithmic ideas. Moved to Block 5 and reframed: "identify the problem
class first, then choose the algorithm family." The emphasis shifts from "here is
how bubble sort works" to "how do I know which algorithm to ask for?"

#### Main topics

- Trees; sorting (bubble, quicksort, insertion); searching (list, set, BST);
  binary search; performance (Big-O conceptually); heuristics; A* search
- **[ADDED]** Algorithm recognition strategy
- **[ADDED]** AI and algorithm selection

#### Key takeaways

- The problem class determines the algorithm family; identify the class first.
- AI defaults to adequate-but-not-optimal algorithms — knowing the class lets you
  guide the AI.

#### Change Notes

**Content to ADD**:
- "Algorithm Recognition" exercise (~3 slides): given a problem description, identify
  the class (search, sort, path, partition) before looking at any algorithm. Practice
  with 4 engineering scenarios.
- "AI and Algorithm Selection" (~2 slides): AI defaults to linear search or bubble
  sort unless specified. Knowing the class lets you prompt "use Dijkstra" and verify
  the AI used the correct algorithm.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here are the major algorithms" → "Here is how to recognize which algorithm class
  your problem belongs to."

**Agentic workflow integration**:
- "Before prompting: identify the problem class. Include it in the prompt:
  'implement a binary search for this sorted list.' Verify the AI used it."

**Symbols to add**: 🔄 on algorithm pattern slides; 📂 on data structure slides.

**Cross-references**:
- → `09b_Rekursion` (S09): recursion as divide-and-conquer strategy
- → `10a_Graphprobleme` (S10): graph algorithms as a problem class

---

### 09b_Rekursion

**Block**: Block 5 — Problem Classes | **Session**: S09
**Status**: MOVED from Block 3 + REFRAMED | **Primary symbols**: 🔄
**Source file**: `oldx/04b_Rekursion.qmdx`

#### Summary: Recursive Functions

Moved to Block 5 and reframed as a divide-and-conquer strategy, not a Python
language feature. Stack/heap content is removed — that is now in `02b_Speicher`
(S02). Engineering examples from BIM hierarchy traversal and spatial subdivision
replace the canonical factorial.

#### Main topics

- Recursion as divide-and-conquer; recursive functions; base case and recursive case
- Preventing infinite recursion
- **[REMOVED]** Stack/heap content → moved to S02
- **[ADDED]** BIM hierarchy traversal; spatial subdivision; recursion vs iteration

#### Key takeaways

- Recursion is a strategy for problems that decompose into smaller same-type instances.
- BIM models and spatial trees are natural recursive structures in civil engineering.
- Students already understand the call stack from `02b_Speicher` (S02).

#### Change Notes

**Content to ADD**:
- Divide-and-conquer framing (~2 slides): recursion is a strategy; problems that
  decompose into smaller same-type problems are candidates.
- BIM hierarchy traversal (~3 slides): Building → Floors → Rooms → Elements; each
  level delegates to the same function. AI generates; students verify base case and
  recursive step.
- Spatial subdivision example (~2 slides): quadtree for geographic data.
- Recursion vs iteration comparison (~2 slides): when each is appropriate; stack depth
  constraints.

**Content to REMOVE or REDUCE**:
- REMOVE stack/heap content: now in `02b_Speicher` (S02). Only reference:
  "You already understand the call stack from Session 02."
- REDUCE factorial example: keep as minimal intro; engineering examples are primary.

**Content to REFRAME**:
- "Recursion is how Python handles self-reference" → "Recursion is a divide-and-
  conquer strategy for hierarchical engineering data."

**Agentic workflow integration**:
- "When AI generates a recursive function: verify base case, trace first two recursive
  calls, check stack depth for expected input size."

**Symbols to add**: 🔄 on divide-and-conquer diagram.

**Cross-references**:
- → `02b_Speicher` (S02): call stack explained there — reference, don't repeat
- → `09a_Algorithmen` (S09): recursion as a divide-and-conquer algorithm strategy

---

### 10a_Graphprobleme

**Block**: Block 5 — Problem Classes | **Session**: S10
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📂 ⇄
**Source file**: NEW — create `10a_Graphprobleme.qmdx`

#### Summary: Graph Problems

New lecture on graph problems as a problem class. Transportation networks, utility
networks, and routing are the domain examples — all directly relevant to civil and
environmental engineering. Students learn to recognize a graph problem, represent it
as a data structure, and select the appropriate algorithm family.

#### Main topics

- Graph problems in engineering: transport networks, utility networks, routing, flow
- Graph data structure: nodes, edges, weights, direction
- Traversal: BFS and DFS (conceptually)
- Shortest path: Dijkstra's algorithm (conceptually)
- `networkx` library demo
- AI prompt pattern for graph problems

#### Key takeaways

- Many civil engineering problems are graph problems in disguise.
- The graph representation determines which algorithms are efficient.
- AI generates graph traversal code correctly when you specify the representation and
  algorithm family.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem class introduction — what makes a problem a graph problem?
  (entities with relationships that can be traversed)
- Slides 3–4: Civil engineering examples — road network (routing), pipe network
  (flow), building floor plan (connectivity), drainage network (directed flow)
- Slides 5–6: Graph data structure — nodes (intersections), edges (roads/pipes),
  weights (length/capacity), direction
- Slides 7–8: BFS for shortest hop count (flood extent from source); DFS for
  reachability (connected network components)
- Slides 9–10: Dijkstra's algorithm — shortest weighted path; evacuation route with
  travel times
- Slides 11–12: `networkx` demo — create road network, run `shortest_path()`,
  visualize
- Slides 13–14: AI prompt pattern — "Given a weighted directed graph representing
  [pipe network], implement [Dijkstra] using `networkx`. Nodes have [demand]; edges
  have [diameter, length]."
- Slide 15: Verification checklist — correct graph type (directed/undirected),
  weights present, algorithm matches problem class

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Recognize graph → specify representation → include algorithm family in prompt →
  verify graph type and weights → run on test case."

**Symbols to add**: ⇄ on relationship/edge diagrams; 📂 on data structure slides;
🔄 on traversal/algorithm slides.

**Cross-references**:
- → `09a_Algorithmen` (S09): algorithm recognition strategy applied here
- → `10b_Geometrieprobleme` (S10): geometry complements graph problems in spatial
  engineering

---

### 10b_Geometrieprobleme

**Block**: Block 5 — Problem Classes | **Session**: S10
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📂 ⇄
**Source file**: NEW — create `10b_Geometrieprobleme.qmdx`

#### Summary: Geometric Problems

New lecture on geometric problems as a problem class. CAD, BIM, and GIS are all
geometric domains. Students learn the problem class signature, relevant data
structures, and the `shapely` library.

#### Main topics

- Geometric problems in engineering: CAD, BIM, GIS, spatial relationships
- Vector algebra basics: point, line, polygon, vector operations
- Point-in-polygon, distance, intersection, area
- Coordinate systems and projections (briefly)
- `shapely` library demo
- AI prompt pattern for geometric problems

#### Key takeaways

- Geometric problems require specifying both representation and coordinate system.
- `shapely` implements most 2D geometric operations — AI can be prompted to use it;
  engineer verifies the geometry is correctly represented.
- Floating-point precision is a common source of errors in geometric AI code.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem class introduction — what makes a problem geometric?
- Slides 3–4: Civil engineering examples — building footprint analysis, structural
  member intersections, flood zone delineation, road alignment geometry
- Slides 5–6: Vector algebra — point as (x,y,z), line segment, polygon as ordered
  point list, distance, cross product for orientation
- Slides 7–8: Key operations — point-in-polygon (sensor inside zone?), distance
  (nearest facility), intersection (pipe collision?)
- Slides 9–10: `shapely` demo — create building polygon, buffer, containment check
- Slides 11–12: Coordinate systems — why projections matter (WGS84 vs local CRS);
  common AI omission
- Slides 13–14: AI prompt pattern — "Given building polygons in WGS84, return all
  buildings within 500m of a given point. Use `shapely`."
- Slide 15: Verification checklist — geometry type, CRS specified, floating-point
  tolerance for equality checks

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Recognize geometry → specify representation and CRS → verify geometry type →
  test with known spatial relationship."

**Symbols to add**: ⇄ on spatial relationship diagrams; 📂 on data structure slides;
🔄 on algorithm slides.

**Cross-references**:
- → `10a_Graphprobleme` (S10): spatial networks combine graphs and geometry
- → `11a_Raster_Simulation` (S11): raster is the alternative spatial representation

---

### 11a_Raster_Simulation

**Block**: Block 5 — Problem Classes | **Session**: S11
**Status**: NEW (~20–30 min, ~18 slides) | **Primary symbols**: 🔄 📂
**Source file**: NEW — create `11a_Raster_Simulation.qmdx`

#### Summary: Raster Problems

New lecture on raster data as a problem class. Environmental models, climate grids,
terrain analysis, and remote sensing are raster problems — directly relevant to
environmental engineering. Students learn what makes a problem a raster problem,
how grids are represented as arrays, and what grid-based analysis looks like.

#### Main topics

- Raster problems: terrain, climate grids, land cover, remote sensing
- Grid as data structure: 2D numpy array, cell size, extent, NoData
- Grid analysis: overlay, reclassification, zonal statistics
- `numpy` for grid operations; `matplotlib` for visualization
- AI prompt pattern for raster problems

#### Key takeaways

- A raster represents continuous spatial phenomena discretized to a grid — resolution
  is a modeling choice.
- Most raster operations are element-wise or neighborhood operations on 2D arrays.
- AI generates correct array operations but often ignores resolution, extent, or
  NoData handling — verify the metadata.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem class introduction — continuous field discretized to grid
- Slides 3–4: Environmental examples — digital terrain model, land cover
  classification, precipitation grid, air pollution concentration
- Slides 5–6: Grid data structure — 2D numpy array, cell size, extent, CRS (brief),
  NoData values
- Slides 7–9: Grid operations — reclassification (threshold to binary mask), overlay
  (multiply grids), zonal statistics (mean elevation within polygon zone)
- Slides 10–12: numpy demo — load terrain grid, compute slope, apply flood threshold
  mask, visualize
- Slides 13–14: Metadata pitfalls — AI generates correct array math but forgets:
  cell size match, extent alignment, NoData handling. Failing example shown.
- Slides 15–16: AI prompt pattern — "Given a 2D numpy array representing [soil
  moisture] with cell size [50m] and NoData [-9999], return fraction of cells above
  threshold t."
- Slides 17–18: Verification checklist — shape matches extent, NoData excluded,
  units correct, output type matches requirement

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Recognize raster → specify shape, cell size, NoData in prompt → verify extent and
  metadata → test on small synthetic array."

**Symbols to add**: 📂 on data structure slides; 🔄 on grid operation slides.

**Cross-references**:
- → `10b_Geometrieprobleme` (S10): vector and raster are complementary representations
- → `11b_UIDesign` (S11): raster analysis results visualized in a dashboard

---

### 11b_UIDesign

**Block**: Block 5 — Problem Classes | **Session**: S11
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📂 🔍
**Source file**: NEW — create `11b_UIDesign.qmdx`

#### Summary: UI Design for Engineering Applications

New lecture introducing user interface design as an engineering output. A computation
result is only useful if it can be communicated. AI can generate UI scaffolding
(dashboards, forms); the engineer verifies that data is correctly mapped to the
display. Streamlit and Gradio are used as accessible tools for quick engineering UIs.

#### Main topics

- UI types: console, Jupyter notebook, Streamlit web app, Gradio, PDF report
- Design principles for engineering data presentation: clarity, units, meaningful
  labels
- Streamlit and Gradio for rapid prototyping
- AI-generated UI scaffolding: what AI does well, what the engineer must verify
- Worked example: sensor data monitoring dashboard
- Motivation for Block 6: UI needs persistent data at scale

#### Key takeaways

- The output format is part of the engineering solution.
- AI generates a working Streamlit skeleton; the engineer verifies that the data
  mapping is meaningful.
- Displaying incorrect data clearly is worse than correct data obscurely — data
  mapping is always the engineer's responsibility.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem context — "You computed contamination risk for 500 sites. Who
  sees the result, and how?"
- Slides 3–4: UI type taxonomy — console, Jupyter, Streamlit, Gradio, PDF; when each
  is appropriate
- Slides 5–6: Design principles — appropriate precision (units, significant figures);
  clarity (one chart = one message); meaningful labels (not "value_1" but "PM2.5
  [µg/m³]")
- Slides 7–9: Streamlit demo — AI generates basic dashboard: file upload → filter →
  plot → download. Show code, then verify: labels correct? Units displayed? Ranges
  meaningful?
- Slides 10–11: Gradio demo (brief): for interactive ML / simulation model interfaces
- Slides 12–13: AI-generated UI verification checklist — □ labels include units
  □ axis ranges meaningful □ color scale appropriate □ data correctly mapped
  □ error states handled
- Slides 14–15: Transition to Block 6 — "The dashboard works. But 10M records from
  files? We need databases."

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Prompt: 'Generate a Streamlit app displaying sensor time series from CSV with
  threshold slider.' → verify: correct column names, axis labels, threshold logic."

**Symbols to add**: 📂 on data mapping slides; 🔄 on workflow diagrams;
🔍 on UI verification checklist.

**Cross-references**:
- → `11a_Raster_Simulation` (S11): raster results visualized in a dashboard
- → `12a_Datenhaltung` (S12): data persistence motivates databases over files
- → `08b_CodeReview` (S08): UI code review follows same checklist principles

---

## Block 6 — Data Management (Sessions 12–13)

*Key question: How do we persist and scale information?*
*SQL is de-emphasized as a learning objective. Focus: information models, design,
normalization. AI generates SQL; students verify.*

---

### 12a_Datenhaltung

**Block**: Block 6 — Data Management | **Session**: S12
**Status**: REFRAMED | **Primary symbols**: 📂 🗄
**Source file**: `oldx/09_Datenhaltung.qmdx`

#### Summary: Working with Files

Covers persistent data storage through files and file systems. Opens with engineering
scenarios (sensor CSV, GeoJSON, BIM JSON) and adds an AI file-I/O verification
section: AI-generated file-reading code often makes incorrect assumptions about
encoding, delimiters, and structure.

#### Main topics

- Read, write, list, test, delete files; TXT/JSON/GeoJSON/XML/CSV; XLS/ZIP
- Storage hierarchy: CPU cache → RAM → SSD/HDD; file systems
- **[ADDED]** AI file-I/O verification

#### Key takeaways

- Different formats suit different tasks — format choice is a data modeling decision.
- AI-generated file reading often assumes UTF-8, comma delimiter, and flat structure —
  engineering data frequently violates these.

#### Change Notes

**Content to ADD**:
- Opening engineering scenarios (~2 slides): "Your monitoring station outputs CSV.
  Your GIS exports GeoJSON. Your BIM software exports IFC JSON. How do you read
  them?"
- AI file-I/O verification (~3 slides): common AI assumptions that break on
  engineering data — encoding, delimiter, header row, missing value encoding. Verify
  each with `pandas`.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Files are storage" → "Files are how engineering data arrives — the format is
  determined by the tool that produced it."

**Agentic workflow integration**:
- "When AI generates file-reading code: (1) check encoding, (2) check delimiter,
  (3) check header handling, (4) verify on small real sample before full dataset."

**Symbols to add**: 📂 on file structure/format slides; 🗄 on storage hierarchy.

**Cross-references**:
- → `12b_Datenbanktypen` (S12): file limitations motivate databases
- → `11b_UIDesign` (S11): data read from files powers the dashboard

---

### 12b_Datenbanktypen

**Block**: Block 6 — Data Management | **Session**: S12
**Status**: REFRAMED | **Primary symbols**: 🗄
**Source file**: `oldx/10a_Datenbanktypen.qmdx`

#### Summary: Database Types

Introduces databases and surveys the major families. Reframed around the motivation
"files aren't enough." Revision slides reviewing earlier topics removed. Database
type choice is motivated by the information model (problem class from Block 5).

#### Main topics

- File-based systems vs database systems; Codd's rules
- Relational, NoSQL (document, key-value, search, graph)
- Criteria for selecting a database type
- **[ADDED]** Information-model perspective on database type choice
- **[REMOVED]** Revision slides reviewing Vererbung and Agile

#### Key takeaways

- Databases manage data when files fail: scale, concurrency, integrity, query power.
- Match the database model to the information model — not to fashion.
- Graph DBs for network data; document DBs for BIM; relational for tabular.

#### Change Notes

**Content to ADD**:
- Information-model motivation (~2 slides): "Your Block 5 problem class guides the
  database type. Graph problem → graph DB. BIM document → document DB. Structured
  tabular → relational."

**Content to REMOVE or REDUCE**:
- REMOVE revision slides reviewing Vererbung (inheritance) and Agile — these review
  topics from earlier sessions and do not belong in a database introduction.

**Content to REFRAME**:
- "Here are database types" → "Choose the database model that matches your information
  model."

**Agentic workflow integration**:
- "When AI suggests a database technology: ask 'does this match our information
  model?' A graph problem in a relational database has an impedance mismatch."

**Symbols to add**: 🗄 on all database type slides.

**Cross-references**:
- → `12a_Datenhaltung` (S12): file limitations motivate databases
- → `12c_Datenbanken_Entwurf` (S12): design before implementation
- → `10a_Graphprobleme` (S10): graph DBs as the natural fit

---

### 12c_Datenbanken_Entwurf

**Block**: Block 6 — Data Management | **Session**: S12
**Status**: MOVED EARLIER (before relational/SQL) + EXPANDED | **Primary symbols**: ⇄ 🗄 📋
**Source file**: `oldx/11a_Datenbanken_Entwurf.qmdx`

#### Summary: Relational Database Design

Explains database design through entity-relationship modeling. Moved to S12 (before
any SQL content) to establish that design precedes implementation — consistent with
Block 2. An environmental monitoring ER example replaces abstract academic examples.
"ER Diagram to Prompt" section added.

#### Main topics

- Database design workflow: conceptual → logical → physical
- ER diagrams: entities, relationships, attributes, cardinalities
- Normalization; OO vs relational model comparison
- **[ADDED]** Environmental monitoring ER example (Stations/Sensors/Measurements)
- **[ADDED]** ER diagram → AI prompt

#### Key takeaways

- Good databases begin with conceptual modeling — like UML for software.
- ER diagrams are the information model; SQL tables are the implementation.
- AI generates CREATE TABLE from ER descriptions — design the ER, then verify the
  generated SQL matches it.

#### Change Notes

**Content to ADD**:
- Environmental monitoring ER example (~4 slides): "Stations have many Sensors.
  Sensors produce Measurements with timestamp, value, unit." Draw ER diagram →
  identify entities, attributes, relationships, cardinalities.
- "ER Diagram to Prompt" section (~3 slides): convert ER to a Claude Code prompt —
  list entities as bullet points, list relationships, specify constraints. AI generates
  SQL; student verifies against ER.
- Connect to UML from Block 2 (~1 slide): "ER diagrams and UML class diagrams serve
  the same purpose at different layers — both are information models."

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here is how to design a database" → "The ER diagram is the specification you give
  the AI; design before implementation."

**Agentic workflow integration**:
- "Design the ER first. Then prompt: 'Generate SQL CREATE TABLE statements for this
  ER: [description].' Verify: each entity → table, each FK → relationship, each
  cardinality → constraint."

**Symbols to add**: ⇄ on relationship/association diagrams; 🗄 on design slides;
📋 on "ER to prompt" slide.

**Cross-references**:
- → `03c_Softwareentwurf` (S03): UML introduced there — same modeling spirit
- → `13a_RelationaleDatenbanken` (S13): relational concepts implement the ER design
- → `13b_Datenbanken_SQL_Select` (S13): SQL queries work on tables designed here

---

### 13a_RelationaleDatenbanken

**Block**: Block 6 — Data Management | **Session**: S13
**Status**: REFRAMED | **Primary symbols**: 🗄
**Source file**: `oldx/10b_RelationaleDatenbanken.qmdx`

#### Summary: Relational Databases

Introduces core relational database concepts. Explicitly references the ER design
from Session 12. Adds a note on AI-generated SQL: AI produces syntactically correct
SQL but often lacks constraints — students verify.

#### Main topics

- Table structure, primary keys, foreign keys, integrity constraints
- SQLite example
- **[ADDED]** Connection to ER design from S12
- **[ADDED]** AI-generated SQL without constraints

#### Key takeaways

- Relational tables implement the ER entities and relationships from S12.
- AI often generates tables without NOT NULL or UNIQUE constraints — checking
  constraint coverage is a required review step.

#### Change Notes

**Content to ADD**:
- Connection to S12 ER (~2 slides): monitoring ER from S12 → relational tables. "The
  table is the implementation of the entity."
- AI SQL verification note (~2 slides): "AI generates syntactically correct SQL but
  often omits NOT NULL, UNIQUE, CHECK. Your ER specifies them — verify they appear."

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here are relational concepts" → "Relational tables implement your ER design;
  verify the implementation matches the design."

**Agentic workflow integration**:
- "AI generates CREATE TABLE. Verify: (1) all entities → tables, (2) all attributes
  → columns with correct types, (3) all FK relationships present, (4) all cardinality
  constraints expressed as NOT NULL or UNIQUE."

**Symbols to add**: 🗄 on all relational concept slides.

**Cross-references**:
- → `12c_Datenbanken_Entwurf` (S12): ER design implemented here
- → `13b_Datenbanken_SQL_Select` (S13): querying the tables defined here

---

### 13b_Datenbanken_SQL_Select

**Block**: Block 6 — Data Management | **Session**: S13
**Status**: REFRAMED + REDUCED | **Primary symbols**: 🗄 🔍
**Source file**: `oldx/10c_Datenbanken_SQL_Select.qmdx`

#### Summary: Analyzing Tables with SQL

SQL SELECT queries. SQL is framed explicitly as a tool — not a learning objective.
The learning objective is "verify that AI-generated SQL returns the expected result."
Depth in aggregation and complex joins is reduced.

#### Main topics

- Saving tables to SQLite with `pandas`; SELECT, WHERE, JOIN; aggregation (light)
- **[ADDED]** Prompting for SQL
- **[ADDED]** Verifying AI-generated SQL against expected results
- **[REDUCED]** Sorting, limiting, nested queries (reference only)

#### Key takeaways

- SQL is how you ask questions of a relational database — AI generates the query, you
  verify the result.
- SELECT, WHERE, JOIN cover the vast majority of engineering query needs.
- Verification: run the AI-generated SQL on a small known dataset and check the output
  matches expectations.

#### Change Notes

**Content to ADD**:
- "Prompting for SQL" pattern (~3 slides): specify schema (from S12–S13), desired
  result, conditions. "Given Stations/Sensors/Measurements, return all PM2.5 readings
  above 50 µg/m³ from the last 30 days, sorted by station."
- Verification approach (~2 slides): "Generate a small dataset where you know the
  expected output. Run the AI SQL on it. If output matches, the query is correct.
  Don't trust SQL by reading it."

**Content to REMOVE or REDUCE**:
- REDUCE aggregate functions: keep COUNT, SUM, AVG, MAX/MIN. Remove window functions,
  HAVING detail, GROUPING SETS.
- REDUCE sorting/limiting to one-slide reference. Remove subqueries, CTEs.

**Content to REFRAME**:
- "Learn SQL syntax" → "SQL is a tool; AI generates it; you verify the result against
  expected output."

**Agentic workflow integration**:
- "SQL is the 'generate' step output. Verification: does the result on a known dataset
  match what the requirement specifies?"

**Symbols to add**: 🗄 on SQL slides; 🔍 on verification slides.

**Cross-references**:
- → `12c_Datenbanken_Entwurf` (S12): schema designed there is queried here
- → `08a_UnitTest` (S08): verification approach mirrors unit testing

---

### 13c_Datenbanken_SQL_Create

**Block**: Block 6 — Data Management | **Session**: S13
**Status**: REFRAMED + REDUCED | **Primary symbols**: 🗄 🔍
**Source file**: `oldx/11b_Datenbanken_SQL_Create.qmdx`

#### Summary: Create Tables with SQL

Covers SQL DDL — creating and populating tables. Reframed as a verification step:
"does the AI-generated SQL match your ER design?" Learning objective is verification
of AI output against the ER, not DDL syntax mastery.

#### Main topics

- CREATE TABLE with types, constraints; PK, FK, NOT NULL, UNIQUE; INSERT
- Creating tables from existing data
- **[REDUCED]** ALTER TABLE, DROP TABLE (reference only)
- **[ADDED]** DDL as ER implementation verification checklist
- **[ADDED]** Alternative models for non-relational data

#### Key takeaways

- SQL DDL turns an ER design into a schema — AI generates DDL, engineer verifies
  against ER.
- Constraints not in the DDL are not enforced — every missing constraint is a data
  quality risk.
- For non-relational data (graph networks, BIM), SQL is not the right tool — match
  the tool to the information model.

#### Change Notes

**Content to ADD**:
- DDL as ER verification (~3 slides): checklist — □ each entity → CREATE TABLE
  □ each attribute → column with correct type □ each FK relationship → FOREIGN KEY
  □ each NOT NULL cardinality → NOT NULL constraint □ each uniqueness → UNIQUE
- Alternative models (~2 slides): "For road networks: graph DB. For BIM elements:
  document DB. SQL is not universal."

**Content to REMOVE or REDUCE**:
- REDUCE ALTER TABLE / DROP TABLE to one-slide reference.
- Remove schema evolution content — mention it exists; don't teach it.

**Content to REFRAME**:
- "Learn to create tables" → "Verify that AI-generated SQL correctly implements your
  ER design."

**Agentic workflow integration**:
- "AI generates CREATE TABLE. Walk through the DDL verification checklist against the
  ER diagram. If a constraint is missing, add it to the prompt and regenerate."

**Symbols to add**: 🗄 on DDL slides; 🔍 on verification checklist slide.

**Cross-references**:
- → `12c_Datenbanken_Entwurf` (S12): ER design is the specification for this DDL
- → `08b_CodeReview` (S08): DDL review follows the same checklist pattern

---

## Action Required Before Implementation

1. **Create `variable.svg`** in `lectures/_extensions/ai4sc-style/assets/icons/` —
   simple labeled box (□) representing a named memory location.
2. **Update `lectures/_toc.yaml`** to reorder entries to match the 13-session
   sequence above.
3. Consider adding `graph.svg` to the icons directory for Block 5 session headers.

## New Files to Create (8 total)

| File | Session | Purpose |
|------|---------|---------|
| `02b_Speicher.qmdx` | S02 | Memory model, stack/heap, references, visual diagrams |
| `01c_AgentischesProgrammieren.qmdx` | S01 | LLM basics, agentic workflow, prompt structure, code reading |
| `04a_Anforderungen.qmdx` | S04 | Requirements engineering, user stories, quality criteria |
| `10a_Graphprobleme.qmdx` | S10 | Graph problems — transport, utility networks, routing |
| `10b_Geometrieprobleme.qmdx` | S10 | Geometric problems — CAD, BIM, GIS, vector algebra |
| `11a_Raster_Simulation.qmdx` | S11 | Raster problems — environmental models, climate, remote sensing |
| `11b_UIDesign.qmdx` | S11 | UI types, visualization design, Streamlit/Gradio dashboards |
| `08b_CodeReview.qmdx` | S08 | Code review, requirement review, AI evaluation checklist |

## Files with Major Changes

| File | Key Change | Session |
|------|-----------|---------|
| `03c_Softwareentwurf.qmdx` | MOVED to S03; remove 6 revision slides; add agentic dev loop + UML | S03 |
| `09b_Rekursion.qmdx` | MOVED to S09; remove stack/heap (→ S02); reframe as divide-and-conquer | S09 |
| `02a_Computerhardware.qmdx` | EXPANDED; receive stack/heap from `09b`; add sequential execution model | S02 |
| `12c_Datenbanken_Entwurf.qmdx` | MOVED EARLIER to S12; add environmental ER example + ER-to-prompt | S12 |
| `04c_Objects.qmdx` | SPLIT VIEW: design concept (S04) + Python implementation (S06) | S04, S06 |
| `02c_Datentypen.qmdx` | MOVED from Block 2 to S02; reframe as memory representations | S02 |
