# Task: 09a_Algorithmen

| Field | Value |
|-------|-------|
| **New file** | `../09a_Algorithmen.qmdx` |
| **Source file** | `../oldx/05c_Algorithmen.qmdx` |
| **Block** | Block 5 — Problem Classes |
| **Session** | S09 |
| **Status** | MOVED from Block 3 + REFRAMED |

> Open `../oldx/05c_Algorithmen.qmdx` as starting point (or create new if Status is NEW).
> **Read `../lecture_skill/SKILL.md` before writing any slides.**
> Apply its conventions for layout, icons, code blocks, and Quarto syntax.

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
