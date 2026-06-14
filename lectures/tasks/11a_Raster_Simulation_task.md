# Task: 11a_Raster_Simulation

| Field | Value |
|-------|-------|
| **New file** | `../11a_Raster_Simulation.qmdx` |
| **Source file** | NEW — create `11a_Raster_Simulation.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S11 |
| **Status** | NEW (~20–30 min, ~18 slides) |

> Open NEW — create `11a_Raster_Simulation.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

---

### 11a_Raster_Simulation

**Block**: Block 5 — Problem Classes | **Session**: S11
**Status**: NEW (~20–30 min, ~18 slides) | **Primary symbols**: 🔄 📂
**Source file**: NEW — create `11a_Raster_Simulation.qmdx`

#### Summary: Raster Problems

New lecture on raster data as a problem class. Environmental models, climate grids,
terrain analysis, and remote sensing are raster problems — directly relevant to
environmental engineering. Students learn what makes a problem a raster problem,
how grids are represented as arrays, and what grid-based analysis looks like.

#### Main topics

- Raster problems: terrain, climate grids, land cover, remote sensing
- Grid as data structure: 2D numpy array, cell size, extent, NoData
- Grid analysis: overlay, reclassification, zonal statistics
- `numpy` for grid operations; `matplotlib` for visualization
- AI prompt pattern for raster problems

#### Key takeaways

- A raster represents continuous spatial phenomena discretized to a grid — resolution
  is a modeling choice.
- Most raster operations are element-wise or neighborhood operations on 2D arrays.
- AI generates correct array operations but often ignores resolution, extent, or
  NoData handling — verify the metadata.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem class introduction — continuous field discretized to grid
- Slides 3–4: Environmental examples — digital terrain model, land cover
  classification, precipitation grid, air pollution concentration
- Slides 5–6: Grid data structure — 2D numpy array, cell size, extent, CRS (brief),
  NoData values
- Slides 7–9: Grid operations — reclassification (threshold to binary mask), overlay
  (multiply grids), zonal statistics (mean elevation within polygon zone)
- Slides 10–12: numpy demo — load terrain grid, compute slope, apply flood threshold
  mask, visualize
- Slides 13–14: Metadata pitfalls — AI generates correct array math but forgets:
  cell size match, extent alignment, NoData handling. Failing example shown.
- Slides 15–16: AI prompt pattern — "Given a 2D numpy array representing [soil
  moisture] with cell size [50m] and NoData [-9999], return fraction of cells above
  threshold t."
- Slides 17–18: Verification checklist — shape matches extent, NoData excluded,
  units correct, output type matches requirement

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Recognize raster → specify shape, cell size, NoData in prompt → verify extent and
  metadata → test on small synthetic array."

**Symbols to add**: 📂 on data structure slides; 🔄 on grid operation slides.

**Cross-references**:
- → `10b_Geometrieprobleme` (S10): vector and raster are complementary representations
- → `11b_UIDesign` (S11): raster analysis results visualized in a dashboard
