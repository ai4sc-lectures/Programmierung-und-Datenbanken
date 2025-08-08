---
title: "Einführung in Programmierung und Datenbanken"
subtitle: "Programmablauf"
author: "Joern Ploennigs"
format: 
  revealjs:
    theme: default
    transition: slide
    background-transition: fade
    highlight-style: github
    code-line-numbers: true
    slide-number: true
---

## Programmierung und Datenbanken

::: {style="display: flex; justify-content: space-between; align-items: center;"}
::: {style="flex: 1;"}
**Themenübersicht:**

- Motivation Computer und Architekturen
- Programmierung und Datentypen
- Fehler und Debugging
- Objektorientierung u. Softwareentwurf
- Verzweigungen und Schleifen
- Funktionen und Rekursion
:::

::: {style="flex: 1; text-align: center;"}
**Grundlagen**  
**Modellierung**
:::
:::

---

## Programmablauf

![DALL·E 2 Generated Image](images/dalle_programmablauf.png){fig-align="center"}

---

## Programmkonzeption - Problem Definieren

- Die wichtigste Fähigkeit beim Programmieren ist es, ein Problem der echten Welt in einzelne Programmanweisungen (also Operationen in Zeichen) zu übersetzen.

- **Erster Schritt:** Was sind Eingaben, was sind Ausgaben des aktuellen Problems?

- Nicht unähnlich dazu wie eine Funktion definiert wird!
  - Eingabeparameter
  - Return-Wert

---

## Hörsaalfrage {.smaller}

::: {style="font-size: 2em; text-align: center; color: #2c3e50; padding: 2em;"}
**Welche Ein- und Ausgaben gibt es bei der Volumenberechnung eines Quaders (Haus)?**
:::

---

## Programmkonzeption - Beispiel: Volumenberechnung eines Quaders (Haus)

- **Vereinfachung:** Das Haus ist rechteckig und hat ein Flachdach.

- **Eingaben:** Seitenlängen a und b, Höhe h (in m)

- **Ausgaben:** Volumen in m³

- **Erste Überlegungen:**
  - Welche Datentypen haben diese Ein- und Ausgaben?
  - Welche verschiedenen Situationen gibt es?

---

## Programmkonzeption - Problem in Schritte Aufteilen

- **Die Kernfrage:**  
  *„Wie gelangen wir von der gegebenen Eingabe zu der gewünschten Ausgabe?"*

- **Nicht Einfach:** Um diese Frage für beliebige Probleme beantworten zu können, muss man sich eine Denkweise aneignen, das Problem in Schritte zu zerlegen und abzuarbeiten.

- **Unser Vorteil:** Das Zerlegen und Lösen von Problemen ist eine Grundfähigkeit von Ingenieuren.

---

## Programmablaufpläne - Ein Werkzeug zum Entwerfen von Algorithmen

- Auch **„Flussdiagramme"** genannt
- Beschreiben Abfolgen von Operationen
- Kann folgende Elemente haben, welche mit Pfeilen verbunden werden:

::: {style="display: flex; justify-content: space-around; align-items: center; margin: 2em 0;"}
::: {style="text-align: center;"}
**Beginn/Ende**  
![Oval](images/oval.svg)
:::

::: {style="text-align: center;"}
**Statement**  
![Rectangle](images/rectangle.svg)
:::

::: {style="text-align: center;"}
**Unterprogramm**  
![Double Rectangle](images/double_rectangle.svg)
:::

::: {style="text-align: center;"}
**Eingabe/Ausgabe**  
![Parallelogram](images/parallelogram.svg)
:::

::: {style="text-align: center;"}
**Verzweigung**  
![Diamond](images/diamond.svg)
:::
:::

---

## Programmablaufpläne - Grundlagen

- **Die wichtigsten Blöcke:**

::: {style="display: flex; justify-content: space-around; align-items: center; margin: 2em 0;"}
::: {style="text-align: center;"}
**Statement**  
![Statement Block](images/statement.svg)  
*Eingang → Ausgang*
:::

::: {style="text-align: center;"}
**Bedingung**  
![Condition Block](images/condition.svg)  
*Eingang → Ja/Nein (Ausgang)*
:::
:::

- Von einer Verzweigung gehen Pfeile aus, welche repräsentieren ob die Bedingung True oder False zurückgegeben hat (if/else).

- Statements müssen dabei nicht in der Syntax einer Programmiersprache geschrieben sein – es kann sich um „Pseudocodes" handeln.

---

## Programmablaufpläne - Beispiel: Division durch 0 abfangen

```{mermaid}
flowchart TD
    A([Start]) --> B[Dividend und Divisor definieren]
    B --> C{Ist Divisor 0?}
    C -->|Ja| D[Ergebnis ist undefiniert]
    C -->|Nein| E[Division ausführen]
    D --> F([Ende])
    E --> F
```

---

## Wofür braucht man das im normalen Leben?

::: {style="display: flex; justify-content: space-between; align-items: flex-start;"}
::: {style="flex: 1; margin-right: 2em;"}
**Prozessmodellierung**

- Geothermie-Verfahrensabläufe
- IP-Management Prozessoptimierung
- Geschäftsprozesse
- Qualitätssicherung
:::

::: {style="flex: 1;"}
**Patente**

- Algorithmische Beschreibungen
- Verfahrenspatente
- Technische Dokumentation
:::
:::

::: {style="margin-top: 2em; font-size: 0.8em;"}
*Quellen:*  
- [TEWAG Geothermie Verfahrensablauf](https://www.tewag.de/files/tewag-theme/media/leistungen/verfahrensablauf_geothermie.png)
- [Serviva Prozessoptimierung](https://serviva.com/white-paper/prozessoptimierung-im-ip-management/)
:::

---

## Hörsaalfrage - Fragen?

::: {style="text-align: center; padding: 3em;"}
![DALL·E 2: A psychedelic DJ with a question mark for a head](images/dalle_dj_question.png){width="400px"}

**Haben Sie Fragen zum Programmablauf?**
:::

---

## Zusammenfassung

- **Problemdefinition:** Ein- und Ausgaben identifizieren
- **Schrittweise Zerlegung:** Komplexe Probleme in einfache Schritte aufteilen
- **Programmablaufpläne:** Visualisierung von Algorithmen
- **Praktische Anwendung:** Von der Programmierung bis zur Prozessmodellierung

::: {style="margin-top: 2em; text-align: center; font-style: italic;"}
*„Das Zerlegen und Lösen von Problemen ist eine Grundfähigkeit von Ingenieuren."*
:::