# Task: 01b_Programmiersprachen + 01c_Programmiersprachen_ani

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New files** | `../01b_Programmiersprachen.qmdx` + `../01c_Programmiersprachen_ani.ipynb` |
| **Source files** | `../oldx/01d_Programmiersprachen.qmdx` + `../oldx/01d_Programmiersprachen_ani.ipynb` |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S01 |
| **Status** | REFRAMED |

## Instructions

1. Read `../lecture_skill/SKILL.md` — follow its conventions for layout, icons, Quarto syntax, and slide structure throughout.
2. Read the source file(s):
   - `../oldx/01d_Programmiersprachen.qmdx`
   - `../oldx/01d_Programmiersprachen_ani.ipynb`
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../01b_Programmiersprachen.qmdx`

---

### 01b_Programmiersprachen

**Block**: Block 1 — Computational Foundations | **Session**: S01
**Status**: REFRAMED | **Primary symbols**: ≡ 🔄
**Source file**: `../oldx/01d_Programmiersprachen.qmdx`, `../oldx/01d_Programmiersprachen_ani.ipynb`

#### Summary: Programming Languages

Overview of programming languages and their historical development. A new section
adds Python's position in the AI ecosystem: Python is the lingua franca of LLMs,
data science, and engineering automation — students learn Python because AI
generates Python.

#### Main topics

- Generations of programming languages; machine code → assembly → high-level
- Why new languages emerge; popularity trends
- Python as the primary course language
- **[ADDED]** Python in the AI ecosystem

#### Key takeaways

- Languages differ in abstraction level, usability, and domain fit.
- Python is emphasized because it is the dominant language in LLM training data and
  code output.
- Understanding Python is how you evaluate what the AI generates.

#### Change Notes

**Content to ADD**:
- "Python in the AI Ecosystem" section (~3 slides): Python dominates LLM training
  corpora; most AI-generated engineering code will be Python; language knowledge
  enables verification.
- include the visualization from `01d_Programmiersprachen_ani` in the redesign. it animates the pupularity of prgramming languages over time


**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- Language popularity trends → "why Python won in the AI era" — bridge the historical
  chart to current AI tooling.

**Agentic workflow integration**:
- Closing callout: "When you prompt Claude Code or Copilot, you will almost always
  receive Python. Understanding the language is how you evaluate the output."

**Symbols to add**: ≡ on the slide introducing Python types.

**Cross-references**:
- → `01c_Programmiersprachen_ani` (S01): companion notebook using Python
- → `01c_AgentischesProgrammieren` (S01): language knowledge enables code reading
