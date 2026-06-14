# Task: 06c_Module

| Field | Value |
|-------|-------|
| **New file** | `../06c_Module.qmdx` |
| **Source file** | `../oldx/07a_Module.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S06 |
| **Status** | REFRAMED |

> Open `../oldx/07a_Module.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 06c_Module

**Block**: Block 3 — Programming Foundations | **Session**: S06
**Status**: REFRAMED | **Primary symbols**: 📂 ⚙
**Source file**: `../oldx/07a_Module.qmdx`

#### Summary: Modularization

Explains how Python programs are organized across files, modules, and packages.
Reframed: modules are the granularity at which AI generates code. Understanding the
import system helps students evaluate whether an AI-generated module fits their
project structure.

#### Main topics

- Files, modules, packages; standard library and external packages; `main()` pattern
- **[ADDED]** Modules as the unit of AI code generation
- **[ADDED]** "Prompt for a module" demo

#### Key takeaways

- AI generates code at module granularity — knowing how modules work helps you prompt
  and evaluate AI output.
- Module boundaries are architecture boundaries.

#### Change Notes

**Content to ADD**:
- "Modules as AI generation units" (~2 slides): when you prompt for "a module that
  processes sensor data," the expected output is a `.py` file with a clear interface.
- "Prompt for a module" demo (~2 slides): live prompt → AI generates
  `sensor_processing.py` → students verify the interface matches the requirement.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Organize your code into files" → "Structure your project so AI output lands in the
  right place; module boundaries are architecture boundaries."

**Agentic workflow integration**:
- "When AI generates a module, check: Is the public interface what you specified?
  Are internal helpers private? Does the module import only what it needs?"

**Symbols to add**: 📂 on module structure diagrams; ⚙ on function interface slides.

**Cross-references**:
- → `04c_Objects` impl view (S06): classes organized into modules
- → `08b_CodeReview` (S08): module structure is part of the review checklist
