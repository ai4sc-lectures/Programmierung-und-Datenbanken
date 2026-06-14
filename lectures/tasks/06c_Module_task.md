# Task: 06c_Module

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../06c_Module.qmdx` |
| **Source file** | `../oldx/07a_Module.qmdx` |
| **Block** | Block 3 — Programming Foundations |
| **Session** | S06 |
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
   - `../06c_Module.qmdx`

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
