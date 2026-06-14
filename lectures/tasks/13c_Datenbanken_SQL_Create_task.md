# Task: 13c_Datenbanken_SQL_Create

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../13c_Datenbanken_SQL_Create.qmdx` |
| **Source file** | `../oldx/11b_Datenbanken_SQL_Create.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S13 |
| **Status** | REFRAMED + REDUCED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../13c_Datenbanken_SQL_Create.qmdx`

---

### 13c_Datenbanken_SQL_Create

**Block**: Block 6 — Data Management | **Session**: S13
**Status**: REFRAMED + REDUCED | **Primary symbols**: 🗄 🔍
**Source file**: `../oldx/11b_Datenbanken_SQL_Create.qmdx`

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
