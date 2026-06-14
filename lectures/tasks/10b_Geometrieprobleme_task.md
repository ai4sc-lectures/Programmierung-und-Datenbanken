# Task: 10b_Geometrieprobleme

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../10b_Geometrieprobleme.qmdx` |
| **Source file** | NEW — create `10b_Geometrieprobleme.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S10 |
| **Status** | NEW (~20 min, ~15 slides) |

## Instructions

1. Follow the `.qmdx` conventions in `CLAUDE.md` (auto-loaded — do not read any other files).
2. Create `../10b_Geometrieprobleme.qmdx` from scratch as a new `.qmdx` lecture file.
3. Use the **Change Notes** below as the complete content specification — they define every section, slide group, and callout to include.
4. Save the finished file to `../10b_Geometrieprobleme.qmdx`.

---

### 10b_Geometrieprobleme

**Block**: Block 5 — Problem Classes | **Session**: S10
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📂 ⇄
**Source file**: NEW — create `10b_Geometrieprobleme.qmdx`

#### Summary: Geometric Problems

New lecture on geometric problems as a problem class. CAD, BIM, and GIS are all
geometric domains. Students learn the problem class signature, relevant data
structures, and the `shapely` library.

#### Main topics

- Geometric problems in engineering: CAD, BIM, GIS, spatial relationships
- Vector algebra basics: point, line, polygon, vector operations
- Point-in-polygon, distance, intersection, area
- Coordinate systems and projections (briefly)
- `shapely` library demo
- AI prompt pattern for geometric problems

#### Key takeaways

- Geometric problems require specifying both representation and coordinate system.
- `shapely` implements most 2D geometric operations — AI can be prompted to use it;
  engineer verifies the geometry is correctly represented.
- Floating-point precision is a common source of errors in geometric AI code.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem class introduction — what makes a problem geometric?
- Slides 3–4: Civil engineering examples — building footprint analysis, structural
  member intersections, flood zone delineation, road alignment geometry
- Slides 5–6: Vector algebra — point as (x,y,z), line segment, polygon as ordered
  point list, distance, cross product for orientation
- Slides 7–8: Key operations — point-in-polygon (sensor inside zone?), distance
  (nearest facility), intersection (pipe collision?)
- Slides 9–10: `shapely` demo — create building polygon, buffer, containment check
- Slides 11–12: Coordinate systems — why projections matter (WGS84 vs local CRS);
  common AI omission
- Slides 13–14: AI prompt pattern — "Given building polygons in WGS84, return all
  buildings within 500m of a given point. Use `shapely`."
- Slide 15: Verification checklist — geometry type, CRS specified, floating-point
  tolerance for equality checks

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Recognize geometry → specify representation and CRS → verify geometry type →
  test with known spatial relationship."

**Symbols to add**: ⇄ on spatial relationship diagrams; 📂 on data structure slides;
🔄 on algorithm slides.

**Cross-references**:
- → `10a_Graphprobleme` (S10): spatial networks combine graphs and geometry
- → `11a_Raster_Simulation` (S11): raster is the alternative spatial representation
