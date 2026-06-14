# Task: 03c_Softwareentwurf

| Field | Value |
|-------|-------|
| **New file** | `../03c_Softwareentwurf.qmdx` |
| **Source file** | `../oldx/05a_Softwareentwurf.qmdx` |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S03 |
| **Status** | MOVED from Block 3 + EXPANDED |

> Open `../oldx/05a_Softwareentwurf.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 03c_Softwareentwurf

**Block**: Block 2 — Computational Engineering | **Session**: S03
**Status**: MOVED from Block 3 + EXPANDED | **Primary symbols**: 📋 ⇄ ⚙ 🔄
**Source file**: `../oldx/05a_Softwareentwurf.qmdx`

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
