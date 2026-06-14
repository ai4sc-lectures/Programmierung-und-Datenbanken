# Task: 04b_Programmablauf

| Field | Value |
|-------|-------|
| **New file** | `../04b_Programmablauf.qmdx` |
| **Source file** | `../oldx/05b_Programmablauf.qmdx` |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S04 |
| **Status** | MOVED from Block 3 + REFRAMED |

> Open `../oldx/05b_Programmablauf.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
