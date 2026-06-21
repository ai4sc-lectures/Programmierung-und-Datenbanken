# Summary: Einführung

This lecture introduces the **programming exercise course** (*Übung*) as part of the broader "KI für Digitales Bauen" program. It sets expectations for both the lecture and exercise components, outlines the **agent-based workflow** (Prompt → Generate → Understand → Verify → Iterate) that students will practice throughout the semester, and explains the practical logistics: how to access assignments via JupyterLab, how to submit work through Nbgrader, and what is required for exam eligibility. The lecture also grounds the course in real-world engineering applications, showing where computer science intersects with civil engineering — from CAD design and virtual environments to building automation and GIS.

The core pedagogical thesis is a shift in the engineer's role: rather than writing code from scratch, the modern engineer acts as **architect and verifier** — formulating prompts for AI code generation, reading and understanding the output, modifying it to meet requirements, and verifying its correctness. This competency profile reflects current industry standards and is reinforced through every topic in the course.

The instructor **Prof. Dr. Jörn Plönnigs** presents the lecture portion, while **Dr. Markus Berger** leads the exercise sessions. Together they structure the course around Python fundamentals, databases, and AI-assisted development, with graded weekly exercises that must be completed individually.

## Main topics (What is the structure of the lecture)
- **Agentischer Arbeitsablauf**: The five-step cycle of prompt → generate → understand → verify → iterate as the core working method
- **Vorstellung der Dozierenden**: Introduction of Prof. Plönnigs (lecture) and Dr. Berger (exercises) with contact details
- **Lernziele und Zielsetzung**: Shift from writing code to reading, modifying, and verifying AI-generated code
- **Symbollegende**: Course-wide icon legend for concepts (variables, data types, objects, algorithms, tests, databases, etc.)
- **Kursthemen und Ablauf**: Overview of Python basics, data structures, algorithms, and database concepts mapped through the agentive cycle
- **Übungsformat und Abgabe**: Weekly video-based exercises, Nbgrader workflow, individual submission, 50% pass threshold
- **Prüfungszulassung**: Grading breakdown across foundational and advanced topics (Python, operators, functions, algorithms, errors, design, data management, database queries, database design)
- **JupyterLab und Nbgrader**: Step-by-step guide on fetching, editing, validating, and submitting assignments
- **Informatik im Ingenieurwesen**: Applications of computer science in civil engineering — CAD, virtual environments, structural planning, construction automation, building robotics, GIS, building automation, CAFM
- **Literaturempfehlungen**: Recommended textbooks and online resources (Python handbook, database texts, official docs, W3Schools)

## Key takeways (What are the resulting takeways/skills teached)
- Use the **agentive cycle** (Prompt → Generate → Understand → Verify → Iterate) as your primary working method for all exercises
- Develop the skill of **reading and understanding** Python code — not just writing it from scratch
- **Modify AI-generated code** to meet specific engineering requirements
- **Verify** code correctness against technical specifications before accepting outputs
- Understand that in the engineering profession, the ability to **assess AI output** is now a core competency
- Complete exercises **individually** — group work is not permitted and exam admission depends on meeting the 50% completion threshold
- Use **Nbgrader's validation** feature before submitting to confirm all tests pass

## Code Examples (What code examples are shown)
- None — this is an introductory/orientation lecture that focuses on course structure and workflow, not on specific code demonstrations.

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/01a_Ueberblick/mj_title_band.jpg` — Cover image with David Allen quote
- `images/01a_Ueberblick/Ploennigs.jpg` — Portrait photo of Prof. Dr. Jörn Plönnigs
- `images/01a_Ueberblick/mj_target.png` — Midjourney-generated imagery illustrating course goals
- `images/01a_Ueberblick/ablauf.svg` — SVG diagram showing the course topic structure and flow
- `images/01a_Ueberblick/ablauf2.svg` — SVG diagram illustrating the lecture/exercise workflow
- `images/01a_Ueberblick/ablauf3.svg` — SVG diagram detailing the exercise structure
- `images/01a_Ueberblick/image_4.png` — Screenshot of the lecture slide repository
- `images/01a_Ueberblick/image_2.png` — Screenshot of StudIP (university learning management system)
- `images/01a_Ueberblick/webpage.png` — Screenshot of the course documentation website
- `images/01a_Ueberblick/image_5.png` — Screenshot of https://ai4sc-lectures.github.io/
- `images/01a_Ueberblick/python-in-notebook.png` — Screenshot showing Python in Jupyter Notebook
- `images/01a_Ueberblick/mj_train.png` — Midjourney image illustrating the exercise component
- `images/01a_Ueberblick/Markus_Berger.jpg` — Portrait photo of Dr. Markus Berger
- `images/01a_Ueberblick/mj_student.png` — Midjourney image of student aiming for a goal
- `images/01a_Ueberblick/mj_student2.png` — Midjourney image of student with a deadline
- `images/01a_Ueberblick/jupyterlab-markdown.png` — Screenshot of the JupyterLab interface
- `images/01a_Ueberblick/login.png` — Screenshot of the JupyterLab login page
- `images/01a_Ueberblick/nbgrader_menu.png` — Screenshot of Nbgrader menu navigation
- `images/01a_Ueberblick/nbgrader_menu_assignments.png` — Screenshot of available assignments view
- `images/01a_Ueberblick/nbgrader_menu_assignments2.png` — Screenshot of downloaded assignments list
- `images/01a_Ueberblick/nbgrader_notebook2.png` — Screenshot of Nbgrader notebook with code cells and test cells
- `images/01a_Ueberblick/nbgrader_validate.png` — Screenshot of the Nbgrader validation button
- `images/01a_Ueberblick/dijkstra.jpg` — Photo of Edsger W. Dijkstra with his famous quote
- `images/01a_Ueberblick/use_case_cad.png` — Autodesk Revit LT screenshot for CAD applications
- `images/01a_Ueberblick/use_case_render.jpg` — FIRSTinVision VR/AR rendering example
- `images/01a_Ueberblick/use_case_static.png` — Structural planning (Tragwerksplanung) example
- `images/01a_Ueberblick/use_case_report.png` — BauGorilla construction diary app for construction automation
- `images/01a_Ueberblick/use_case_gis.png` — Geoinformationssystem (GIS) visualization
- `images/01a_Ueberblick/step_design.png` — STEP file CAD design workflow (referenced from 01b)
- `images/01a_Ueberblick/step_bau.png` — Construction process automation workflow (referenced from 01b)
- `images/01a_Ueberblick/step_operate.png` — Facility operation workflow (referenced from 01b)

## Plots
- None — no plotly plots or data visualizations in this lecture.

## Examples (What examples are used)
- **Real-world engineering applications**: CAD (Autodesk Revit), virtual/AR environments (FIRSTinVision), structural planning, construction diary apps (BauGorilla), GIS, building automation (München Digital Twin), and CAFM (Dynamic Space Planning)
- **Video demonstrations**: `Baubot.mp4` (construction robotics), `MunchDigitalTwin.mp4` (building digital twin), `DynamicSpacePlanning.mov` (facility management), `mj_python.mp4` and `mj_motivation.mp4` (motivational animations)
- **Dijkstra quote**: "Computer science is no more about computers than astronomy is about telescopes" — used to provoke classroom discussion on the definition of computer science
- **AI4SC icon system**: Braces for data types, workflow symbol for algorithms, test-tube for verification — recurring visual language throughout the course
- **Nbgrader workflow walkthrough**: Step-by-step examples of fetching, editing (`YOUR CODE HERE` replacement), validating, and submitting assignments

## Remarks
- This is a **bilingual German-English** lecture — headings and most content are in German, while the summary is rendered in English per the synthesis rules.
- The file references images and SVGs from a `resources` directory (`data/01a_Ueberblick`) not directly visible in the glob results; those are Quarto resource declarations.
- The lecture uses **Midjourney-generated images** extensively, marked with `Midjourney:` captions — these serve as visual metaphors rather than technical diagrams.
- The `%%def Informatik` custom block defines the term "Informatik" (computer science) as the systematic processing of information, bridging mathematics (logic, algorithms) and electrical engineering (hardware).
- The `::content-visible unless-format="typst"` directives indicate format-specific rendering: some content (videos, special layouts) appears only in HTML/RevealJS formats, not in PDF/Typst.
- The lecture references materials from **lecture 01b** (`01b_Anwendungen/step_design.png`, etc.), indicating this is part of a connected lecture series.
- No actual Python code examples appear — code demonstration begins in subsequent lectures.
- A previous summary file already exists at `lectures/01a_Ueberblick.summary.md`; it has been overwritten.
# Summary: Programmiersprachen

This lecture introduces the concept and evolution of programming languages, tracing the journey from raw machine code through assembly and high-level languages to modern-day Python. It grounds the historical overview in a contemporary context: Python's dominance in the AI era, driven by the fact that large language models (LLMs) were trained predominantly on Python code. The lecture serves as a conceptual bridge in the course, explaining why Python literacy is the foundational skill for **agentive programming** — where engineers read, verify, and iterate on AI-generated code rather than writing it from scratch.

The core thesis is that understanding a programming language, especially Python, is not an end in itself but a **verification tool**. In the agentive workflow (prompt → generate → understand → verify → iterate), the engineer's primary role shifts from writing code to critically evaluating code produced by AI assistants. This reframes the learning objective of the course.

## Main topics (What is the structure of the lecture)
- **Definition of a programming language**: formal language defined by character set, syntax, and semantics (`%%book`, `%%def`)
- **Three generations of programming languages**: machine code (1st gen), assembly (2nd gen), high-level languages with compilers/interpreters (3rd gen)
- **Evolution and popularity of programming languages**: from C++ → Java → PHP/Perl/JavaScript → Python, driven by changing software requirements
- **Python in the data science and AI ecosystem**: readability, ecosystem breadth, and LLM training data dominance (>30% of public GitHub code)
- **The agentive programming workflow**: prompt → AI generates Python → engineer reads and verifies → iterate
- **Quiz**: reinforcing definitions, generational characteristics, and the rationale for Python literacy in the AI era

## Key takaways (What are the resulting takeways/skills teached)
- A programming language is a formal language defined by **character set, syntax, and semantics** — it translates human intent into machine-executable instructions
- Each generation of languages traded hardware-specific detail for **human readability**, using compilers or interpreters to bridge the gap to machine code
- **Python's popularity is structurally reinforced**: LLMs were trained on Python, they generate Python, creating a self-reinforcing cycle
- Engineers must develop **Python reading competence** — the ability to verify and critique AI-generated code is more important than writing code from scratch
- The **agentive workflow** (Prompt → Generate → Understand → Verify → Iterate) makes language understanding a verification tool, not a self-purpose
- New programming languages emerge continuously to meet evolving software requirements; popularity depends on community, application domain, and tooling

## Code Examples
- **1st generation machine code** (raw binary): demonstrates how the earliest computers were programmed directly in binary (`1101 0000 0000 0111 1011`) — processor-directly executable but not human-readable
- **2nd generation assembly** (x86-style `nasm`): shows labeled mnemonics (`MOV AL, 2`, `ADD AL, 3`) translated by an assembler into machine code, introducing human-readable commands tied to specific hardware
- **3rd generation high-level** (Python `while` loop): illustrates human-readable, natural-language-like code that a compiler/interpreter translates to machine code (`while i < 20: x = x + i * i`)

## Visualizations
- **`images/partA_2.svg`** (SVG diagram): course structural workflow ("Ablauf") showing the four main modules — Motivation, Computer and Architecture, Programming and Data Types, Errors and Debugging — connected in a flow diagram
- **`images/01b_Programmiersprachen/mj_title_band.jpg`** (JPEG): title banner image (Midjourney-generated, "Code Rain" aesthetic inspired by The Matrix)
- **`images/01b_Programmiersprachen/top_prog_languages.mp4`** (MP4, animated): visualization of programming language popularity trends 2004–2022 sourced from the TIOBE Index
- **Google Trends embeds** (HTML/JS widgets): two side-by-side interactive time-series charts showing global search trends for `Python` and `data science` from 2004–2025

## Plots
- **Google Trends — Python** (`/m/0jt3_q3`) `[interactive/static embed]`: worldwide search interest for Python over 20 years
- **Google Trends — Data Science** (`/m/05z1_`) `[interactive/static embed]`: worldwide search interest for data science over 20 years
- **TIOBE Index MP4** (`top_prog_languages.mp4`) `[animated]`: video showing shifting popularity of programming languages from 2004 to 2022

## Examples
- **Bjarne Stroustrup's famous quote**: "There are only two kinds of programming languages: the ones people complain about and the ones nobody uses" — used to frame the lecture's playful yet pragmatic tone
- **KI als Junior-Entwickler (AI as junior developer)**: the metaphor that AI tools (Claude Code, GitHub Copilot, Cursor) act like junior developers who produce Python code, requiring a senior engineer to review and verify
- **Agentischer Workflow example**: a step-by-step scenario (prompt → generate → read → verify → iterate) showing how engineers interact with AI-generated code in practice
- **Cross-reference to `01c_AgentischesProgrammieren`**: the lecture explicitly points to the next lecture (S01) for deeper exploration of the agentive programming cycle

## Remarks
- The lecture is written in **German** but the summary is in English per instructions. Key German terms retained on first reference (e.g. *Maschinencode*, *Assemblersprachen*, *agentische Programmieren*).
- The lecture intentionally contains **no deep code** — all code examples are minimal illustrations of generational differences rather than substantive demonstrations.
- Quiz content (`quizdown` format) is excluded from the Code Examples section per the rule to skip quiz-only code.
- Google Trends embeds are **client-side JavaScript widgets** rendered in HTML output; they do not appear in PDF/Typst format (controlled by `{.content-visible unless-format="typst"}`).
- The `%%# Python im KI-Ökosystem` heading is a slide section marker (not a slide), splitting the Python subsection into a thematic grouping.
- Image credit: title artwork is from **Midjourney** ("P+D Code Rain", Matrix-inspired).
# Summary: Agentisches Programmieren

This introductory lecture establishes the core philosophy of the course: **agentive programming** — the practice of using AI language models as junior developers while the human engineer serves as the architect, reviewer, and verifier. Rather than teaching students to write more code by hand, the lecture reframes programming around three competencies: **prompt formulation**, **code comprehension**, and **verification**. It sets the stage for an entire course built around an iterative **Prompt → Generate → Understand → Verify → Iterate** cycle.

The lecture explains *why* verification is non-negotiable — because large language models are probabilistic, not deterministic, and generate plausible rather than guaranteed-correct code. It then introduces the practical tools (Claude Code, GitHub Copilot, Cursor), the anatomy of a well-structured prompt, and the recommended reading strategy for AI-generated code. The lecture closes with a quiz that tests the conceptual understanding of the agentive workflow.

## Main topics (What is the structure of the lecture)
- **Grundlagen**: Introduction to the course's core thesis — reading, assessing, and correcting AI-generated code is more important than writing code yourself
- **LLM-Grundverständnis**: How language models work (token prediction, probability-based output) and why their output differs fundamentally from databases and compilers
- **Verifikationspflicht**: Why LLM-generated code always requires human verification — the model lacks project-specific constraints and specifications
- **Der agentische Zyklus**: The five-step iterative workflow (Prompt → Generate → Understand → Verify → Iterate) as the course's central methodology
- **Werkzeuglandschaft**: Overview of tools used in the course (Claude Code as primary tool), alongside Copilot and Cursor, sharing the principle of probabilistic output
- **Prompt-Struktur**: The five elements of an effective prompt (Role, Context, Task, Constraint, Output Format) with a step-by-step example
- **Code-Lesen**: A four-level reading strategy (Signature → Docstring → Tests → Implementation) and the "test-first reading" verification approach
- **Ingenieursverantwortung**: The role shift from code author to architect and verifier — the engineer remains fully accountable for production code
- **Kursstruktur**: Mapping of the agentive cycle across the four course blocks (B1–B4)

## Key takeways (What are the resulting takeways/skills teached)
- **LLMs generate plausible, not correct code** — verification is mandatory, not optional
- **Write prompts like requirements specifications** — include Role, Context, Task, Constraint, and Output Format
- **Constraints matter** — missing constraints lead to unexpected solutions (e.g., unnecessary library dependencies)
- **Read code in the right order** — Signature → Docstring → Tests → Implementation; never start with the implementation body
- **Write a test before reading the implementation** — this forces requirement-perspective thinking over implementation-perspective thinking
- **You are the senior engineer, the AI is your junior** — you remain fully responsible for code that ships to production
- **The agentive cycle repeats** — improve the prompt, regenerate, verify again until the requirement is safely met

## Code Examples (What code examples are shown)
- `celsius_to_kelvin` (no constraints) — demonstrates how a vague prompt leads the model to use `numpy` unnecessarily
- `celsius_to_kelvin` (with constraints) — demonstrates how adding "keine externen Bibliotheken" and type hints produces clean, requirement-compliant code
- Complete prompt example (step-by-step build) — shows evolving a vague prompt into a structured, five-element prompt for the temperature conversion task

## Visualizations (What image references are used)
- `images/01c_AgentischesProgrammieren/mj_title_band.jpg` — Title band image (cover art)
- `images/partA_3.svg` — Workflow diagram showing the lecture's sequence structure ("Ablauf")
- `images/01c_AgentischesProgrammieren/mj_question.png` — Question slide image: engineer inspecting a blueprint generated by a robot (referenced but not found on disk)
- `images/01c_AgentischesProgrammieren/mj_senior_engineer.png` — Visual metaphor of the engineer as architect and verifier (referenced but not found on disk)
- `images/01c_AgentischesProgrammieren/mj_title.mp4` — Animated title slide video background

## Plots
- None

## Examples (What examples are used)
- **Celsius-to-Kelvin conversion** — the central concrete example used throughout the lecture to demonstrate prompt evolution, the impact of constraints, and code review
- **"KI als Junior-Entwickler"** — the core metaphor framing the engineer's role: the AI is a junior developer; the human is the senior engineer who accepts the work
- **"Vibe Coding"** (Karpathy quote) — opening hook referencing Andrej Karpathy's concept of fully handing over to AI, used to contrast with the course's verification-first approach
- **Determinism comparison** — database queries, compilers, and LLMs compared side-by-side to illustrate why probabilistic output demands verification
- **Environmental monitoring project** — the contextual framing used in the prompt-building example to give the task a realistic scenario

## Remarks
- The lecture is delivered entirely in **German**, with key technical terms introduced alongside English equivalents (e.g., "Verifikation" (verification), "Merksatz" (key takeaway)).
- Three cross-references to other lectures: `04a_Anforderungen` (S04) for requirements/specifications, `08a_UnitTest` (S08) for test-driven verification, and `01a_Ueberblick` (S01) for the course overview.
- Two image files referenced in the lecture (`mj_question.png`, `mj_senior_engineer.png`) are **not found** on disk — the `01c_AgentischesProgrammieren/` directory only contains `mj_title_band.jpg`, `mj_title.mp4`, and `top_prog_languages.mp4`.
- The `top_prog_languages.mp4` asset is present on disk but **not referenced** in the `.qmdx` file content, suggesting it may be used in a different lecture or was intended but not yet linked.
- The lecture includes a **6-question quiz** covering LLM fundamentals, verification necessity, code-reading order, the engineer's role, prompt structure, and token prediction.
- The `%%note Merksatz:` blocks highlight two critical rules: "Verifikation ist Pflicht" (Verification is mandatory) and "Constraints sind Anforderungen" (Constraints are requirements).
- This lecture is a meta-level introduction — it deliberately does not contain deep programming exercises but rather establishes the mindset and framework for the entire course.
# Summary: Computerhardware

This lecture introduces the fundamental hardware architecture of modern computers and explains how all data is internally represented in binary form. It serves as the foundational bridge between abstract programming concepts and the physical machine that executes them. The lecture covers the core components — CPU, GPU, RAM, and storage — and walks through how high-level Python code is translated into machine-level instructions, establishing the mental model students need before diving deeper into memory management and data types in subsequent lectures.

## Main topics (What is the structure of the lecture)
- **Definition & Types of Computers**: Formal definition of a computer; overview of categories (supercomputers, mainframes, servers, PCs, laptops, smartphones, tablets, embedded systems)
- **Computer Hardware Architecture**: Core modules (CPU, GPU, RAM, HDD/SSD) and their roles; motherboard and communication bus
- **Memory Hierarchy**: Analogy to human memory — CPU/GPU registers (ultra-short-term), RAM (short-term/volatile), HDD/SSD (long-term/permanent)
- **CPU & Sequential Execution Model**: Instruction Pointer (Program Counter), register-based computation, transistors as logical gates
- **Memory Cells & Registers**: RAM cells with addresses and binary values; the data flow path from RAM → register → ALU → back to RAM
- **From Python to Machine Code**: Python source → bytecode → machine instructions; the disconnect between human-readable variable names and hardware addresses
- **Binary Number System**: Why computers use base-2; transistor states (on/off, true/false); binary representation of integers; hexadecimal as a compact notation
- **Binary Arithmetic**: Binary addition (XOR + AND gates), binary multiplication (bit-shifting and partial products)
- **Floating-Point Numbers**: IEEE 754 standard (sign bit, biased exponent, mantissa); approximation and rounding errors for real numbers
- **Character Encoding**: ASCII/Unicode mapping of characters to numbers and then to binary; example lookup tables
- **Image Representation**: Pixel grids, RGB color model (3 bytes per pixel), binary encoding of color values
- **Data Growth & Real-World Impact**: Exponential data growth (IDC Global DataSphere forecast); Tesco Ireland sensor/ML case study for energy savings
- **Learning Strategy (Lessons Learned)**: Memory consolidation, spaced repetition, and the role of subconscious processing in learning
- **Quiz**: 20-question review covering all topics

## Key takeways (What are the resulting takeways/skills teached)
- All data in a computer — numbers, text, images, programs — is stored as **binary** (sequences of 0s and 1s)
- The **CPU** executes instructions sequentially via the **Instruction Pointer**, using **registers** for active computation
- **Python code is translated** into many machine-level instructions; variable names are human labels, not hardware constructs
- The **memory hierarchy** (registers → cache → RAM → SSD) trades speed for permanence, mirroring human memory types
- **RAM is volatile** (lost on power-off); **SSD/HDD is non-volatile** (persistent storage)
- **Binary addition** maps to **XOR** (sum) and **AND** (carry) logic gates at the hardware level
- **Floating-point numbers** are approximations in IEEE 754 format — rounding errors are inherent and unavoidable
- **Characters and images** are ultimately stored as binary numbers: ASCII/Unicode for text, RGB pixel values for images
- **Memory units in computing** use powers of 1024 (KiB, MiB, GiB) rather than 1000 due to binary representation
- **Spaced (interval) learning** is the most effective way to retain knowledge long-term

## Code Examples (What code examples are shown)
- `z = x + y` → translated to four machine instructions (`LOAD`, `LOAD`, `ADD`, `STORE`) demonstrating how one Python line becomes multiple low-level operations
- ASCII/Unicode character-to-binary lookup tables (e.g., `a` → `01100001`, `A` → `01000001`, `0` → `00110000`)
- Decimal-to-binary conversion example: `13₁₀ = 1101₂` via decomposition into powers of 2
- Floating-point example: `-13.25` converted to IEEE 754 binary format (`1 10000010 10101000000000000000000`)
- RGB pixel encoding example: `(120, 200, 150)` → `01111000 11001000 10010110` (24-bit color)

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_2.svg` — Course structure/workflow diagram showing the lecture sequence
- `images/02a_Computerhardware/computer_hardware.svg` — Block diagram of computer hardware components (CPU, GPU, RAM, HDD/SSD)
- `images/02a_Computerhardware/computer_hardware2.svg` — Memory hierarchy visualization (registers → cache → RAM → storage)
- `images/02a_Computerhardware/binary_addition.svg` — Circuit diagram of a binary adder using XOR and AND gates
- `images/02a_Computerhardware/binary_multiply.svg` — Circuit diagram of binary multiplication using AND gates and adders
- `images/02a_Computerhardware/tesco.svg` — Case study diagram illustrating Tesco Ireland's sensor and ML energy-saving system
- `images/02a_Computerhardware/gedaechnis.svg` — Memory consolidation diagram illustrating learning intervals
- `images/02a_Computerhardware/mj_title_band.jpg` — Title banner image (Midjourney, inspired by Fritz Kahn)
- `images/02a_Computerhardware/image_5.jpg` — CPU wafer close-up (source: ial-fa.com)
- `images/02a_Computerhardware/image_10.png` — Pixel grid zoom of a digital image showing resolution breakdown
- `images/02a_Computerhardware/image_13.png` — Worldwide IDC Global DataSphere forecast chart (2022–2026)
- `images/02a_Computerhardware/mj_teddy.png` — Lessons Learned section image (DALL-E 2: teddy bear scientists)
- `images/02a_Computerhardware/image_1.jpg` — Brain/memory illustration (DALL-E 2: exploding brain)
- `images/02a_Computerhardware/image_3.png`, `image_4.jpg`, `image_6.png`, `image_15.jpg` — Humorous audience question images (Midjourney/DALL-E 2)

## Plots
- None

## Examples (What examples are used)
- **Tesco Ireland sensor/ML case study**: The supermarket chain deployed energy-monitoring sensors across stores; the data grew too large for manual analysis, so IBM Research applied machine learning to identify patterns that saved 20% of cooling energy
- **Human memory analogy**: CPU registers = ultra-short-term (like a notepad on your desk), RAM = short-term memory (volatile), HDD/SSD = long-term memory (persistent)
- **Binary number systems**: Decimal 13 → binary 1101 via decomposition into 2³ + 2² + 2⁰
- **Floating-point representation**: -13.25 broken down into sign bit, biased exponent, and mantissa in IEEE 754
- **"How far can you count with your fingers?"** audience question — interactive engagement about binary counting
- **"Which types of computers exist?"** audience question — review of computer categories
- **"What hardware makes up a computer?"** audience question — review of core components
- **"How many sensors does a supermarket have?"** audience question — transition to data growth topic
- **"What types of memory do you know?"** audience question — reflection prompt during Lessons Learned section

## Remarks
- The lecture is primarily **German-language** (slides and content in German), with this summary translated into English per instructions
- This lecture is **part A of Unit 2** (Computer Hardware) and serves as the hardware foundation before `02b_Speicher` (memory/stack/heap) and `02c_Datentypen` (data types)
- The course uses a **custom Quarto reveal.js theme** (`ai4sc-style-revealjs`) with integrated video title slides, custom icons (`{{< ai4sc-icon ... >}}`), and interactive elements
- A **20-question quiz** (`%%book` section with `quizdown` blocks) covers all major topics and is included at the end
- The **Instructions Pointer (IP)** concept uses the `□` symbol (Hollow Square) throughout the course to denote abstract variables/memory cells
- The lecture includes a **"Hörsaalfrage" (lecture hall question)** pattern — humorous slide prompts with custom backgrounds and AI-generated images to maintain engagement
- The **Lessons Learned** section is an intentional off-topic interlude focused on learning strategies and metacognition, not technical content
- Quiz questions reference material from **subsequent lectures** (`02b_Speicher`, `09b_Rekursion`) as forward-looking preview
- Some referenced image files (`.mp4`, `.svg`, `.png`) are not present in the current filesystem but are listed as they appear in the source
# Summary: Speicher

This lecture introduces Python's memory model, explaining that variables are **names bound to objects in memory** rather than containers holding values. It covers the distinction between mutable and immutable types, the phenomenon of **aliasing**, and the two fundamental memory regions — **stack** and **heap** — including how the call stack manages function frames and how garbage collection reclaims memory. The lecture concludes with practical **AI-code review workflows** to detect common memory-related bugs generated by AI tools and to read tracebacks as call-stack diagnostics.

Positioned as the second of three memory-focused lectures (following `02a_Computerhardware` and preceding `02c_Datentypen`), it builds a mental model of how Python manages data in RAM. The lecture is heavily oriented toward **agentic programming** — teaching students to critically review AI-generated code through the lens of Python's reference semantics.

## Main topics (What is the structure of the lecture)
- **Variablen als Referenzen**: Python variables are names pointing to objects; `id()` reveals object identity; small integers and strings are cached/interned.
- **Werttypen und Referenztypen**: Immutable types (`int`, `str`, `tuple`) vs. mutable types (`list`, `dict`, `set`) and the safety implications of aliasing.
- **Aliasing und Mutation**: Shared references cause unexpected side effects; `.copy()`, slicing, and `copy.deepcopy()` provide real copies.
- **Stack und Heap**: Stack (LIFO, function frames, fast, limited) vs. Heap (dynamic objects, garbage-collected, larger); both types of objects live on the Heap in Python.
- **Der Call Stack**: Stack frames for each function call, LIFO growth/shrinkage, recursion depth limits and `RecursionError` risk.
- **Der Heap und Garbage Collection**: Reference counting, objects surviving beyond local scope, cycle collection for circular references.
- **Engineering: KI-Fehler erkennen**: Mutation of input arguments and mutable default arguments as the two most common AI-generated bugs in Python.
- **Debugging: Tracebacks lesen**: Reading tracebacks bottom-up as a call-stack diagnostic to locate the true error source.

## Key takeways (What are the resulting takeways/skills teached)
- A Python variable is a **name bound to an object**, not a box containing a value — `id()` reveals the memory address.
- Use `==` for value equality and `is` for object identity; prefer `==` for own objects.
- Immutable types are **aliasing-safe** (no shared mutable state); mutable types require explicit copying (`.copy()`, slicing, `copy.deepcopy()`).
- Never use mutable objects (`list`, `dict`, `set`) as **default arguments** — use `None` and instantiate inside the function instead.
- AI-generated functions that mutate inputs (`.sort()`, `.append()`) silently destroy original data — verify with `id(eingabe) == id(rückgabe)`.
- The **call stack** grows on function entry and shrinks on return; deep recursion risks `RecursionError` — prefer iterative alternatives when needed.
- **Tracebacks are call stacks**: read from bottom (error location) to top (call origin) to diagnose issues.
- Python uses **reference counting** for garbage collection; circular references require a separate cycle collector.

## Code Examples (What code examples are shown)
- **`id()` and integer caching**: `x = 42; y = 42; print(id(x), id(y))` — demonstrates that small integers share the same memory address.
- **Rebinding and old-object removal**: `x = [1,2,3]; x = [4,5,6]` — shows that reassignment creates a new object and triggers garbage collection of the old one.
- **String interning and `is` vs `==`**: `a = "Hallo"; b = "Hallo"; c = a` — illustrates string caching, identity guarantee, and value equality.
- **Immutable aliasing safety**: `a = 42; b = a; b = b + 1; print(a)` — demonstrates that modifying one name does not affect the other for immutable types.
- **Mutable aliasing bug**: `a = [1,2,3]; b = a; b.append(4); print(a)` — shows how two names sharing a mutable object cause unintended side effects.
- **Explicit copying techniques**: `.copy()`, slicing (`a[:]`), and `copy.deepcopy()` — three ways to create real copies of lists.
- **Agentic check for mutation**: `lst.sort(); return lst` vs. `return sorted(lst)` — contrasts in-place mutation with functional-style non-mutation.
- **Stack and heap lifetimes**: `def berechne(x): y = x * 2; return y` — demonstrates local variable on stack vs. returned object on heap.
- **Garbage collection via reference counting**: `result = None` — shows how releasing the last reference triggers memory reclamation.
- **Traceback reading**: `berechne(x)` → `ZeroDivisionError` — bottom-up stack trace walkthrough.
- **Mutable default argument bug**: `def füge_messwert_hinzu(wert, liste=[])` — the classic Python trap; fixed version uses `liste=None`.

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/02b_Speicher/mj_title_band.jpg` — artistic title image for the lecture's book section.
- `images/02b_Speicher/mj_title.mp4` — video background for the Reveal.js title slide (generated with Midjourney: "Memory palace").
- **ASCII variable diagrams**: `x ──▶ Objekt: 42` and `x ──▶ [1,2,3]` — show the name-to-object reference model.
- **Stack diagram**: RAM layout with labeled Stack and Heap regions showing frame boxes and object blocks.
- **Stack/Heap interaction diagram**: Stack frames with arrows pointing to Heap objects (list `[1,2,3]`, integer `42`, string `"Hallo Welt"`).
- **Call Stack visualization**: Multi-frame stack showing `__main__`, `main`, and `berechne_fläche` with their local variables.

## Plots
- None

## Examples (What examples are used)
- **Matthew McConaughey quote** ("I never wrote things down so I could forget") — sets the theme of persistence vs. memory in the book section.
- **Two paths metaphor**: "Two paths leading to the same destination" (Midjourney image) for the Hörsaalfrage on `a = b`.
- **Messwerte (measurement values)**: `daten = [3.2, 1.1, 4.5, 2.0]` — real-world lab data scenario used throughout the mutation and AI-bug sections.
- **Fläche berechnen (area calculation)**: `berechne_fläche(breite=5, höhe=3)` — simple function used to demonstrate call stack frames.
- **Fakultät (factorial)**: Recursive `fakultät(n)` — demonstrates stack frame growth with recursion.
- **ZeroDivisionError debugging**: `berechne(x)` → `verarbeite(daten)` — traceable error chain from module entry through multiple functions.
- **KI als Junior-Entwickler** (implicit theme): Multiple "AI-generated — WRONG" code blocks frame the lecture around reviewing AI output critically.

## Remarks
- Cross-references: Prerequisite `02a_Computerhardware` is cited for memory hierarchy context; follow-ups `02c_Datentypen` (data type memory representations) and `09b_Rekursion` (recursion with call stack) are mentioned.
- The lecture is delivered in **German** but this summary is in English per instructions; German terms appear in parentheses on first reference (e.g. *Immutable*, *Veränderliche*, *Agentic Workflow*).
- The `%%note Merksatz:` blocks (e.g., `==` vs `is`, mutable default rule) are the primary "takeaway cards" students should memorize.
- The `%%warning` blocks are explicitly labeled as **Agentic Workflows** — practical checklists for verifying AI-generated code.
- No plotly plots or `.json`/`.pvd` animation files are present in this lecture.
- All memory diagrams are ASCII/text art, not vector graphics or SVG.
- The existing `02b_Speicher.summary.md` file found in the directory has been overwritten.
# Summary: Datentypen (Data Types)

This lecture introduces the foundational concept of **data types** in Python, framing them not merely as language syntax but as **modeling decisions** that determine how values are stored and interpreted in computer memory. It begins by explaining variables and Python's dynamic typing system, then systematically walks through simple (primitive) and composite (complex) data types — including numerics, booleans, strings, binary data, sequences, sets, dictionaries, and `None`. A recurring theme is the practical relevance of type choices for engineering applications, reinforced through an **agentic workflow** pattern that teaches students to verify and correct AI-generated code. The lecture concludes with a comprehensive quiz covering all type categories, mutability, and memory representation.

## Main topics (What is the structure of the lecture)
- **Variablen und Konstanten**: Definition, naming conventions, assignment rules, and Python's dynamic typing vs. static typing in other languages.
- **Einfache Datentypen (Primitive Types)**: Numerical (`int`, `float`), logical (`bool`), textual (`str`), and binary (`bytes`) types with memory representation details.
- **Zusammengesetzte Datentypen (Composite Types)**: Sequences (`list`, `tuple`, `range`), sets (`set`), and dictionaries (`dict`) — their syntax, mutability, and element access patterns.
- **Null-Werte (`None`)**: The purpose of `None`, the `NoneType`, and the inherent ambiguity between "undefined" and "explicitly None" values.
- **Mutability**: Mutable vs. immutable data types, with a comparison table of Python's mutable (`list`, `set`, `dict`, `bytearray`) and immutable (`tuple`, `frozenset`, `frozendict`, `bytes`) counterparts.
- **Agentic Workflow — Typprüfung**: A structured approach to verifying AI-generated type choices (e.g., `int` vs. `float` for physical measurements) and correcting them.
- **Übung & Quiz**: Hands-on exercise with a wall-area calculation bug, followed by a 19-question multiple-choice quiz covering all type categories.

## Key takeways (What are the resulting takeways/skills teached)
- Python is a **dynamically typed** language — types are determined at assignment time, not declared upfront.
- Variable naming should use **snake_case**, be descriptive, avoid special characters (ä, ö, ü, ß), and never use reserved keywords.
- The choice between `int` and `float` is a **modeling decision**, not a stylistic one — wrong type choice causes precision errors.
- Use `type(variable)` to check a variable's actual type, especially when reviewing **AI-generated code**.
- `list` is mutable (can be modified in place); `tuple` is immutable (cannot be changed after creation).
- Negative indexing (`list[-1]`) and slicing (`list[0:10]`) are Python convenience features for accessing list portions.
- `set` automatically deduplicates values and provides efficient membership testing with the `in` operator.
- `dict` maps unique keys to values and supports dynamic key/value assignment and deletion via `del`.
- `None` represents a missing/undefined value, but distinguishing "not present" from "explicitly None" requires sentinel values (e.g., `dict.get(key, default)`).
- `bytes` (prefix `b"..."`) is Python's binary type; individual bytes are accessed as `int` values (0–255).
- Python's `str` covers both single characters and multi-character strings — no separate `char` type exists.

## Code Examples (What code examples are shown)
- `nummer = 1` followed by `print(nummer)` and `nummer` (implicit print): Basic variable assignment and display in a notebook.
- `nummer = 2` → `print("Wert:", nummer, "\nDatentyp:", type(nummer))`: Demonstrating dynamic type reassignment and `type()` inspection.
- `nummer = "text"` → `print("Wert:", nummer, "\nDatentyp:", type(nummer))`: Reassigning a variable to a different type (numeric → string).
- `hoehe = 3; breite = 5; flaeche = hoehe * breite` vs. `hoehe: float = 2.85; breite: float = 4.70`: Contrasting `int` precision loss vs. correct `float` usage for physical measurements.
- `zeichen = 'a'` and `zeichenkette = 'hallo welt'`: Demonstrating that Python uses `str` for both single characters and strings, with `len()` showing lengths 1 and 11.
- `"hallo 'welt'"` and `'hallo \'welt\''`: Nested quoting — using alternating quote styles vs. explicit escaping with `\`.
- `f"der wert von nummer ist '{nummer}'"`: Demonstrating f-strings for inline variable interpolation.
- `wort = b"byte"` and `wort[0]`: Creating a `bytes` object and accessing individual byte elements as `int`.
- `liste = [1, 2, 3, "a", True]` with `liste[1] = "anders"` and `liste.append(False)`: Demonstrating mutable list element modification and dynamic length change.
- `tuple = (1, 2, 3, "a", True)` with attempted `tuple[0] = True` (error): Demonstrating `tuple` immutability.
- `zahlenfolge = range(1, 10)`: Creating a `range` object for integer sequences.
- `liste[0]`, `liste[-1]`, `liste[0:10]`, `liste[:10]`, `liste[-10:]`: Positive indexing, negative indexing, and slicing patterns.
- `menge = {1, 2, 3}` and `1 in menge`: Creating a set and membership testing.
- `set(listmitwiederholung)` to deduplicate: Using `set()` to remove duplicates from a list.
- `haus = {"Gebäudetyp": "Wohnhaus", "Baujahr": 2022}` with `haus['Material'] = "Stein"` and `del haus['Material']`: Dict creation, dynamic key addition, and deletion.
- `haus.get('schluessel_fehlt')` and `haus['ist_none'] = None`: Demonstrating the ambiguity of `dict.get()` returning `None` for both missing and explicitly `None` keys.
- `hoehe = 3; breite = 5; flaeche = hoehe * breite` (KI exercise): A complete wall-area calculation task where students identify the `int` type error and correct it with `float` values and type annotations.

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/02c_Datentypen/mj_title_band.jpg` — Artistic title banner image (Midjourney, referencing Henri Rousseau style).
- `images/02c_Datentypen/datentyp1.svg` — Classification diagram showing the split between **simple (primitive)** and **composite (complex)** data types.
- `images/02c_Datentypen/datentyp2.svg` — Memory representation overview of numeric types (`int`, `float`, `bool`) with bit-level storage.
- `images/02c_Datentypen/datentyp3.svg` — Python-specific numeric type mapping (`int` for whole numbers, `float` for reals).
- `images/02c_Datentypen/datentyp4.svg` — Boolean/logical type diagram showing `True`/`False` values.
- `images/02c_Datentypen/datentyp5.svg` — Python `bool` type visualization.
- `images/02c_Datentypen/datentyp6.svg` — Textual type classification: `Char` (single character) vs. `String` (multi-character).
- `images/02c_Datentypen/datentyp7.svg` — Python `str` type visualization covering both chars and strings.
- `images/02c_Datentypen/datentyp8.svg` — Binary type classification: `Byte` (single) vs. `Bytearray/Bytestring` (multiple).
- `images/02c_Datentypen/datentyp9.svg` — Python `bytes` type visualization.
- `images/02c_Datentypen/datentyp10.svg` — Sequence type diagram: ordered collections with index-based access.
- `images/02c_Datentypen/datentyp11.svg` — Set and Dictionary classification diagrams (shared visual).
- `images/02c_Datentypen/datentyp11a.svg` — Python sequence types (`list`, `tuple`, `range`) visualization.
- `images/02c_Datentypen/datentyp11b.svg` — Python `set` type visualization.
- `images/02c_Datentypen/datentyp11c.svg` — Python `dict` type visualization with key-value pairs.
- `images/02c_Datentypen/datentyp12.svg` — Null/undefined value diagram (`None` type).
- `images/partA_3.svg` — Lecture flow/structure diagram shown at the beginning.
- `images/02c_Datentypen/mj_title.mp4` — Video background for the title slide.

## Plots
None — this lecture contains no plotly or data visualization plots.

## Examples (What examples are used)
- **"KI als Junior-Entwickler" pattern**: The lecture repeatedly frames AI-generated code as something that needs human verification — the `distanz = 5` example (wrong type → should be `float`) is the core illustration.
- **Wall area calculation exercise**: A complete scenario where AI generates code using `int` for wall dimensions, and students must identify the precision loss and correct it with `float` and type annotations.
- **Building properties dictionary**: `haus = {"Gebäudetyp": "Wohnhaus", "Baujahr": 2022}` — a concrete, relatable example for introducing `dict` syntax.
- **Name deduplication with sets**: Using `set()` on a list `[1, 2, 2, 2, 2, 2, 3]` to extract unique values — a practical use case for set deduplication.
- **Naming convention examples**: A detailed comparison table of good (`age`, `first_name`, `birth_year`, `email_address`, `is_on`, `product_list`, `score_total`, `user_count`) vs. bad (`a`, `fn`, `by`, `email`, `on`, `products`, `score`, `count`) variable names.
- **Cross-reference to `02a_Computerhardware`**: The lecture explicitly references the prior lecture for understanding how data is stored as binary bit sequences in memory.

## Remarks
- The lecture is taught in **German** but this summary is written in English per instructions. Original German terms appear on first reference where relevant (e.g., *Modellierungsentscheidung* (modeling decision), *Syntaxzucker* (syntax sugar)).
- This is lecture **02c** in the **S02** module of "Programmieren und Datenbanken" (Programming and Databases), part of the **ai4sc-style** course framework (AI for Science).
- The lecture intentionally emphasizes an **agentic workflow** — the practice of verifying and correcting AI-generated code — as a recurring pedagogical pattern, not just a one-off topic.
- Python's `None` ambiguity (whether a `dict.get()` returning `None` means "key missing" or "key explicitly set to None") is flagged as a well-known software engineering problem, similar to Java's issues with null references.
- The quiz at the end (19 questions, via `quizdown`) covers all topics and is configured with shuffled questions and answers.
- The lecture does **not** contain any animated plots or interactive visualizations — all visuals are static SVG diagrams.
- The `%%note`, `%%tip`, and `%%warning` custom blocks are used sparingly, primarily for the agentic workflow sidebar and the `None` caveat.
- The `%%def` blocks define formal terminology (Variable, Konstante, Datentyp, Mutability) in both the `%%book` and `%%slides` sections, providing a consistent glossary across formats.
# Summary: Wissenspyramide

This lecture introduces the **Wissenspyramide** (Knowledge Pyramid) as the central conceptual framework of the entire course. It maps the progression from raw **characters** ("Zeichen") at the base, through **syntax**, **data**, **semantics**, **information**, and **processing** ("Verarbeitung"), up to **knowledge** ("Wissen") at the apex. Each level of the pyramid corresponds to a course block, and students climb the pyramid as they advance through the semester.

The lecture uses analogies from natural language (German grammar), HTML, and Egyptian hieroglyphs to illustrate how each transformation in the pyramid works — from mere symbols to meaningful, actionable knowledge. A significant portion is dedicated to positioning **AI tools** (e.g., GitHub Copilot, Claude) within the pyramid, emphasizing that AI operates at the data-to-information boundary and that the engineer's responsibility is to verify that AI-generated code carries correct engineering meaning.

Finally, the lecture closes with a meta-reflection on learning styles ("Lerntypen") — visual, auditory, and haptic — encouraging students to leverage multiple sensory channels for more effective learning.

## Main topics (What is the structure of the lecture)
- **Einführung der Wissenspyramide**: Conceptual backbone of the course; each level maps to a course block (Blocks 1–6)
- **Kurs-Karte**: Explicit table mapping pyramid levels to transformations (Zeichen→Daten→Informationen→Verarbeitung→Wissen) and their corresponding course blocks
- **Wo sitzt KI?**: AI tools operate at the data→information boundary; the engineer must verify engineering meaning
- **Zeichen → Syntax → Daten**: Definitions and examples for the first three pyramid levels, using German grammar, HTML, and ASCII character encoding
- **Daten → Semantik → Informationen**: Meaning interpretation; dictionaries as semantic references, HTML DOM trees as semantic structures
- **Informationen → Verarbeitung → Wissen**: Connecting information via algorithms and context to derive knowledge; browser rendering as a processing example
- **Hieroglyphen-Anwendung**: Interactive quiz using Egyptian hieroglyphs to apply all six pyramid concepts
- **Lerntypen**: Learning style categories (visual, auditory, haptic) and strategies for type-specific studying
- **Quiz**: 11-question quizdown quiz reinforcing definitions of all pyramid elements

## Key takeways (What are the resulting takeways/skills teached)
- Understand the **Wissenspyramide** as the course map: every lecture builds one level higher
- **Zeichen** are the atomic units (letters, digits, punctuation); **Syntax** is the rule system for composing them
- **Daten** are syntactically well-formed representations; **Semantik** provides their interpretation rules
- **Informationen** are data endowed with meaning and purpose; **Verarbeitung** links information via algorithms and expertise
- **Wissen** is integrated, experience-backed knowledge that enables decisions and actions
- **AI-generated code is syntactically valid but semantically unverified** — the engineer must cross the data→information boundary
- The **Agentenworkflow** (agent workflow) sits precisely at the data→information interface: verify that AI output solves the correct engineering problem
- Effective learning leverages **multiple sensory channels** (visual, auditory, haptic), not just one's preferred type
- Hieroglyphs provide a concrete analogy: individual glyphs = Zeichen, column reading direction = Syntax, glyph meanings = Semantik, contextual interpretation = Verarbeitung

## Code Examples (What code examples are shown)
- **HTML table snippet**: A basic `<table>` with `<tr>` and `<td>` elements used to illustrate how syntax produces a tree structure (Daten) and how interpretation yields meaning (Informationen)
- **Mermaid DAG (HTML tree)**: `graph TD` diagram showing the hierarchical structure of HTML elements (`table` → `tr` → `td1`, `td2`)
- **Mermaid DAG (processed HTML)**: Same structure but with computed attributes (`width=300`, `height=50`, cell widths halved), illustrating processing/Verarbeitung
- **Quizdown quiz**: 11 interactive multiple-choice questions covering definitions of every pyramid level and hieroglyph application

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_2.svg` — Part A workflow diagram showing lecture sequencing
- `images/03a_Wissenspyramide/wissenspyramide.svg` — The core pyramid visualization with four levels (Zeichen, Daten, Informationen, Wissen)
- `images/03a_Wissenspyramide/pyramide1.svg` — Pyramid highlighting the **Zeichen** level at the base
- `images/03a_Wissenspyramide/pyramide2.svg` — Pyramid highlighting the **Syntax** level
- `images/03a_Wissenspyramide/pyramide3.svg` — Pyramid highlighting the **Daten** level
- `images/03a_Wissenspyramide/pyramide4.svg` — Pyramid highlighting the **Semantik** level
- `images/03a_Wissenspyramide/pyramide5.svg` — Pyramid highlighting the **Informationen** level
- `images/03a_Wissenspyramide/pyramide6.svg` — Pyramid highlighting the **Verarbeitung** level
- `images/03a_Wissenspyramide/pyramide7.svg` — Pyramid highlighting the **Wissen** level at the apex
- `images/03a_Wissenspyramide/pyramide8.svg` — Complete pyramid with all levels shown
- `images/03a_Wissenspyramide/syntax.svg` — Python syntax elements illustration
- `images/03a_Wissenspyramide/semantik.svg` — Python semantic elements illustration
- `images/03a_Wissenspyramide/lerntypen.svg` — Learning types diagram (visual/auditory/haptic)
- `images/03a_Wissenspyramide/test.svg` — Learning style self-test worksheet
- `images/03a_Wissenspyramide/hyroglyphe.jpg` — Egyptian hieroglyphs image used for interactive questions
- `images/03a_Wissenspyramide/hyroglyphe2.jpg` — Hieroglyphs answer illustration
- `images/03a_Wissenspyramide/hieroglyphs.png` — PNG version of hieroglyphs image used in quiz
- `images/03a_Wissenspyramide/wissenspyramide_quizz1.png` — Quiz pyramid diagram for ordering exercise
- `images/03a_Wissenspyramide/mj_title_band.jpg` — Midjourney title band image (Tower of Babel theme)

## Plots
- None

## Examples (What examples are used)
- **German language**: "Ich Bahnhof nur verstehe" (syntactically correct but meaningless) → "Ich verstehe nur Bahnhof" (correct idiom meaning "I don't understand anything")
- **HTML as a tree**: `<table>` → `<tr>` → `<td>` demonstrates data→information→processing
- **Egyptian hieroglyphs**: Individual glyphs = Zeichen, column layout = Syntax, glyph meanings = Semantik, contextual reading = Verarbeitung
- **Web browser rendering**: Interprets HTML tags and computes cell widths (2×150px) from a 300px table — an example of Verarbeitung
- **AI as "Junior Engineer"**: AI generates syntactically valid code (Daten level) but cannot guarantee it solves the right engineering problem (Informations level) — the human engineer must verify
- **Midjourney "Six Sense"**: Animated video used as a meta-reflection on how senses relate to learning

## Remarks
- The lecture is entirely in **German** (except for this English summary); key German terms are retained in parentheses on first reference.
- No traditional programming code (Python, R, etc.) is present — the lecture is purely **conceptual/theoretical**, establishing the course's foundational vocabulary.
- The lecture includes an animated title video (`mj_title.mp4`) referencing the Tower of Babel, thematically linking knowledge fragmentation with the pyramid metaphor.
- A separate animation `mj_senses.mp4` plays on the "Six Sense" slide but its content is commented out in the source.
- The course is structured into **6 blocks**: Block 1 (Datentypen), Block 2 (Computational Engineering), Blocks 3–5 (Implementierung), Block 6 (Datenbanken).
- Quiz questions use the **quizdown** Quarto extension with shuffle enabled.
- The lecture intentionally uses **no deep code** — it focuses on mental models and vocabulary.
# Summary: Softwarearchitektur

This lecture traces the historical evolution of **software architecture** — from monolithic, machine-code programs of the pre-1950 era to the distributed, cloud-native systems of today. It establishes a core thesis: architecture is not an afterthought but a **pre-code decision** that defines what any system (human-written or AI-generated) can achieve. The lecture argues that every architectural shift — operating systems, virtualization, client-server separation, containerization — was a response to requirements outgrowing existing boundaries, and that **AI code generation operates within whatever architectural limits the engineer sets**.

The second half of the lecture pivots to the **agentive era**, where AI tools like Claude Code can generate individual functions, classes, and modules, but cannot decide component boundaries, relationships, or responsibilities. These remain the domain of the software engineer. The lecture explicitly connects this content to lecture `03a_Wissenspyramide` (the information layer maps to architecture) and `03c_Softwareentwurf` (UML and process models are the tools for designing architecture before writing code).

## Main topics (What is the structure of the lecture)
- **Historical overview**: Five eras of software architecture (pre-1950 → 1960s OS → 1970s high-level languages → 1995 virtualization → 2000 distributed/web → 2010 cloud/container)
- **Architectural lessons per era**: Each era demonstrates that tight coupling creates rigidity, and adding abstraction layers increases freedom at the cost of complexity or overhead
- **Agentive era**: AI generates components (functions, classes, modules) but cannot define inter-component relationships — that is the engineer's responsibility
- **Prompt boundaries as architecture**: Every prompt implicitly defines architectural boundaries; good architecture is decided before the first `%%note` prompt
- **Cross-lecture integration**: Links to `03a_Wissenspyramide` (information layer ↔ architecture layer) and `03c_Softwareentwurf` (UML/modeling as pre-prompt tools)

## Key takeways (What are the resulting takeways/skills teached)
- **Software fails at the architectural level, not the code level** — poor architecture cannot be fixed by better code
- **Every abstraction layer decouples but adds complexity** — adding OS, runtime, or virtualization layers increases portability at the cost of overhead
- **AI code generation is bounded by the prompt's architectural assumptions** — defining component boundaries in a prompt is itself an architecture decision
- **Clear component boundaries enable independent scaling** — but they must be decided before writing code, not retrofitted
- **Pre-prompt workflow**: (1) Identify components, (2) Define their boundaries, (3) Specify inter-component communication, (4) Generate each component separately
- **Architectural decisions outlive code** — code gets rewritten; architecture endures

## Code Examples (What code examples are shown)
- None — this lecture is conceptual and historical; it contains no executable code blocks (the quiz content uses `{quizdown}` markup, not executable code)

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_2.svg` — "Ablauf" (workflow) diagram showing the overall process flow
- `images/03b_Softwarearchitektur/archi_1.svg` — Pre-1950 monolithic architecture: **Programm ↔ Hardware** (direct coupling, no abstraction)
- `images/03b_Softwarearchitektur/archi_3.svg` — 1960s architecture: **Programm → Betriebssystem → Treiber → Hardware** (first abstraction layer)
- `images/03b_Softwarearchitektur/archi_5.svg` — 1970s architecture: **Quellcode → Compiler → Betriebssystem → Hardware** (high-level language decoupling)
- `images/03b_Softwarearchitektur/archi_7.svg` — 1995+ architecture: **Programm → Laufzeitumgebung → Betriebssystem → Hardware** (virtualization layer)
- `images/03b_Softwarearchitektur/archi_8.svg` — 2000+ distributed architecture: **Frontend → Backend → Datenbank** (explicit component boundaries)
- `images/03b_Softwarearchitektur/archi_10.svg` — 2010+ cloud architecture: **Service → Container → Cloud-Infrastruktur → Nutzer** (scalable distributed systems)
- `images/03b_Softwarearchitektur/archi_11.svg` — Classification of programming languages by historical application
- `images/02a_Computerhardware/computer_hardware2.svg` — Review diagram of computer hardware architecture
- `images/03b_Softwarearchitektur/mj_title_band.jpg` — Title page decorative image
- `images/03b_Softwarearchitektur/mj_datariver.png` — Background visual for binary numbers review question
- `mj_title.mp4` — Background video for the title slide

## Plots
- None — no plotly or data visualization plots are used in this lecture

## Examples (What examples are used)
- **Historical progression as case studies**: Each architectural era (pre-1950 → 2010s) serves as a concrete example of how requirements outgrew existing architectures, forcing a new design
- **"KI als Junior-Entwickler" analogy**: AI generates code like a junior developer — it can write functions and classes, but doesn't decide the system's overall structure
- **Sensor data prompt example**: Asking Claude Code to "read sensor data and output a warning" bundles two concerns into one component — an implicit architectural decision with long-term consequences
- **Quiz review questions**: Reinforce historical milestones (binary code pre-1950, OS abstraction 1960s, virtualization 1995, cloud 2010) and the limits of AI code generation
- **Louis Kahn quote**: "Good architecture is not just about structure — it's about intention" — framing architecture as purpose-driven design, not just technical organization

## Remarks
- The lecture is written primarily in **German** with English technical terms retained where appropriate
- It intentionally contains **no executable code** — this is a conceptual/architectural lecture that sets up the practical exercises in later sessions
- The lecture uses **%%note Merksatz:** blocks (labeled "Architekturlektion" and "Agentic Workflow") to distill actionable mental models from each historical era
- Cross-references to lectures `03a_Wissenspyramide` and `03c_Softwareentwurf` position this lecture as the architectural bridge between data theory (03a) and design modeling (03c)
- The opening "Hörsaalfrage" (auditorium question) review of "Was ist Informatik?" ties back to lecture `01a_Ueberblick`, reinforcing course continuity
- The resource directory `data/02a_Softwarearchitektur` is referenced but not directly accessed in this summary
# Summary: Softwareentwurf

This lecture introduces the bridge between a stakeholder's natural-language requirement and actual Python code. It presents a structured software engineering pipeline — requirement definition, design, implementation, and acceptance — and positions **UML class diagrams** as the formal language that translates requirements into a design that can be handed to a developer or a KI coding assistant. The lecture culminates in a concrete **BIM (Building Information Models)** example that walks through the full "Anforderung → UML → KI-Prompt → Verifikation → Code" workflow.

The lecture also surveys four **process models** (Wasserfall, V-Modell, Agile, and the **agentischen Loop**) and explains when each is appropriate based on requirements stability, safety criticality, team size, and the availability of AI tools. By framing the agentischen Loop as a formal fourth process model, the lecture connects this topic back to Lecture `01c_AgentischesProgrammieren` and shows how the human's core competence shifts from writing code to **Verstehen und Verifizieren** (understanding and verifying).

## Main topics (What is the structure of the lecture)
- **Anforderung → Code-Lücke**: The gap between a stakeholder's requirement and what a developer needs; the four-phase development pipeline (Anforderungsdefinition, Entwurf, Ausführung, Abnahme)
- **Vorgehensmodelle (Process Models)**: Wasserfall (sequential), V-Modell (safety-critical, test-driven), Agile (iterative, MVP-first), and Agentischer Loop (KI generates, human verifies)
- **UML Klassendiagramme**: Class structure (name, attributes, methods), notation for attributes and methods, and the role of class diagrams as a bridge between requirement and prompt
- **Referenzen zwischen Klassen**: Three relationship types — **Assoziation**, **Aggregation**, and **Komposition** — with cardinality/multiplicity notation
- **Vererbung (Inheritance)**: Subclass/superclass relationships with filled-triangle notation; a large polygon inheritance hierarchy as a worked example
- **BIM Anwendungsbeispiel (Case Study)**: Full end-to-end flow from a natural-language building requirement → UML class diagram → KI prompt → verification checklist

## Key takeways (What are the resulting takaways/skills teached)
- Every project starts with a **Klassenmodell** (class model) that answers which classes, attributes (with types), methods (with signatures), and relationships are needed
- The **UML class diagram** is an ISO-standard visualization that serves as both design documentation and a precise prompt for KI code generation
- **Komposition** (the part cannot exist without the whole) vs **Aggregation** (the part can exist independently) vs **Assoziation** (independent objects)
- The **agentischen Loop** maps sprint planning → Prompt formulation, sprint → KI code generation, sprint review → human verification, retrospective → prompt refinement
- In the AI-augmented workflow, the engineer's core skill is **Verifizieren** (understanding and verifying KI output), not typing code
- Process model choice depends on: requirements stability, safety criticality, team size, and KI tool availability

## Code Examples
- **UML Mermaid class diagram for `Point`** (`03c_Softwareentwurf.qmdx:91-96`): Minimal class showing attribute `+float x` and method `+float distance(Point p)` — demonstrates the three-level class structure
- **UML Mermaid for Aggregation, Composition, Association** (`03c_Softwareentwurf.qmdx:565-583`): Side-by-side diagrams showing each relationship type with multiplicity (`"1" o-- "1..*"`, `"1" *-- "1..*"`, `"1" --> "1..*"`)
- **UML Mermaid for `Line` → `Point` aggregation** (`03c_Softwareentwurf.qmdx:650-661`): `Line` aggregates exactly 2 `Point` objects (start, end) — demonstrates multiplicity in context
- **Inheritance hierarchy** (`03c_Softwareentwurf.qmdx:699-713`): `Polygon` superclass with `Triangle`, `Tetragon`, `Pentagon` subclasses using `--|>` notation — demonstrates inheritance visualization
- **Full polygon hierarchy diagram** (`03c_Softwareentwurf.qmdx:731-775`): Large multi-level class diagram with composition, inheritance chains (Triangle → Scalene → Isosceles → Equilateral, Tetragon → Parallelogram → Rectangle → Square, Kite → Rhombus)
- **BIM example UML** (`03c_Softwareentwurf.qmdx:828-847`): `Building`, `Room`, `Window` class diagram with associations (`1 → 1..*`, `1 → 0..*`) — the complete design for the case study

## Visualizations
- `images/partA_6.svg` — Structural diagram showing the lecture's place in the course (Ablauf overview)
- `images/03c_Softwareentwurf/waterflow.svg` — **Waterfall model** workflow diagram (sequential phases)
- `images/03c_Softwareentwurf/vmodel.svg` — **V-Modell** diagram showing development arm (left) and testing arm (right) with their corresponding activities
- `images/03c_Softwareentwurf/agile.svg` — **Agile development** iterative cycle diagram showing MVP and recurring release sprints
- `images/03c_Softwareentwurf/ifc_classes.jpg` — Real-world **IFC class hierarchy** from Building Information Modeling, showing how industry standards use OO concepts like inheritance and specialization
- `images/03c_Softwareentwurf/mj_title_band.jpg` — Title band image (Midjourney, "Waterfall in chinese mountain range")
- `images/03c_Softwareentwurf/waterfall.png` — Background image for the opening "Hörsaalfrage" slide
- `images/03c_Softwareentwurf/mj_title.mp4` — Title slide background video (Midjourney waterfall)
- **Mermaid class diagrams** (embedded): Multiple interactive mermaid diagrams for class structure, relationships, inheritance, and the BIM example

## Plots
- None

## Examples
- **Wasserverbrauch-Berechnung**: A stakeholder request to calculate a building's water consumption per room — used to illustrate the gap between natural-language requirements and developer specifications
- **BIM (Building Information Models)**: A full case study where a building has rooms, each room has windows; the program should calculate total window area per room — demonstrates the entire pipeline from requirement → UML → prompt → verification → code
- **Vergleich Software- vs. Bauingenieurwesen**: Side-by-side comparison of software development phases (Anforderung, Entwurf, Ausführung, Abnahme) with civil engineering equivalents (Ausschreibung, Entwurf, Ausführung, Abnahme)
- **Polygon-Inheritance-Hierarchie**: A rich geometry example (`Polygon` → `Triangle` → `Scalene_Right` → `Isosceles_Right` → `Equilateral`) that demonstrates how inheritance chains scale in UML
- **KI als Junior-Entwickler (implied)**: The agentischen Loop frames the KI as the code generator (the "junior developer") while the human engineer acts as reviewer and verifier
- **IFC-Standard**: Reference to Industry Foundation Classes used in real construction drawings as a concrete industry example of object-oriented modeling

## Remarks
- The lecture is in **German** throughout, with English terminology retained for technical terms (e.g., **UML**, **MVP**, **BIM**)
- Cross-references: The agentischen Loop was previously introduced in `01c_AgentischesProgrammieren`; UML application to Python classes will be covered in `04c_Objects` (S04)
- The Mermaid class diagrams are the primary visual learning tool — they are rendered as static diagrams (not animated plots)
- The `%%book` blocks contain the substantive explanatory prose, while `%%slides` blocks are presentation summaries with code and diagrams
- The lecture intentionally stays at the design/modeling level and does not dive deep into implementation code — it focuses on **how to think about the design before writing code**
- The four process models are presented as a spectrum from rigid (Wasserfall) to flexible (Agil) to AI-augmented (Agentisch)
# Summary: Anforderungen — Vom Problem zum Prompt

This lecture introduces the foundational role of **requirement analysis** in AI-assisted software development. It argues that large language models and agentic coding tools (e.g., Claude Code) faithfully execute the prompts they are given, but cannot independently determine whether those prompts address the right problem. Therefore, systematic requirement engineering — identifying stakeholder needs, categorizing requirements, and formulating measurable acceptance criteria — is the indispensable prerequisite for both effective prompting and meaningful testing. The lecture establishes a unifying framework called the **Traceability Triangle** linking requirements, prompts, and tests as three interdependent artifacts.

The core thesis is that requirement analysis is not a separate phase but the continuous source of truth for every step in the agentic development cycle. A well-structured requirement becomes a precise prompt, which in turn yields objectively verifiable tests. The lecture introduces **Test-Driven Prompting** — a variant of Test-Driven Development adapted for AI-assisted development — where acceptance criteria are first written as tests before any code or prompt is produced.

## Main topics (What is the structure of the lecture)
- **Why requirements matter**: Requirements are the source of both the prompt and the test; without them, neither prompting nor verification is possible
- **Three categories of requirements**: Functional (what the system must do), non-functional (how well), and constraints (what limits the solution space)
- **Stakeholder perspectives**: Different roles derive different requirements from the same system; conflict identification and prioritization
- **Quality criteria for requirements**: Translating vague wishes into measurable acceptance criteria; patterns across domains
- **User Stories**: The role/function/benefit template as a natural bridge from requirements to prompts
- **From requirement to prompt**: Two-step conversion of user stories into structured Claude Code prompts
- **From requirement to test**: Direct translation of acceptance criteria into unit tests (pytest)
- **Test-Driven Prompting**: Writing tests before prompts and code to ensure objective verification
- **The Traceability Triangle**: Requirements, prompts, and tests as three interdependent artifacts where any change requires updating all three

## Key takeways (What are the resulting takeways/skills teached)
- **Treat requirements as the single source of truth** — they feed both the prompt and the test in the agentic development cycle
- **Classify every requirement** into functional, non-functional, or constraint to ensure completeness
- **Write measurable, testable requirements** — vague statements like "fast" or "stable" are useless for prompting and testing
- **Every non-functional requirement needs a quantitative acceptance criterion** — otherwise it cannot be verified
- **Use the User Story template** (As a [role], I want [function], so that [benefit]) to structure requirements for AI prompt consumption
- **Apply Test-Driven Prompting**: write acceptance tests before prompts and code, so verification is objective and automated
- **Maintain the Traceability Triangle** — any change to requirement, prompt, or test must update all three simultaneously
- **Conflict between stakeholder requirements is normal** and must be explicitly negotiated, not implicitly resolved

## Code Examples (What code examples are shown)
- `test_dashboard_load_time()`: Measures elapsed time for dashboard load and asserts it is under 2 seconds — demonstrates converting a performance acceptance criterion into a pytest test
- `test_alarm_acknowledgment()`: Creates an alarm, acknowledges it, and asserts the UTC timestamp and user fields are set — demonstrates converting a functional acceptance criterion into a unit test
- Prompt context block: Structured prompt template with role, task, user, and goal fields derived from a User Story — demonstrates step 1 of requirement-to-prompt conversion
- Full prompt block: Complete Claude Code prompt for a Streamlit sensor-alarm dashboard with requirements and test instructions — demonstrates step 2 of requirement-to-prompt conversion

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/04a_Anforderungen/mj_title_band.jpg` — Title image for the book section
- `images/04a_Anforderungen/mj_engineer_blueprint.png` — Civil engineer reviewing a digital blueprint with an AI assistant (title slide visual)
- ASCII diagram of the **Traceability Triangle** (Anforderung ↔ Prompt ↔ Test) — illustrates the three-way dependency relationship

## Plots
- None

## Examples (What examples are used)
- **Bridge sensor monitoring system** — A running贯穿 example throughout the lecture: moisture and temperature sensors on a bridge structure, used to illustrate all three requirement categories, stakeholder perspectives, and requirement-to-prompt conversion
- **Three stakeholder perspectives**: Tragwerksplaner (structural engineer), Facility Manager, and Behördenprüfer (regulatory inspector) — each with distinct needs from the same underlying sensor data
- **Henry Ford quote** ("faster horses") — illustrates the classic problem of stakeholders describing solutions rather than needs
- **AI as Junior-Entwickler** (implied): The metaphor that AI fulfills the prompt, not the underlying need — the developer is the bridge between stakeholder needs and AI-generated code
- **Common errors table**: Examples of vague/untestable/implementation-oriented requirements vs. measurable/testable/problem-oriented ones

## Remarks
- Cross-references to other lectures: `01c_AgentischesProgrammieren` (prompt structure), `03c_Softwareentwurf` (requirements precede design), `04b_Programmablauf` (flowcharts operationalize requirements), `08a_UnitTest` (deep dive into pytest unit testing)
- The lecture is delivered in **German** within an English-language course; key German terms are retained (e.g., "Anforderungen" (requirements), "Randbedingungen" (constraints))
- Uses the **ai4sc-style** Quarto extension with the "mineral" theme and a Midjourney-generated background video (`mj_title.mp4`) for the HTML slides
- No interactive plots or Plotly visualizations — this lecture is conceptually focused rather than code-heavy
- The `%%note Definition: Anforderung` and `%%tip Merksatz` blocks highlight two key mental models: requirements describe what, not how; and every non-functional requirement needs a quantitative acceptance criterion
- The lecture intentionally does not teach deep coding — it prepares the ground for later practical sessions on prompting, testing, and software design
# Summary: Programmablauf

This lecture introduces **program flow** as a foundational concept in engineering-oriented programming: before writing code or formulating prompts, one must design the logic of a program using **flowcharts** (Programmablaufpläne / Flussdiagramme). The core thesis is that a well-structured flowchart is not merely a documentation tool — it is a **direct template for AI prompts**. By translating real-world problems into visual step-by-step sequences with decisions, inputs/outputs, and function calls, students learn to produce precise, unambiguous prompts that reduce costly verify-iterate cycles with AI coding agents.

The lecture is structured in three main layers: (1) the syntax and building blocks of flowcharts (start/end nodes, statements, decisions, subroutines), (2) a concrete worked example tracing Python program execution and the Pythagoras function, and (3) the bridge from flowchart to prompt, demonstrated through a crack-inspection decision scenario. A group exercise and quiz reinforce the material.

The lecture sits within the broader course sequence as a **design artifact** that connects earlier requirement-gathering (lecture 04a) to later agent-driven programming workflows (lecture 01c). It emphasizes computational thinking — decomposing a real-world problem into inputs, outputs, and ordered steps — as a core engineering competency.

## Main topics (What is the structure of the lecture)
- **Flowchart fundamentals**: The five basic building blocks — statements, variables, decisions, loops, and functions — and their standard diagram shapes
- **Shape syntax**: Detailed explanation of oval (start/end), rectangle (statements), rhombus (I/O), diamond (decisions), and double-bordered rectangle (subroutines)
- **Worked example — Christmas shopping**: A complete flowchart mapping a gift-buying scenario through decision branches to concrete subroutines
- **Program execution tracing**: Step-by-step walkthrough of a Python `pythagoras` function, illustrating sequential execution, function definition vs. invocation, and `return` behavior
- **Problem decomposition**: How to identify inputs and outputs (e.g., volume calculation of a rectangular house) and translate them into a step-by-step procedure
- **Flowchart → AI prompt**: Mapping each diagram element to a prompt construct (process box → instruction, diamond → if/then, sequence → ordering)
- **Crack inspection case study**: A real-world multi-level decision flowchart translated into a ready-to-use Python function prompt
- **Group exercise**: Role-based workflow where one group defines requirements, another draws the flowchart, and a third converts it into a Claude-Code prompt
- **Spaced repetition flashcard system**: A meta-learning reminder about the lecture's flashcard review schedule (4 tiers)

## Key takeways (What are the resulting takeways/skills teached)
- **Design before coding**: Always create a flowchart *before* writing code or crafting a prompt — it eliminates ambiguity and reduces iteration
- **Shape-to-code mapping**: Each flowchart shape has a direct Python/programming equivalent (diamond → `if/elif`, double rectangle → function call)
- **Problem-first thinking**: Identify inputs and outputs first, then ask "how do we get from input to output?" to guide step decomposition
- **Flowchart → prompt translation**: A process box becomes an instruction, a diamond becomes a condition, and sequence becomes prompt ordering — making the flowchart itself a structured prompt specification
- **Function decomposition**: Any real-world problem can be modeled like a function: defined inputs, processing logic, and a single output/return value
- **Spaced repetition**: Use the 4-tier flashcard system (daily → every 2 days → weekly → monthly) to retain core concepts
- **Cross-disciplinary utility**: Flowcharts are used beyond programming — in process modeling, patent documentation, and quality assurance

## Code Examples (What code examples are shown)
- **Pythagoras with trace prints** (`import math` script): Demonstrates sequential execution order, function definition vs. call timing, and how `return` prevents subsequent lines from executing — each line annotated with `"Zeile X"` print statements
- **Pythagoras clean version**: A minimal version of the same function (`math.sqrt((a*2)+(b*2))`) without trace prints, showing the actual computation without debugging noise
- **Crack inspection prompt**: A natural-language prompt template that specifies a Python function `beurteile_riss(rissgroesse_mm, feuchtigkeit)` with four conditional branches mapping directly to the flowchart's decision diamonds

## Visualizations (What visualizations plotly/svg/etc. are used)
- **`images/partA_6.svg`**: Course module overview diagram showing "Grundlagen" (Motivation, Computerarchitekturen, Programmierung) and "Modellierung" (Fehler und Debugging, Objektorientierung, Verifikationen) as interconnected blocks
- **`images/04b_Programmablauf/elements.svg`**: Reference graphic illustrating the five flowchart element shapes with labels
- **`images/04b_Programmablauf/rectangle.png`**: Midjourney-generated image of a rectangular house used as the visual anchor for the volume calculation example
- **`images/04b_Programmablauf/wiederholung.svg`**: Flashcard review system diagram showing the 4-tier spaced repetition schedule
- **`images/04b_Programmablauf/mj_title_band.jpg`**: Title band image for the book-style opening
- **`images/04b_Programmablauf/mj_title.mp4`**: Animated title slide background (Midjourney: Doves to Blocks, M. C. Escher reference)
- **`images/04b_Programmablauf/mj_dorian.mp4`**: Animated "Lesson Learned" background referencing "Dorian Gray" (Midjourney)

## Plots
None

## Examples (What examples are used)
- **Christmas shopping flowchart**: A relatable scenario — waiting for Christmas, getting money, deciding on the best gift (wine, socks, or book), then shopping at the appropriate store — used to teach branching logic
- **Crack inspection decision tree**: A civil engineering scenario where measured crack width (>0.3 mm, >1.0 mm) and moisture presence determine actions (seal, inspect, observe, inform expert) — demonstrates multi-level nested decisions
- **Volume calculation of a rectangular house**: Students identify inputs (`a`, `b`, `h` in meters) and output (volume in m³), discussing data types and edge cases
- **Grady Booch quote**: "A fool with a tool is still a fool" — framing the lecture's philosophy that tools (prompts, AI) require good design thinking

## Remarks
- The lecture is in **German**, with all technical terms kept in English where applicable. German terms appear in parentheses on first reference (e.g., "Flussdiagramme" (flowcharts), "Drachenviereck" (diamond/rhombus for decisions)).
- **Mermaid diagrams** are used extensively (7 total) — both as standalone content and repeated across slides for pedagogical reinforcement.
- Cross-references point to **lecture S04 04a_Anforderungen** (requirements → flowchart) and **lecture S01 01c_AgentischesProgrammieren** (prompt structure), situating this lecture in the course sequence.
- The group exercise (`exercises/04b_Flussdiagramm_Gruppenübung/`) is explicitly referenced as a follow-up assignment with role-based collaboration.
- The quiz (via `quizdown`) contains 8 questions testing shape recognition, concept mapping, ordering, and the flowchart-to-prompt methodology.
- No animated plots (Plotly) are present — all visuals are static diagrams or images.
- The "Lesson Learned" slide with "Dorian Gray" uses a video background but contains no extractable content beyond its title.
# Summary: Objekte (Objects)

This lecture introduces **object-oriented programming (OOP)** as a **design concept** — not a Python syntax lesson. It teaches students to think in terms of entities, attributes, responsibilities, and relationships *before* writing any code. The lecture positions itself as the design-phase counterpart to the later implementation-focused lecture on Python class syntax (06), linking back to the UML notation introduced in the software design unit (03). A central thesis is that good OOP begins with deliberate **domain decomposition**, captured in a UML class diagram, which then serves as a **specification for AI-assisted code generation**.

The lecture is structured around three core problems that objects solve — **syntactic**, **semantic**, and **behavioral** — and presents a practical workflow for **agentic programming**: design → prompt → generate → verify. Using a BIM (Building Information Modeling) example of a building hierarchy, students practice translating a domain into classes, attributes, methods, and relationships.

## Main topics (What is the structure of the lecture)
- **Warum in Objekten denken?** — OOP as a design strategy, introducing the three problems objects solve (syntactic, semantic, behavioral)
- **Klassen als Entwurfseinheiten** — Classes as blueprints vs. instances as concrete objects; relationship between design and runtime
- **Beziehungen zwischen Objekten** — Association, aggregation, and composition; UML diagram notation with direction and multiplicity
- **Design before you prompt** — The agentic workflow: design a UML diagram, prompt an AI with it, generate Python code, verify the output
- **BIM-Beispiel: Gebäudehierarchie** — Practical domain decomposition exercise using a building → floor → room → window hierarchy
- **Querverbindungen** — Cross-references to prior and future lectures (S03 UML, S06 Python implementation, S08 unit testing)

## Key takeways (What are the resulting takeways/skills teached)
- Think in **entities, attributes, and responsibilities** before writing any code
- Use **UML class diagrams** as a complete specification that an AI can implement from
- Distinguish **association** (uses), **aggregation** (contains loosely), and **composition** (composed of tightly)
- Treat the UML diagram as the **single source of truth** — if it's not in the diagram, the AI will hallucinate it
- Follow the agentic cycle: **Entwerfen → Prompten → Generieren → Verifizieren** (Design → Prompt → Generate → Verify)
- Verify generated code against the UML diagram, not against intuition

## Code Examples
- Point coordinate without object: `punkt_1 = (54.083336, 12.108811)` — demonstrates the **semantic problem** (unclear which value is latitude vs. longitude)
- Point coordinate with object: `punkt_1.latitude = 54.083336`, `punkt_1.longitude = 12.108811` — shows how **attribute names make meaning explicit**
- `punkt.distanz()` method vs. free function `distanz()` — demonstrates the **behavioral problem** (encapsulation prevents misuse on wrong types)
- Quiz code blocks (multiple-choice questions) — used for knowledge checks, not instructional code

## Visualizations
- `images/partA_6.svg` — Workflow diagram showing the lecture sequence within Part A
- `images/04c_Objects/mj_title_band.jpg` — Cover image for the book-style front matter (Bauhaus line drawing)
- `images/04c_Objects/mj_title.mp4` — Animated background video for the title slide (HTML/reveal.js output)
- Mermaid flowchart: **Klasse → Instanzen** — Visualizes the relationship between a class as blueprint and multiple instances as runtime objects
- Mermaid flowchart: **Punkt → Instanzen** — Reused diagram for UML notation illustration (referenced with aside citing 03c_Softwareentwurf)
- Three-column layout for **Assoziation / Aggregation / Komposition** — Visual comparison of the three relationship types with examples (Ingenieur→Werkzeug, Polygon→Punkte, Gebäude→Etagen)
- Two-column layout: **Ohne Objekt vs. Mit Objekt** — Side-by-side comparison for both the semantic and behavioral problems

## Plots
- None

## Examples
- **BIM building hierarchy** (Gebäude → Etage → Raum → Fenster) — a real-world architectural domain model used as the central design exercise
- **"KI als Junior-Entwickler" metaphor** — the AI generates code from the UML specification but can hallucinate; the human engineer acts as the verifier
- **"Was nicht im Diagramm steht, wird die KI erfinden — oft falsch."** — a memorable *Merksatz* (key phrase) about the necessity of complete UML specifications
- **Ingenieur → Werkzeug**, **Polygon → Punkte**, **Gebäude → Etagen** — running examples used throughout to illustrate association, aggregation, and composition
- **Quiz** — 8 multiple-choice questions reinforcing concepts (object definition, semantic problems, class vs. instance, composition, UML, etc.)

## Remarks
- The lecture is intentionally **design-only** — no Python `class` syntax is written. That is deferred to lecture 06 (`04c_Objects` implementation).
- The course is in **German** (with English code), reflecting a bilingual engineering education context.
- Cross-references are explicit: S03 (UML notation), S06 (Python class implementation), S08 (unit testing verification).
- The `%%tip Merksatz:` block is used for a single memorable takeaway about UML completeness — a signature teaching device in this course.
- The `%%final` block at the end signals this is the closing lecture of its subsection.
- Mermaid diagrams are used as structural visuals rather than data plots, aligning with the design/uml focus.
# Summary: Operatoren

This lecture introduces **operators** in Python as the fundamental building blocks of expressions — the symbols and keywords that instruct the interpreter to perform operations on values. Rather than expecting students to write code from scratch, the session's learning objective emphasizes **reading and tracing** AI-generated expressions step by step. The lecture builds on prior knowledge of the **knowledge pyramid** (Zeichen → Daten → Informationen → Wissen) and **data types** before diving into the full taxonomy of Python operators, from arithmetic to logical to bitwise.

The structure follows a pattern of concept introduction (reference tables), live code demonstrations, and interactive "Hörsaalfrage" (lecture hall quiz) prompts. A recurring theme is **operator precedence** and the importance of tracing complex expressions logically before executing them — a skill framed as essential when working with AI-generated code. The lecture also covers operator overloading in Python and warns about type errors that commonly arise.

## Main topics
- **Wiederholung (Recap):** Knowledge pyramid (Zeichen → Wissen) and data types in general and in Python
- **Grundbegriffe:** Statements, expressions, and operators defined; variable assignment syntax
- **Arithmetische Operatoren:** Addition, subtraction, multiplication, division, floor division, modulo, exponentiation
- **Zuweisungsoperatoren:** Assignment and compound assignment (`+=`, `*=`, etc.); no increment/decrement in Python
- **Vergleichsoperatoren:** Equality, inequality, greater/less than, and chained comparisons (`0 < a < 2`)
- **Identitätsoperatoren:** `is` and `is not` — testing object identity (memory reference)
- **Logische Operatoren:** `and`, `or`, `not` — combining boolean expressions
- **Bitweise Operatoren:** AND, OR, XOR, NOT, shift-left, shift-right on integer operands
- **Überladen von Operatoren:** Operator behavior varies by type (e.g., `+` concatenates strings, extends lists, is undefined for sets)
- **Mitgliedsoperatoren:** `in` and `not in` — membership testing in collections
- **Quiz:** Binary numbers, binary code, and truth tables for AND, OR, XOR, NOT, NAND, NOR, XNOR

## Key takaways
- **Read before you execute:** When encountering AI-generated expressions, trace operator precedence step by step on paper first
- **Operator precedence matters:** `is` → `not` → `>` → `and`; parentheses make intent explicit
- **Python's compound assignment** (`+=`, `*=`) is shorthand for `x = x op value`, but Python lacks `++`/`--`
- **`==` vs `=`:** Double equals tests equality; single equals assigns — a common beginner mistake
- **Boolean keywords differ from C-style:** Python uses `and`, `or`, `not` instead of `&&`, `||`, `!`
- **Chained comparisons work naturally:** `0 < a < 2` is valid and evaluates left to right
- **Operators are overloaded:** The same symbol (`+`, `-`) has different semantics depending on operand types
- **Type consistency is enforced:** Python requires both operands to be the same type (e.g., no implicit `str + int`; use `str()` or `int()`)
- **Bitwise operators are reserved for low-level work:** Used rarely, mainly for masking or compiler-style optimizations via shifts
- **`is` tests identity, `==` tests value:** Two objects can be equal (`==`) without being the same object (`is`)

## Code Examples
- `x = 5; ergebnis = x ** 2 - 3 * x + 1` — Tracing a polynomial expression with mixed arithmetic operators
- `a = 1 + 1; print(a)` — Basic arithmetic operator usage
- `a = a + 1` followed by `a += 1` and `a *= 2` — Demonstrating compound assignment shorthand
- `(6 + a) * (-2)` vs `6 + a * -2` — Parentheses change evaluation order and results
- `c1 == c2`, `c1 != c2`, `c1 < c2`, `c1 <= c2`, `c1 > c2`, `c1 >= c2` — All comparison operators on variables
- `c1 > c2 or c1 == c2` — Chaining comparisons with `or` instead of `≥`
- `x = 10; ergebnis = not x is None and x > 0.0` — Complex boolean expression with precedence tracing
- `a = 10; b = 4; c = a & b`, `c = a | b` — Bitwise AND and OR on integers
- `c = a << 2`, `d = c >> 2` — Shift-left (multiply by 4) and shift-right (divide by 4)
- `"Der " + "Ball " + "ist " + "rund."` — String concatenation via overloaded `+`
- `liste1 = [1,2,3]; liste12 = liste1 + liste2` — List concatenation via overloaded `+`
- `menge1 = {1,2,3}; menge12 = menge1 - menge2` — Set difference via overloaded `-`
- `"Der Wert ist " + 1` (error) vs `"Der Wert ist " + str(1)` — Type error and casting fix
- `"1" + 1` (error) vs `int("1") + 1` — Casting to resolve type ambiguity
- `i = 1; i *= 2; i *= 3` — Compound assignment chaining

## Visualizations
- `images/03a_Wissenspyramide/pyramide1.svg` — Knowledge pyramid diagram (Zeichen → Daten → Informationen → Wissen)
- `images/05a_Operatoren/datentypen.svg` — General data types taxonomy illustration
- `images/05a_Operatoren/datentypen_python.svg` — Python-specific data types overview
- `images/partA_4.svg` — Part A course workflow/sequencing diagram
- `images/05a_Operatoren/logic0.svg` — Logic truth table reference (before quiz reveal)
- `images/05a_Operatoren/logic.svg` — Logic truth table reference (after quiz reveal)
- `images/05a_Operatoren/Logic_AND.svg` — AND gate truth table
- `images/05a_Operatoren/Logic_OR.svg` — OR gate truth table
- `images/05a_Operatoren/Logic_XOR.svg` — XOR gate truth table
- `images/05a_Operatoren/Logic_NOT.svg` — NOT gate truth table
- `images/05a_Operatoren/Logic_NAND.svg` — NAND gate truth table
- `images/05a_Operatoren/Logic_NOR.svg` — NOR gate truth table
- `images/05a_Operatoren/Logic_XNOR.svg` — XNOR gate truth table
- `images/05a_Operatoren/mj_title_band.jpg` — Title banner image
- `images/05a_Operatoren/mj_tower.png` — Tower of Babel image for knowledge pyramid question
- `images/05a_Operatoren/mj_avocado.png` — Avocado-shaped chair image for data types question
- `images/05a_Operatoren/mj_python.png` — Python programming a robot image for Python types question

## Plots
None

## Examples
- **Quiz analogies:** Binary numbers linked to the Latin "binarius" (two-fold); binary code compared to natural language text and graphics representations
- **AI code reading scenario:** Tracing `not x is None and x > 0.0` step-by-step — framed as a real-world task when reviewing AI-generated code
- **Agentischer Arbeitsablauf (Agentic Cycle):** A structured 3-step workflow for analyzing AI-generated boolean expressions (identify precedence → evaluate inward → simplify)
- **Cross-lecture reference:** Knowledge pyramid recap from lecture 03a (Wissenspyramide)
- **Cross-language contrast:** Python's lack of `++`/`--` compared to other languages; Python's strict type equality vs. Java/JavaScript's implicit casting

## Remarks
- The entire lecture is in **German**, with English technical terms in parentheses (e.g., statement, expression, operator, floor division).
- The learning objective is explicitly framed around **reading and tracing** AI-generated code, not writing from scratch (`%%tip Lernziel dieser Sitzung`).
- Multiple **Hörsaalfrage** (lecture hall quiz) slides use a yellow background (`#FFD966`) with Midjourney-generated images as visual prompts.
- The quiz at the end covers **digital logic gates** (AND, OR, XOR, NOT, NAND, NOR, XNOR) alongside Python-specific questions — bridging computer hardware concepts with programming language syntax.
- No **`%%note Merksatz:`** blocks were found; key takeaways are embedded in `%%book` blocks and inline warnings.
- No **plotly plots** or **animated visualizations** are present; all visuals are static SVG diagrams or static images.
- The `%%final` block at the end marks the formal conclusion of the session.
- One quiz question at the bottom explicitly contrasts Python's boolean keywords (`AND`, `OR`, `NOT` — all lowercase in actual Python) with C-style operators (`&&`, `||`, `!`), highlighting a common cross-language pitfall.
# Summary: Verzweigung

This lecture introduces **conditional branching** (Verzweigung) in Python — the foundational control-flow mechanism that allows programs to execute different code paths based on logical conditions. The topic positions itself as part of a broader course on scientific programming that emphasizes **reading and verifying AI-generated code** rather than simply writing it from scratch. A recurring theme is the **Branch-Lesestrategie** (branch-reading strategy): systematically identifying conditions, tracing branches, mapping inputs to paths, and checking for missing edge cases before accepting auto-generated branching logic.

The lecture is structured around three branching constructs (`if`, `else`, `elif`), extended to nested branching and Python 3.10's `match-case` statement. Practical examples revolve around error handling (division by zero, type validation) and threshold classification (structural stress levels). The pedagogical approach interleaves concise code demonstrations, AI-code-reading exercises, and a study-method module (SQRRR notes strategy).

## Main topics (What is the structure of the lecture)
- **Einführung in bedingtes Verzweigen**: Concept of `if` statements, indentation requirements, and boolean evaluation of Python objects.
- **Logische Operatoren und Implizite Wahrheitswerte**: `not`, `and`, `or`; truthiness of strings, lists, dicts, and `None`.
- **Die Alternative (`else`)**: Two-branch branching with `else`, including division-by-zero error prevention.
- **Verschachtelte Verzweigungen**: Nested `if-else` structures and their readability limitations.
- **Alternatives Verzweigen (`elif`)**: Flattening nested branches with `elif`, using `isinstance()` for type checking, ordering pitfalls with dynamic typing.
- **Mehrfachverzweigung (`match-case`)**: Python 3.10's structural pattern matching as an alternative to long `if-elif-else` chains.
- **KI-generierten Code lesen und verifizieren**: The 4-step Branch-Lesestrategie applied to a `classify_stress()` function, with unit-test per-branch verification and boundary-value analysis.
- **Lernmethoden (SQRRR)**: Study notes strategy (Survey, Question, Read, Recite, Review) with embedded YouTube resources.

## Key takaways (What are the resulting takeways/skills teached)
- Write and read `if`/`else`/`elif` blocks with correct indentation and Python syntax (`:` required).
- Understand Python's **truthiness rules**: empty containers, `None`, `0` → `False`; non-empty, non-zero → `True`.
- Prefer **explicit comparisons** (`!= 0`, `is not None`) over implicit truthiness to avoid bugs with dynamic typing.
- Use **`isinstance()`** for type checking instead of `type() == int` for cleaner, more readable code.
- Always **order type checks before value checks** in dynamically typed languages to prevent misleading error messages.
- Apply the **Branch-Lesestrategie**: identify conditions → count branches → map inputs → check for missing cases (especially `None`, negatives, boundary values).
- Write **at least one test per branch**, with special attention to boundary values where `<` vs `<=` errors commonly hide.
- Structure notes using the **SQRRR method** for effective post-lecture review and self-testing.

## Code Examples (What code examples are shown)
- Basic `if` with `True`/`False` boolean variable — demonstrates execution only when condition is met.
- `not` negation and truthiness of `0` vs `2` — shows implicit boolean conversion of integers.
- Truthiness of empty vs non-empty strings — demonstrates that `""` is falsy but `" "` (space) is truthy.
- Truthiness of empty vs non-empty lists — `[]` is falsy, `["nicht_leer"]` is truthy.
- `None` handling with both `if bedingung:` and `if bedingung is not None:` — distinguishes implicit falsy from explicit `None` checks.
- `if-else` with `True` and `False` — two-branch alternative execution.
- **Division by zero** (implicit and explicit versions) — `if nenner:` vs `if nenner != 0:` with `None` fallback.
- **Deeply nested type-checked division** — triple-nested `if` checking `zaehler` type, `nenner` type, and `nenner != 0`.
- **Flattened `elif` version** of the same division logic using `isinstance()` checks — demonstrates the readability improvement.
- Pitfall demonstration: `if not nenner:` before `isinstance` produces wrong error for `nenner = []` — shows ordering danger.
- **Sign testing** with both nested `if-else` and clean `if-elif-else` — negative / positive / zero classification.
- **`classify_stress()` function** — AI-generated threshold classifier for structural stress values (MPa).
- **Unit tests per branch** for `classify_stress()` including boundary values (0, 150, 250).
- **`match-case` pattern** (Python 3.10+) — comparison of traditional `if-elif-else` vs new structural matching syntax.

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_4.svg` — **Ablauf** (workflow) diagram showing sequential → branching process structure.
- `images/05b_Verzweigung/process.svg` — Study process diagram used in the "Notizen" slide about note-taking best practices.
- `images/05b_Verzweigung/mj_title_band.jpg` — Title image for the book opening section (Midjourney artwork).
- `images/05b_Verzweigung/mj_title.mp4` — Title slide background video (Midjourney: "Red or Blue Pill").
- `images/05b_Verzweigung/mj_senses.mp4` — Background video for "Lesson Learned" slide on learning types (Midjourney: "Six Sense").

## Plots
None

## Examples (What examples are used)
- **Division by zero** — the canonical example for `if-else` error handling in arithmetic operations.
- **Structural stress classification** (`classify_stress()`) — engineering use case where AI-generated threshold logic must be verified before use in an Ingenieurbau context.
- **Sign testing** (negative / positive / zero) — minimal three-way branching example, shown with both nested and `elif` forms.
- **AI-generated code reading exercise** (`wert > 100 / > 50` threshold) — students trace which inputs map to which branches and identify missing edge cases.
- **Yogi Berra quote** ("When you come to a fork in the road, take it.") — humorous opening metaphor for branching.
- **SQRRR study method** — real pedagogical framework (Survey, Question, Read, Recite, Review) for post-lecture note processing, paired with two YouTube video links.

## Remarks
- The lecture is entirely in **German** (with English code, technical terms, and some English slide content mixed in).
- The course emphasizes **AI-assisted programming**: a major theme is reading, understanding, and verifying AI-generated code rather than authoring it.
- The **`%%note Info` block** (lines 547–548) provides an important warning about dynamic-typing pitfalls when ordering checks — this is a key conceptual insight.
- The **`%%quizdown` block** at the end contains 18 quiz questions covering syntax, truthiness, `elif`, `isinstance`, and the `classify_stress` function — these are self-assessment tools, not instructional content.
- Quiz code blocks are excluded from the Code Examples section per extraction rules.
- The lecture includes a **`%%final`** marker, signaling the end of content.
- Cross-reference: boundary-value testing is linked to lecture `08a_UnitTest`.
- The `match-case` feature is noted as introduced in **Python 3.10**, contextualizing its recency.
- The lecture intentionally **does not contain complex algorithms** — its scope is narrowly focused on branching syntax, semantics, and code-review habits.
# Summary: Schleifen

This lecture introduces **loops** (Schleifen) in Python as a fundamental mechanism for repeating operations, covering both `for` and `while` constructs. It is part of a programming course aimed at engineering students who work with large-scale data (thousands of sensor readings, BIM models, soil samples) and increasingly rely on **AI-generated code**. The central thesis is that engineers don't need to write every loop from scratch — but they **must** be able to read, understand, and verify them.

The lecture is structured into three major themes: (1) `for`-loops with known iteration counts, including For-Each patterns on lists, tuples, and dictionaries, plus the `range()` and `enumerate()` utilities; (2) `while`-loops with unknown iteration counts, contrasting While, Do-While, and Repeat-Until variants; and (3) **loop control** (`break`, `continue`), **infinite loop detection**, and safety strategies (max-iteration guards, timeout-based breaks). A recurring emphasis is on reading and verifying AI-generated loops using a structured three-step approach: identify the iterable, trace the first few iterations, and check for termination.

## Main topics (What is the structure of the lecture)
- **Why loops?** — Engineering-scale data processing (10,000 soil samples, 1M sensor readings) requires automated repetition
- **`for`-loop basics** — For-Each iteration over lists, tuples, and dictionaries; iterator variable holds the current element
- **`for` with `range(n)`** — Classical index-based loops mimicking C/Java `for` patterns
- **`enumerate()`** — Pythonic shortcut to get both index and value during iteration
- **Dictionary iteration** — Iterating over keys with `seq[key]` lookup vs. using `items()` for key–value tuples
- **Practical example** — Converting imperial feet measurements to meters using a `for`-loop and list comprehension
- **Verifying AI-generated loops** — Trace-table method (Spur-Tabelle): identify iterable, trace iterations, check termination
- **`while`-loop fundamentals** — Condition-checked repetition; loop body may execute zero times
- **Loop variant comparison** — While vs. Do-While vs. Repeat-Until semantics and their Python equivalents
- **Infinite loop risks** — Identifying warning signs (unmodified loop variable, condition never becoming `False`)
- **Safety strategies** — Max-iteration guards and timeout-based `break` mechanisms
- **`break` and `continue`** — Premature loop exit and skipping iterations for filtering
- **Program flow control recap** — `if`/`else`/`elif` (conditional) + `while`/`for` (repetition) as universal algorithmic building blocks

## Key takaways (What are the resulting takeways/skills teached)
- **Three-step loop verification**: When AI generates a loop, (1) identify the iterable, (2) trace the first two and last iteration, (3) confirm termination
- **`for` in Python is always For-Each** — it iterates over elements of a sequence, not indices by default
- **Use `range(n)`** for classical index-based loops when you need numeric counters
- **Prefer `enumerate()`** over manual `range(len(seq))` indexing for cleaner, more Pythonic code
- **Use `dict.items()`** to iterate key–value pairs directly instead of separate lookups
- **Always add safety nets to `while` loops** — max-iteration or timeout guards prevent infinite loops
- **`break` exits the loop; `continue` skips to the next iteration** — both are performance optimization tools
- **Loop variables persist outside the loop scope in Python** — be aware of leftover values
- **AI-generated loops must be read before execution** — verify logic with a trace table first

## Code Examples (What code examples are shown)
- **For-Each over list and tuple** — iterating `['a','b','c', 1]` and `('a','b','c', 1)` to print each element
- **`range(n)` counter loop** — generating numbers 0 through n−1 with `for i in range(n)`
- **Index-based list traversal** — using `range(len(seq))` with `seq[i]` indexing (classic C/Java style)
- **`enumerate()` usage** — unpacking index and value simultaneously with `for i, wert in enumerate(seq)`
- **Dictionary iteration by keys** — looping over keys and looking up values via `seq[key]`
- **Dictionary iteration with `items()`** — unpacking key–value pairs directly with `for key, wert in seq.items()`
- **Imperial-to-metric conversion** — transforming a list of foot measurements to meters using a `for`-loop, then shown as a list comprehension
- **AI-generated average calculator** — `temperaturen` list summed in a loop to compute the average (used for trace-table exercise)
- **Standard `while` loop** — countdown from `n=3` to 0, printing each iteration
- **Zero-initialization `while`** — `n=0` case where the loop body never executes
- **Do-While simulation in Python** — initializing `bedingung = True`, setting it inside the loop body at the end
- **Repeat-Until simulation in Python** — using `while not bedingung` with `n` counting up to 0
- **Infinite loop detection example** — `while x > 0` without modifying `x` (intentional trap)
- **Max-iteration guard function** — `while_loop_mit_abbruch(n, max_iterations=99)` with a secondary counter condition
- **Infinity edge case** — calling `while_loop_mit_abbruch(math.inf)` showing the safety net catching an un-terminatable loop
- **`break` and `continue` — "edible items in backpack"** — iterating `dinge_in_meinem_rucksack`, skipping non-edible items, finding the first edible one (`Apfel`), then breaking
- **Timeout-based infinite loop with `break`** — `while True` loop with `time.time()` elapsed check that breaks after 3 seconds
- **`time.sleep(3)`** — proper way to pause execution (contrasted with busy-wait timeout loop)

## Visualizations (What visualizations are used)
- `images/partA_4.svg` — Workflow/Schematic diagram illustrating the general loop execution flow
- `images/05c_Schleifen/mj_title_band.jpg` — Title banner image (Midjourney, inspired by Robert Delaunay)
- `images/05c_Schleifen/mj_title.mp4` — Title slide background video (Midjourney)

## Plots
None

## Examples (What examples are used)
- **Engineering data scale** — 10,000 soil samples from a construction site, 1M daily sensor readings, 50,000 BIM components
- **"KI als Code-Generator" (AI as code generator)** — recurring theme: engineers read and verify AI-written loops rather than writing them from scratch
- **Spur-Tabelle (trace table)** — fill-in-the-blank table tracking `t` and `summe` values across four iterations of a temperature-averaging loop
- **Feet-to-meters conversion** — practical engineering unit conversion from `[4.2, 2.3, 6.2, 10.5]` feet to meters
- **Backpack "edible items" search** — finding the first edible item (`Apfel`) among `["Papier", "Stift", "Apfel", "Brot", "Messer"]`, using `break` and `continue`
- **Infinite loop trap** — `while x > 0` printing `x` without ever modifying it
- **Quiz exercises** — 13 multiple-choice and sequencing questions covering all loop concepts (multiple correct answers supported)

## Remarks
- The lecture is written in **German** with English technical terminology; German terms are preserved on first reference (e.g., *Spur-Tabelle*, *Endlosschleife*).
- Cross-references to other lectures: `02c_Datentypen` (collection types), `09a_Algorithmen` (loops as algorithm building blocks).
- The lecture includes **quizdown** interactive quiz content with multiple-select and code sequencing questions.
- `%%tip Merksatz:` and `%%warning Achtung:` blocks provide explicit memory aids and cautions — a key pedagogical device for retaining core concepts.
- The "AI-generated code reading" narrative is a unifying theme throughout, framing loops not just as syntax but as **verification challenges** in the age of AI-assisted programming.
- This lecture intentionally does not contain plotly charts or data visualizations; it is purely code and concept focused.
# Summary: Funktionen

This lecture introduces **functions** in Python as a core programming construct. Building on prior knowledge of conditional branching (`if`/`elif`/`else`) and loops (`for`/`while`), it covers function definitions, signatures, return values, variable scope, argument passing semantics, and default parameter pitfalls. A recurring theme is the **agentic workflow** — a structured method for reading, validating, and correcting AI-generated code.

The lecture is structured in three parts: an interactive review of control flow, a deep dive into function mechanics, and a practical exercise cycle for reviewing AI-generated code. It emphasizes writing clean, modular, and reusable code through well-defined functions with explicit type signatures and docstrings.

## Main topics (What is the structure of the lecture)
- **Review of control flow** — recap of `if`/`elif`/`else` branching and `for`/`while` loops, including the distinction between while, do-while, and repeat-until patterns
- **Mathematical vs. programming functions** — mapping from mathematical function notation to Python's `def` syntax, with the function signature as a "contract"
- **Function definition syntax** — `def` keyword, parameters, indentation, docstrings, and type annotations
- **Return values** — `return` behavior, single vs. multiple returns (tuples), and multiple assignment unpacking
- **Default parameters** — optional arguments with defaults and the mutable default argument trap (`liste=[]`)
- **Variable scope and argument passing** — local vs. global variables, pass-by-assignment, mutable vs. immutable types, pass-by-reference pitfalls
- **Built-in functions** — overview of Python's standard built-in function catalog (`print`, `len`, `abs`, `max`, `min`, `sorted`, etc.)
- **Agentic code review workflow** — a 5-step cycle for reading and validating AI-generated functions: read signature → write test → check docstring → inspect implementation → correct and re-prompt
- **Quiz** — comprehensive self-assessment covering all lecture concepts

## Key takeways (What are the resulting takeways/skills teached)
- Write functions with **clear, descriptive names**, **typed parameters**, and **docstrings** to establish a verifiable contract before implementation
- Use `return` to end execution and send values back; a function without `return` yields `None`
- Multiple return values produce a **tuple**, which can be unpacked via multiple assignment (`a, b = func()`)
- Default parameters with **mutable types** (`list`, `dict`, `set`) cause shared-state bugs — use `None` as the default and initialize inside the function
- Python uses **pass-by-assignment**: immutable types are copy-like, mutable types are reference-like; reassigning a parameter has no external effect
- Functions improve **modularity**, **reusability**, and **readability** — decompose programs into small, focused functions
- When reviewing AI-generated code, **verify the signature first** before inspecting the implementation

## Code Examples (What code examples are shown)
- **`mal2` bit-shift function** — demonstrates a compact function that doubles a value using bit shifting (`arg1 << 1`) instead of multiplication
- **`distance` Euclidean distance** — computes the Euclidean distance between two 2D points using `math.sqrt` and demonstrates positional arguments
- **`calculate_area` type-annotated function** — a clean example of a function with type hints (`float -> float`) and a docstring
- **`flow_velocity` AI-generated function** — a 3-step exercise: read signature only → write tests → review implementation; exposes missing guard clauses and edge-case handling
- **`funktion_mit_einer_ausgabe` / `funktion_mit_zwei_ausgaben`** — demonstrates single and multiple return values, tuple unpacking, and the fact that code after `return` is unreachable
- **`measurement` with default parameter** — shows a default argument (`unit="meters"`) and how overrides work
- **`sammle_messwerte` mutable default bug** — demonstrates the classic `def f(x, l=[])` pitfall and the correct `l=None` pattern
- **`meine_funktion` scope demonstrations** — four variants showing local variable scope, pass-by-value for primitives, reassignment of lists, and in-place mutation of lists (pass-by-reference)
- **Recursive `count_down` quiz question** — conceptual exercise on writing a proper recursive function with a base case

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_5.svg` — program execution flow diagram (control flow visualization)
- `images/06a_Funktionen/mj_title_band.jpg` — artistic title image for the book-style chapter header
- `images/06a_Funktionen/mj_yinyang.jpg` — visual metaphor accompanying the `if/elif/else` review question
- `images/06a_Funktionen/mj_loop.png` — artistic image for the loop review question
- `images/06a_Funktionen/mj_title.mp4` — background video on the title slide (Midjourney-generated "Functional Lines")

## Plots
- None

## Examples (What examples are used)
- **AI-generated code review exercise** (`flow_velocity`) — students practice a structured review workflow on a function that computes fluid flow velocity in a pipe, learning to write tests *before* reading the implementation
- **"KI als Junior-Entwickler" (AI as Junior Developer)** — the agentic workflow frames AI code generation as a mentorship task: the human reviews and corrects AI output
- **Hydraulic gradient function** — real-world physics example (`hydraulic_gradient`) used to contrast clear vs. unclear function signatures
- **Verdopplung (doubling) comparison** — contrasts naive multiplication with bit-shift optimization
- **Quiz scenarios** — multiple-choice questions reinforce concepts like recursion, scope, default arguments, and return behavior

## Remarks
- The lecture is primarily in **German** (slide headings, explanations, quiz), but the summary follows English conventions per the synthesis rules. Original German terms are preserved on first reference.
- This is part of a larger course sequence: it follows lectures on **control flow** (`if`/`elif`/`else`, loops) and precedes deeper topics like recursion, modules, and error handling.
- The `%%book` blocks provide additional prose and runnable Python code cells beyond the `%%slides` content, including detailed scope examples with intentional error demonstrations.
- The lecture intentionally avoids deep code complexity — it focuses on **concepts and patterns** (signatures, scope, mutability) rather than advanced features.
- The agentic workflow is a recurring meta-theme: it appears in multiple slides and is summarized as a 5-step cycle for AI-assisted development.
- Quiz answers are embedded as `quizdown` blocks within the `%%book` section and are excluded from code example descriptions.
# Summary: Objekte — Implementierung

This lecture bridges the gap between UML-based object-oriented design and concrete Python implementation. It builds directly on the earlier lecture S04 (`04c_Objects`), which introduced classes and UML class diagrams as design artifacts, by showing how to translate those diagrams into working Python code. The core thesis is that AI-generated class code must always be verified against the original UML specification — students are taught systematic verification habits rather than blind trust in AI output.

The lecture walks through the complete mapping from UML elements to Python syntax: class definitions, constructors (`__init__`), instance attributes, methods, associations, encapsulation, and inheritance. Alongside the translation mechanics, it highlights three common AI-generated code pitfalls — mutable default arguments, missing `self`, and confused `cls`/`self` — equipping students with a three-question verification checklist they can apply to any AI-generated class.

Positioned in the course as Part B of the Objects module, this lecture serves as the implementation counterpart to the design-focused S04, and sets up the upcoming S06 (`06c_Module`) where classes will be organized into modules.

## Main topics (What is the structure of the lecture)
- **UML-to-Python mapping**: Direct translation of UML class diagram elements (`class`, attributes, methods, associations) into Python syntax
- **Python class syntax in detail**: Constructor (`__init__`), instance vs. class attributes, methods, and instance creation
- **Implementing associations**: Mapping UML multiplicities (`0..*`, `1`, `0..1`) to Python instance attributes (lists, required parameters, optional `None`)
- **Encapsulation**: Private (`__name`), protected (`_name`), and public attributes with getter methods; UML visibility markers (`+`, `#`, `-`)
- **Inheritance and polymorphism**: Subclass syntax (`class Kind(Eltern)`), `super().__init__()`, and method overriding
- **Typical AI errors at class level**: Mutable default in `__init__`, missing `self`, and `cls` instead of `self`
- **Code verification checklist**: Three questions for critically reviewing AI-generated class code

## Key takeways (What are the resulting takeways/skills teached)
- Translate any UML class diagram into correct Python by applying a systematic element-by-element mapping
- Use `self` for instance methods, `cls` for `@classmethod`, and no first parameter for `@staticmethod`
- Avoid mutable defaults (`[]`, `{}`) in `__init__` parameter lists — use `None` with explicit initialization instead
- Verify AI-generated class code against the UML diagram by checking attributes, method signatures, associations, and encapsulation
- Distinguish instance attributes (`self.x` in `__init__`) from class attributes (defined at class level, shared across all instances)
- Implement UML associations as instance attributes whose type depends on multiplicity (`0..*` → list, `1` → required param, `0..1` → optional `None`)
- Apply the three-question verification checklist: what is modeled, which requirements are implemented, what could go wrong

## Code Examples (What code examples are shown)
- **`class Raum` with `__init__`**: Demonstrates translating UML attributes (`name: str`, `fläche: float`, `höhe: float`) into Python constructor with `self` assignments
- **`class Raum` with methods and associations**: Shows `berechne_volumen()` and `get_fenster()` methods plus `self.fenster = []` for `0..*` association to `Fenster`
- **`class Punkt` with `__init__`**: Minimal example of constructor with default parameters (`x=0.0, y=0.0`)
- **Instance vs. class attributes**: Side-by-side comparison of `self.fläche` (per-instance) vs. `einheit = "m²"` (shared across all instances)
- **Association implementation with `add_fenster`**: Shows how to grow a `0..*` list association using `append`
- **Encapsulation with private attribute `__fläche`**: Demonstrates name-mangled private attribute and a getter method
- **Inheritance: `Serverraum(Raum)`**: Subclass calling `super().__init__()` and adding its own attribute `kühlleistung`
- **Mutable default error**: `def __init__(self, fenster=[])` — shared list bug — corrected with `fenster=None` pattern
- **Missing `self` error**: Method without `self` parameter causing `TypeError`
- **`cls` instead of `self` error**: Using class method convention on an instance method
- **`raum = Raum(name="Büro 1", ...)`**: Instance creation with named parameters and attribute/method access via dot syntax

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_6.svg` — Course module overview diagram showing the part structure: Motivation, Computerarchitekturen, Programmierung und Datentypen, Fehler und Debugging, **Objektorientierung u. Softwareentwurf** (highlighted), and Verweisungen und Schleifen / Funktionen und Rekursion
- `images/06b_Objects/mj_title_band.jpg` — Bauhaus-style architectural line drawing (Midjourney) used as decorative title image in the `%%book` block
- `images/04c_Objects/mj_title_band.jpg` — Reused Bauhaus architectural line drawing from S04, referenced in the quiz slide for cross-context

## Plots
None

## Examples (What examples are used)
- **BIM (Building Information Modeling) domain**: The `Raum` (room) class with attributes like `fläche` and `höhe`, and associations to `Fenster` (windows) — modeling real building data
- **"KI als Junior-Entwickler" (AI as junior developer)**: The lecture frames AI as a code generator that produces syntactically correct but sometimes semantically flawed class code — students learn to review rather than trust
- **Hörsaalfrage (lecture hall quiz question)**: Students are asked to identify the correct Python class that corresponds to the UML diagram of `Raum` from S04
- **Quizdown quiz**: 13 multiple-choice and ordering questions covering UML-to-Python translation, AI error detection, constructor behavior, `super()`, encapsulation, and instance vs. class attributes
- **Cross-references**: Links to S04 (UML design), S06c (module organization), and S08b (code review best practices for OOP)

## Remarks
- The lecture is entirely in **German** (slides, notes, quiz) but this summary is written in English per instructions, with original German terms preserved in parentheses.
- The lecture intentionally does **not** contain deep code — it focuses on the translation layer between UML design and Python, preparing students to read and verify AI-generated code.
- The `%%note Merksatz:` block provides the memorable rule: "`self` = Instanzmethode · `cls` = `@classmethod` · kein Parameter = `@staticmethod`"
- Henry Ford's quote ("Nothing is particularly hard if you divide it into small jobs") opens the `%%book` block, setting the pedagogical tone of breaking down OOP into manageable translation steps.
- The `%%warning` block explicitly calls out the danger of mutable class attributes (lists, dicts) being shared across all instances.
- The `%%slides` flow follows a clear pedagogical pattern: UML mapping → Python syntax detail → AI error patterns → verification checklist.
# Summary: Modularisierung (Modularization)

This lecture introduces the principles of Python module organization and project structure. It explains how to split code across multiple files to keep programs maintainable, scalable, and collaboratively manageable. A key theme is the relationship between **module boundaries** and **AI-assisted code generation** — the lecture argues that deciding where one module ends and another begins is an architectural decision that directly shapes how AI-generated code integrates into a project. The lecture also covers Python's import system, the `main()` entry-point pattern, and the role of external packages (via PyPI) in turning Python into a pipeline and glue language.

## Main topics (What is the structure of the lecture)
- **Projektstruktur als Architekturentscheidung**: Why large programs must be split across files; module organization strategies (one class per file, one topic per file, one task area per file); hierarchical packages (`geometry/points/`, `geometry/shapes/`).
- **Module als KI-Generierungseinheiten**: Designing modules for AI-generated code — clear public interfaces, private helpers (`_` prefix), minimal imports; example prompt → `sensor_processing.py`.
- **Verifikation generierter Module**: Checklist for verifying AI output: correct function name, return type, private marking, and minimal imports.
- **Die `main()`-Funktion und `__name__`-Pattern**: The standard entry point; using `if __name__ == "__main__":` to prevent execution on import; best practices (only function/class definitions before `main()`, no global assignments or side effects).
- **Import-System in Python**: Three import styles — `import package.module`, `import as`, and `from ... import`; handling deeply nested packages with aliases; the `*` wildcard import.
- **Standard-Pakete und externe Bibliotheken**: Overview of Python standard library modules (os, json, urllib, logging, etc.); installing third-party packages via `pip`; end-to-end example: fetching weather data from DWD API, processing with pandas, visualizing with plotly, serving with dash.
- **Priorisierung (Lesson Learned)**: Eisenhower matrix metaphor for task prioritization in software projects.

## Key takaways (What are the resulting takeways/skills teached)
- **Design module boundaries deliberately** — they determine how AI-generated code fits into your project and how teams collaborate.
- **One class per file** when defining classes; **one topic/task per file** for utility functions, to keep code discoverable and avoid version conflicts.
- **AI-generated modules should have a clear public interface** — expose named public functions/classes, mark helpers as private with `_`, and import only what is needed.
- **Always use `if __name__ == "__main__":`** to make `.py` files safe to both run directly and import as libraries.
- **Avoid global variables and side effects at module top level** — only function and class definitions should appear before the `__name__` guard.
- **Prefer `from ... import as` for concise, readable imports** of submodules or individual names without full dotted paths.
- **Python's strength lies in its ecosystem** — PyPI offers 400,000+ packages; Python works as an interface and pipeline language by composing existing libraries.
- **Verify AI-generated code against the original prompt** — check function signature, return types, privacy of helpers, and import cleanliness.

## Code Examples (What code examples are shown)
- **`sensor_processing.py` (AI-generated)**: Demonstrates a module with a public function `clean_readings(values)` that filters outliers using 2σ, plus a private helper `_is_outlier`.
- **`main()` with `__name__` guard**: `def main(): print(...)`, followed by `if __name__ == "__main__": main()` — the standard Python entry-point pattern.
- **Full package imports**: `import geometry.points.ImmutablePoint` showing how deeply nested dotted paths must be spelled out.
- **Import with alias**: `import geometry.points.ImmutablePoint as point` — shortens long dotted references.
- **`from ... import`**: `from geometry.shapes.Line import Line` — imports a single class directly into namespace.
- **`os.listdir` usage**: Iterating over files in a directory with `os.path.isfile` checks.
- **DWD weather API fetch**: Using `urllib.request` to fetch JSON from a weather station API, `json.loads` to parse, `pprint.pprint` to display.
- **External package installation**: `subprocess.run(["pip", "install", "pandas", "plotly", "dash", "--quiet"])`.
- **Pandas DataFrame + Plotly line chart**: `pd.DataFrame(wetter[...])` → `px.line(df, x="dayDate", y=["temperatureMin", "temperatureMax"])`.
- **Dash web app**: Creating a Dash app with `dash.html.Div`, `dash.html.H1`, and `dash.dcc.Graph` to serve an interactive plot.

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partB_1.svg`: Course overview diagram showing the Part B curriculum blocks: "Fehler und Debugging", "Objektorientierung und Softwareentwurf", "Funktionen und Rekursion", "Datenhaltung", "Datenbanken", "Datenbankentwurf", "Trends und KI".
- `images/06c_Module/priotisierung.svg`: Midjourney-generated SVG diagram illustrating the Eisenhower matrix for prioritization (urgent vs. important).
- `images/06c_Module/wetter.png`: Screenshot of a web page displaying weather data chart served by a Dash app.
- `images/06c_Module/pip.png`: Screenshot of the PyPI website showing the Python Package Index.
- `images/06c_Module/eisenhower.jpg`: Photo of Dwight D. Eisenhower's desk with the famous prioritization quote ("I have two kinds of problems, the urgent and the important...").
- `images/06c_Module/mj_title_band.jpg`: Cover-style band image for the book section, sourced from Midjourney (Modular Blocks, Piet Mondrian).
- `images/06c_Module/mj_title.mp4`: Short background video on the title slide, Midjourney-generated.

## Plots
- `px.line` weather chart (temperatureMin / temperatureMax over dayDate) — rendered as SVG via `fig.show(renderer="svg")`, `[static]`.
- Dash Graph component rendering the same plot in a web page — `[interactive]`.

## Examples (What examples are used)
- **`geometry` package**: A full hierarchical project structure example grouping geometry classes into `points/` (ImmutablePoint, Point) and `shapes/` (Line, Triangle, Pentagon, etc.).
- **`city.py` project**: A simple three-file project (`city.py`, `buildings.py`, `streets.py`, `geometry.py`) demonstrating basic imports.
- **DWD weather station API**: Real-world scenario of fetching weather forecasts for Rostock-Hansaviertel (station ID 12495) from the German Weather Service API and building a full data pipeline (fetch → parse → visualize → serve).
- **AI agent workflow**: "KI als Junior-Entwickler" — treating the AI like a junior developer who produces a module from a prompt, which you then verify against the specification.
- **Eisenhower matrix metaphor**: Using the urgent/important framework as a lesson-learned bridge for prioritizing software tasks.
- **Cross-reference**: Links back to [Klassendefinition](04c_Objects.ipynb) lecture for geometry class definitions from a prior topic.

## Remarks
- The lecture is in **German** throughout, with English technical terms kept where appropriate. German terms like **Modularisierung**, **Verifikation**, and **Modulegrenzen** appear on first reference in parentheses.
- The `%%slides` blocks use `%%col`, `%%sep`, and `%%div` structural syntax — these are Quarto-specific and excluded from the summary per the rules.
- There are no `%%note Merksatz:` blocks in this lecture; takeaways are derived from `%%book` explanatory text and the verification checklist under `%%slides`.
- The external weather API example demonstrates a realistic end-to-end workflow (API → JSON → Pandas → Plotly → Dash) and uses `--quiet` pip installation for reproducibility.
- No plotly animation frames or `.json`/`.pvd` plot files were found — all plots are static (or interactive via Dash).
- An existing `06c_Module.summary.md` file is already present in the directory; this rewrite replaces it.
# Summary: Exceptions

This lecture introduces the concept of **exceptions** in Python and how they relate to the broader framework of software debugging, particularly in the context of **AI-generated code**. It builds on the course's foundational topics — the knowledge pyramid (Wissenspyramide) and fundamental programming elements — to frame exceptions as semantically-level errors that reveal violated assumptions. The lecture teaches students to read and interpret Python tracebacks, apply **guard clauses** to protect against invalid inputs, and use `try-except` blocks for structured error handling. It also introduces a practical **agentic workflow** for diagnosing and fixing AI-generated code that throws exceptions.

The lecture is organized around three layers of error classification (lexical/syntactic, semantic, and logical) and demonstrates how exceptions specifically address semantic errors — code that is syntactically valid but fails at runtime. Through concrete Python examples (sensor data analysis, recursive factorial computation, custom division functions), students learn to identify, handle, and raise exceptions deliberately. The lecture concludes with a comprehensive quiz that reinforces key concepts about traceback analysis, guard clauses, `try-except-else-finally` blocks, and the agentic debugging cycle.

## Main topics (What is the structure of the lecture)
- **Wiederholung (Review):** Recap of the knowledge pyramid (Wissenspyramide) and fundamental programming elements (statements, functions, conditionals, loops) to establish a framework for error classification.
- **Ablauf (Workflow):** Overview of Part A lecture sequence positioning this lecture within the broader course structure.
- **KI-Code und Exceptions:** AI-generated code often contains implicit assumptions about inputs; exceptions reveal which assumption was violated — diagnosed via **traceback analysis** (bottom-to-top reading).
- **Guard Clauses:** Explicit precondition checks at the start of functions to prevent crashes from `None` returns, empty lists, or zero divisors.
- **Agentic Workflow for Exception Diagnosis:** A 4-step cycle — read traceback → identify violated assumption → add guard clause or fix data → reprompt with explicit constraint.
- **Klassen von Fehlern (Error Classifications):** Errors classified along the knowledge pyramid (lexical, syntactic, semantic, logical), by frequency/reproducibility (deterministic vs. sporadic), and by detection time (static vs. dynamic).
- **Lexikalische und syntaktische Fehler:** Characteristics, examples (misspelled keywords, unclosed quotes, wrong indentation), and typical handling strategies.
- **Semantische Fehler und Exception-Handling:** `try-except` blocks, typed vs. untyped exception catching, `else` and `finally` clauses, and traceback-driven diagnosis.
- **Exceptions selbst erzeugen:** Using `raise` with specific exception types (e.g., `ValueError`, `RecursionError`), exception propagation up the call stack.
- **Logische Fehler:** Characteristics (often no exceptions, wrong results), examples (wrong conversion factor, wrong loop type, timezone bugs), and handling via unit tests and debugging.
- **Quiz:** 18 questions covering traceback reading, guard clauses, `try-except`, `raise`, error classification, and agentic debugging workflows.

## Key takeways (What are the resulting takeways/skills teached)
- **Read tracebacks bottom-to-top:** The lowest line shows the crash point, the exception type reveals the violated assumption, and upward lines show the call path.
- **Guard clauses prevent semantic crashes:** Check for `None`, empty collections, zero divisors, and wrong types at function entry before risky operations.
- **AI-generated code errors signal violated assumptions, not fundamental failure:** Each exception is a diagnostic hint about missing constraints in the original prompt.
- **Use typed exceptions in `try-except`:** Catch specific types (`TypeError`, `ZeroDivisionError`) rather than bare `except` for precise error messages and targeted handling.
- **Leverage `else` and `finally` in `try-except`:** `else` runs only when no exception occurs; `finally` always runs (ideal for cleanup like closing files).
- **Raise specific exceptions with `raise`:** Use meaningful exception types (`ValueError`, `RecursionError`) to make error handling at higher stack levels more informative.
- **Follow the agentic debugging cycle:** Traceback → identify assumption → add guard/fix data → reprompt with explicit constraint.
- **Logical errors require tests and debugging tools:** Unlike semantic errors, they produce wrong results without exceptions; unit tests and debuggers are the primary remedies.

## Code Examples (What code examples are shown)
- **Sensor data analysis with implicit `None` assumption:** `hole_messungen()` returns `None` via `dict.get()` when sensor ID is missing, causing `TypeError` in `berechne_mittleren_durchfluss()` — demonstrates how AI-generated code silently assumes non-None returns.
- **Guard clause version of sensor analysis:** Adds `if messungen is None` and `if len(messungen) == 0` checks to prevent `None` and `ZeroDivisionError` crashes.
- **Untyped `try-except` for division:** Catches all exceptions when dividing by zero, printing a generic "Divisionsfehler" message.
- **Typed `except Exception as e` for division:** Captures the exception type and message, showing how to inspect errors programmatically.
- **Multiple typed `except` blocks (`TypeError`, `ZeroDivisionError`):** Demonstrates specific exception handling with distinct error messages for wrong input types vs. division by zero.
- **`try-except-else-finally` full pattern:** Shows all four blocks working together — success path in `else`, guaranteed output in `finally`.
- **Custom `division()` function with `raise ValueError`:** Demonstrates explicit guard clauses combined with typed exception raising for invalid input types.
- **Recursive `factorial_recursiv()` with `RecursionError` guard:** Depth limit of 20; calling with `21` triggers a `RecursionError` — demonstrates exception propagation up the call stack.
- **`try-except` with `traceback.print_exc()`:** Catches `RecursionError` and prints the full stack trace for diagnosis.

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_7.svg` — Workflow diagram showing the lecture sequence (Ablauf) for Part A, Section 7.
- `images/03a_Wissenspyramide/pyramide1.svg` — Knowledge pyramid diagram used in the review section, showing Zeichen → Daten → Informationen → Wissen hierarchy.
- `images/wissenspyramide.svg` — Knowledge pyramid diagram used to illustrate error classification (lexical, syntactic, semantic, logical) along pyramid levels.
- `images/07a_Exceptions/mj_title_band.jpg` — Title band image for the lecture (AI-generated, inspired by Salvador Dalí).
- `images/07a_Exceptions/mj_title.mp4` — Animated title background video for the HTML slide deck.

## Plots
- None

## Examples (What examples are used)
- **KI als Junior-Entwickler:** The lecture frames the AI as a junior developer who writes working code but makes silent assumptions about inputs (e.g., "sensor always exists"), producing exceptions in real-world scenarios.
- **Sensor data analysis:** A concrete real-world scenario where an AI-generated function to calculate average flow fails when a sensor ID is not found — connects exceptions to practical data analysis workflows.
- **Recursive factorial with depth guard:** Demonstrates exception propagation in recursive functions and the need for stack-level error handling.
- **Murphy's Law ("Anything that can go wrong, will go wrong"):** Used as an epigraph in the book block to frame the lecture's philosophy.
- **Quiz examples:** Includes practical error scenarios like division by zero, incorrect `raise` usage (string instead of exception object), and ordering exercises for constructing correct `try-except` blocks.

## Remarks
- The lecture is written primarily in **German** with English technical terms (e.g., *guard clauses*, *traceback*, *try-except*, *agentic workflow*).
- Cross-references to other lectures: `08a_UnitTest` (unit testing), `07b_Debugging` (debugging tools, breakpoints).
- The lecture intentionally does **not** contain deep code — it focuses on concepts, error classification, and the diagnostic workflow for AI-generated code.
- The quiz section contains 18 questions including multiple-choice, multi-select, and ordering exercises. Quiz answers are marked with `[x]` and are excluded from the Code Examples section.
- The lecture references Midjourney AI-generated imagery throughout (title card, section headers, cross-references to other lectures' title images).
- The agentic workflow presented reflects the course's broader theme of **iterative AI-assisted development** — treating exceptions as feedback signals rather than failures.
# Summary: Debugging

This lecture introduces a systematic **five-step debugging strategy** specifically tailored for debugging AI-generated code. It argues that while logics errors in AI-generated programs rarely produce exceptions or tracebacks, they still require structured investigation — not blind reading or trial-and-error. The lecture bridges a conceptual framework (Reproduce → Isolate → Hypothesize → Inspect → Fix & Re-verify) with practical tooling (`print()` debugging, Python's `logging` module, and IDE graphical debuggers), positioning debugging as the critical **Verify** step in the agentic coding loop (`prompt → generate → understand → verify → iterate`).

The lecture is positioned after exceptions (`07a_Exceptions`) and before unit testing (`08a_UnitTest`), framing debugging as the connective tissue between error detection and error prevention. It emphasizes that the choice of tool matters less than disciplined application of the strategy itself.

## Main topics (What is the structure of the lecture)
- **Five-step debugging strategy** — systematic approach: Reproduce, Isolate, Hypothesize, Inspect, Fix & Re-verify
- **Step 1: Reproduce** — find minimal input that triggers the bug; determine whether it is deterministic or conditional
- **Step 2: Isolate** — write a focused unit test for the suspect function; cross-references lecture `08a_UnitTest`
- **Step 3: Hypothesize** — contrast expected vs. actual behavior; identify common wrong assumptions (wrong types, off-by-one, unhandled edge cases)
- **Step 4: Inspect** — use breakpoints and step-through debugging to observe where expectation diverges from reality
- **Step 5: Fix & Re-verify** — apply minimal fix, re-run unit test, check neighboring functions for collateral damage
- **Debugging tools** — `print()` debugging, Python `logging` module, and IDE graphical debuggers (VS Code, Jupyter)
- **Multi-function module walkthrough** — debugging nested AI-generated functions using Step Into/Over/Out navigation
- **Quiz** — reinforcement of core concepts (definition of debugging, limitations of static analysis, logging purpose, try-except structure)

## Key takeways (What are the resulting takeways/skills teached)
- A bug you cannot **reproduce** is a bug you cannot debug — always start with minimal failing input
- **Isolate** the problem by writing a targeted unit test before inspecting anything else
- Formulate an explicit **hypothesis** by comparing expected output to actual output; watch for wrong types, parameter order, off-by-one errors, and unhandled edge cases
- The **debugger** shows the full execution state — `print()` only shows what you chose to display
- Apply a **minimal fix** and re-verify with both the unit test and adjacent functions
- In IDE debuggers, **Step Into** suspect code, **Step Over** known-correct code, and **Step Out** when you've gone too deep
- Always start debugging at the **entry point** of the call chain, not deep inside the code
- Debugging is the **Verify** step in the agentic coding workflow: `prompt → generate → understand → verify → iterate`

## Code Examples (What code examples are shown)
- `print()`-based `division(zaehler, nenner)` function with debug logging for input parameters, type-checking errors, zero-division warnings, and result output — demonstrates verbose `print`-debugging
- `division(10, 0)` — minimal reproduction of the zero-division error case
- `for nenner in range(-2, 8): division(10, nenner)` — loop showing how excessive `print()` output can obscure real errors
- `logging`-based `division` function using `log.debug`, `log.error`, `log.warning`, and `log.info` — demonstrates categorized, filterable logging
- `log.setLevel(logging.WARNING)` — filters the same loop to show only warnings
- `log.setLevel(logging.DEBUG)` — elevates verbosity for debugging
- Custom `logging.Formatter` with `%(asctime)s`, `%(name)s`, `%(levelname)s`, and `%(message)s` — demonstrates timestamped, named log output for cloud/production debugging
- Multi-function nested example (`verarbeite_daten → bereinige → berechne → formatiere`) — illustrates why debugger navigation is needed for AI-generated code with multiple functions

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_7.svg` — course structure diagram showing where Debugging fits in Part A
- `images/07b_Debugging/mj_title_band.jpg` — title banner image (Midjourney: wave/boat)
- `images/07b_Debugging/mj_title.mp4` — title slide background video
- `images/07b_Debugging/debug_vscode_1.png` — VS Code screenshot showing how to set a breakpoint
- `images/07b_Debugging/debug_vscode_2.png` — VS Code debug control icons (start debug, step-into, etc.)
- `images/07b_Debugging/debug_vscode_3.png` — VS Code debugger panel showing highlighted line, variables, and call stack during a debug session

## Plots
- None

## Examples (What examples are used)
- **Division by zero** — the running code example throughout the lecture: a `division(zaehler, nenner)` function that handles type validation and zero-division gracefully
- **AI as multi-function generator** — the `verarbeite_daten` → `bereinige` → `berechne` → `formatiere` chain illustrates how AI-generated code often contains several nested functions, making simple `print()` debugging insufficient
- **Cloud application debugging** — real-world scenario: production servers log at `INFO` level but switch to `DEBUG` when errors occur, requiring log-based investigation instead of screen output
- **Quiz reinforcement** — multiple-choice questions covering debugging definition, static vs. dynamic analysis, `print`-debugging, `logging` purpose, try-except structure, and zero-division behavior
- **Cross-reference to agentic workflow** — debugging is framed as the "Verify" step: `prompt → generate → understand → verify → iterate`

## Remarks
- The lecture is in **German**, with all summary content rendered in English per instructions
- The `%%note Merksatz:` blocks provide key memory aids ("Ein Bug, den man nicht reproduzieren kann, kann man nicht debuggen"; "Starte immer am Anfang der Aufrufkette")
- The `%%tip Agentic Workflow` blocks explicitly connect debugging to the agentic coding paradigm used in the course
- Cross-references to `07a_Exceptions` (preceding lecture) and `08a_UnitTest` (following lecture) situate this lecture within a debugging pipeline
- The quiz block uses the `{quizdown}` format but quiz answer code blocks are excluded from the Code Examples section per the extraction rules
- The lecture does not cover advanced topics (e.g., remote debugging, logging to files, assertion-based debugging) — scope is introductory
# Summary: Unit-Tests

This lecture introduces unit testing as a foundational practice in software development and, more specifically, in **agentic programming** where AI generates code. It reframes tests from being merely a quality-control tool to being the **specification** itself — the precise, machine-readable description of expected behavior that guides an AI in producing correct code. The lecture covers the spectrum of error-management strategies (prevention, detection, correction, handling, and exclusion), with a deep focus on unit testing techniques including functional tests, boundary-value tests, and data-type tests. It culminates in the concept of **Test-Driven Prompting (TDP)**, a workflow where tests are written before prompting an AI, providing verifiable acceptance criteria for generated code.

The lecture uses a running environmental engineering example — classifying soil contamination levels — to demonstrate the full TDP cycle: writing tests, receiving AI-generated code, identifying failures, diagnosing bugs, and iterating. It also introduces **test coverage** (line and branch coverage) as a metric for evaluating how thoroughly tests exercise generated code, emphasizing that untested branches in AI output represent invisible risks.

## Main topics (What is the structure of the lecture)
- **Introduction to Unit-Tests**: Definition, purpose, and the role of `assert` for simple validation
- **Five error-management strategies**: Prevention, detection, correction, handling, and exclusion
- **Error detection types**: Syntactic errors (IDE), static errors (lint tools), and dynamic errors (automated unit tests)
- **Test-Driven Prompting (TDP)**: Writing tests before prompting an AI to operationalize requirements
- **TDP workflow cycle**: Understand requirement → write tests → prompt AI → execute tests → iterate on failure
- **Running example — soil contamination classification**: Full TDP demonstration with 5 tests and AI-generated code
- **Test coverage**: Line coverage vs. branch coverage as metrics for untested code risks
- **Three test types**: Functional tests, boundary-value tests, and data-type tests using the `division()` function
- **Error handling in Python**: `try`/`except`/`raise`/`finally`/`else` mechanism and exception propagation
- **Semantic errors and exceptions**: Exception stack unwinding, exception levels (OS, language, custom), and real-world use cases
- **Error exclusion**: Formal mathematical verification (Hoare calculus) for safety-critical systems
- **Quiz**: Multiple-choice review covering all lecture concepts

## Key takeways (What are the resulting takeways/skills teached)
- **Tests are the specification**: Writing tests before code (or before prompting an AI) operationalizes requirements into measurable conditions
- **A failed test on AI code is success**: It means a bug was caught before deployment
- **Three test strategies**: Functional tests verify correct outputs, boundary-value tests check edge cases, and data-type tests validate unexpected inputs
- **Use `assert` for quick inline tests** or frameworks like `unittest` / `nose` for automated test suites
- **Test coverage matters**: Branch coverage is more important than line coverage because AI code often contains hidden conditional branches
- **`try`/`except`/`raise` pattern**: Catch known exceptions, handle them gracefully, and re-raise when appropriate to propagate errors up the call stack
- **Iterative debugging cycle**: Write tests → get AI code → run tests → diagnose failure → reprompt → re-test

## Code Examples (What code examples are shown)
- `division()` function (lines 59–70): A division function with type checking, zero-division handling, and print statements — used as the running example throughout the lecture
- Functional test `test_funktion()`: Asserts correct results for multiple input/output pairs (10/2=5, 10/5=2, etc.)
- Boundary-value test `test_grenzwert()`: Tests `math.inf`, division by zero (returns `None`), and `math.nan` edge cases
- Data-type test `test_datentyp()`: Uses `try-except` blocks to verify that invalid input types raise `ValueError`
- Simplified `division()` (line 765): Trivial `zaehler / nenner` to demonstrate how tests catch regressions
- **Soil contamination example — 5 TDP tests**: Tests for "Sauber", "Beobachten", "Kritisch" classifications plus two boundary cases at values 50 and 150
- **AI-generated `klassifiziere_boden()` (first version)**: Contains a subtle off-by-one bug at the ≥150 boundary
- **Reprompt diagnosis and corrected `klassifiziere_boden()`**: Shows the fix and the iterative TDP workflow
- `count_up_and_down()` with `try-except`: Demonstrates exception propagation and raising `ValueError`

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partB_2.svg`: Workflow diagram showing the lecture's position in Part B of the course
- `images/08a_UnitTest/stack3.svg`: Illustrates exception stack unwinding — exceptions propagate upward through call frames
- `images/08a_UnitTest/stack4.svg`: Shows exception handling — catching and resolving an exception before it propagates further
- `images/08a_UnitTest/mj_title_band.jpg`: Midjourney artwork (waves testing a boat, Hokusai reference) used as a thematic visual for the lecture
- `images/08a_UnitTest/mj_title.mp4`: Video background for the title slide (same Midjourney theme)

## Plots
- None

## Examples (What examples are used)
- **Soil contamination classification** (`klassifiziere_boden`): The central running example — classifying mg/kg measurements into "Sauber", "Beobachten", or "Kritisch" categories with defined thresholds (< 50, 50–149, ≥ 150)
- **Division function** (`division(zaehler, nenner)`): Used to demonstrate functional, boundary-value, and data-type testing across multiple sections
- **Robert C. Martin quote**: "The only way to go fast is to go well" — frames the philosophy that careful testing enables speed
- **Quiz questions**: 10 multiple-choice questions reinforcing lecture concepts including TDP, test types, coverage, and assertion behavior
- **Cross-references**: Links to lecture `01c_AgentischesProgrammieren` (agentic cycle), `04a_Anforderungen` (requirements), and `08b_CodeReview` (next verification step)

## Remarks
- The lecture is taught in **German** but uses English code and technical terminology (e.g., `assert`, `AssertionError`, `try-except`)
- The `%%book` blocks contain the main instructional content, while `%%slides` blocks are used for slide-style summaries, definitions (`%%def`), and structured layouts (`%%col`, `%%sep`)
- **Mermaid diagrams** are used to visualize test flow (input → function → output) for functional, boundary, and data-type tests
- The distinction between the **classical view of tests** (detect errors in finished code) and the **agentic view** (tests define behavior and serve as AI acceptance criteria) is a key conceptual pivot in the lecture
- Quiz content uses `quizdown` with shuffled questions and answers
- The lecture intentionally bridges traditional testing practices with the emerging paradigm of AI-driven development, positioning testing as a specification tool rather than just a verification tool
# Summary: Code Review

This lecture introduces **Code Review** as the essential verification step in an agentic programming workflow where AI tools like Claude Code or GitHub Copilot generate code. It argues that AI-generated code must be reviewed just as rigorously — and perhaps even more carefully — than human-written code, because AI displays no uncertainty signals and often produces syntactically correct but functionally incomplete or architecturally misaligned code. The lecture presents a structured, three-dimensional review framework (requirements, design, implementation) augmented with a concrete checklist and an agentic loop: generate → understand → verify → iterate.

The core thesis is that Code Review fills the gap that automated tests cannot cover: it catches missing requirements, design mismatches against UML specifications, and AI-specific hallucinations (non-existent functions, wrong API usage). The lecture positions Code Review as the **Verify** phase of the agentic cycle, closing the loop between prompting an AI and producing reliable code.

## Main topics (What is the structure of the lecture)
- **Introduction — Why review AI code?**: AI tools produce code quickly but not always correctly; AI shows no uncertainty, making human review indispensable
- **Three dimensions of Code Review**: Requirements verification (Does it do what was asked?), design verification (Does it match the architecture?), and implementation verification (Is it correct, safe, maintainable?)
- **Requirements verification**: Systematically checking each functional requirement against the code using an "Implemented → Tested → Passing?" three-question framework
- **Requirements tracing example**: A concrete Python function for calculating slope percentage with a missing multiplication-by-100 — demonstrating how tests reveal incomplete implementations
- **Design verification**: Comparing generated code against UML design — checking module structure, class names, method signatures, and detecting structural mismatches
- **Design mismatch example**: UML `Messung` class vs. AI-generated `DataPoint` class — showing wrong names, wrong attributes, and missing methods
- **Implementation verification**: Systematic scanning for common error patterns: division by zero, mutable default arguments, missing type annotations, hardcoded values
- **Implementation scan checklist**: A deterministic six-point checklist for every AI-generated code block
- **AI hallucinations**: Non-existent functions, non-existent modules, wrong API usage, and unnecessary abstractions — errors that only surface at runtime
- **KI-Evaluierungscheckliste (AI evaluation checklist)**: A seven-point structured checklist spanning all three review dimensions to reduce cognitive load
- **Code Review as the Verify phase**: Positioning review within the agentic cycle (Prompt → Generate → Understand → Verify → Iterate) and the feedback loop for failed reviews

## Key takeways (What are the resulting takeways/skills teached)
- **AI code is confidently wrong**: AI models generate syntactically plausible but incomplete or incorrect code without showing any uncertainty — human judgment is non-negotiable
- **Review covers what tests cannot**: Tests verify execution; Code Review verifies requirements coverage, design alignment, and architectural consistency
- **Three-dimensional review model**: Always check requirements, design, and implementation — each dimension catches different classes of errors
- **Use a deterministic implementation scan**: Systematically check for division-by-zero, mutable defaults, missing type annotations, hardcoded values, missing return statements, and meaningful exceptions
- **Verify every import and method call against documentation**: AI hallucinates functions and modules that don't exist — only running code or checking docs catches these
- **Treat UML design as a review standard**: AI doesn't know your architecture — always compare generated classes, methods, and modules against the planned design
- **The agentic verify-iterate loop**: When review fails, name the specific error in the prompt, use checklist items as prompt refinements, regenerate, and re-review
- **Tests automate; Code Review catches blind spots**: Automated tests are necessary but insufficient — review fills the gaps

## Code Examples (What code examples are shown)
- `berechne_neigung()` — slope calculation missing `× 100`: Demonstrates how AI can implement a formula partially, leaving a requirement unfulfilled
- `assert berechne_neigung(1, 10) == 10.0`: A test that exposes the missing percentage conversion (returns 0.1 instead of 10.0)
- `Messung` (UML) vs. `DataPoint` (AI-generated): Shows naming mismatch, attribute mismatch, and missing `validiere()` method — design drift
- `neigung(h, l)` with and without null check: Demonstrates `ZeroDivisionError` prevention via explicit `ValueError`
- `sammle()` with mutable default `liste=[]` vs. `liste=None`: Classic Python pitfall corrected to avoid shared mutable state
- `verarbeite()` with and without type annotations: Shows adding `list[float]` type hints for clarity
- Hardcoded `temp > 100` vs. `MAX_TEMP_CELSIUS = 100`: Demonstrates replacing magic numbers with named constants
- `df.interpolate_missing()` / `df.to_geojson()`: Hallucinated pandas methods that don't exist
- `import geopandas_lite` / `import pandas.geospatial`: Hallucinated modules
- `model.fit_transform(X_test)` / `model.score(X, y, metric="f1")`: Misused scikit-learn API calls
- `class SingletonLoader`: Unnecessary abstraction over-engineered by AI for a one-time use case
- Agentic cycle diagram (text-based flowchart): `Prompt → Generate → Understand → Verify → Iterate`

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/08b_CodeReview/mj_title_band.jpg`: Midjourney artwork — thematic cover image for the lecture (referenced but not present on disk)
- `images/08b_CodeReview/mj_engineers_reviewing.png`: Midjourney image — two engineers reviewing blueprints together (referenced but not present on disk)
- `images/08b_CodeReview/mj_title.mp4`: Video background for the title slide (referenced in YAML but not present on disk)

## Plots
- None

## Examples (What examples are used)
- **Slope calculation (`berechne_neigung`)**: A real-world engineering scenario — computing incline percentage from height and length — used to demonstrate incomplete requirement implementation
- **Soil measurement class (`Messung` vs `DataPoint`)**: A domain modeling example showing how AI invents class names that don't match the UML specification
- **"If everyone is thinking alike, then somebody isn't thinking" — George S. Patton**: Opening quote framing the necessity of independent human judgment in code review
- **AI as Junior-Entwickler (implicit analogy)**: Throughout the lecture, AI is implicitly treated like a junior developer who writes correct-looking but incomplete code — requiring supervision
- **Cross-references**: Links to `04a_Anforderungen` (requirements as review standards), `03c_Softwareentwurf` (UML design as the second review standard), `08a_UnitTest` (tests as automated verification), and the agentic cycle from `01c_AgentischesProgrammieren`
- **Quiz-like checklist**: The KI-Evaluierungscheckliste functions as a self-assessment tool covering all seven review points across the three dimensions

## Remarks
- The lecture is taught in **German** but uses English code and technical terms (e.g., `AttributeError`, `ZeroDivisionError`, `ValueError`)
- No `images/08b_CodeReview/` directory exists on disk — referenced images (`mj_title_band.jpg`, `mj_engineers_reviewing.png`, `mj_title.mp4`) are not present in the repository
- No SVG diagrams, Plotly plots, or animated visuals are used in this lecture — it is primarily text/code/checklist driven
- The `%%note Erkennungsstrategie` block is a practical tip: check every `import` and method call against documentation, and **run** the code — don't just read it
- The `%%tip Merksatz` block distills the core message: "Tests check automatically. Code Review checks what tests can't see."
- This lecture is a natural successor to `08a_UnitTest` — where unit tests automate verification, Code Review handles what automation misses
- The lecture intentionally avoids deep code — it focuses on review *process* and *checklists* rather than coding techniques
- The agentic workflow diagram (text-based flowchart) visually anchors Code Review as the "Verify" step in the agentic programming cycle
- The bibliography `references.bib` is declared but no specific citations appear in the lecture body
# Summary: Algorithmen

This lecture introduces the foundational concepts of algorithms as well-defined, unambiguous procedural instructions and teaches students to first identify the **problem class** of a task before selecting an appropriate algorithm. It covers four core problem classes — **sorting**, **searching**, **pathfinding**, and **partition** — and presents classic algorithms for each, from naive approaches (Bubble Sort, linear search) to efficient ones (Quick Sort, binary search). The lecture culminates in a practical discussion of algorithm complexity (**Big-O notation**) and a meta-skill: how to correctly prompt AI coding assistants by embedding problem-class knowledge into your prompts, ensuring they generate efficient rather than merely functional code.

## Main topics (What is the structure of the lecture)
- **Introduction to algorithms:** Definition as well-defined procedural instructions; programming = algorithms + data structures
- **Four problem classes:** Sorting, searching, pathfinding, and partition — with recognition cues and example algorithms for each
- **Heuristics:** Approximate methods like A* that sacrifice optimality guarantees for practical speed on complex problems
- **Tree data structures:** Binary trees as recursive structures, representation in Python (dicts and tuples), recursive traversal
- **Sorting algorithms:** Bubble Sort, Quick Sort, Insertion Sort, and Python's built-in `sorted()` with performance comparisons
- **Searching algorithms:** Linear search, binary search (on sorted lists and binary search trees), Python's `in` operator and `set` lookups
- **Algorithmic complexity:** Big-O notation ($O(n)$, $O(\log n)$, $O(n^2)$, $O(n \log n)$) and empirical performance benchmarks
- **AI and algorithm selection:** How AI defaults to naive algorithms, and strategies for prompting AI with problem-class knowledge to get optimal solutions

## Key takeways (What are the resulting takeways/skills teached)
- **Identify the problem class first** (sorting, searching, path, or partition) before choosing or implementing any algorithm
- **Bubble Sort modifies in-place** (mutating the original list), while Quick Sort returns a new sorted list — know the difference
- **Binary search requires sorted input** and achieves $O(\log n)$ vs. linear search's $O(n)$, making it orders of magnitude faster on large datasets
- **Binary search trees enable efficient search** without separate sorting, because they maintain sorted order during insertion
- **Python's built-in `sorted()` uses Timsort** (a C-implemented hybrid of merge/insertion sort) and is the pragmatic default for production code
- **Use `set` for membership tests** on large datasets — hash-based lookups are roughly $O(1)$, far faster than list or tree-based search
- **Prompt AI with the problem class** explicitly (e.g., "implement a binary search") to avoid naive, inefficient code generation
- **Always verify AI-generated algorithm code:** check correctness, termination conditions, and complexity class against expectations

## Code Examples (What code examples are shown)
- **Tree representation as a dictionary** (`baum = {"wert": 12, "links": {...}, "rechts": {...}}`) — demonstrates recursive data structure modeling
- **Recursive tree traversal** (`traverse(tree)`) — prints all node values in depth-first order (left before right)
- **Bubble Sort implementation** (`bubbleSort(numbers)`) — nested loops comparing adjacent elements and swapping out-of-order pairs
- **Quick Sort implementation** (`quickSort(elements)`) — divide-and-conquer using a pivot to partition into less/equal/greater lists, then recursively combine
- **Insertion Sort implementation** (`insertion_sort(arr)`) — iteratively inserts each element into its correct position in the sorted prefix
- **Python `sorted()` usage** — one-line replacement showing the production-recommended approach
- **Performance benchmarks with `timeit`** — comparing all four sorting algorithms on both small (7 elements) and large (10,000 elements) datasets
- **Linear search / `contains()`** — naive `for` loop checking each element for equality
- **Binary search implementation** (`binarySearch(arr, suchwert)`) — recursive divide-and-conquer on a sorted array
- **Binary search tree search** (`suchBaum(tree, suchwert)`) — exploits sorted structure to traverse only one path
- **Binary search tree insertion** (`erweitereBaum(tree, neuer_wert)`) — builds a sorted tree incrementally by inserting values one at a time
- **Python `in` operator and `set` membership** — idiomatic comparisons between list lookup and hash-set lookup
- **Large-scale search benchmarks** — empirical comparison of linear search, binary search, tree search, and set lookup on 5,000-element datasets

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partA_6.svg` — workflow diagram showing the algorithm development process (Problemklasse → Algorithmus → Implementierung)
- `images/09a_Algorithmen/astar.svg` — A* pathfinding algorithm visualization showing search expansion on a grid with obstacles
- `images/09a_Algorithmen/bin_suche.svg` — binary search visualization showing recursive division of a sorted array
- `images/09a_Algorithmen/polymap.png` — map illustrating a point-in-polygon test scenario (e.g., building within a flood zone)
- `images/09a_Algorithmen/polymap2.png` — Google Maps-style visualization of polygon containment
- `images/09a_Algorithmen/mj_title_band.jpg` — decorative title image (Midjourney: "Two Towers, ref. M.C. Escher")
- `images/09a_Algorithmen/astar.gif` — animated A* search demonstration showing progressive exploration of the grid
- `images/09a_Algorithmen/bin_suche.png` — static binary search illustration (companion to the SVG)

## Plots
- None — this lecture uses static diagrams, SVG illustrations, and GIF animations but no plotly or data plots.

## Examples (What examples are used)
- **Rain gauge station monitoring:** "Find the nearest rain gauge station to a monitoring point" → **search** (minimum distance)
- **Construction bid ordering:** "Order construction bids by cost" → **sorting**
- **Flood route calculation:** "Calculate the shortest access route to a flood zone" → **pathfinding** (Dijkstra, A*)
- **Building classification in flood zones:** "Check which buildings lie within the flood zone" → **partition** (point-in-polygon test, Ray Casting)
- **AI as a junior developer analogy:** AI tends to generate the most obvious (naive) algorithm — linear search instead of binary search, Bubble Sort instead of Quick Sort — because it optimizes for code that *works and is readable*, not for *performance*
- **Card-sorting metaphor for Insertion Sort:** mirrors the human strategy of inserting playing cards into a hand in sorted order
- **Quiz scenarios:** multiple-choice and ordering exercises covering algorithm definitions, sorting mechanics, tree structure, and AI prompting pitfalls

## Remarks
- The `%%def Algorithmen` block provides the formal definition: "Algorithmen sind wohldefinierte, eindeutige Handlungsanweisungen."
- The lecture includes interactive **Hörsaalfragen** (lecture hall questions) at the start and middle, using real-world spatial scenarios (Google Maps, rain gauge networks) to prime problem-class identification.
- The **A* algorithm** is presented as an "Exkurs" (digression) — a heuristic for NP-complete pathfinding problems on grids with obstacles.
- The lecture is part of a sequence: this is **09a_Algorithmen**, with **09b_Rekursion** following as a deeper dive into recursion as a Divide-and-Conquer strategy.
- All code examples use Python. The `timeit` benchmarks demonstrate empirical performance differences, reinforcing theoretical Big-O analysis with concrete timing data.
- The lecture concludes with a **Quiz** block (`%%book`) containing multiple-choice and code-ordering questions covering all topics.
- The Einstein quote ("Everything should be made as simple as possible, but not simpler") frames the lecture's philosophy: algorithm design balances simplicity with sufficient complexity to solve the problem correctly and efficiently.
# Summary: Rekursion

Dieser Vortrag führt das Konzept der **Rekursion** als allgemeine Lösungsstrategie für Probleme ein, die sich in kleinere Teilprobleme desselben Typs zerlegen lassen. Rekursion wird dabei nicht als Python-spezifische Syntax präsentiert, sondern als Implementierung des **Divide-and-Conquer**-Prinzips — einer der fundamentalen Algorithmenstrategien der Informatik. Der Fokus liegt auf ingenieurspraktischen Anwendungen aus der Bauplanung (BIM-Modelle) und Umweltinformatik (Quadtree-Räumliche Unterteilung), wobei KI-generierter Code bewusst als Lernmaterial dient, den es zu lesen und zu verifizieren gilt, nicht blind zu übernehmen.

Die Session beginnt mit der Grunddefinition des rekursiven Musters (Basisfall und rekursiver Fall), zeigt eine minimale Python-Einführung über die Fakultät und warnt vor Endlosrekursion. Anschließend werden zwei domänenspezifische Beispiele vertieft: die rekursive Traversierung von BIM-Gebäudemodellen und die quadratische Raumaufteilung durch einen Quadtree. Der Vortrag schließt mit einer Abwägung zwischen Rekursion und Iteration und einer Leitlinie für die praktische Entscheidung, wann welcher Ansatz gewählt werden sollte.

## Main topics
- **Rekursion als Divide-and-Conquer-Strategie**: Definition, Grundmuster aus Basisfall und rekursivem Fall, Bezug zu Session 09a (Algorithmen)
- **Python-Syntax am Beispiel Fakultät**: Minimalbeispiel zur Einführung der rekursiven Funktion, Warnung vor Endlosrekursion und Stack Overflow (Verweis auf Session 02: Call-Stack)
- **Agentic Workflow zur Code-Verifikation**: Drei-Schritte-Check für KI-generierte rekursive Funktionen (Basisfall identifizieren, erste Aufrufe manuell durchspielen, Stack-Tiefe abschätzen)
- **BIM-Hierarchie traversieren**: Gebäudeframework als natürliches rekursives Problem — Stockwerke, Räume, Elemente; KI-generierter Traversierungscode zum Verstehen und Verifizieren
- **Quadtree — räumliche Unterteilung**: Rekursive Aufteilung geografischer Gebiete in vier Quadranten für GIS, Sensornetze und Geländemodelle; Basisfall bei Tiefenlimit oder ≤ 1 Punkt
- **Rekursion vs. Iteration**: Pro/Contra-Vergleich, Entscheidungsmatrix: wann Rekursion (hierarchische Daten, kontrollierbare Tiefe) und wann Iteration (flache Listen, Performance-kritisch)

## Key takeways
- **Rekursion ist Divide-and-Conquer in Code**: Jedes rekursive Problem zerlegt sich in gleichartige Teilprobleme bis ein direkt lösbare Basisfall erreicht ist
- **Jede rekursive Funktion braucht explizit einen Basisfall**, der ohne Selbstaufruf terminiert — sonst führt das zu einem `RecursionError` bei ~1000 Aufrufen in Python
- **KI-generierter rekursiver Code ist ein Lernwerkzeug**: Studierende sollen Basisfall und rekursiven Schritt selbst verifizieren, nicht blind übernehmen
- **BIM-Modelle sind natürliche Rekursionsziele**: Gebäude → Stockwerke → Räume → Elemente — dieselbe Funktion traversiert alle Ebenen
- **Quadtree ist Divide-and-Conquer auf geometrische Gebiete**: Vier quadratische Unterregionen, Rekursion bis zu einer maximalen Tiefe oder wenn jeder Bereich ≤ 1 Punkt enthält
- **Rekursion ist ausdrucksstark äquivalent zu Iteration**, aber die Wahl hängt von Datenstruktur, Lesbarkeit und Stack-Risiken ab

## Code Examples
- `factorial(x)`: Minimales rekursives Python-Beispiel zur Einführung der Syntax — Berechnet x! durch rekursiven Abstieg auf den Basisfall x ≤ 1
- `bim_traversiere(element, tiefe=0)`: KI-generierte Funktion zur rekursiven Traversierung von BIM-Gebäudemodellen; gibt jede Ebene mit Einrückung aus und demonstriert impliziten Basisfall über leere `kinder`-Liste
- `quadtree_unterteile(grenzen, punkte, max_tiefe, tiefe)`: Divide-and-Conquer-Funktion teilt ein rechteckiges Gebiet in vier Quadranten auf, je mit ihren enthaltenen Punkten; Basisfall bei `max_tiefe` oder ≤ 1 Punkt
- Allgemeines rekursives Muster (`löse(problem)`): Template, das das Grundschema aller rekursiver Funktionen abbildet: Basisfall → Zerlegung → rekursive Delegation → Kombination

## Visualizations
- `images/09b_Rekursion/mj_title_band.jpg` — Titelbild (Midjourney: Fractal)
- `images/09b_Rekursion/mj_title.mp4` — Titel-Video-Hintergrund (Fractal-Animation)
- `images/09b_Rekursion/image_1.jpg` — Verwendet in der Hörsaalfrage zu Inventarisierung mehrstöckiger Gebäude und in der Mindmap-Folie (Midjourney: Building floor plan / BIM hierarchy)
- `images/09b_Rekursion/stack_1.svg` — SVG-Diagramm des Call-Stacks (verwiesen im Kontext von Endlosrekursion und Verweis auf Session 02)
- `images/09b_Rekursion/stack_2.svg` — SVG-Diagramm des Call-Stacks (zweiter Stack-Status, Kontext: Rekursions-Tiefe)

## Plots
- None

## Examples
- **Inventarisierung mehrstöckiger Gebäude**: Hörsaalfrage — Wie inventarisiert man alle Räume eines Gebäudes ohne vorher die Tiefe zu kennen? → rekursiver Ansatz
- **BIM-Gebäudemodell "Gebäude A"**: Konkretes Beispiel mit Stockwerken, Räumen (101, 102, 201), Tür und Fenster — zeigt die hierarchische Struktur als natürlicher rekursiver Anwendungsfall
- **KI als Junior-Entwickler**: Leitmotiv — KI generiert rekursiven Code, Studierende sollen ihn lesen und verifizieren (Basisfall prüfen, manuelle Trace, Stack-Tiefe)
- **SOPALR-Lerntechnik (Survey, Question, Read, Recite, Review, Reflect)**: Mindmap-basierte Nacharbeitsempfehlung am Ende der Session, mit YouTube-Verweisen
- **Verweis auf S02**: Call-Stack, Stack Overflow und Speichermodell werden wiederholt auf Session 02 verwiesen — keine Wiederholung, sondern Verknüpfung

## Remarks
- Die Sprache des Vortrags ist **Deutsch**; Fachbegriffe wie **Rekursion**, **Basisfall**, **rekursiver Fall**, **Quadtree** und **BIM** werden im Deutschen behandelt und teilweise im Englischen belassen.
- Es gibt **keine Plotly-Visualisierungen** in dieser Session — der Fokus liegt rein auf algorithmischem Verständnis und Code-Verifikation.
- Die Vorlage `Löse(problem)` im `%%book`-Block dient als abstraktes Schema und wird in den `%%slides` etwas vereinfacht wiederholt — leichte Variation zwischen Book- und Slide-Version.
- Die Videodatei `mj_title.mp4` dient als Hintergrund für die Titel-Folie (Reveal.js-Feature); die Video-Folie "Six Sense" (Lesson Learned) referenziert `images/03a_Wissenspyramide/mj_senses.mp4` aus einer anderen Session.
- Der Vortrag ist Teil der Reihe **S09** (Algorithmen und Entwurf), speziell die vertiefende rekursive Komponente nach S09a.
- Die Struktur `::: {.content-visible unless-format="typst"}` und andere Quarto-Formatierungssyntax wurden gemäß den Regeln ignoriert.
# Summary: Graphprobleme

This lecture introduces **graph problems** (Graphprobleme) as a fundamental modeling paradigm for engineering applications, particularly in civil engineering. It teaches students to recognize when a real-world problem can be represented as a network of entities and connections, and how to solve such problems using graph algorithms. The lecture bridges theoretical graph concepts with practical Python implementation via **NetworkX**, while also showing how to leverage AI tools to specify, implement, and verify graph-based solutions.

The content is structured around three pillars: (1) recognizing and formulating graph problems from domain scenarios, (2) core graph algorithms for traversal and shortest-path computation, and (3) a complete AI-augmented workflow for modeling, solving, and verifying graph problems. By the end, students should be able to identify graph problems in their own work, select the appropriate algorithm (BFS, DFS, or Dijkstra), and implement solutions with proper verification.

## Main topics (What is the structure of the lecture)
- **Graphprobleme erkennen**: Identifying whether a problem is a graph problem based on entities, connections, and reachability/flow questions
- **Der Graph als Datenstruktur**: Nodes (vertices), edges, weights, and directionality; `nx.Graph` vs `nx.DiGraph`
- **Traversierung und kürzeste Wege**: Breadth-first search (BFS), depth-first search (DFS), and Dijkstra's algorithm for weighted shortest paths
- **Mit KI Graphprobleme lösen**: Using AI to generate graph code, prompting patterns, and a verification checklist

## Key takeways (What are the resulting takeways/skills teached)
- **Recognize graph problems** by spotting entities + connections + path/flow/reachability questions in any domain
- **Choose the right graph type**: `DiGraph` for directional flows (drainage, one-way streets), `Graph` for symmetric connections (pipes with pressure equalization, two-way roads)
- **Match algorithm to question**: BFS for unweighted hop-distance, DFS for reachability and connected components, Dijkstra for weighted shortest paths
- **AI-augmented workflow**: "Recognize → Specify → Verify" — prompt a graph problem template, generate NetworkX code, then verify with a structured checklist
- **Always verify**: check graph type, edge weights exist and are non-negative, and algorithm matches the problem before trusting results

## Code Examples (What code examples are shown)
- **Creating a directed graph with weighted edges**: Builds a road network with `time` weights and computes the shortest path from A to D using `nx.shortest_path` and `nx.shortest_path_length`
- **Visualizing a weighted graph with matplotlib**: Draws the network with node positions, labels, and edge weight labels using `nx.draw` and `nx.draw_networkx_edge_labels`
- **Algorithm selection code snippets**: `nx.bfs_tree`, `nx.dfs_tree`, `nx.connected_components` for traversal; `nx.is_connected` for connectivity checks
- **Verification code**: `G.is_directed()`, `nx.get_edge_attributes(G, "time")` to validate graph configuration
- **Prompt template for AI**: Structured prompt pattern to generate NetworkX graph code for any domain (road network, drainage, floor plan)

## Visualizations (What visualizations plotly/svg/etc. are used)
- **`mj_title_band.jpg`**: Cover image for the book-style opening section
- **`mj_title.mp4`**: Background video on the title slide — blueprint-style city road and water pipe network viewed from above
- **`mj_netzwerk.png`** (referenced, not present in filesystem): Blueprint-style image of interconnected roads and water pipes under a city — used to introduce the concept of network modeling
- **`mj_graph_abstract.png`**: Abstract visualization of connected nodes and edges on a dark background — used to illustrate what a graph problem looks like conceptually
- **ASCII diagrams**: Text-based illustrations of unirected graphs, directed graphs (Digraph), BFS layer progression (Schicht 0–3), and DFS path traversal

## Plots
- None (no plotly or chart-based visualizations used)

## Examples (What examples are used)
- **Road network routing**: Intersections as nodes, roads as edges, travel time as weight — finding the shortest route A → B
- **Pipe network flow**: Valves as nodes, pipes as edges, diameter/length as weight — minimizing pressure loss
- **Building floor plan connectivity**: Rooms as nodes, doors as edges — checking if all rooms are reachable
- **Drainage network**: Catchment areas as nodes, flow directions as edges, slope/capacity as weight — tracing where water flows
- **Evacuation routing**: A→C→B→D with weighted travel times (3 + 2 + 1 = 6 min) demonstrating Dijkstra vs BFS on the same network
- **AI prompt example**: Specifying a drainage network graph problem for an LLM, with catchment areas (ha), flow directions (slope %, length m), and finding the path from "EZG_07" to "Kanal_A"

## Remarks
- The lecture is part of the **Programmieren und Datenbanken** course (indicated by the `footertext`)
- Code examples are **AI-generated** and explicitly flagged with "vor dem Ausführen lesen" (read before executing) — students are prompted to reason about correctness before running
- The lecture includes a structured **verification checklist** (Graphtyp prüfen, Gewichte prüfen, Algorithmus prüfen) as a critical habit
- Uses the German **BFS layer numbering** ("Schicht 0", "Schicht 1", etc.) consistent with German technical education terminology
- The `%%note Merksatz` block defines the formal graph definition: G = (V, E)
- The image `mj_netzwerk.png` is referenced on slide 33 but does not exist in the `lectures/images/10a_Graphprobleme/` directory — may need to be added
- No plotly or animated visualizations are present; the lecture relies on ASCII diagrams and static images for illustration
# Summary: Geometrieprobleme

This lecture introduces **geometric problems** as a core problem class in civil engineering, showing how tasks ranging from CAD floor-plan analysis to BIM collision detection and GIS flood-zone mapping all reduce to a small set of fundamental geometric operations. The lecture teaches students to recognize the common structure underlying these diverse applications — input coordinates and shapes, queries about containment, distance, or intersection, and boolean/numeric outputs — and to solve them using the Python library **`shapely`**. A strong emphasis is placed on the frequent pitfalls of **AI-generated geometric code**, particularly the neglect of coordinate reference systems (KBS), and on systematic verification strategies for engineering software.

The lecture is structured into six thematic blocks: the nature and domains of geometric problems, vector algebra fundamentals, basic geometric operations, the `shapely` library, coordinate systems and projections, and AI prompt patterns and verification. Through concrete civil-engineering scenarios (sensor placement, hospital proximity, pipeline collision, parcel overlap), students learn to abstract real-world problems into standard geometric primitives and operations.

## Main topics (What is the structure of the lecture)
- **Geometrische Probleme** — definition, problem-class signature, and application domains (CAD, BIM, GIS, network routing) in civil engineering
- **Ingenieursanwendungen** — concrete building and infrastructure examples: footprint calculation, point-in-room checks, collision detection, and road alignment
- **Vektoralgebra** — fundamental geometric objects (points, line segments, polygons) and operations (Euclidean distance, 2D cross product for orientation)
- **Grundoperationen** — the three core operations (contains/within, distance, intersects/intersection) unified under `shapely`
- **shapely** — the Python standard library for 2D geometry: core types, methods (`.area`, `.buffer()`, `.contains()`), and reading AI-generated code
- **Koordinatensysteme** — why projections matter: WGS84 (degrees) vs. local metric systems (UTM, EPSG:25833), and how to transform with `pyproj`
- **KI-Prompt-Muster** — how to write precise geometric prompts specifying CRS, units, and libraries; common AI error patterns
- **Verifikation** — systematic checklist for reviewing AI-generated geometric code: geometry types, CRS, closed polygons, float tolerance

## Key takaways (What are the resulting takeways/skills teached)
- Recognize that diverse engineering problems share a common structure: **three operations** (contains/within, distance, intersects/intersection) solve them all
- Use **`shapely`** as the go-to Python library for 2D geometric computations in civil engineering
- Always specify a **coordinate reference system (KBS)** — never compute distances on raw WGS84 coordinates
- Write **precise AI prompts** that explicitly state CRS, units, and target libraries to avoid silent bugs
- Apply a **verification checklist** before executing AI-generated geometric code (geometry type, CRS, polygon closure, float tolerance)
- Use **numerical tolerance** (`TOL = 1e-9`) instead of exact equality for floating-point geometric comparisons
- The **ray-casting algorithm** (odd = inside, even = outside) underlies Point-in-Polygon tests

## Code Examples (What code examples are shown)
- **Geometric primitives** — creating points, line segments, and closed polygons as Python tuples/lists
- **2D cross product** — `kreuzprodukt_2d()` function to determine whether a point lies left, right, or on a directed line
- **Point-in-Polygon with shapely** — `zone.contains(sensor)` and `sensor.within(zone)` to test if a sensor lies inside a building zone
- **Distance calculation** — `Point.distance()` to find the distance between a hospital and an accident location
- **Line intersection** — `LineString.intersects()` and `.intersection()` to detect and locate pipeline crossings in BIM
- **Buffer and area** — computing building area and creating a 5-meter buffer zone around a polygon
- **AI-generated code to read** — `gebaeude_in_radius()` function that finds buildings within a radius using `.buffer()` and `.intersects()`
- **Projection with pyproj** — transforming WGS84 coordinates to UTM (EPSG:25833) using `Transformer.from_crs()` and `shapely.ops.transform`
- **Float tolerance pattern** — replacing `== 0` with `< TOL` for robust distance comparisons

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/10b_Geometrieprobleme/mj_title_band.jpg` — artistic title image (Midjourney: geometric city plan / architectural blueprint)
- `images/10b_Geometrieprobleme/mj_title.mp4` — animated title slide background video (Midjourney-generated)
- `images/10b_Geometrieprobleme/mj_hoersaalfrage_geometrie.png` — referenced image for lecture question slide (engineer analyzing 3D city model blueprint); **not found** on disk
- `images/10b_Geometrieprobleme/mj_building_footprint.png` — Midjourney image of a building footprint, used to illustrate building geometry examples

## Plots
- None

## Examples (What examples are used)
- **Plato quote** — "God eternally geometrizes" frames the philosophical underpinning of geometry
- **Sensor in a room** — Point-in-Polygon: checking whether a sensor lies inside a building space
- **Nearest hospital** — Distance calculation: finding the closest hospital to an accident location
- **Pipeline collision** — Intersection check: detecting whether two pipes cross in a BIM model
- **Parcel overlap** — Area intersection: determining if two construction plots overlap
- **Flood zone analysis** — GIS scenario: which buildings lie in a flood-prone zone
- **Berlin → Potsdam distance** — Concrete demonstration of the WGS84 vs. UTM pitfall (0.35° meaningless vs. 28,422 m correct)
- **Midjourney AI art** — Repeated use of AI-generated images (geometric city plans, engineering blueprints) as slide visuals

## Remarks
- The lecture is in **German** (title, headings, body text), but this summary is written in English per the template guidelines. Key German terms are preserved in parentheses on first reference.
- Several `%%tip` blocks contain **"Merksatz"** (mnemonic) statements, e.g., "Ungerade = drinnen. Gerade = draußen." (Odd = inside. Even = outside.)
- The lecture deliberately uses **no plotly or animated plots** — it is a conceptual and code-oriented lecture focused on geometric problem abstraction.
- The `%%note Häufiger KI-Fehler` block highlights a specific, recurring AI code error: computing distances directly from WGS84 coordinates.
- The image file `mj_hoersaalfrage_geometrie.png` is referenced in the HTML but **not present** in the `images/10b_Geometrieprobleme/` directory.
- The lecture uses `%%scol` (split columns), `%%sep` (column separators), and `ai4sc-icon` shortcode elements typical of the AI4SC Quarto style extension.
- The lecture intentionally bridges **engineering intuition** with **programmatic practice**, positioning the engineer as a verifier of AI-generated geometric code rather than a passive consumer.
# Summary: Raster-Simulation

This lecture introduces **raster (grid) data** as a fundamental paradigm for representing continuous environmental phenomena — such as terrain elevation, temperature, precipitation, and air quality — in a discretized, computable form. It bridges the conceptual understanding of what a raster is (a regular grid of equal-sized cells, each holding a single value) with practical Python/NumPy operations for loading, analyzing, and visualizing raster data. A strong through-line is the **agent-centric workflow**: using AI to generate code while the student takes responsibility for specifying metadata, verifying results, and avoiding common pitfalls like unmasked NoData values or mismatched raster shapes.

The lecture is structured into three conceptual layers: (1) the theory and examples of raster problems in environmental engineering, (2) hands-on NumPy operations including reclassification, overlay, zonal statistics, slope calculation, and visualization, and (3) a meta-layer on AI-generated code — common traps, verification checklists, and reusable prompt patterns. It positions itself as a follow-up to the vector data lecture (`10b_Geometrieprobleme`) and a precursor to interactive dashboard design (`11b_UIDesign`), completing the spatial data representation arc of the course.

## Main topics (What is the structure of the lecture)
- **Raster problem class**: Definition of rasters, resolution as a modeling decision, and the trade-off between detail and computational cost
- **Environmental raster examples**: Digital elevation models (DGM), precipitation/climate grids, land cover and air quality rasters
- **Raster data structure**: 2D NumPy arrays as the core data structure, metadata requirements (shape, cell size, extent, CRS, NoData)
- **Raster operations**: Reclassification (threshold masks), overlay (element-wise combination of two rasters), zonal statistics (aggregation within zones)
- **NumPy terrain analysis demo**: Synthetic 20×20 terrain generation, slope calculation via `np.gradient`, and 3-panel visualization
- **AI pitfalls and prompt patterns**: Metadata traps that AI overlooks, NoData handling mistakes, reusable prompt templates, and a verification checklist
- **Agentic workflow**: Six-step cycle (recognize → specify → generate → understand → verify → iterate) for solving raster problems with AI assistance

## Key takeways (What are the resulting takeways/skills teached)
- **Rasterize continuous fields** by discretizing them onto a regular grid; resolution is a conscious modeling choice, not a technical default
- **Always mask NoData values** before any computation to avoid corrupted means, sums, and thresholds
- **Use NumPy boolean indexing** for threshold masks, overlay arithmetic, and zonal aggregation
- **Verify AI-generated code** with a small synthetic test case before applying it to real geodata
- **Specify complete metadata in prompts** (phenomenon, cell size, NoData value, output type, test case) to reduce AI errors
- **Check shape and extent alignment** before performing overlay operations — AI does not verify this automatically
- **Calculate slope numerically** using `np.gradient` and the Pythagorean formula, then convert to percent or degrees

## Code Examples (What code examples are shown)
- **5×5 terrain array**: Creating a small synthetic elevation grid and inspecting `.shape`, `.dtype`, `.min()`
- **NoData filtering**: Masking `-9999` values with a boolean index, computing mean with `np.nanmean()` as a float alternative
- **Reclassification / flood mask**: Creating a binary mask (`terrain < 110`), counting affected cells, computing the fraction
- **Overlay (risk index)**: Element-wise multiplication of a probability raster and a damage raster to produce a combined risk raster, with an `assert` shape check
- **Zonal statistics**: Iterating over zone IDs, masking the terrain array, and computing per-zone mean elevation
- **Synthetic 20×20 terrain generation**: Using `np.linspace` + `np.random.normal` to create a realistic-looking elevation grid
- **Slope calculation**: Using `np.gradient` to compute numerical derivatives in x and y, then converting to percent and degrees
- **Three-panel visualization**: `plt.subplots(1, 3)` displaying terrain height, slope percentage, and flood risk mask side-by-side
- **NoData bug demonstration**: Comparing a buggy function (`np.mean(grid > t)` without filtering) against a corrected version
- **Corrected `fraction_above` function**: Full AI-generated function with NoData filtering, edge-case handling (all NoData), and an integrated `assert` test
- **Prompt template code blocks**: Two text-based templates for crafting complete raster analysis prompts for AI

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/11a_Raster_Simulation/mj_title_band.jpg` — Opening band image (Midjourney aerial river catchment)
- `images/11a_Raster_Simulation/mj_watershed.png` — Satellite view of a German river catchment (referenced in slide `imgR` attribute, used as the introductory discussion image)
- `images/11a_Raster_Simulation/mj_terrain.png` — Midjourney hillshade visualization of a digital elevation model over a forested valley
- `images/11a_Raster_Simulation/mj_title.mp4` — Background video on the title slide (Midjourney aerial view)

## Plots
- **Three-panel terrain visualization** (matplotlib `imshow`): Terrain height (terrain colormap), slope percentage (Reds colormap), and flood risk mask (Blues colormap) — `[static]`

## Examples (What examples are used)
- **Aristotle's "whole is greater than the sum of its parts"** — framing the lecture theme
- **Hörsaalfrage (lecture question)**: "How would you store the elevation of every point in a watershed?" — used to engage students before introducing raster concepts
- **Flood risk index** = probability × damage potential — a concrete environmental engineering use case combining two rasters
- **Zone-based elevation statistics** — computing average elevation per sub-catchment zone
- **Bodenfeuchtigkeit (soil moisture) NoData bug** — demonstrating how `-9999` silently corrupts a mean calculation
- **Real-world resolution table**: Stadtplanung (1–5 m), Einzugsgebiet (10–50 m), Niederschlag (1 km), Klimamodell (25 km)
- **AI as Junior-Entwickler metaphor** (implicit throughout): AI produces correct array math, but the student must supply metadata, write tests, and verify — mirroring a junior developer workflow

## Remarks
- The lecture is in **German**, with all summaries and takeaways rendered in English per instructions. German technical terms like *Hangneigung* (slope), *Exposition* (aspect), *Zonenstatistik* (zonal statistics), and *Digitales Geländemodell* (DGM, digital elevation model) appear inline.
- The course uses **Quarto custom blocks**: `%%book` for key takeaways, `%%note` for definitions, `%%tip` for rules of thumb, `%%warning` for common pitfalls, and `%%references` for lecture connections.
- The lecture explicitly references **Pattern C** (read AI code before executing it) and the **agentic verification workflow**, positioning it within a broader pedagogical framework of the course.
- Cross-references: `10b_Geometrieprobleme` (vector vs. raster data) as predecessor, `11b_UIDesign` (dashboard visualization of raster results) as successor.
- No Plotly or animated plots are present; the only visualization is a static matplotlib `imshow` composite.
- The `data/11a_Raster_Simulation` directory is declared in frontmatter but contains no discoverable files — possibly a placeholder or external data resource.
- `mj_watershed.png` is referenced in a slide attribute (`imgR`) but does not exist as an isolated file in the images directory; it may be embedded or expected to be present at render time.
# Summary: UI-Design für Ingenieuranwendungen

This lecture addresses a gap often overlooked in engineering education: the design of user-facing interfaces for technical results. While engineering curricula emphasize calculation and simulation, they rarely cover how to present those results to decision-makers such as city planners, regulatory agencies, or management. The core thesis is that computation is merely an intermediate step — the choice of output format and interface is itself an engineering decision, not a peripheral concern.

The lecture introduces a structured approach to interface design using **Design Thinking** (Empathize → Define → Ideate → Prototype → Test), visual design principles from Edward Tufte and Gestalt psychology, and practical demonstrations with **Streamlit** and **Gradio** as Python-based UI frameworks. A key theme is the **agentive workflow**: using AI to generate initial code scaffolds in seconds, then applying systematic engineering verification to ensure correctness.

The lecture bridges into Block 6 (persistent data storage), positioning dashboards built on CSV files as a stepping stone toward database-backed systems that can handle millions of records and concurrent users.

## Main topics (What is the structure of the lecture)
- **UI-Typen im Vergleich**: Console, Jupyter, Streamlit, Gradio, and PDF as output formats — each serving different audiences and use cases.
- **Design Thinking für Ingenieur-UIs**: A five-step user-centered design process adapted for engineering dashboards and reports.
- **Design-Prinzipien**: Clarity, precision, Gestalt principles, Tufte's Data-Ink-Ratio, and affordances as foundations of good visual communication.
- **Agentischer Streamlit-Workflow**: Using AI to scaffold a Streamlit dashboard, then verifying column names, units, thresholds, and edge cases.
- **Gradio-Interfaces**: Parameter-input + model-execution pattern for sharing computation tools with non-technical colleagues.
- **UI-Verifikations-Checkliste**: A systematic four-category checklist (labeling, data mapping, representation, error handling) for validating AI-generated UIs.
- **Ausblick auf persistente Datenhaltung**: Limitations of CSV-based dashboards and motivation for relational databases in Block 6.

## Key takeways (What are the resulting takeways/skills teached)
- **Computation is an intermediate step, not an end** — presenting results correctly is an integral engineering responsibility.
- **Design Thinking structures user-centered UI development** — start with the audience's questions, not the data's dimensions.
- **Every chart should convey one message** — avoid overloading visuals with too many curves or axes.
- **Units are non-optional** — "value" is not information; "PM2.5 [µg/m³]" is.
- **AI generates scaffolds; engineers verify correctness** — apply Pattern C (AI-Code Reading) before running generated code.
- **Four verification dimensions ensure quality**: data mapping, representation, logic, and user guidance.
- **Falsely displayed data is more dangerous than inaccessible correct data** — systematic verification prevents silent misinformation.
- **Streamlit for data dashboards, Gradio for model interfaces** — choose based on whether the user loads data or runs a model.
- **CSV does not scale** — databases are the next step for production systems with large datasets and concurrent users.

## Code Examples (What code examples are shown)
- **KI-generiertes Streamlit Sensor-Dashboard**: A Streamlit app that loads a CSV, filters by location via dropdown, adds a threshold slider, and renders a Plotly line chart with a horizontal threshold line — demonstrates AI-generated scaffolding for a sensor-monitoring dashboard.
- **KI-generiertes Gradio Abfluss-Rechner**: A Gradio interface that takes rainfall amount and soil type as inputs, computes runoff using a simple factor, and returns the result — demonstrates AI-generated scaffolding for a parameter-to-model interface.

## Visualizations (What are the visualizations plotly/svg/etc. are used)
- `images/11b_UIDesign/mj_title_band.jpg` (JPEG): Cover image for the lecture section — Midjourney-generated title artwork.
- `images/11b_UIDesign/mj_title.mp4` (video): Background video for the title slide — Midjourney-generated futuristic engineering control room with sensor dashboards.
- `mj_engineer_presentation.png` (PNG, referenced but not present on disk): Described as "an environmental engineer presenting contamination risk maps to city planners" — intended as a contextual visual for the opening scenario.

## Plots
- None explicitly defined in this lecture (Plotly is referenced for the Streamlit dashboard but no pre-rendered plot file is included).

## Examples (What examples are used)
- **500 contamination sites scenario**: A realistic engineering case where 500 locations with 12-column CSV results must be presented to decision-makers — illustrates the gap between computation and communication.
- **PM2.5 sensor monitoring**: Air quality monitoring with threshold lines on Plotly charts — used throughout as the running example for UI design and verification.
- **Runoff calculator (Abfluss-Rechner)**: A simple hydrological model (rainfall × soil factor) wrapped in Gradio — demonstrates sharing domain-specific computation tools.
- **"KI als Junior-Entwickler"**: The metaphor of AI as a junior developer who produces working scaffolds but requires senior engineer review — reinforces the agentive workflow pattern.
- **Stadtrat (city council) vs. Python developer**: Contrasting audiences to illustrate why error messages and UI clarity must be tailored to the end user, not the developer.

## Remarks
- This lecture is **11b** in a sequence (following `11a_Raster_Simulation`), explicitly positioning itself as the presentation layer after computation.
- Cross-references include `08b_CodeReview` (verification principles) and `12a_Datenhaltung` (database introduction in Block 6).
- The lecture uses **Midjourney-generated images** for visual context (title slide, section headers, scenario illustrations).
- The file references `mj_engineer_presentation.png` in slide attributes but this file does not exist on disk.
- Code blocks are marked with `eval: false`, indicating they are illustrative rather than meant to execute in the rendered slide.
- The lecture is delivered in **German** (course: "ProgrammierUebung"), with English summary here per instructions.
- No animated plots are present — Plotly is mentioned only as the intended chart library for the Streamlit dashboard.
# Summary: Datenhaltung

This lecture introduces the central role of **file handling** and **data persistence** in engineering workflows. Rather than treating files as mere storage, it frames them as the primary entry point through which specialized tools (sensors, GIS, BIM, CAD) deliver data to Python programs. The core thesis is that understanding the origin tool and its format conventions is a prerequisite for correctly reading, verifying, and processing data — especially when relying on AI-generated code that may assume idealized defaults.

The lecture progresses from the nature of files as engineering data channels, through memory hierarchies and file systems, into concrete Python I/O techniques. It then covers key data formats used in practice (CSV, JSON, GeoJSON, XML, XLSX) and concludes with an **agentic workflow for AI-code verification** when reading files, plus a forward-looking note on when files become insufficient and databases are needed.

## Main topics (What is the structure of the lecture)
- **Dateien als Eingangskanal**: Files are not just storage — they are the format through which engineering tools deliver data to Python programs.
- **Speicher und Dateisysteme**: Overview of storage hierarchies (registers → RAM → SSD/HDD), file systems, and where files sit in the computer architecture.
- **Dateien mit Python**: Core `open()`, `pathlib` operations, text vs. binary modes, and file management (listing, checking existence, deleting).
- **Fachformate verstehen**: Detailed survey of engineering-relevant formats — CSV, JSON, GeoJSON, XML, XLSX, ZIP — including their internal structure and use cases.
- **KI-Verifikation beim Datei-I/O**: Typical pitfalls of AI-generated file-reading code, verification checklist, and an agentic workflow for validating AI output against real data.
- **Grenzen von Dateien**: Strengths and limitations of file-based data handling; preview of databases (lecture 12b) and dashboard data access (lecture 11b).

## Key takeways (What are the resulting takeways/skills teached)
- Files are **engineering data channels** — always ask which tool produced the file before choosing how to read it.
- **Format choice is a modeling decision**, not a technical afterthought; file extension does not guarantee simplicity.
- When using `open()` with `with`, the file is automatically closed even if an error occurs.
- Use `pathlib.Path` for robust path handling, directory listing, existence checks, and file deletion.
- **Text ≠ simple**: a text format like GeoJSON or XLSX can be deeply nested or containerized internally.
- AI-generated `read_csv` code often assumes wrong encoding, delimiter, header position, or missing-value markers — **always verify on real sample data**.
- The agentic workflow for file I/O: (1) check encoding & separator, (2) verify header & missing values, (3) test on a small real sample, (4) refine prompts with source-tool knowledge.
- Files work well for import/export but struggle with concurrent access, versioning, and complex querying — databases are the next step.

## Code Examples (What code examples are shown)
- `with open("messung.csv", "rt") as fi: text = fi.read()` — reads an entire text file into a string; illustrates `read()` behavior and prompts discussion of data type and binary incompatibility.
- `pathlib` example with `Path.iterdir()`, `is_file()`, `exists()`, and `unlink(missing_ok=True)` — demonstrates directory listing, file filtering, existence checking, and safe deletion.
- `pd.read_csv(..., sep=";", encoding="latin-1", header=0, na_values=[...])` — proper pandas CSV reading with explicit encoding, separator, header, and missing-value handling; demonstrates verification on a sample read with `head()` and `dtypes`.
- `pd.read_csv("messung.csv")` (minimal AI-generated code) — used as a critique example to highlight four common failure modes (delimiter, encoding, header, missing values).

## Visualizations (What visualizations/ images are used)
- `images/12a_Datenhaltung/mj_title.mp4` — video background for the title slide (AI-generated).
- `images/12a_Datenhaltung/mj_title_band.jpg` — book cover image used in the `%%book` opening block (AI art: book/binder with "Datenhaltung").
- `images/12a_Datenhaltung/mj_title.png` — static title image alternative.
- `images/12a_Datenhaltung/image_4.jpg` — DALL-E 2 image (early iPhone designs by Leonardo da Vinci) used as the visual prompt for the lecture's opening question.
- `images/12a_Datenhaltung/computer_hardware2.svg` — SVG diagram of **Speicherhierarchie im Computer** showing register → cache → RAM → SSD/HDD hierarchy.
- `images/12a_Datenhaltung/oscomp.png` — image comparing operating-system-level file organization across platforms.

## Plots
None

## Examples (What examples are used)
- **Monitoring station scenario**: Time-series sensor data exported as CSV with semicolon delimiters, missing values as `-9999`, and possible Umlaute in headers — a realistic field-deployment situation.
- **GIS / BIM scenario**: GeoJSON from environmental tools (nested geometries in `properties`) and IFC/XML from planning software — illustrating domain-specific format challenges.
- **AI as junior engineer metaphor**: The lecture frames the AI code generator as assuming "plausible but wrong" defaults, mirroring how a junior developer might write `read_csv()` without verifying format details.
- **Quiz**: Four multiple-choice questions reinforcing key concepts (tool-specific formats, risky AI assumptions, CSV parameters, GeoJSON definition, XLSX internals).
- **Cross-references**: Links to lecture 11b (UIDesign dashboards reading data) and lecture 12b (database types) to position file handling as a stepping stone toward relational databases.

## Remarks
- The lecture is delivered in **German** with English summary (technical terms retained in German where relevant).
- Image credit given to **Midjourney** (librarian motif referencing Giuseppe Arcimboldo) and **DALL-E 2** (prompt illustration).
- The quiz block uses the `quizdown` quarto extension with shuffled questions and answers.
- This lecture is a conceptual/practical overview — it does not go deep into any single format but instead builds **format literacy** and **verification habits**, particularly for AI-assisted development.
- The structure follows a clear pedagogical arc: motivation → concepts → Python basics → format survey → AI-code pitfalls → limitations → preview of next topic.
# Summary: Datenbanktypen

This lecture introduces the landscape of database technologies and provides a framework for choosing the right database type based on the structure of the data — not on trends or popularity. It builds directly on lecture `12a_Datenhaltung`, which demonstrated the limits of file-based storage when dealing with growing data volumes, concurrent access, and complex queries. The core thesis is that the **information model** (tabular, document-like, graph/network, key-value, or full-text) should drive the database choice.

The lecture walks through five major database families — **relational**, **document stores**, **key-value stores**, **search-engine databases**, and **graph databases** — each linked to a specific information model and typical engineering use cases (e.g., BIM documents, pipeline networks, administrative records). It closes with an **agent verification checklist** for AI-assisted technology decisions and a set of memorization statements summarizing the selection heuristic: model first, technology second.

## Main topics (What is the structure of the lecture)
- **Grenzen dateibasierter Speicherung** — when files break down under concurrency, scale, and query complexity; callback to lecture `12a_Datenhaltung`
- **DB vs. DBMS vs. Datenbanksystem** — formal definitions distinguishing data, management system, and the combined system
- **Codd's requirements** — integration, user views, integrity, transactions, concurrency, and disaster recovery
- **The model-first selection heuristic** — matching tabular, document, graph, key-value, and full-text structures to database families
- **Relationale Datenbanken** — tables, schemas, SQL, JOINs, and integrity rules
- **Dokumentenorientierte Datenbanken** — JSON documents, flexible/nested structures, BIM use cases
- **Key-Value-Datenbanken** — simple key→value mapping, caching, sessions, extreme speed
- **Suchmaschinen-Datenbanken** — full-text search, ranking, stemming for unstructured documents
- **Graphdatenbanken** — nodes and edges, network/dependency modeling, connection to lecture `10a_Graphprobleme`
- **Agentischer Prüfpunkt** — a three-step AI verification workflow for database technology recommendations
- **Auswahlkriterien & Ausblick** — model before technology, design before implementation, preview of `12c_Datenbanken_Entwurf`

## Key takaways (What are the resulting takeways/skills teached)
- Switch to a database when file-based storage fails on **concurrency**, **scale**, or **integrity** requirements
- Always identify the **information model** of your problem before selecting a database technology
- **Relational databases** for stable, tabular data with strong consistency and JOINs
- **Document stores** for nested, variable-structure data (e.g., BIM objects, JSON-like payloads)
- **Key-value stores** for ultra-fast direct lookups, caching, sessions, and state management
- **Search-engine databases** for full-text retrieval across large corpora of reports and documents
- **Graph databases** for network/dependency problems where relationships are the core of the problem
- When using AI for tech recommendations, verify the **model-to-technology mismatch** before committing

## Code Examples (What code examples are shown)
None

## Visualizations (What visualizations/svg/etc. are used)
- `images/12b_Datenbanktypen/mj_title_band.jpg` — decorative title banner image
- `images/12b_Datenbanktypen/mj_thief.png` — Midjourney illustration of a thief breaking into a bank safe, used as a visual metaphor for file-based storage "overflowing"
- `images/12b_Datenbanktypen/databases.svg` — SVG diagram showing the distribution of database types across the ecosystem
- `images/12b_Datenbanktypen/mj_title.mp4` — video background for the title slide (Midjourney-generated)

## Plots
None

## Examples (What examples are used)
- **Pipe/traffic networks** → graph databases (cross-references `10a_Graphprobleme`)
- **BIM / project documents** with nested, variable objects → document stores
- **Structured administrative records** with consistent columns → relational databases
- **Reports, expert opinions, protocols** needing full-text search → search-engine databases
- **Caches, sessions, configuration, state** → key-value stores
- **Pat Helland quote** — "Eventually, you have to throw the data over a wall." — framing the boundary between applications and persistence
- **AI agent verification** — a structured three-step workflow for critically evaluating AI-suggested database technologies

## Remarks
- The lecture is intentionally **conceptual and comparative** — no code examples are included; the focus is on decision-making frameworks.
- Cross-references appear throughout: `12a_Datenhaltung` (file storage limits), `10a_Graphprobleme` (graph problems → graph databases), and `12c_Datenbanken_Entwurf` (design phase preview).
- The lecture uses a **German-language** pedagogical style with structured `%%book` (deep reading) and `%%slides` (presentation) blocks, `%%def` (definition) blocks, `%%col` (side-by-side columns), and `%%note`/`Merksätze` (memorization statements).
- Image credits attribute Midjourney-generated artwork (e.g., "Database Tree, ref. Gustav Klimt").
- The referenced image assets (`mj_thief.png`, `databases.svg`, etc.) are not present on disk but are clearly described through context.
- The lecture intentionally avoids the "which database is modern?" framing in favor of "which information model fits our problem?" — a design-first philosophy consistent with the course's engineering-oriented approach.
# Summary: 12c Datenbankentwurf

This lecture introduces the conceptual design phase of database development using Entity-Relationship (ER) diagrams, deliberately positioned before the SQL sessions in the course sequence. Its core thesis — echoing Linus Torvalds' dictum that good programmers worry about data structures rather than code — is that database modeling is a *specification* task distinct from implementation. The lecture establishes the ER diagram as the authoritative blueprint that must exist before any `CREATE TABLE` statements are written, including those generated by AI assistants.

The lecture progresses through three layers of database design (conceptual, logical, physical), teaches the building blocks of ER modeling (entities, attributes, relationships, cardinalities), and demonstrates the entire workflow using a concrete **Umweltmonitoring** (environmental monitoring) scenario: stations, sensors, and measurements. It culminates in an **agentic workflow** where the student produces an ER model, crafts a structured AI prompt from it, and then verifies the AI-generated SQL against the original specification line by line.

## Main topics (What is the structure of the lecture)
- **Design before implementation**: Why ER modeling precedes SQL, with analogy to software design (`03c_Softwareentwurf`)
- **Three layers of database design**: Conceptual (entities, relationships), logical (tables, keys, types), physical (indexes, performance)
- **ER fundamentals vs. UML**: Parallel modeling ideas — UML for software structure, ER for information structure
- **ER building blocks**: Entity types, entities, attributes, relationships, and cardinalities (`1`, `0..1`, `0..*`, `1..*`)
- **Notation**: UML-style `<<Entity>>` notation with `PK` markers and cardinality labels on relationships
- **Cardinality → SQL constraints**: Mapping ER cardinalities to `NOT NULL`, foreign keys, and multi-row relationships
- **Normalization**: 1NF (no nested lists/JSON in cells), 2NF (full dependency), 3NF (no transitive redundancy) with monitoring examples
- **ER-to-prompt workflow**: Structuring AI prompts with entities, relationships, and constraints; verification checklist after AI generates SQL
- **Bridge to next sessions**: Connecting to relational databases (S13a), SQL queries (S13b)

## Key takaways (What are the resulting takeways/skills teached)
- **Good databases begin with conceptual modeling** — never jump directly to SQL
- **ER diagrams are the specification** — tables, foreign keys, and constraints are just implementations
- **AI may generate DDL, but the designer must own the conceptual layer** — verification is mandatory
- **Cardinality determines SQL constraints** — `1→1` becomes `NOT NULL` FK, `1→0..*` allows multiple child rows
- **Normalization prevents redundancy** — 1NF–3NF is sufficient everyday mental framework
- **Structured AI prompts improve output quality** — include entities, relationships with cardinalities, and explicit constraints
- **Systematic verification checklist** after AI generation: every entity → table, every relationship → FK, cardinalities → NULL/NOT NULL, no silent additions or omissions

## Code Examples (What code examples are shown)
- **1NF violation** (`Station` with `JSON` column): Demonstrates why nested/complex values in a single cell break first normal form
- **1NF fix** (`Sensor` as separate table with `station_id` FK): Shows correct atomic decomposition into a dedicated table
- **3NF violation** (`Measurement` with `sensor_typ` and `station_name`): Illustrates transitive redundancy where lookup data is repeated in every measurement row
- **3NF fix** (normalized `Station`, `Sensor`, `Measurement` tables with FKs): Shows how to eliminate transitive redundancy via proper foreign-key joins
- **Textual ER model** (6-line ASCII diagram): Compact specification of entities, attributes, PKs, and relationships — ready as an AI prompt
- **AI prompt template** for `CREATE TABLE` generation: Structured prompt with entities, relationships, and constraints

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/12c_Datenbanken_Entwurf/mj_title_band.jpg` — Book cover / section opener image (Midjourney-generated)
- `images/12c_Datenbanken_Entwurf/mj_datenbank0.png` — Title slide decorative image (Midjourney: "Data Bank")
- `images/partB_3.svg` — **Ablauf** (workflow) diagram showing the lecture's place within Part B of the course

## Plots
- None

## Examples (What examples are used)
- **Umweltmonitoring (Environmental monitoring)** — The running case study: field measurement stations with sensors and time-series measurements. This mirrors real-world environmental and civil engineering data systems
- **AI as junior SQL writer** — Positioning AI as a code generator that must be supervised, analogous to a junior developer who writes SQL but doesn't understand the data model
- **Analogy to `03c_Softwareentwurf`** — Just as UML class diagrams precede code, ER diagrams precede SQL tables
- **Quiz questions** — Five multiple-choice questions covering the rationale for pre-SQL modeling, ER content, monitoring relationships, prompt structure, and AI verification

## Remarks
- The lecture intentionally contains **no plotly plots** — it is a conceptual/design lecture focused on modeling methodology
- All code examples are minimal **SQL CREATE TABLE** snippets used purely as pedagogical contrast (wrong vs. right)
- The course uses **UML-style notation** for ER diagrams (`<<Entity>>`, `PK`) rather than traditional Chen or Crow's Foot notation — this bridges students' prior knowledge from the software design lecture
- The **agentic workflow** is a recurring motif: design first, prompt second, verify third — this pattern extends beyond this lecture into later SQL and AI-assisted development sessions
- Cross-references are explicit: `03c_Softwareentwurf` (S03), `13a_RelationaleDatenbanken` (S13a), `13b_Datenbanken_SQL_Select` (S13b)
- The lecture includes an embedded `%%quizdown` quiz at the end for formative assessment
- Language: The lecture is in German; this summary is in English with German terms preserved in parentheses on first reference
# Summary: 13a Relationale Datenbanken

This lecture introduces the relational database model as the concrete, technical implementation of the Entity–Relationship (ER) design covered in the preceding lecture S12. It bridges conceptual data modeling with actual database schemas, showing how entities become tables, attributes become columns, and relationships become foreign-key constraints. The lecture emphasizes that a relational table is not just a spreadsheet-like data container but the engineered realization of a planned *Fachmodell* (subject model), and it stresses the importance of integrity constraints (primary keys, foreign keys, `NOT NULL`, `UNIQUE`, `CHECK`) for ensuring both local table integrity and global database consistency. A strong thread throughout is the **agentic workflow**: when AI generates SQL, the student must systematically verify that the output faithfully implements the ER design, since AI commonly produces syntactically valid but semantically incomplete schemas.

## Main topics (What is the structure of the lecture)
- **Introduction & flow**: Positioning of relational databases within Part B of the course (see `partB_2.svg` workflow diagram)
- **From ER model to tables**: Mapping entities (e.g. *Gemeinde*, *Bauwerk*) and their attributes to concrete table schemas (`gemeinden`, `bauwerke`)
- **Relationships become foreign keys**: Translating ER relationships and cardinalities into `FOREIGN KEY` constraints and integrity rules
- **Key concepts & terminology**: *Relation*, *Tupel*, *Relationenschema*, *Primärschlüssel*, *Fremdschlüssel*, and key types (UID, GUID, UUID)
- **Integrity conditions & data quality**: Primary keys for *local integrity* (within a table), foreign keys for *global integrity* (across the database)
- **AI-generated SQL pitfalls**: Typical gaps in AI-created `CREATE TABLE` statements (missing `NOT NULL`, `UNIQUE`, `CHECK`, proper `FOREIGN KEY`)
- **Verification workflow**: A four-step checklist for validating AI-generated DDL against the original ER model
- **Quizzes & lessons learned**: Knowledge-check questions and a brief time-management / procrastination analogy
- **Real-world reference**: OpenData Hanse-Stadt Rostock as an example of a multi-table open-data portal

## Key takeways (What are the resulting takeways/skills teached)
- Every relational **table** implements one **entity** or **relationship** from the ER model — verify this mapping before proceeding to SQL queries
- **Primary keys** guarantee local table integrity (uniqueness, no duplicates); **foreign keys** guarantee global database integrity (referential consistency)
- Relationships with cardinality (e.g. "many Bauwerke belong to one Gemeinde") are realized by adding a foreign-key column on the "many" side
- AI-generated SQL is often syntactically correct but frequently missing constraints like `NOT NULL`, `UNIQUE`, `CHECK`, or proper `FOREIGN KEY` definitions — always verify
- Systematic verification checklist: (1) entities → tables, (2) attributes → columns with types, (3) relationships → foreign keys, (4) cardinalities → `NOT NULL`/`UNIQUE`
- Use stable identifier columns (not row numbers) as keys because rows can be deleted
- **UUID / GUID** are standards for globally unique identifiers

## Code Examples (What code examples are shown)
- **QuizDown multiple-choice questions**: Eight questions and one ordering question testing understanding of tables, keys, `NOT NULL`, `UNIQUE`, foreign keys, AI SQL gaps, and cardinality constraints (no standalone code blocks — quiz answers only)
- Inline SQL keywords referenced throughout: `CREATE TABLE`, `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`, `SELECT` (used in S13b follow-up)

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/partB_2.svg` — Course-part roadmap SVG showing Part B topics: *Fehler und Debugging*, *Objektorientierung u. Softwareentwurf*, *Funktionen und Rekursion*, *Datenbankentwurf*, *Trends und KI*, and *Datenerhaltung* (highlighted section)
- `images/13a_RelationaleDatenbanken/mj_title_band.jpg` — Title-band decorative image (Midjourney: "Tabular Relief", ref. Ben Nicholson)
- `images/13a_RelationaleDatenbanken/mj_databank2.png` — Decorative image (Midjourney: "Relational Database")
- `images/13a_RelationaleDatenbanken/mj_title.mp4` — Video background for the title slide
- `images/13a_RelationaleDatenbanken/procrastbrain.png` — Meme-style image illustrating procrastination (Lesson Learned)
- `images/13a_RelationaleDatenbanken/timing0.svg` — Bar chart (static): *Aufwand* vs. *zur erledigende Zeit* — procrastination timing diagram showing task effort exceeding available time
- `images/13a_RelationaleDatenbanken/timing1.svg` — Gantt-style chart (static): *Multitasking (Timeboxing)* showing available time slices vs. task blocks with color-coded segments

## Plots
- `timing0.svg` — Static bar chart illustrating procrastination risk when task effort exceeds available time
- `timing1.svg` — Static Gantt-style chart illustrating **multitasking / Timeboxing** as a time-management strategy

## Examples (What examples are used)
- **Gemeinde / Bauwerk domain**: German municipalities (*Dummerstorf*, *Graal-Müritz*, *Sanitz*) and construction types (*Tankstelle*, *Hotel*, *Kirche*) as running example for ER-to-table mapping
- **OpenData Hanse-Stadt Rostock**: Real-world multi-table open-data portal (Bebauungspläne, Gemeinden, Baustellen, Bodenrichtwerte, Adressenliste) illustrating how real engineering data is distributed across tables
- **Procrastination / procrastbrain meme**: Humor-based lesson connecting time management to the lecture's broader course themes
- **Quiz scenarios**: Concrete questions like "Which key identifies a row?" and "How does `bauwerke.gemeinde_id` reference `gemeinden.gemeinde_id`?"

## Remarks
- Language: The lecture is primarily in **German** with English technical terms (e.g. "relation", "tuple", "primary key", "foreign key") used throughout. German terms are kept in parentheses on first reference per style guidelines.
- This lecture is **13a** (conceptual/introductory); the follow-up **13b** (*Datenbanken_SQL_Select*) and **13c** (*Datenbanken_SQL_Create*) handle SQL query and DDL creation in depth.
- The lecture contains **no standalone code fences** — it is concept-heavy with inline SQL keywords, relying on table diagrams and quizzes for practice.
- Cross-references: S12 (ER-Modell) is the foundational prior lecture; S13b/S13c are the SQL follow-ups.
- The *agentic workflow* sidebar notes (appearing repeatedly) form a recurring meta-theme: always verify AI-generated database schemas against the ER design.
- The `%%book` block contains the core definitions (`%%def Relationale Datenbank`) and the quiz; `%%slides` blocks carry the conceptual exposition.
- The `%%final` marker at the end signals the end of the lecture file.
# Summary: SQL SELECT

This lecture (S13) builds on the database schema design from the previous session (S12) and shifts the focus to querying that schema with SQL. The core thesis is that SQL is a tool, not a learning end in itself — the real skill is translating requirements into queries and then systematically verifying whether the results are correct. The lecture introduces the agentive workflow of AI-assisted SQL: the AI generates the query (`generate`), and the student verifies the output (`verify`).

The lecture covers the fundamental pattern of `SELECT` with `WHERE` and `JOIN`, demonstrates how to load CSV data into SQLite via `pandas`, and walks through the full cycle of prompt engineering for SQL, AI-generated query verification using small known test datasets, and lightweight aggregations. It explicitly connects the verification approach to unit testing principles introduced earlier in the course (S08), reinforcing a test-driven mindset.

## Main topics (What is the structure of the lecture)
- **S12 → S13 transition**: Moving from schema design to querying, focusing on `SELECT`, `WHERE`, and `JOIN` as core tools
- **Loading data into SQLite**: Using `pandas` to write CSV DataFrames directly into a local SQLite database
- **The `SELECT` Grundmuster (basic pattern)**: The three-part structure of `SELECT`, `FROM`, and `WHERE`
- **Filtering with `WHERE`**: Comparison operators, logical combinators (`AND`, `OR`, `NOT`), and formulating business questions first
- **`JOIN` to connect tables**: Using primary/foreign keys to link `measurements`, `sensors`, and `stations`; table aliases with `AS` and join conditions with `ON`
- **Prompting for SQL**: Providing schema, desired result, and conditions in prompts to get reliable AI-generated queries
- **Verification (`Verifikation`)**: Building a small known-test-dataset to validate AI-generated SQL, analogous to unit tests in S08
- **Lightweight aggregations**: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` with `GROUP BY`
- **Sorting and limiting**: `ORDER BY` and `LIMIT` as reference knowledge

## Key takeways (What are the resulting takeways/skills teached)
- Formulate the business/fachliche question first, then translate it into SQL syntax
- Use small, hand-crafted test datasets with known expected outputs to verify AI-generated queries before running on real data
- When AI produces a `JOIN`, verify the key pairs in `ON`, estimate expected row counts, and watch for duplicate rows
- Always provide the database schema in SQL prompts so the AI doesn't guess
- Don't trust SQL by reading it — verify by executing (`Merksatz: Don't trust SQL by reading it`)
- The agentive workflow: AI handles query generation, the student handles result verification
- Aggregation functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) are sufficient for many engineering questions

## Code Examples (What code examples are shown)
- **Loading CSV into SQLite** (`Python`): Using `sqlite3.connect` and `to_sql()` to write `stations`, `sensors`, and `measurements` DataFrames into a local `.sqlite` file
- **Basic SELECT projection** (`SQL`): Selecting specific columns (`station_id`, `measured_at`, `pm25`) from `measurements` — used as a debugging starting point
- **WHERE filtering** (`SQL`): Filtering measurements where `pm25 > 50` — demonstrates conditions and the principle of stating the business question first
- **Multi-table JOIN** (`SQL`): Joining `measurements`, `sensors`, and `stations` with aliases (`AS m`, `AS se`, `AS st`) and explicit `ON` conditions
- **Good SQL prompt** (`text`): A full prompt template including schema definition, desired output columns, filter conditions (PM2.5 > 50, last 30 days), and sort order
- **AI-generated SQL query** (`SQL`): The full query combining `SELECT`, `JOIN`, `WHERE`, `datetime('now', '-30 days')`, and `ORDER BY`
- **Verification in Python** (`Python`): Using `pd.read_sql(sql, con)` to execute the AI query against test data and comparing with an `expected` DataFrame constructed manually
- **Aggregation example** (`SQL`): `AVG(pm25)` and `MAX(pm25)` grouped by `station_id` — demonstrates `GROUP BY`
- **Sort and limit example** (`SQL`): `ORDER BY pm25 DESC` with `LIMIT 5` — reference knowledge for ranking queries

## Visualizations (What visualizations plotly/svg/etc. are used)
- `images/13b_Datenbanken_SQL_Select/mj_title_band.jpg` — Cover image for the lecture book section (Midjourney-generated "Deep Dive in a Wimmelbild")
- `images/13b_Datenbanken_SQL_Select/baustellen.png` — Image of "Open Data Baustellen" (construction sites) used as a concrete example for tabular data queries
- `images/13b_Datenbanken_SQL_Select/mj_title.mp4` — Title slide background video (Midjourney-generated)

## Plots
- None

## Examples (What examples are used)
- **PM2.5 air quality measurements**: The running example uses environmental sensor data (PM2.5 particulate matter) from weather stations, with filters for critical thresholds (PM2.5 > 50 µg/m³)
- **AI as query generator**: The lecture frames the AI tool as a junior developer who writes SQL — the student's job is to review and verify ("Agentischer Workflow")
- **Mini-dataset with 4 measurements**: A hand-crafted test case with 2 stations, 2 sensors, and 4 measurement rows to manually verify expected query output
- **Quiz question**: "You ask an AI tool: 'Which measurement values are critical?' How do you know the generated SQL query is really correct?"
- **Cross-reference to S08**: The verification approach is explicitly connected to unit testing principles (known input → expected output) from an earlier lecture

## Remarks
- This is session S13 in the course sequence (following S12 on schema design); it is part of a broader database topic (S13b).
- The lecture intentionally avoids deep SQL syntax — only `SELECT`, `WHERE`, `JOIN`, and basic aggregation are covered in depth. Complex constructs like subqueries or window functions are noted as out of scope.
- Language: The lecture is in German, with key takeaways and the `Merksatz` presented in English ("Don't trust SQL by reading it").
- The course uses a custom Quarto style (`ai4sc-style`) with AI/ML focus ("Kompetenz von KI & für KI").
- No plotly plots or animated visualizations are present in this lecture.
- The lecture provides reference materials only for `ORDER BY` and `LIMIT`, suggesting these will be revisited later.
# Summary: SQL-DDL aus dem ER-Modell ableiten

This lecture teaches students how to **verify** SQL Data Definition Language (DDL) generated by AI tools against a previously designed Entity–Relationship (ER) model. Rather than teaching students to memorize `CREATE TABLE` syntax, it focuses on the critical skill of reading an ER diagram as a formal specification and checking whether an AI-produced schema faithfully implements it. The approach mirrors the checklist-driven code review mindset introduced in lecture `08b_CodeReview`.

The lecture covers the full workflow from ER model to DDL: understanding DDL building blocks (primary keys, foreign keys, constraints), extracting tables from entities, inserting data, and recognizing when a relational database is even the right tool. It also touches on alternative database paradigms — graph databases for networked data and document databases for flexible, nested structures — reinforcing the engineering principle of matching the data model to the problem domain.

## Main topics (What is the structure of the lecture)
- **DDL fundamentals**: What `CREATE TABLE` defines — columns, types, keys, and constraints
- **Minimal `CREATE TABLE` syntax and SQLite data types**: The structural template and when AI-proposed types are plausible
- **KI-generierte DDL verifizieren**: Two-part checklist for auditing AI-generated table definitions against the ER model
- **Agentischer Workflow (ER → SQL → Review)**: Step-by-step process for reading ER diagrams first, then verifying AI output
- **Data insertion with `INSERT`**: Populating tables and using constraint violations as diagnostics
- **Derived tables via `CREATE TABLE ... AS SELECT`**: Quick copies and the loss of constraints
- **When SQL is not the right fit**: Graph databases for networks, document databases for flexible/nested data
- **Schema evolution references**: `ALTER TABLE` and `DROP TABLE` introduced only as concepts

## Key takeways (What are the resulting takeways/skills teached)
- The **ER model is the specification**; the DDL is the implementation — never trust AI output without checking against the source model
- **Missing constraints are real data-quality risks**: a table that works technically but lacks `NOT NULL`, `UNIQUE`, or `FOREIGN KEY` rules silently degrades data integrity
- A constraint that does not appear in DDL is never enforced by the database
- Use the same checklist mindset from code review (`08b_CodeReview`): read the specification first, compare the artifact, flag missing conditions, then iteratively prompt the AI
- **SQL is strong for relational data but not universal** — understand the information model before choosing a database type (graph or document databases may be better fits)
- `INSERT` failures and unexpected acceptances are diagnostic signals that point to missing or misdefined constraints

## Code Examples (What code examples are shown)
- **Minimal `CREATE TABLE` template**: Generic skeleton showing column definitions and table-level constraints
- **Geometry example — `Points` and `Lines` tables**: AI-generated DDL with `AUTOINCREMENT` primary keys, `REAL` coordinate columns, `NOT NULL` constraints, and bidirectional `FOREIGN KEY` references on `Lines` → demonstrates entity-to-table mapping and relationship-as-foreign-key conversion
- **`INSERT` statements for `Points` and `Lines`**: Concrete data insertion into the geometry schema with coordinate values and foreign key references
- **`CREATE TABLE ... AS SELECT` pattern**: Copying `Points` into `PointsCopy` → demonstrates quick materialization and warns that constraints are not automatically carried over
- **`ALTER TABLE` and `DROP TABLE` reference**: Renaming a table (`Punkte`) and dropping with `IF EXISTS` → introduced only for recognition, not mastery

## Visualizations (What visualizations plotly/svg/etc. are used)
- `mj_title_band.jpg` — Cover/thumbnail image for the book-style section
- `mj_babel2.png` — "Construction plan of the Tower of Babel" metaphor for the Hörsaalfrage: questioning whether AI-generated SQL truly reflects the intended ER design
- `mj_title.mp4` — Video background on the title slide

## Plots
- None

## Examples (What examples are used)
- **Geometry schema (Points + Lines)**: A concrete spatial example where a `Lines` table references `Points` twice (start and end), illustrating self-referencing foreign keys and the `FOREIGN KEY` mapping of relationships
- **Tower of Babel metaphor**: AI-generated SQL is compared to a Babel construction plan — impressive at first glance, but correctness must be verified against the original architectural intent (the ER diagram)
- **Graph databases for street/utility networks**: Nodes and edges, shortest paths, reachability — relational tables are a poor fit compared to graph databases
- **Document databases for BIM elements**: Nested, optional properties and frequently changing schemas align better with JSON-like document stores than rigid relational tables
- **Code review checklist mindset**: Cross-references `08b_CodeReview` to reinforce the pattern of "specification → artifact → gap analysis"

## Remarks
- The lecture is taught in **German** with English summary; original German terms (e.g. *Pflichtattribute*, *Kardinalitäten*, *Merksatz*) appear in parentheses on first reference.
- The opening book quote by **David McGoveran** ("The problem with SQL is that it pretends to implement the relational model, but doesn't") sets a critical, reflective tone.
- This is lecture **13c**, following `12c_Datenbanken_Entwurf` (ER modeling) and building on `08b_CodeReview` (checklist-driven verification). It is intentionally light on syntax memorization and strong on **critical evaluation** of AI output.
- No plots or interactive visualizations are used; the lecture relies on SQL code blocks, checklists, and conceptual comparisons.
- `ALTER TABLE` and `DROP TABLE` are explicitly scoped as "reference only" — students need to know the terms but not master them in this session.
