# Task: 13b_Datenbanken_SQL_Select

| Field | Value |
|-------|-------|
| **New file** | `../13b_Datenbanken_SQL_Select.qmdx` |
| **Source file** | `../oldx/10c_Datenbanken_SQL_Select.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S13 |
| **Status** | REFRAMED + REDUCED |

> Open `../oldx/10c_Datenbanken_SQL_Select.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 13b_Datenbanken_SQL_Select

**Block**: Block 6 — Data Management | **Session**: S13
**Status**: REFRAMED + REDUCED | **Primary symbols**: 🗄 🔍
**Source file**: `../oldx/10c_Datenbanken_SQL_Select.qmdx`

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
