# Task: 13c_Datenbanken_SQL_Create

| Field | Value |
|-------|-------|
| **New file** | `../13c_Datenbanken_SQL_Create.qmdx` |
| **Source file** | `../oldx/11b_Datenbanken_SQL_Create.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S13 |
| **Status** | REFRAMED + REDUCED |

> Open `../oldx/11b_Datenbanken_SQL_Create.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
