# Task: 12a_Datenhaltung

| Field | Value |
|-------|-------|
| **New file** | `../12a_Datenhaltung.qmdx` |
| **Source file** | `../oldx/09_Datenhaltung.qmdx` |
| **Block** | Block 6 — Data Management |
| **Session** | S12 |
| **Status** | REFRAMED |

> Open `../oldx/09_Datenhaltung.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
