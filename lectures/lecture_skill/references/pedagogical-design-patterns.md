# Pedagogical Design Patterns

Use this reference when designing the **content and narrative arc** of a lecture
deck, not just its technical format. The patterns here apply before you write a
single slide: they shape what goes in, in what order, and at what depth.

---

## 1. Narrative Architecture

### Problem-first structure (default for all lectures)

```text
1. Open with a concrete pain point — numbers, a failure case, a question
2. Build cognitive tension (why this is hard / what we don't yet have)
3. Introduce the solution / concept
4. Demonstrate and derive
5. Close with reflection, references, and an open question
```

Do not open with definitions. Open with a problem the audience can feel.

### Three-act arc

- **Act I: The Problem** — show what fails, why, at what scale
- **Act II: The Solution** — introduce the key idea that resolves the tension
- **Act III: The Evolution** — historical development, variants, trade-offs

### Bridge from known to unknown

- Start with an audience question that activates prior knowledge
- Connect to a familiar domain example before abstract theory
- State explicitly what prior lecture knowledge you assume

---

## 2. Mathematical Progression

Build mathematical concepts in deliberate stages — never jump to notation first:

```text
Level 1: Concrete arithmetic     (pixel counts, parameter counts, worked numbers)
Level 2: Operational definitions (convolution, padding, stride — in words)
Level 3: Formal notation         (subscripts, summations, index notation)
Level 4: Architectural/design    (depth vs. width trade-offs, complexity class)
```

### Dual representation strategy

Every major concept should appear in at least two forms on the slide and in full
in the book prose:

- **Visual** — diagram, animation, heatmap
- **Mathematical** — formal notation with subscripts/superscripts
- **Computational** — Python/code implementation
- **Intuitive** — natural language explanation

The formalization sequence is always:
`intuitive explanation → visual → formal notation → code implementation`

For introductory/programming lectures, replace formal notation with an
AI-generated code example (Pattern C) as the primary formal representation.
Reserve notation-first treatment for lectures where the audience is expected to
handle it (ML, numerical methods).

---

## 3. Content Density Rules

**On slides (revealjs)**:

- One concept per slide
- Short bullet points, no full sentences
- Bold only for subheadings, not emphasis
- Italic for scientific terms at first mention
- Visual anchor on every slide

**In book/page (html/pdf)**:

- Full paragraphs with context
- Comprehensive explanations
- Fewer visual breaks

Move extended explanation to `%%book`. Keep slides sparse.

---

## 4. Concept Introduction Pattern

For each new concept, follow this sequence:

```text
1. Intuitive explanation (natural language)
2. Visual representation (diagram, animation, figure)
3. Formal representation — choose ONE based on audience:
   a. AI-generated code example (introductory/programming lectures)
   b. Mathematical notation (advanced lectures: ML, numerical methods)
4. Read/verify exercise (students predict output or check assumption)
5. Interactive exploration (Plotly figure or parameter sweep)
```

Do not skip the intuitive step to save time. It is load-bearing for retention.

---

## 5. Code Pedagogy Patterns

### Pattern A — Minimal Working Example (for exercises)

```python
# Clear input/output specification
# ~10–20 lines maximum
# Self-contained (no hidden dependencies)
# Immediate visual or numerical result
```

### Pattern B — Progressive Enhancement (for exercises)

```text
1. Simple (single item)
2. Add complexity (batch processing)
3. Add optimization (caching, device selection)
4. Add robustness (error handling, fallback)
```

### Pattern C — AI-Code Reading Pattern (primary for in-lecture code blocks)

```text
1. Present code block labelled "AI generated"
2. Pose comprehension questions before running:
   "What does this function return?"
   "Which line causes a side effect?"
3. Students trace / predict output
4. Run and compare prediction to actual output
5. Identify what the AI got wrong, omitted, or assumed
```

Use Pattern C whenever the goal is critical engagement with generated code,
not just demonstration of a result. This trains agentic verification habits.

### Code visibility options

```python
#| echo: true       # Teaching code — show by default
#| echo: false      # Implementation detail — show output only (e.g. plots)
#| code-fold: true  # Optional detail or very long block — show on demand
#| error: true      # Demonstrating a failure — code is expected to fail
```

---

## 6. Agentic Verification Pattern

Every concept students will encounter in AI-generated code needs a verification
callout. Place it immediately after the concept introduction:

```markdown
> **Agentic workflow:** When AI generates [concept]:
> 1. [What to read / check first]
> 2. [What assumption to verify]
> 3. [What to add to the prompt if it fails]
```

Examples:

- **Functions**: "Read the signature first. Is the return type correct? Does it
  match the requirement? Write a test before reading the implementation."
- **Loops**: "Identify what it iterates over. Trace the first and last
  iterations. Verify it terminates."
- **SQL**: "Run on a small known dataset. Does the result match the requirement?
  Don't trust SQL by reading it."

---

## 7. Reusable Teaching Patterns

### A. Opening Hook

```text
1. Audience question (Hörsaalfrage) — activate prior knowledge
2. Concrete problem statement with numbers
3. Visual demonstration of the problem
4. Preview of the solution approach
```

### B. Concept Introduction (see §4 above for full sequence)

### C. Architecture / Method Comparison

```text
1. Historical timeline (when introduced, who)
2. Key innovation (what changed and why it mattered)
3. Architectural diagram (visual structure)
4. Performance comparison (benchmarks)
5. Trade-off analysis (when to use each)
```

### D. Practical Example

```text
1. Real-world motivation (why this matters)
2. Problem setup (inputs / outputs)
3. Implementation (complete working code, Pattern A or C)
4. Results visualization (interactive figure or image grid)
5. Failure case analysis (what doesn't work and why)
6. Insights (lessons learned, connection to theory)
```

### F. Caching Pattern (for all Plotly lectures)

```python
out_path = f"data/{LECTURE_NAME}/{figure_name}.json"
if not os.path.exists(out_path):
    fig = create_complex_visualization()
    pio.write_json(fig, out_path)
```

Expensive computations are cached as JSON so lecture builds take seconds.
See [plotly-code-and-equations.md](plotly-code-and-equations.md) for the
full render pattern.

---

## 8. Progressive Skill Building

Structure exercises and assessments against these levels:

```text
Level 1: Recognition    — identify components
Level 2: Understanding  — explain why it works
Level 3: Application    — implement in code
Level 4: Analysis       — compare approaches
Level 5: Synthesis      — design new variants
```

State learning objectives at the lecture start, mapped to these levels.
Homework / exercises should be visually distinguished (colored callout box).

---

## 9. Historical and Contextual Framing

- Present technique evolution as a narrative story (who, when, what changed)
- Credit researchers by name; link to awards and recognition
- State explicitly what this lecture assumes from prior lectures
- Name upcoming topics ("next week we look at…") — but don't over-promise

---

## 10. Language and Accessibility

- Primary language: German (appropriate for audience)
- Technical terms: retain English as used in the field
- Language style: clear, formal academic German
- Code comments: match surrounding language context
- Multiple modalities per concept: visual + verbal + computational + mathematical
- Optional depth: use `code-fold` for deep-dives that break flow
