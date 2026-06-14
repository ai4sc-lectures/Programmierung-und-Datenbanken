# Task: 04a_Anforderungen

| Field | Value |
|-------|-------|
| **New file** | `../04a_Anforderungen.qmdx` |
| **Source file** | NEW — create `04a_Anforderungen.qmdx` |
| **Block** | Block 2 — Computational Engineering |
| **Session** | S04 |
| **Status** | NEW (~20 min, ~15 slides) |

> Open NEW — create `04a_Anforderungen.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 04a_Anforderungen

**Block**: Block 2 — Computational Engineering | **Session**: S04
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 📋 🔍
**Source file**: NEW — create `04a_Anforderungen.qmdx`

#### Summary: Requirements Engineering

New lecture covering requirements engineering as the foundation for AI-assisted
development. A requirement is the source of a prompt and the source of a test — so
requirements engineering is the prerequisite for both prompting well and verifying
confidently.

#### Main topics

- Functional requirements: what the system must do
- Non-functional requirements: performance, reliability, maintainability
- Constraints: hardware, platform, regulatory
- Stakeholder perspectives
- Quality criteria: measurable acceptance conditions
- User stories: as a [role], I want [action] so that [benefit]
- Requirements as AI prompt specifications
- Requirement → test case traceability

#### Key takeaways

- A requirement is a measurable statement of what the system must do, not how.
- Every functional requirement should generate at least one test case.
- A well-written requirement is the best possible prompt for an AI code generator.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Why requirements matter — "AI satisfies the prompt, not the
  stakeholder. You are the bridge."
- Slides 3–5: Functional vs non-functional requirements; constraints; worked examples
  in sensor monitoring (civil/environmental domain)
- Slides 6–7: Stakeholder perspectives — structural engineer, facility manager,
  regulatory inspector each need different things from the same system
- Slides 8–9: Quality criteria — measurable acceptance conditions: "response < 2s",
  "handles 1M records", "output matches IFC schema"
- Slide 10: User story format — as a [facility manager], I want [sensor alert
  dashboard] so that [I can respond before an SLA breach]
- Slides 11–12: Requirement → prompt — user story converted step-by-step into a
  Claude Code prompt using the structure from `01c_AgentischesProgrammieren`
- Slides 13–14: Requirement → test — same user story converted into a unit test
  (motivates `08a_UnitTest` in S08)
- Slide 15: Traceability triangle: requirement ↔ test ↔ prompt; changing one must
  trigger updating the others

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- Requirements formalize the "prompt" step; unit tests formalize the "verify" step.
  This lecture makes the connection explicit.

**Symbols to add**: 📋 on every requirements slide; 🔍 on test-traceability slides.

**Cross-references**:
- → `01c_AgentischesProgrammieren` (S01): prompt structure applied here
- → `03c_Softwareentwurf` (S03): requirements precede design
- → `04b_Programmablauf` (S04): flowcharts operationalize requirements
- → `08a_UnitTest` (S08): test-driven prompting is the "verify" step
