# Task: 10a_Graphprobleme

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../10a_Graphprobleme.qmdx` |
| **Source file** | NEW — create `10a_Graphprobleme.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S10 |
| **Status** | NEW (~20 min, ~15 slides) |

## Instructions

1. Follow the `.qmdx` conventions in `CLAUDE.md` (auto-loaded — do not read any other files).
2. Create `../10a_Graphprobleme.qmdx` from scratch as a new `.qmdx` lecture file.
3. Use the **Change Notes** below as the complete content specification — they define every section, slide group, and callout to include.
4. Save the finished file to `../10a_Graphprobleme.qmdx`.

---

### 10a_Graphprobleme

**Block**: Block 5 — Problem Classes | **Session**: S10
**Status**: NEW (~20 min, ~15 slides) | **Primary symbols**: 🔄 📂 ⇄
**Source file**: NEW — create `10a_Graphprobleme.qmdx`

#### Summary: Graph Problems

New lecture on graph problems as a problem class. Transportation networks, utility
networks, and routing are the domain examples — all directly relevant to civil and
environmental engineering. Students learn to recognize a graph problem, represent it
as a data structure, and select the appropriate algorithm family.

#### Main topics

- Graph problems in engineering: transport networks, utility networks, routing, flow
- Graph data structure: nodes, edges, weights, direction
- Traversal: BFS and DFS (conceptually)
- Shortest path: Dijkstra's algorithm (conceptually)
- `networkx` library demo
- AI prompt pattern for graph problems

#### Key takeaways

- Many civil engineering problems are graph problems in disguise.
- The graph representation determines which algorithms are efficient.
- AI generates graph traversal code correctly when you specify the representation and
  algorithm family.

#### Change Notes

**Content to ADD** (new file — full content outline):
- Slides 1–2: Problem class introduction — what makes a problem a graph problem?
  (entities with relationships that can be traversed)
- Slides 3–4: Civil engineering examples — road network (routing), pipe network
  (flow), building floor plan (connectivity), drainage network (directed flow)
- Slides 5–6: Graph data structure — nodes (intersections), edges (roads/pipes),
  weights (length/capacity), direction
- Slides 7–8: BFS for shortest hop count (flood extent from source); DFS for
  reachability (connected network components)
- Slides 9–10: Dijkstra's algorithm — shortest weighted path; evacuation route with
  travel times
- Slides 11–12: `networkx` demo — create road network, run `shortest_path()`,
  visualize
- Slides 13–14: AI prompt pattern — "Given a weighted directed graph representing
  [pipe network], implement [Dijkstra] using `networkx`. Nodes have [demand]; edges
  have [diameter, length]."
- Slide 15: Verification checklist — correct graph type (directed/undirected),
  weights present, algorithm matches problem class

**Content to REMOVE or REDUCE**: CREATE NEW FILE — nothing to remove.

**Agentic workflow integration**:
- "Recognize graph → specify representation → include algorithm family in prompt →
  verify graph type and weights → run on test case."

**Symbols to add**: ⇄ on relationship/edge diagrams; 📂 on data structure slides;
🔄 on traversal/algorithm slides.

**Cross-references**:
- → `09a_Algorithmen` (S09): algorithm recognition strategy applied here
- → `10b_Geometrieprobleme` (S10): geometry complements graph problems in spatial
  engineering
