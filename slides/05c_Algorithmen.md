---
title: "Programmieren und Datenbanken - Programmablauf"
author: "Joern Ploennigs"
format: revealjs
---

## Programmkonzeption - Algorithmen

- *Definition:* Algorithmen sind wohldefinierte, eindeutige Handlungsanweisungen.

- *Bekannte Beispiele:*
  - Schriftliche Division
  - Dreieckskonstruktion

- *In der Informatik-Praxis:* computerausführbar und endlich

- Programmieren bedeutet Algorithmen und Datenstrukturen so zu kombinieren, dass man von der gewünschten Eingabe zur gewünschten Ausgabe kommt.



## Exkurs – Beispiel für – Teile und Herrsche – Binäre Suche

:::: {.columns}

::: {.column width="50%"}
- Finde den Index einer Zahl in einer Liste (z. B. um zu prüfen ob die Zahl in einer Menge (set) vorkommt)

- Anstatt die ganze Liste zu durchsuchen, teil man die Liste rekursiv in zwei Teile und schaut ob die gesuchte Zahl gleich (gefunden), größer (rechts) oder kleiner (links) in der Liste ist
:::

::: {.column width="50%"}
```{mermaid}
flowchart TD
    A[Start] --> B[Wähle Index in der Mitte des Bereichs]
    B --> C{Gleich?}
    C -->|Ja| D[Ende]
    C -->|Nein| E{Größer?}
    E -->|Ja| F[Neuer Bereich rechts von Index]
    E -->|Nein| G[Neuer Bereich links von Index]
    F --> B
    G --> B
```
:::

::::



## Programmkonzeption - Heuristiken

- Basieren nicht auf wohldefinierten oder eindeutigen Schritten, sondern auf praktischen Erfahrungen

- Versuchen schnell ein hinreichend korrektes Ergebnis zu erreichen. *KEINE* Garantie die optimale Lösung zu finden.

- *Beispiel:*
  - Die Schätzung eines Experten
  - Schrittweises Annähern



## Exkurs – Beispiel für eine Heuristik: A*Star Suchalgorithmus

:::: {.columns}

::: {.column width="50%"}
- Die Wegsuche gehört zu den komplexesten Problemen in der Informatik (NP-Komplex: Aufgrund des kombinatorischen Problems)

- A* ist eine Heuristik um den kürzesten Weg zwischen zwei Punkten in einem Feld mit Hindernissen zu finden
:::

::: {.column width="50%"}
```{mermaid}
flowchart TD
    A[Start] --> B[Berechne Entfernung aller Nachbarn]
    B --> C{Nachbarn übrig?}
    C -->|Ja| D[Gehe zu Nachbar am nächsten zum Ziel]
    C -->|Nein| E[Verwerfe Nachbar und gehe einen Schritt zurück]
    D --> F{Am Ziel?}
    F -->|Ja| G[Ende]
    F -->|Nein| B
    E --> B
```
:::

::::



## Beispielproblem - Befindet sich ein Punkt X in einem Polygon?

- Ein Polygon ist ein beliebiges Vieleck

- Die Lösung dieses Problems ist ein häufiger Teil von Berechnungen in den Bau- und Umweltwissenschaften, z. B. um zu testen, ob ein geplantes Objekt in einem Naturschutzgebiet liegt.

![Polygon Beispiel](https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Polygon-definition.svg/300px-Polygon-definition.svg.png)



## Hörsaalfrage {.center}

### Wie kann ich bestimmen ob ein Punkt in einem Polygon liegt?

::: {.center}
*Google Maps Beispiel*
:::



## Hörsaalfrage {.center}

### Was sind die Ein- und Ausgaben?

::: {.center}
*Google Maps Beispiel*
:::



## Beispielproblem - Was sind unsere Aus- und Eingaben?

*Eingaben:*
- Die Position des Punktes X
- Ein Linienzug der den Rand des Polygons beschreibt
  - Eine Liste von verbundenen, aufeinanderfolgenden Linien

*Ausgaben:*
- Ein Boolean



## Beispielproblem - Entwerfen eines Algorithmus

:::: {.columns}

::: {.column width="50%"}
*Was sind Berechnungen, die man auf Punkten und Linien ausführen kann?*

- Wir können prüfen ob der Punkt genau auf einer Linie liegt.
- Wir können prüfen auf welcher Seite einer Linie ein Punkt liegt.

*Reicht Punkt 2 aus? Für konvexe Flächen - ja:*
- Befindet sich der Punkt auf der gleichen Seite aller Linien des Polygons, befindet er sich im Polygon.
:::

::: {.column width="50%"}
*Trifft aber nicht für konkave Flächen zu => es handelt sich also um eine Heuristik!*

![Konvexes Polygon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cG9seWdvbiBwb2ludHM9IjIwLDIwIDgwLDIwIDgwLDgwIDIwLDgwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSI1MCIgeT0iOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiPktvbnZleDwvdGV4dD4KPC9zdmc+)

![Konkaves Polygon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cG9seWdvbiBwb2ludHM9IjIwLDIwIDgwLDIwIDUwLDUwIDgwLDgwIDIwLDgwIiBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSI1MCIgeT0iOTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiPktvbmthdjwvdGV4dD4KPC9zdmc+)
:::

::::



## Beispielproblem - Entwerfen eines Algorithmus

*Entwurf* bedeutet oft ein Problem aus verschiedenen Richtungen zu betrachten und neue Berechnungsperspektiven zu finden.

*Hier:* Die Krux ist ob eine Fläche konkav oder konvex ist. Man bestimmt diese Eigenschaften durch das Ziehen von Linien und Schnitttests.

*Liegt der Schlüssel zu diesem Problem also in den Schnitttests zwischen Linien?*

Gibt es eine Linie vom gesuchten Punkt X zu einem anderen Punkt Y, deren Schnittpunkte mit den Polygon-Linien eine Antwort auf die Fragestellung geben?



## Beispielproblem - Entwerfen eines Algorithmus

*Die Antwort:* Jeder beliebige Punkt außerhalb des Polygons!

- Liegt Punkt X innerhalb des Polygons dann wird die gezogene Linie die Grenze mindestens einmal schneiden.

- Läuft die gezogene Linie zufällig durch einen konkaven Bereich dann wird es zwei weitere Schnittpunkte geben, für insgesamt 3 Schnittpunkte, oder 5, oder …

- Liegt der Punkt X außerhalb wird es also entweder keine Schnittpunkte geben, oder 2, oder 4, oder …

*Das Problem kann also auf die Anzahl von Schnittpunkten reduziert werden!*



## Beispielproblem - Als Programmablaufplan aufzeichnen

:::: {.columns}

::: {.column width="50%"}
*Beispiele für:*
- Strahl 1 hat 1 Schnittpunkt → ungerade = innenliegend
- Strahl 2 hat 3 Schnittpunkte → ungerade = innenliegend  
- Strahl 3 hat 5 Schnittpunkte → ungerade = innenliegend
:::

::: {.column width="50%"}
```{mermaid}
flowchart TD
    A[Input Polygon] --> B[Input Punkt]
    B --> C[Start]
    C --> D[Strahl in zufällige Richtung konstruieren]
    D --> E[Schnittpunkte finden]
    E --> F[Alle Linien Strahl]
    F --> G{Anzahl ungerade?}
    G -->|Ja| H[Punkt im Polygon]
    G -->|Nein| I[Punkt nicht im Polygon]
    H --> J[Ende]
    I --> J
```
:::

::::



## Beispielproblem - Welche Funktionen müssen implementiert werden?

- *Strahl konstruieren*

- *Schnitttest zwischen Strahl und Linien*

- *Eine Funktion, die die Inputs annimmt und die anderen Funktionen aufruft.*
  - Diese zentrale Funktion wird meistens *main-Funktion* genannt.



## Programmkonzeption - Beispielproblem

*Wie setzt man den Schnitttest über die Linien programmiertechnisch um?*

- Man müsste die selbe Anweisung (Schnitttest) für jede Linie einmal ausführen, abhängig davon wie viele Linien das Polygon hat.

- *Mit unseren derzeitigen Mitteln nicht machbar!*

- Eines der wichtigsten Programmierwerkzeuge fehlt uns noch: *Schleifen und Iteration*

- *Dazu mehr in der nächsten Vorlesung!*



## Fragen? {.center}

::: {.center}
![DALL·E 2: A psychedelic DJ with a question mark for a head](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjgwIiBmaWxsPSIjZmY2YjZiIi8+CiAgPHRleHQgeD0iMTAwIiB5PSIxMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iNjAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZmlsbD0iI2ZmZiI+Pz88L3RleHQ+Cjwvc3ZnPg==)
:::



## Custom CSS Styles

```css
/* Add this to styles.css file */
.center {
  text-align: center;
}

.columns {
  display: flex;
  gap: 1rem;
}

.column {
  flex: 1;
}

/* Responsive design */
@media (max-width: 768px) {
  .columns {
    flex-direction: column;
  }
}