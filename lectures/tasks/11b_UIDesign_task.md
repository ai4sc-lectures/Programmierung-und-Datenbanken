# Task: 11b_UIDesign

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../11b_UIDesign.qmdx` |
| **Source file** | NEW — create `11b_UIDesign.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S11 |
| **Status** | NEW (~20 min, ~15 slides) |

## Instructions

1. Use `../lecture_skill/SKILL.md` for `.qmdx` authoring conventions. Do NOT open completed lectures in `lectures/` to check patterns — the skill has everything.
2. Create `../11b_UIDesign.qmdx` from scratch as a new `.qmdx` lecture file.
3. Use the **Change Notes** below as the complete content specification — they define every section, slide group, and callout to include.
4. Save the finished file to `../11b_UIDesign.qmdx`.

---

### 11b_UIDesign

**Block**: Block 5 — Problem Classes | **Session**: S11
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📂 🔍
**Source file**: NEW — create `11b_UIDesign.qmdx`

#### Summary: UI Design for Engineering Applications

New lecture introducing user interface design as an engineering output. A computation
result is only useful if it can be communicated. AI can generate UI scaffolding
(dashboards, forms); the engineer verifies that data is correctly mapped to the
display. Streamlit and Gradio are used as accessible tools for quick engineering UIs.

#### Main topics

- UI types: console, Jupyter notebook, Streamlit web app, Gradio, PDF report
- Design principles for engineering data presentation: clarity, units, meaningful
  labels
- Streamlit and Gradio for rapid prototyping
- AI-generated UI scaffolding: what AI does well, what the engineer must verify
- Worked example: sensor data monitoring dashboard
- Motivation for Block 6: UI needs persistent data at scale

#### Key takeaways

- The output format is part of the engineering solution.
- AI generates a working Streamlit skeleton; the engineer verifies that the data
  mapping is meaningful.
- Displaying incorrect data clearly is worse than correct data obscurely — data
  mapping is always the engineer's responsibility.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem context — "You computed contamination risk for 500 sites. Who
  sees the result, and how?"
- Slides 3–4: UI type taxonomy — console, Jupyter, Streamlit, Gradio, PDF; when each
  is appropriate
- Slides 5–6: Design principles — appropriate precision (units, significant figures);
  clarity (one chart = one message); meaningful labels (not "value_1" but "PM2.5
  [µg/m³]")
- Slides 7–9: Streamlit demo — AI generates basic dashboard: file upload → filter →
  plot → download. Show code, then verify: labels correct? Units displayed? Ranges
  meaningful?
- Slides 10–11: Gradio demo (brief): for interactive ML / simulation model interfaces
- Slides 12–13: AI-generated UI verification checklist — □ labels include units
  □ axis ranges meaningful □ color scale appropriate □ data correctly mapped
  □ error states handled
- Slides 14–15: Transition to Block 6 — "The dashboard works. But 10M records from
  files? We need databases."

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Prompt: 'Generate a Streamlit app displaying sensor time series from CSV with
  threshold slider.' → verify: correct column names, axis labels, threshold logic."

**Symbols to add**: 📂 on data mapping slides; 🔄 on workflow diagrams;
🔍 on UI verification checklist.

**Cross-references**:
- → `11a_Raster_Simulation` (S11): raster results visualized in a dashboard
- → `12a_Datenhaltung` (S12): data persistence motivates databases over files
- → `08b_CodeReview` (S08): UI code review follows same checklist principles
