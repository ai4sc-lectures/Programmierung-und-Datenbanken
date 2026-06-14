# Task: 13a_RelationaleDatenbanken

| Field | Value |
|-------|-------|
| **New file** | `../13a_RelationaleDatenbanken.qmdx` |
| **Source file** | `../oldx/10b_RelationaleDatenbanken.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S13 |
| **Status** | REFRAMED |

> Open `../oldx/10b_RelationaleDatenbanken.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
