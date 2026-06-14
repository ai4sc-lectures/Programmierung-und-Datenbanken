# Task: 13b_Datenbanken_SQL_Select

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../13b_Datenbanken_SQL_Select.qmdx` |
| **Source file** | `../oldx/10c_Datenbanken_SQL_Select.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S13 |
| **Status** | REFRAMED + REDUCED |

## Instructions

1. Follow the `.qmdx` conventions in `CLAUDE.md` (auto-loaded — do not read any other files).
2. The **Summary**, **Main topics**, and **Key takeaways** sections below describe the existing content — do not open the source file.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../13b_Datenbanken_SQL_Select.qmdx`

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
