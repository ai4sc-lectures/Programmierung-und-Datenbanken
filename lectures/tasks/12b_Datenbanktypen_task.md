# Task: 12b_Datenbanktypen

| Field | Value |
|-------|-------|
| **New file** | `../12b_Datenbanktypen.qmdx` |
| **Source file** | `../oldx/10a_Datenbanktypen.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S12 |
| **Status** | REFRAMED |

> Open `../oldx/10a_Datenbanktypen.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
