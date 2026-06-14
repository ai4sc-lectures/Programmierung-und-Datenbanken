# Task: 08b_CodeReview

| Field | Value |
|-------|-------|
| **New file** | `../08b_CodeReview.qmdx` |
| **Source file** | NEW — create `08b_CodeReview.qmdx` |
| **Block** | Block 4 — Verification & Quality |
| **Session** | S08 |
| **Status** | NEW (~20 min, ~15 slides) |

> Open NEW — create `08b_CodeReview.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 08b_CodeReview

**Block**: Block 4 — Verification & Quality | **Session**: S08
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔍 📋 ⇄
**Source file**: NEW — create `08b_CodeReview.qmdx`

#### Summary: Code Review of AI-Generated Code

New lecture introducing code review as the final verification step before accepting
AI-generated code. Three review dimensions: requirement review (does the code do
what was asked?), design review (does it follow the architecture?), and
implementation review (is it correct, safe, maintainable?). An AI-specific
evaluation checklist is the practical output.

#### Main topics

- What code review is; why it is mandatory for AI output
- Requirement review: does the code match functional requirements?
- Design review: does it match the UML design and module structure?
- Implementation review: type safety, error handling, performance
- AI hallucinations and incomplete implementations
- AI evaluation checklist

#### Key takeaways

- Review standard is the requirement and the design — same as for human code.
- Common AI failure modes: hallucinated function calls, missing edge cases, incorrect
  type assumptions, over-engineered solutions.
- A structured checklist reduces cognitive load when reviewing unfamiliar AI code.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Why review AI code — "AI is confident but not always correct."
- Slides 3–4: Requirement review — for each functional requirement: is it
  implemented? Does a test exist? Does it pass?
- Slides 5–6: Design review — module structure matches architecture? Class interfaces
  match UML design?
- Slides 7–9: Implementation review — scan for: hardcoded values, missing type
  annotations, unsafe operations (division without zero-check), mutable defaults,
  missing `return` statements
- Slides 10–11: AI hallucination patterns — calling nonexistent functions, importing
  nonexistent modules, incorrect API usage, unnecessary abstractions
- Slides 12–14: AI evaluation checklist: □ requirement coverage □ design match
  □ type correctness □ edge cases □ error handling □ no hallucinated calls
  □ test suite passes
- Slide 15: Code review is the final "verify" step; if review fails, iterate

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- Code review is the formalized "verify" step. This lecture gives it a checklist
  and a process.

**Symbols to add**: 🔍 on review activity slides; 📋 on checklist slides;
⇄ on design match slides.

**Cross-references**:
- → `08a_UnitTest` (S08): tests are automated part of review; manual review covers
  what tests can't
- → `04a_Anforderungen` (S04): requirements are the review standard
- → `03c_Softwareentwurf` (S03): design is the second review standard
