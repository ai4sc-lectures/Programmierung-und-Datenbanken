# Task: 12a_Datenhaltung

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../12a_Datenhaltung.qmdx` |
| **Source file** | `../oldx/09_Datenhaltung.qmdx` |
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
   - `../12a_Datenhaltung.qmdx`

---

### 12a_Datenhaltung

**Block**: Block 6 — Data Management | **Session**: S12
**Status**: REFRAMED | **Primary symbols**: 📂 🗄
**Source file**: `../oldx/09_Datenhaltung.qmdx`

#### Summary: Working with Files

Covers persistent data storage through files and file systems. Opens with engineering
scenarios (sensor CSV, GeoJSON, BIM JSON) and adds an AI file-I/O verification
section: AI-generated file-reading code often makes incorrect assumptions about
encoding, delimiters, and structure.

#### Main topics

- Read, write, list, test, delete files; TXT/JSON/GeoJSON/XML/CSV; XLS/ZIP
- Storage hierarchy: CPU cache → RAM → SSD/HDD; file systems
- **[ADDED]** AI file-I/O verification

#### Key takeaways

- Different formats suit different tasks — format choice is a data modeling decision.
- AI-generated file reading often assumes UTF-8, comma delimiter, and flat structure —
  engineering data frequently violates these.

#### Change Notes

**Content to ADD**:
- Opening engineering scenarios (~2 slides): "Your monitoring station outputs CSV.
  Your GIS exports GeoJSON. Your BIM software exports IFC JSON. How do you read
  them?"
- AI file-I/O verification (~3 slides): common AI assumptions that break on
  engineering data — encoding, delimiter, header row, missing value encoding. Verify
  each with `pandas`.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Files are storage" → "Files are how engineering data arrives — the format is
  determined by the tool that produced it."

**Agentic workflow integration**:
- "When AI generates file-reading code: (1) check encoding, (2) check delimiter,
  (3) check header handling, (4) verify on small real sample before full dataset."

**Symbols to add**: 📂 on file structure/format slides; 🗄 on storage hierarchy.

**Cross-references**:
- → `12b_Datenbanktypen` (S12): file limitations motivate databases
- → `11b_UIDesign` (S11): data read from files powers the dashboard
