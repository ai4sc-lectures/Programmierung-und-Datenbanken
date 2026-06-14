# Task: 04b_Programmablauf

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../04b_Programmablauf.qmdx` |
| **Source file** | `../oldx/05b_Programmablauf.qmdx` |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S04 |
| **Status** | MOVED from Block 3 + REFRAMED |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Open the source file listed in the metadata above. Use the **Change Notes** to transform it — the **Summary**, **Main topics**, and **Key takeaways** give context.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../04b_Programmablauf.qmdx`

---

### 04b_Programmablauf

**Block**: Block 2 — Computational Engineering | **Session**: S04
**Status**: MOVED from Block 3 + REFRAMED | **Primary symbols**: 📋 ⚙ 🔄
**Source file**: `../oldx/05b_Programmablauf.qmdx`

#### Summary: Program Flow

Introduces flowcharts as pre-implementation design artifacts. Reframed: flowcharts
are the blueprint from which a prompt is constructed. "Design the flowchart, then
write the prompt" is the key message.

#### Main topics

- Flowchart symbols: start/end, processing, decision, subroutine
- Function flow and problem decomposition
- Common flowchart errors and interpretation exercises
- **[ADDED]** "Flowcharts as Prompts" — translating a flowchart into an AI prompt

#### Key takeaways

- Flowcharts reveal logic gaps before implementation, when they are cheap to fix.
- A flowchart with clear decision nodes translates directly into a structured prompt.
- Every decision diamond becomes a conditional requirement in the prompt.

#### Change Notes

**Content to ADD**:
- "Flowcharts as Prompts" section (~4 slides): take a concrete flowchart (inspection
  decision procedure) and convert it step-by-step into a Claude Code prompt. Each
  decision diamond → a conditional in the prompt.
- Group exercise reference: exercises directory has a role-based exercise where
  students design a flowchart together before prompting.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Flowcharts visualize code" → "Flowcharts are the design artifact you create before
  writing the prompt."

**Agentic workflow integration**:
- A well-drawn flowchart eliminates ambiguity from the prompt and reduces verify-
  iterate cycles.

**Symbols to add**: 📋 on requirements-to-flowchart slide; ⚙ on function flow;
🔄 on "flowchart to prompt" exercise.

**Cross-references**:
- → `04a_Anforderungen` (S04): requirements generate the flowchart
- → `01c_AgentischesProgrammieren` (S01): prompt structure applied here
