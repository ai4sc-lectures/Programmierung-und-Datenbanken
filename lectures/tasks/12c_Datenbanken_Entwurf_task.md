# Task: 12c_Datenbanken_Entwurf

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../12c_Datenbanken_Entwurf.qmdx` |
| **Source file** | `../oldx/11a_Datenbanken_Entwurf.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S12 |
| **Status** | MOVED EARLIER (before relational/SQL) + EXPANDED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../12c_Datenbanken_Entwurf.qmdx`

---

### 12c_Datenbanken_Entwurf

**Block**: Block 6 — Data Management | **Session**: S12
**Status**: MOVED EARLIER (before relational/SQL) + EXPANDED | **Primary symbols**: ⇄ 🗄 📋
**Source file**: `../oldx/11a_Datenbanken_Entwurf.qmdx`

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
