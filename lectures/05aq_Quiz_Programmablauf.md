## Funktionen

```{quizdown}
	---
	shuffleQuestions: true
	shuffleAnswers: true
	---

    ### Was ist der Hauptzweck von Programmablaufplänen?
    - [x] Die Übersetzung eines realen Problems in einzelne Programmschritte
    - [ ] Das Schreiben von effizientem Code
    - [ ] Die Dokumentation fertiger Programme
    - [ ] Die Visualisierung von Datenstrukturen

    ### Welche Form haben Start- und End-Elemente in Flussdiagrammen?
    - [x] Elemente mit runden Ecken
    - [ ] Rechteckige Elemente
    - [ ] Rhomben
    - [ ] Kreise

    ### Welche Form haben Anweisungen (Statements) in Flussdiagrammen?
    - [x] Rechteckige Elemente
    - [ ] Rhomben
    - [ ] Kreise
    - [ ] Elemente mit runden Ecken

    ### Sortiere die folgenden Elemente eines Flussdiagramms nach ihrer typischen Reihenfolge:
    1. `Start (abgerundetes Rechteck)`
    2. `Eingabe (Rhombus)`
    3. `Verarbeitung (Rechteck)`
    4. `Entscheidung (Drachenviereck)`
    5. `Ende (abgerundetes Rechteck)`

    ### Welcher Fehler steckt in diesem Flussdiagramm?
    ```mermaid
    graph TD
        A[Start] --> B{Eingabe}
        B --> C[Verarbeitung]
        C --> D{Entscheidung}
        D --> B
    ```
    - [x] Eingabe wird mit falscher Form (Rhombus statt Parallelogramm) dargestellt
    - [ ] Die Pfeilrichtung ist falsch
    - [ ] Start-Element fehlt
    - [ ] Entscheidungen können nicht zu Eingaben zurückführen

    ### Welche Form wird für if-Anweisungen verwendet?
    - [x] Drachenviereck
    - [ ] Rechteck
    - [ ] Rhombus
    - [ ] Kreis

    ### Was charakterisiert Unterprogramm-Elemente in Flussdiagrammen?
    - [x] Rechteckige Form mit doppelter Linie
    - [ ] Kreisförmige Form
    - [ ] Gestrichelte Linien
    - [ ] Schattierte Rechtecke

```