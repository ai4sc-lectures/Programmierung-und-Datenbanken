# Slide Archetypes

## A. Slide with One Text Block

```md
## KI-Adoption ist Realität

- 78% der Organisationen nutzen KI
- Die Adoption ist in AEC ebenfalls angekommen
- Das ist Motivation, nicht nur Hintergrund
```

Use this for:

- takeaways
- definitions with few bullets
- short discussion prompts

## B. Two-Column Text:Text

```md
## Der Vergleich

%%col 50 50
### Methode A

- Schnell
- Robust
- Gut erklärbar
%%sep
### Methode B

- Flexibler
- Datenhungriger
- Schwerer zu interpretieren
%%/col
```

Use this for:

- pros/cons
- baseline vs method
- theory vs practice

## C. Two-Column Text:Image

```md
## Voraussetzung

%%col 40 60
- Python
- Statistik
- Lineare Algebra
%%sep
![](images/example.png){class="midjourney"}
%%/col
```

Use this when:

- text carries the teaching point
- the image supports recognition, atmosphere, or a quick example

## D. Title or Question Slide with Framed Midjourney

```md
## Hörsaalfrage {background="#FFD966" cols40x60 txtL="Wie viele Sensoren hat ein Supermarkt?" capR="Midjourney: An alien supermarket filled with exotic food" imgR="images/00_Grundlagen/mj_An_alien_supermarket_filled_with_exotic_food.png"}
```

Or:

```md
# Überblick {colR capR="Midjourney: Application of ML in Construction" imgR="images/00_Grundlagen/mj_application_of_machine_learning_in_construction.png" background="#333"}
```

Use this for:

- section openers
- lecture questions
- visually strong concept prompts

## E. Three-Column Slide

```md
## Die Hebel

%%col 33 33 33
#### 1. Bildung

- Weiterbildung
- Ausbildung
%%sep
#### 2. Organisation

- Prozesse
- Tools
%%sep
#### 3. Technik

- Assistenz
- Automatisierung
%%/col
```

Use this for:

- three-way comparisons
- pillars/frameworks
- summary structures

## F. Four-Column Alternating Text:Image

```md
%%col 30 20 30 20
Text block
%%sep
![](images/a.png){class="midjourney"}
%%sep
Text block
%%sep
![](images/b.png){class="midjourney"}
%%/col
```

Use this sparingly. It is dense and works best for enumerated examples.

## G. Hörsaalfrage

Two-column layout: question text on the left (40%), Midjourney image on the
right (60%), yellow background.

```md
## Hörsaalfrage {background="#FFD966" cols40x60 txtL="Wo finden wir ML im Alltag?" capR="Midjourney: Every day life with machine learning" imgR="images/00_Grundlagen/mj_every_day_life_with_machine_learning.png"}
```

Use for:

- opening discussion
- recall checks
- audience activation before explanation

## H. Section-Divider Slides

```md
## {.section-divider}

%%div eyebrow
Part 02
%%/div

%%div display
Results
%%/div

%%div lead
Three projects. Four structural systems. One consistent finding.
%%/div
```

Use this for:

- act breaks in a lecture or talk
- transitions between theory, method, and results
- resetting audience attention before a new section

## I. Quote Slides

```md
## {.quote}

%%div quote-text
The bottleneck isn't data. It's legibility.
%%/div

%%div attribution
Structural engineer, Arup Berlin · project review, Oct 2024
%%/div
```

Use this for:

- expert testimony
- framing statements
- short rhetorical pauses between dense technical sections

## J. Closing Slides

```md
## {.closing}

%%div eyebrow
AI4SC · Sustainable AI for Construction
%%/div

%%div display
Estimate carbon.\
Before you commit\
to structure.
%%/div
```

Use this for:

- a final takeaway
- a call to action
- a branded or memorable closing message before the question slide

## K. Übungsaufgabe (Exercise / Homework)

```md
## Übungsaufgabe {background-color="#D9FF66"}

Wählt ein Paper aus dem Bereich CNN-Architekturen aus und bewertet es nach
folgenden Kriterien:

- Relevanz (25%)
- Technische Tiefe (25%)
- Verständlichkeit (25%)
- Neuheit (25%)
```

Use this for:

- homework assignments
- in-class exercises
- paper-reading tasks or self-study prompts

## L. Pro / Con List

Standard bullet list where the span class controls text color and causes the
CSS to replace the bullet automatically. Write only the class — do not add
`+`, `−`, or `○` characters to the source:

| Class | Bullet | Color |
| ----- | ------ | ----- |
| `.pro` | `+` | green (`--moss-700`) |
| `.con` | `−` | red (`--signal-red`) |
| `.neutral` | `○` | yellow (`--signal-yellow`) |

```md
## Methode A — Bewertung

- [Schnell und ressourceneffizient]{.pro}
- [Gut erklärbar]{.pro}
- [Geringe Datenmengen nötig]{.pro}
- [Kontextabhängig, je nach Datenlage]{.neutral}
- [Weniger flexibel als Deep Learning]{.con}
- [Setzt Feature Engineering voraus]{.con}
```

Classes are defined in the extension and stay consistent across themes.

Use this for:

- method comparison slides
- trade-off analysis
- technology evaluation

---

Color conventions for interactive/special slides:

- `#FFD966` (yellow) — Hörsaalfrage (audience activation, recall check)
- `#D9FF66` (lime green) — Übungsaufgabe / homework
- black background (`#000000` or `.final-slide`) — closing question slide (`%%final`)
