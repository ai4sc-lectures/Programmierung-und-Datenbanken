// Some definitions presupposed by pandoc's typst output.
#let blockquote(body) = [
  #set text( size: 0.92em )
  #block(inset: (left: 1.5em, top: 0.2em, bottom: 0.2em))[#body]
]

#let horizontalrule = line(start: (25%,0%), end: (75%,0%))

#let endnote(num, contents) = [
  #stack(dir: ltr, spacing: 3pt, super[#num], contents)
]

#show terms: it => {
  it.children
    .map(child => [
      #strong[#child.term]
      #block(inset: (left: 1.5em, top: -0.4em))[#child.description]
      ])
    .join()
}

// Some quarto-specific definitions.

#show raw.where(block: true): set block(
    fill: luma(230),
    width: 100%,
    inset: 8pt,
    radius: 2pt
  )

#let block_with_new_content(old_block, new_content) = {
  let d = (:)
  let fields = old_block.fields()
  fields.remove("body")
  if fields.at("below", default: none) != none {
    // TODO: this is a hack because below is a "synthesized element"
    // according to the experts in the typst discord...
    fields.below = fields.below.abs
  }
  return block.with(..fields)(new_content)
}

#let empty(v) = {
  if type(v) == str {
    // two dollar signs here because we're technically inside
    // a Pandoc template :grimace:
    v.matches(regex("^\\s*$")).at(0, default: none) != none
  } else if type(v) == content {
    if v.at("text", default: none) != none {
      return empty(v.text)
    }
    for child in v.at("children", default: ()) {
      if not empty(child) {
        return false
      }
    }
    return true
  }

}

// Subfloats
// This is a technique that we adapted from https://github.com/tingerrr/subpar/
#let quartosubfloatcounter = counter("quartosubfloatcounter")

#let quarto_super(
  kind: str,
  caption: none,
  label: none,
  supplement: str,
  position: none,
  subrefnumbering: "1a",
  subcapnumbering: "(a)",
  body,
) = {
  context {
    let figcounter = counter(figure.where(kind: kind))
    let n-super = figcounter.get().first() + 1
    set figure.caption(position: position)
    [#figure(
      kind: kind,
      supplement: supplement,
      caption: caption,
      {
        show figure.where(kind: kind): set figure(numbering: _ => numbering(subrefnumbering, n-super, quartosubfloatcounter.get().first() + 1))
        show figure.where(kind: kind): set figure.caption(position: position)

        show figure: it => {
          let num = numbering(subcapnumbering, n-super, quartosubfloatcounter.get().first() + 1)
          show figure.caption: it => {
            num.slice(2) // I don't understand why the numbering contains output that it really shouldn't, but this fixes it shrug?
            [ ]
            it.body
          }

          quartosubfloatcounter.step()
          it
          counter(figure.where(kind: it.kind)).update(n => n - 1)
        }

        quartosubfloatcounter.update(0)
        body
      }
    )#label]
  }
}

// callout rendering
// this is a figure show rule because callouts are crossreferenceable
#show figure: it => {
  if type(it.kind) != str {
    return it
  }
  let kind_match = it.kind.matches(regex("^quarto-callout-(.*)")).at(0, default: none)
  if kind_match == none {
    return it
  }
  let kind = kind_match.captures.at(0, default: "other")
  kind = upper(kind.first()) + kind.slice(1)
  // now we pull apart the callout and reassemble it with the crossref name and counter

  // when we cleanup pandoc's emitted code to avoid spaces this will have to change
  let old_callout = it.body.children.at(1).body.children.at(1)
  let old_title_block = old_callout.body.children.at(0)
  let old_title = old_title_block.body.body.children.at(2)

  // TODO use custom separator if available
  let new_title = if empty(old_title) {
    [#kind #it.counter.display()]
  } else {
    [#kind #it.counter.display(): #old_title]
  }

  let new_title_block = block_with_new_content(
    old_title_block, 
    block_with_new_content(
      old_title_block.body, 
      old_title_block.body.body.children.at(0) +
      old_title_block.body.body.children.at(1) +
      new_title))

  block_with_new_content(old_callout,
    block(below: 0pt, new_title_block) +
    old_callout.body.children.at(1))
}

// 2023-10-09: #fa-icon("fa-info") is not working, so we'll eval "#fa-info()" instead
#let callout(body: [], title: "Callout", background_color: rgb("#dddddd"), icon: none, icon_color: black, body_background_color: white) = {
  block(
    breakable: false, 
    fill: background_color, 
    stroke: (paint: icon_color, thickness: 0.5pt, cap: "round"), 
    width: 100%, 
    radius: 2pt,
    block(
      inset: 1pt,
      width: 100%, 
      below: 0pt, 
      block(
        fill: background_color, 
        width: 100%, 
        inset: 8pt)[#text(icon_color, weight: 900)[#icon] #title]) +
      if(body != []){
        block(
          inset: 1pt, 
          width: 100%, 
          block(fill: body_background_color, width: 100%, inset: 8pt, body))
      }
    )
}



#let article(
  title: none,
  subtitle: none,
  authors: none,
  date: none,
  abstract: none,
  abstract-title: none,
  cols: 1,
  lang: "en",
  region: "US",
  font: "libertinus serif",
  fontsize: 11pt,
  title-size: 1.5em,
  subtitle-size: 1.25em,
  heading-family: "libertinus serif",
  heading-weight: "bold",
  heading-style: "normal",
  heading-color: black,
  heading-line-height: 0.65em,
  sectionnumbering: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  toc_indent: 1.5em,
  doc,
) = {
  set par(justify: true)
  set text(lang: lang,
           region: region,
           font: font,
           size: fontsize)
  set heading(numbering: sectionnumbering)
  if title != none {
    align(center)[#block(inset: 2em)[
      #set par(leading: heading-line-height)
      #if (heading-family != none or heading-weight != "bold" or heading-style != "normal"
           or heading-color != black) {
        set text(font: heading-family, weight: heading-weight, style: heading-style, fill: heading-color)
        text(size: title-size)[#title]
        if subtitle != none {
          parbreak()
          text(size: subtitle-size)[#subtitle]
        }
      } else {
        text(weight: "bold", size: title-size)[#title]
        if subtitle != none {
          parbreak()
          text(weight: "bold", size: subtitle-size)[#subtitle]
        }
      }
    ]]
  }

  if authors != none {
    let count = authors.len()
    let ncols = calc.min(count, 3)
    grid(
      columns: (1fr,) * ncols,
      row-gutter: 1.5em,
      ..authors.map(author =>
          align(center)[
            #author.name \
            #author.affiliation \
            #author.email
          ]
      )
    )
  }

  if date != none {
    align(center)[#block(inset: 1em)[
      #date
    ]]
  }

  if abstract != none {
    block(inset: 2em)[
    #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
    ]
  }

  if toc {
    let title = if toc_title == none {
      auto
    } else {
      toc_title
    }
    block(above: 0em, below: 2em)[
    #outline(
      title: toc_title,
      depth: toc_depth,
      indent: toc_indent
    );
    ]
  }

  if cols == 1 {
    doc
  } else {
    columns(cols, doc)
  }
}

#set table(
  inset: 6pt,
  stroke: none
)

#set page(
  paper: "us-letter",
  margin: (x: 1.25in, y: 1.25in),
  numbering: "1",
)

#show: doc => article(
  title: [ueberblick],
  toc_title: [Table of contents],
  toc_depth: 3,
  cols: 1,
  doc,
)

= Überblick
<überblick>
#box(image("images/01a_Ueberblick/mj_title_band.jpg"))

#quote(block: true)[
I never wrote things down to remember; I always wrote things down so I could forget.

--- Matthew McConaughey
]

== 🔄 Agentischer Arbeitsablauf
<agentischer-arbeitsablauf>
#block[
#block[
#block[
#strong[Prompt]

Aufgabe formulieren

]
]
#block[
→

]
#block[
#block[
#strong[Generieren]

KI erstellt Code

]
]
#block[
→

]
#block[
#block[
#strong[Verstehen]

Code lesen & analysieren

]
]
#block[
→

]
#block[
#block[
#strong[Verifizieren]

Anforderung prüfen

]
]
#block[
→

]
#block[
#block[
#strong[Iterieren]

Verbessern & anpassen

]
]
]
In diesem Kurs üben Sie jeden Schritt dieses Zyklus: Sie formulieren klare Aufgaben für KI-Tools, lesen und verstehen den generierten Code, prüfen ob er die ingenieurtechnische Anforderung erfüllt, und iterieren bis das Ergebnis korrekt ist.

== Vorstellung
<vorstellung>
#block[
#block[
#box(image("images/01a_Ueberblick/Ploennigs.jpg"))

]
#block[
Prof.~Dr.-Ing. habil. Jörn Plönnigs

KI für Digitales Bauen

Büro: Justus-von-Liebig-Weg 2, Raum 114

Email: Joern.Ploennigs\@uni-rostock.de

Telefon: 0381 498-3500

]
]
== Zielsetzung
<zielsetzung>
#block[
#block[
- Verständnis und Kenntnisse der Grundlagen der Programmierung und Datenbanken aneignen
- Aneignen praktischer Fähigkeiten, um ingenieurtechnische Probleme mit Software zu lösen
- Kennenlernen aktueller Ansätze und Technologien in Softwareentwicklung

]
#block[
#box(image("images/01a_Ueberblick/mj_target.png"))

]
]
== Lernziele: KI-gestütztes Programmieren
<lernziele-ki-gestütztes-programmieren>
#block[
#block[
#strong[Was Sie lernen:]

- KI-generierten Python-Code #strong[lesen und verstehen]
- Code für die ingenieurtechnische Anforderung #strong[modifizieren]
- Korrektheit und Qualität #strong[verifizieren]

]
#block[
#strong[Warum dieser Ansatz:]

- KI-Tools sind Standard in der Ingenieurpraxis
- Ingenieure müssen KI-Output beurteilen, nicht nur nutzen
- Verständnis von Code ist wichtiger denn je

]
]
Die Lernziele dieses Kurses verschieben sich vom klassischen "Code von Grund auf schreiben" hin zu "KI-generierten Code lesen, für die Anforderung modifizieren und auf Korrektheit prüfen." Dieses Kompetenzprofil entspricht dem, was in der modernen Ingenieurpraxis gefordert wird.

== Der Ingenieur als Architekt und Verifizierer
<der-ingenieur-als-architekt-und-verifizierer>
#block[
#block[
KI generiert Code --- der #strong[Ingenieur] ist:

- Auftraggeber und Architekt
- Leser und Versteher
- Prüfer und Verifizierer

Nicht: blindes Ausführen von KI-Output

]
#block[
#box(image("images/01a_Ueberblick/mj_target.png"))

]
]
Die Rolle des Ingenieurs verändert sich grundlegend: Statt Code von einer leeren Seite zu schreiben, lesen, bewerten und passen Ingenieure zunehmend KI-generierten Code an. Lesen, Modifizieren und Verifizieren sind deshalb die Kernkompetenzen dieses Kurses.

== Symbollegende {{< ai4sc-icon braces >}} {{< ai4sc-icon workflow >}}
<symbollegende>
Diese Symbole erscheinen im Kurs und zeigen, #strong[was für ein Konzept] gerade behandelt wird:

#block[
#block[
#table(
  columns: (47.06%, 52.94%),
  align: (auto,auto,),
  table.header([Symbol], [Konzept],),
  table.hline(),
  [{{< ai4sc-icon variable >}}], [Variable / Wert],
  [{{< ai4sc-icon braces >}}], [Datentyp],
  [{{< ai4sc-icon box >}}], [Objekt / Entität],
  [{{< ai4sc-icon arrow-left-right >}}], [Beziehung],
  [{{< ai4sc-icon square-function >}}], [Funktion],
)
]
#block[
#table(
  columns: (47.06%, 52.94%),
  align: (auto,auto,),
  table.header([Symbol], [Konzept],),
  table.hline(),
  [{{< ai4sc-icon workflow >}}], [Algorithmus / Zyklus],
  [{{< ai4sc-icon clipboard-list >}}], [Anforderung],
  [{{< ai4sc-icon test-tube >}}], [Test / Verifikation],
  [{{< ai4sc-icon list-tree >}}], [Datenstruktur],
  [{{< ai4sc-icon database >}}], [Datenbank],
)
]
]
Die Symbollegende gilt für den gesamten Kurs. Wenn ein Symbol an einer Folie erscheint, zeigt es an, welche Art von Konzept gerade eingeführt oder angewendet wird. So können Sie den Lernstoff strukturiert einordnen.

== Themen ≡
<themen>
#box(image("images/01a_Ueberblick/ablauf.svg"))

Die Kursthemen umfassen Python-Grundlagen (Datentypen ≡, Operatoren, Funktionen, Algorithmen) sowie Datenbankkonzepte. Jedes Thema wird im agentischen Zyklus 🔄 erarbeitet.

== Ablauf
<ablauf>
#box(image("images/01a_Ueberblick/ablauf2.svg"))

== Übungen
<übungen>
#box(image("images/01a_Ueberblick/ablauf3.svg"))

== Vorlesungsfolien
<vorlesungsfolien>
#block[
#block[
#box(image("images/01a_Ueberblick/image_4.png"))

]
#block[
#figure([
#box(image("images/01a_Ueberblick/image_2.png"))
], caption: figure.caption(
position: bottom, 
[
https:\/\/studip.uni-rostock.de
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
]
== Vorlesungsdokumentation
<vorlesungsdokumentation>
#block[
#block[
#box(image("images/01a_Ueberblick/webpage.png"))

]
#block[
#figure([
#box(image("images/01a_Ueberblick/image_5.png"))
], caption: figure.caption(
position: bottom, 
[
https:\/\/ai4sc-lectures.github.io/
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
]
== Übungen
<übungen-1>
#block[
#block[
#box(image("images/01a_Ueberblick/python-in-notebook.png"))

]
#block[
Ab nächster Woche

- Konsultation (PC-Pool 1) Mittwoch 11:15 - 12:45 Uhr

- Digitale Übung:

  - Online Umgebung
  - Übungsvideos

]
]
#block[
#block[
= Übung
<übung>
]
#block[
#figure([
#box(image("images/01a_Ueberblick/mj_train.png"))
], caption: figure.caption(
position: bottom, 
[
Midjourney: Repeat
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
]
== Vorstellung
<vorstellung-1>
#block[
#block[
#box(image("images/01a_Ueberblick/Markus_Berger.jpg"))

]
#block[
Dr.-Ing. Markus Berger

KI für Digitales Bauen

Büro: Justus-von-Liebig-Weg 2, Raum 107

Email: Markus.Berger\@uni-rostock.de

Telefon: 0381 498-3503

]
]
== Zielsetzung
<zielsetzung-1>
#block[
#block[
In der Vorlesung gelernte Programmierkonzepte

- wiederholt praktisch anwenden
- auf andere Probleme beziehen

]
#block[
#figure([
#box(image("images/01a_Ueberblick/mj_student.png"))
], caption: figure.caption(
position: bottom, 
[
Midjourney: Student aiming for a goal
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
]
== Zielsetzung 2
<zielsetzung-2>
Warum Programmieren lernen als Ingenieur?

- Verständnis der Grundelemente des Programmierens

- Kenntnis der üblichen Schritte in einem Softwareprojekt

- Erfahrung mit dem Suchen nach Lösungen

- Strategien Erlernen wie Probleme behandelt werden können

- Im späteren Verlauf: Die Systematik hinter Software verstehen.

- Grundlagen aneignen - von denen aus weitergearbeitet werden kann!

== Ablauf - Zwei Teile
<ablauf---zwei-teile>
#block[
#block[
#emph[Übungsvideo]

- Ansehen
- Selbst mitprogrammieren um die Ansätze zu Erlernen

]
#block[
#emph[Aufgabe]

- Eigene Lösungen überlegen oder recherchieren

]
]
- Beide Teile müssen abgegeben werden!
- Gruppenarbeit ist nicht vorgesehen!

== Konsultation
<konsultation>
#block[
#block[
Fragen an: Markus Berger

Ab nächster Woche

- Mittwoch 11:15--12:45 Uhr in PC-Pool 1 und 2
- Klären von Fragen zu den Videos und den Aufgaben

]
#block[
Markus.Berger\@uni-rostock.de

]
]
== Abgabe
<abgabe>
#block[
#block[
Übungsvideos:

- Veröffentlichung immer Montags
- Konsultation immer Mittwochs
- Abgabe immer Montags

]
#block[
#figure([
#box(image("images/01a_Ueberblick/mj_student2.png"))
], caption: figure.caption(
position: bottom, 
[
Midjourney: Student with a deadline
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
]
== Prüfungszulassung
<prüfungszulassung>
#block[
#block[
- Hausaufgaben werden nicht benotet

- Bewertet stattdessen mit Erfüllt / Nicht-Erfüllt der Aufgabe (Pro gesamter Übung, keine Teilleistungen)

- Am Ende des Semesters müssen mindestens 50% der Übungen erfüllt sein

- Umfangreichere Aufgaben bringen dabei mehr Prozente

]
#block[
#table(
  columns: 2,
  align: (auto,auto,),
  table.header([Thema], [Gewichtung],),
  table.hline(),
  [#strong[Grundlagen];], [],
  [Python & Datentypen], [5%],
  [Operatoren, Verzweigungen & Schleifen], [5%],
  [Funktionen & Objekte], [5%],
  [Algorithmen], [5%],
  [#strong[Erweitertes];], [],
  [Fehler & Tests], [15%],
  [Entwurf], [15%],
  [Datenhaltung], [20%],
  [#strong[Erweitertes];], [],
  [Datenbankanfragen], [15%],
  [Datenbankentwurf], [15%],
)
]
]
== Online Python IDE - Jupyter Books
<online-python-ide---jupyter-books>
#box(image("images/01a_Ueberblick/jupyterlab-markdown.png"))

== Anmeldung bei Jupyter & Abgabe
<anmeldung-bei-jupyter-abgabe>
#block[
#block[
- Account erstellen in der #strong[#emph[nächsten Woche];] unter: #link("https://ml-lab.ai4sc-lectures.auf.uni-rostock.de/")

- Mit folgendem Nutzernamen: „vorname\_nachname”

- Einführung dann im ersten Übungsvideo

]
#block[
#box(image("images/01a_Ueberblick/login.png"))

]
]
== KI: Architekt und Verifizierer, nicht Ausführender
<ki-architekt-und-verifizierer-nicht-ausführender>
- KI #strong[generiert] Code --- das ist der neue Standard in der Ingenieurpraxis

- Ihre Aufgabe: den generierten Code #strong[lesen];, #strong[verstehen] und #strong[verifizieren]

- Grundverständnis von Python ist Voraussetzung, um KI-Output beurteilen zu können

- Der agentische Zyklus 🔄 (Prompt → Generieren → Verstehen → Verifizieren → Iterieren) ist Ihre Arbeitsmethode

- Am Ende eine Extra-Vorlesung + Übung zum Einsatz von KI-Werkzeugen

- Achtung: In der Klausur müssen Sie signifikantes Programmierverständnis zeigen --- die Übungen sind deshalb unbedingt selbst zu erfüllen!

= Hausaufgaben
<hausaufgaben>
#block[
#figure([
#box(image("images/01a_Ueberblick/mj_python.mp4"))
], caption: figure.caption(
position: bottom, 
[
Midjourney: Programming in Python
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
== Abrufen von Aufgaben
<abrufen-von-aufgaben>
Hausaufgaben können auf der JupyterLab-Plattform herunterladen, bearbeiten und abgeben werden

- Menüpunkt `Nbgrader/Assignments` → wichtigste Option, zeigt die Seite mit den Aufgaben
- Menüpunkt `Nbgrader/Courses` → listet alle belegten Kurse
- Menüpunkt `Nbgrader/Formgrader` → nur für Lehrende, zum Einsehen und Bewerten der studentischen Abgaben

#figure([
#box(image("images/01a_Ueberblick/nbgrader_menu.png"))
], caption: figure.caption(
position: bottom, 
[
Nbgrader menu
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


- Menüpunkt `Nbgrader/Assignments` → Ansicht der aktuellen Aufgaben öffnet sich
- Mit „fetch” → ausgewählte Aufgabe herunterladen

#figure([
#box(image("images/01a_Ueberblick/nbgrader_menu_assignments.png"))
], caption: figure.caption(
position: bottom, 
[
Nbgrader: Available assignments
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


- Nach dem Herunterladen erscheint die Aufgabe in der Liste „Downloaded Assignments”
- Klick auf den blauen Aufgabennamen → öffnet den Unterordner der Aufgabe
- Im Unterordner: alle Notebooks und zugehörigen Dateien sichtbar

#figure([
#box(image("images/01a_Ueberblick/nbgrader_menu_assignments2.png"))
], caption: figure.caption(
position: bottom, 
[
Nbgrader: Downloaded Assignments
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


== Bearbeiten von Aufgaben
<bearbeiten-von-aufgaben>
- Lesen sie die Aufgabenstellung durch
- Ersetzen Sie `YOUR CODE HERE` mit richtigem Code
- Ersetzen Sie `YOUR ANSWER HERE` mit einer Textantwort
- Löschen sie ggf. `raise NotImplementedError()`.
- Führen sie die Zelle mit `Shift+Enter` aus.
- Achten Sie darauf, dass die Ausführung erfolgreich war.

#figure([
#box(image("images/01a_Ueberblick/nbgrader_notebook2.png"))
], caption: figure.caption(
position: bottom, 
[
Nbgrader menu
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


- Auf jede zu ergänzende Code-Zelle folg eine Test-Zelle.
- Diese können Sie nicht bearbeiten.
- Aber die Ausführung zeigt Ihne ob sie richtig lagen.

#figure([
#box(image("images/01a_Ueberblick/nbgrader_notebook2.png"))
], caption: figure.caption(
position: bottom, 
[
Nbgrader menu
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


== Einreichen von Aufgaben
<einreichen-von-aufgaben>
- Vor Abgabe jedes Notebook validieren
- Schaltfläche im Menü zum Starten der `Validierung` verwenden
  - Erfolgreiche Validierung → Meldung: "Success! Your notebook passes all the tests."
  - Fehlgeschlagene Validierung → Bericht mit den aufgetretenen Fehlern wird angezeigt

#figure([
#box(image("images/01a_Ueberblick/nbgrader_validate.png"))
], caption: figure.caption(
position: bottom, 
[
Nbgrader menu
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


- Nach erfolgreicher Validierung aller Notebooks → Schaltfläche „Submit” betätigen
- Aufgabe wird eingereicht
- Eingereichte Aufgabe erscheint in der Liste „Submitted Assignments”

#figure([
#box(image("images/01a_Ueberblick/nbgrader_menu_assignments2.png"))
], caption: figure.caption(
position: bottom, 
[
Nbgrader menu
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


== Server herunterfahren
<server-herunterfahren>
- JupyterLab-Umgebung ordnungsgemäß beenden, wenn die Arbeit abgeschlossen ist
- Über Menüpunkt `File/Hub Control Panel` in die Serverkontrollansicht wechseln
- Server mit `Stop my Server` beenden

= Motivation
<motivation>
#block[
#figure([
#box(image("images/01a_Ueberblick/mj_motivation.mp4"))
], caption: figure.caption(
position: bottom, 
[
Midjourney: Programming in Python
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
== Entwurf: CAD - Computer Aided Design
<entwurf-cad---computer-aided-design>
#block[
#block[
#figure([
#box(image("images/01a_Ueberblick/use_case_cad.png"))
], caption: figure.caption(
position: bottom, 
[
https:\/\/www.autodesk.com/campaigns/revit-lt
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
#block[
Software-Anwendungen zum Entwerfen, Konstruieren und Präsentieren von Konstruktionszeichnungen und Karten, sowohl für 2D- als auch für 3D-Modelle. (SoftSelect Glossar / Lexikon)

]
]
== Entwurf: Virtuelle Umgebungen
<entwurf-virtuelle-umgebungen>
#block[
#block[
Anwendungen, die es erlauben Entwürfe in VR (Virtual Reality) oder AR (Augmented Reality) zu visualisieren und zu erkunden.

]
#block[
#figure([
#box(image("images/01a_Ueberblick/use_case_render.jpg"))
], caption: figure.caption(
position: bottom, 
[
http:\/\/www.firstinvision.de/aut\_de\_xhtml-4-produkte.php?entryId=cascados-8
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
]
== Entwurf: Tragwerksplanung
<entwurf-tragwerksplanung>
#block[
#block[
#figure([
#box(image("images/01a_Ueberblick/use_case_static.png"))
], caption: figure.caption(
position: bottom, 
[
https:\/\/www.die.de/all-images
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
#block[
Ziel seiner Tragwerksplanung ist es, die erforderliche Tragfähigkeit und Gebrauchstauglichkeit einer Baukonstruktion während der vorgesehenen Lebensdauer mit den Forderungen nach Wirtschaftlichkeit und Ästhetik in Einklang zu bringen. #link("https://dewiki.de/Lexikon/Tragwerksplaner")[DeWiki]

]
]
== Bau: Bauprozessautomatisierung
<bau-bauprozessautomatisierung>
#block[
#block[
Automatisierung verschiedener Schritte

- Bautagebuch
- Bauzeitenmanagement
- Bauprojektmanagement

]
#block[
#figure([
#box(image("images/01a_Ueberblick/use_case_report.png"))
], caption: figure.caption(
position: bottom, 
[
https:\/\/baugorilla.com/produkt/bautagebuch-app
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


]
]
== Bau: Baurobotik
<bau-baurobotik>
#block[
#block[
#box(image("images/01a_Ueberblick/Baubot.mp4"))

]
#block[
Das Einsatzgebiet von Robotern im Bauhauptgewerbe ist grundsätzlich unabhängig vom bauspezifischen Geschäftsmodell bzw. unabhängig vom Segment, der Aktivität und der eigentlichen Arbeitstätigkeiten.

]
]
== Betrieb: GIS - Geoinformationssystem
<betrieb-gis---geoinformationssystem>
#block[
#block[
Geoinformationssysteme sind Informationssysteme zur Erfassung, Bearbeitung, Organisation, Analyse und Präsentation räumlicher Daten. #link("https://dewiki.de/Lexikon/Geoinformationssystem")[DeWiki]

]
#block[
#box(image("images/01a_Ueberblick/use_case_gis.png"))

]
]
== Betrieb: Gebäudeautomation
<betrieb-gebäudeautomation>
#block[
#block[
#box(image("images/01a_Ueberblick/MunchDigitalTwin.mp4"))

]
#block[
Gesamtheit von Überwachungs-, Steuer-, Regel- und Optimierungseinrichtungen in Gebäuden. #link("https://dewiki.de/Lexikon/Gebäudeautomation")[DeWiki]

]
]
== Betrieb: CAFM - Computer Aided Facility Management
<betrieb-cafm---computer-aided-facility-management>
#block[
#block[
Facilitymanagement bezeichnet die Verwaltung und Bewirtschaftung von Gebäuden sowie deren technischen Anlagen und Einrichtungen (englisch facilities). CAFM ist die Unterstützung des Facilitymanagements durch ein Computerprogramm. #link("https://dewiki.de/Lexikon/Facilitymanagement")[DeWiki]

]
#block[
#box(image("images/01a_Ueberblick/DynamicSpacePlanning.mov"))

]
]
== Literaturempfehlungen
<literaturempfehlungen>
- #link("https://find.ub.uni-rostock.de/id%7Bcolon%7D169925365X")[Python 3: das umfassende Handbuch; Ernesti, Johannes, Kaiser, Peter, 2020]

- #link("https://find.ub.uni-rostock.de/id%7Bcolon%7D1632747588")[Datenbanken: Konzepte und Sprachen; Saake, Gunter, Sattler, Kai-Uwe, Heuer, Andreas, 2018]

- Empfehlung: Verschiedene Online-Tutorials nutzen! #link("https://docs.python.org/3/tutorial/") & #link("https://www.w3schools.com/python/")

- Langfristig am wichtigsten: Ins kalte Wasser springen!
