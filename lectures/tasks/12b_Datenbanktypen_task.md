# Task: 12b_Datenbanktypen

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../12b_Datenbanktypen.qmdx` |
| **Source file** | `../oldx/10a_Datenbanktypen.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S12 |
| **Status** | REFRAMED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../12b_Datenbanktypen.qmdx`

---

### 12b_Datenbanktypen

**Block**: Block 6 — Data Management | **Session**: S12
**Status**: REFRAMED | **Primary symbols**: 🗄
**Source file**: `../oldx/10a_Datenbanktypen.qmdx`

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
