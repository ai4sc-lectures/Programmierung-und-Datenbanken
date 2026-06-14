# Task: 13a_RelationaleDatenbanken

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../13a_RelationaleDatenbanken.qmdx` |
| **Source file** | `../oldx/10b_RelationaleDatenbanken.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S13 |
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
   - `../13a_RelationaleDatenbanken.qmdx`

---

### 13a_RelationaleDatenbanken

**Block**: Block 6 — Data Management | **Session**: S13
**Status**: REFRAMED | **Primary symbols**: 🗄
**Source file**: `../oldx/10b_RelationaleDatenbanken.qmdx`

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
