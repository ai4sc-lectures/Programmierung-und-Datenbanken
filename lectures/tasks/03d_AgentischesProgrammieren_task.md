# Task: 01c_AgentischesProgrammieren

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../01c_AgentischesProgrammieren.qmdx` |
| **Source file** | NEW — create `01c_AgentischesProgrammieren.qmdx` |
| **Block** | Block 1 — Computational Foundations |
| **Session** | S01 |
| **Status** | NEW (~20 min, ~15 slides) |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Create `../01c_AgentischesProgrammieren.qmdx` from scratch as a new `.qmdx` lecture file.
3. Use the **Change Notes** below as the complete content specification — they define every section, slide group, and callout to include.
4. Save the finished file to `../01c_AgentischesProgrammieren.qmdx`.

---

### 01c_AgentischesProgrammieren

**Block**: Block 1 — Computational Foundations | **Session**: S01
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📋 🔍
**Source file**: NEW — create `01c_AgentischesProgrammieren.qmdx`

#### Summary: Agentic Programming

New lecture that introduces the conceptual model and practical workflow for
AI-assisted programming. Explains how LLMs differ from deterministic programs, how
code is generated probabilistically, what the full agentic cycle looks like, and
what the engineer's responsibilities are. Placed in S01 so every subsequent lecture
can reference this foundation.

#### Main topics

- Deterministic programs vs probabilistic LLMs: token prediction
- How AI code generation differs from a database lookup or a compiler
- The agentic workflow cycle: prompt → generate → understand → verify → iterate
- Tool landscape: Claude Code, GitHub Copilot, Cursor
- Effective prompt structure: role / context / task / constraint / output format
- Code reading strategy: signature → docstring → tests → implementation
- Engineering responsibility: the engineer owns the requirement

#### Key takeaways

- LLMs generate plausible code, not guaranteed-correct code — verification is always
  required.
- A well-structured prompt is a form of requirements specification.
- The engineer's role shifts from author to architect, reviewer, and verifier.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slide 1: Title and position ("This is the core workflow for the whole course")
- Slides 2–4: LLM basics — token prediction, training on code corpora, why outputs
  are probabilistic; contrast with a database query (exact retrieval) or a compiler
  (deterministic transformation)
- Slide 5: Agentic cycle diagram — prompt → generate → understand → verify → iterate;
  each node labeled with the skill it requires
- Slides 6–7: Tool landscape — Claude Code (terminal/editor), GitHub Copilot (inline
  suggestion), Cursor (AI-first editor); what each is good for
- Slides 8–10: Prompt structure — worked example building step-by-step: role,
  context, task, constraint ("do not use external libraries"), output format
- Slides 11–12: Code reading strategy — signature and return type first, then
  docstring, then tests, only then implementation
- Slides 13–14: Engineering responsibility — "AI is your junior developer; you are
  the senior engineer who approves the design"
- Slide 15: Preview of how this cycle appears in each course block

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- This lecture defines the agentic cycle — it is the source all other files reference.

**Symbols to add**: 🔄 on cycle diagram; 📋 on prompt structure; 🔍 on code reading.

**Cross-references**:
- → `01a_Ueberblick` (S01): cycle introduced visually there, explained here
- → `04a_Anforderungen` (S04): requirements as the source of a good prompt
- → `08a_UnitTest` (S08): test-driven prompting builds on "verify" step
