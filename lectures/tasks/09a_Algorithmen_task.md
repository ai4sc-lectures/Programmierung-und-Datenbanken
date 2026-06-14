# Task: 09a_Algorithmen

## Course Context

**Course**: "Programming and Databases" — civil/environmental engineering, 1st semester, University of Rostock.

**What we are doing**: Redesigning 13 sessions of lecture slides (`.qmdx` Quarto format with companion Jupyter notebooks) around agentic coding tools (Claude Code, GitHub Copilot, Cursor).

**Why**: AI tools are now standard in engineering practice. The course shifts its pedagogical model from "write code from scratch" to **Understand → Modify → Verify AI-generated code**. Students still need genuine Python competence, computational thinking, and engineering judgment — but they acquire it by reading, questioning, and verifying AI output rather than by typing code from a blank page.

**Goal**: Students leave able to (1) read and understand AI-generated Python, (2) verify it meets the engineering requirement, (3) debug and modify it confidently. The agentic cycle — **prompt → generate → understand → verify → iterate** — is woven into every session.


| Field | Value |
|-------|-------|
| **New file** | `../09a_Algorithmen.qmdx` |
| **Source file** | `../oldx/05c_Algorithmen.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S09 |
| **Status** | MOVED from Block 3 + REFRAMED |

## Instructions

1. Follow the `.qmdx` conventions in `CLAUDE.md` (auto-loaded — do not read any other files).
2. The **Summary**, **Main topics**, and **Key takeaways** sections below describe the existing content — do not open the source file.
3. Apply every item in the **Change Notes** below:
   - ADD the specified content (new slides, callouts, sections).
   - REMOVE or REDUCE the specified content.
   - REFRAME the specified existing content with the new angle described.
   - Add the specified symbols at the indicated locations.
4. Write the result to:
   - `../09a_Algorithmen.qmdx`

---

### 09a_Algorithmen

**Block**: Block 5 — Problem Classes | **Session**: S09
**Status**: MOVED from Block 3 + REFRAMED | **Primary symbols**: 🔄 📂
**Source file**: `../oldx/05c_Algorithmen.qmdx`

#### Summary: Algorithms

Surveys algorithmic ideas. Moved to Block 5 and reframed: "identify the problem
class first, then choose the algorithm family." The emphasis shifts from "here is
how bubble sort works" to "how do I know which algorithm to ask for?"

#### Main topics

- Trees; sorting (bubble, quicksort, insertion); searching (list, set, BST);
  binary search; performance (Big-O conceptually); heuristics; A* search
- **[ADDED]** Algorithm recognition strategy
- **[ADDED]** AI and algorithm selection

#### Key takeaways

- The problem class determines the algorithm family; identify the class first.
- AI defaults to adequate-but-not-optimal algorithms — knowing the class lets you
  guide the AI.

#### Change Notes

**Content to ADD**:
- "Algorithm Recognition" exercise (~3 slides): given a problem description, identify
  the class (search, sort, path, partition) before looking at any algorithm. Practice
  with 4 engineering scenarios.
- "AI and Algorithm Selection" (~2 slides): AI defaults to linear search or bubble
  sort unless specified. Knowing the class lets you prompt "use Dijkstra" and verify
  the AI used the correct algorithm.

**Content to REMOVE or REDUCE**: None.

**Content to REFRAME**:
- "Here are the major algorithms" → "Here is how to recognize which algorithm class
  your problem belongs to."

**Agentic workflow integration**:
- "Before prompting: identify the problem class. Include it in the prompt:
  'implement a binary search for this sorted list.' Verify the AI used it."

**Symbols to add**: 🔄 on algorithm pattern slides; 📂 on data structure slides.

**Cross-references**:
- → `09b_Rekursion` (S09): recursion as divide-and-conquer strategy
- → `10a_Graphprobleme` (S10): graph algorithms as a problem class
