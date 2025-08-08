---
title: "Einführung in Programmierung und Datenbanken"
subtitle: "Algorithmen: Sortieren und Suchen"
author: "joern ploennigs"
format: 
  revealjs:
    theme: default
    slide-number: true
    chalkboard: true
    preview-links: auto
    css: styles.css
---

## Algorithmen: Sortieren und Suchen {background-image="https://via.placeholder.com/1200x800/4a90e2/ffffff?text=Digital+Art+Bear+Economist"}

::: {style="background-color: rgba(255,255,255,0.9); padding: 20px; border-radius: 10px;"}
**Midjourney**: A bear economist in front of a stock chart crashing, digital art.
:::

---

## Rekursion - Beispiel: Tree Traversal

::: {.flex style="display: flex; gap: 2rem;"}
::: {.flex-item style="flex: 1;"}
**Baum-Konzept:**

- Datenstruktur, in der jedes Element auf weitere Unterelemente verweisen kann
- Wir wollen eine Funktion auf jedes Element im Baum anwenden
- Simpelste Repräsentation eines Baumes:
  - Ein Tupel mit einem Wert und einer Liste
  - Diese Liste enthält Tupel mit jeweils einem Wert und einer Liste (Rekursive Datenstruktur!)
:::

::: {.flex-item style="flex: 1;"}
```python
baum = (12, [
    (6,[
        (3,[]),
        (9,[])
    ]),
    (18,[
        (15,[]),
        (21,[])
    ])
])
```

```
        12
      /    \
     6      18
   /  \    /  \
  3    9  15   21
```
:::
:::

---

## Rekursion - Tree Traversal Implementation

::: {.flex style="display: flex; gap: 2rem;"}
::: {.flex-item style="flex: 1;"}
**Traversals** sind Funktionen welche den Baum durchlaufen, z.B. um Elemente zu suchen.

```python
def traverse(tree):
    wert = tree[0]  # der aktuelle Wert
    print(wert)     # gebe den aktuellen Wert aus
    
    if tree[1]:     # wenn Kinder definiert sind
        for child in tree[1]:  # iteriere durch alle Kinder
            traverse(child)    # und rufe die Funktion rekursiv auf

traverse(baum)
```
:::

::: {.flex-item style="flex: 1;"}
**Ausgabe:**
```
12, 6, 3, 9, 18, 15, 21
```

Die Rekursion ermöglicht es, komplexe Baumstrukturen elegant zu durchlaufen.
:::
:::

---

## Informatik-Exkurs: Sortieren

- **Speziell das Sortieren von Listen**, unabhängig vom Datentyp
- Eine der **Standard-Anwendungen** für Schleifen und Rekursion
- **Die Lösung im Programmieralltag**: `sorted()`
- **Aber**: Gutes Beispiel für strukturiertes Informatik-Problem

---

## Sortieren - Algorithmus 1: Bubble Sort

::: {.flex style="display: flex; gap: 2rem;"}
::: {.flex-item style="flex: 1;"}
**Algorithmus:**

- Jedes Element der Liste wird durchlaufen und mit dem nächsten Element verglichen
- Ist das zweite Element kleiner als das erste wird die Position getauscht
- Die Liste wird immer wieder durchlaufen bis dieser Fall nicht mehr auftritt
:::

::: {.flex-item style="flex: 1;"}
```python
def bubbleSort(numbers):
    for i in range(len(numbers)-1):
        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
```
:::
:::

---

## Sortieren - Algorithmus 2: Quick Sort

**Das Grundprinzip ist das Aufteilen der Liste:**

1. Das erste Element der Liste als **„Pivot"-Element** abspeichern
2. Dann wird die Liste durchlaufen und jedes Element mit dem Pivot verglichen
3. **Einsortiert** in eine von drei Listen: **Kleiner**, **Gleich** und **Größer**
4. Dann wird Quick Sort **rekursiv** auf die Listen Kleiner und Größer ausgeführt
5. Am Ende werden alle Listen rekursiv wieder **zusammengeführt**

---

## Informatik-Exkurs: Suchen

- **Speziell das Suchen** auf sortierten Listen und Bäumen
- Meist kennt man die **Anzahl an Elementen**, weiß also genau wo z.B. die Mitte ist
- **Spätere Vorlesungen**: In echten Anwendungen haben Datensätze oft mehr als nur einen Wert (Tabellen anstatt Listen), hier arbeitet man meist mit **Indexierung**

---

## Suchen - Suche in Listen

::: {.flex style="display: flex; gap: 2rem;"}
::: {.flex-item style="flex: 1;"}
**Die einfachste Methode: Lineare Suche**

```python
def contains(list, x):
    for l in list:
        if(l == x):
            return True
    return False
```
:::

::: {.flex-item style="flex: 1;"}
**Das optimale Verfahren: Binäre Suche**

- Deutlich komplexerer Code
- **Idee**: Mittleres Element der Liste finden, dann mit dem gesuchten Wert vergleichen
- **Wert kleiner**: Selbes Verfahren für die erste Hälfte der Liste  
- **Wert größer**: Selbes Verfahren für die zweite Hälfte der Liste
- **Implementation** meistens über Rekursion
:::
:::

---

## Suchen - Suchen in Bäumen

**Strategien um einen unsortierten Baum zu durchsuchen:**

- **Breitensuche**: Vom Ursprung beginnend jede „Ebene" des Baumes von links nach rechts durchlaufen

- **Tiefensuche**: Einem Pfad vom Ursprung bis zum Ende folgen, dann schrittweise rückwärts gehen bis sich weitere Pfade anbieten

---

## Suchen - Suchen in sortierten Bäumen

- In **sortierten Bäumen (Suchbäumen)** kann das Ergebnis extrem effizient gefunden werden, da nur ein Pfad durchlaufen werden muss

- **Wie sortiert man einen Baum?** Erstellen eines binären Suchbaums

- **Beispiel**: `12 6 18 15 3 21 9`

---

## Suchbaum - Schritt für Schritt Aufbau

::: {.flex style="display: flex; gap: 2rem;"}
::: {.flex-item style="flex: 1;"}
**Ausgangsliste:**
```
12 6 18 15 3 21 9
```

**Schritt 1:** 12 als Wurzel
```
12
```

**Schritt 2:** 6 < 12 → links
```
    12
   /
  6
```
:::

::: {.flex-item style="flex: 1;"}
**Schritt 3:** 18 > 12 → rechts
```
    12
   /  \
  6    18
```

**Weitere Schritte:**
- 15 > 12, aber 15 < 18 → links von 18
- 3 < 12, und 3 < 6 → links von 6  
- 21 > 12, und 21 > 18 → rechts von 18
- 9 < 12, aber 9 > 6 → rechts von 6
:::
:::

---

## Finaler Suchbaum

```
        12
      /    \
     6      18
   /  \    /  \
  3    9  15   21
```

**Eigenschaften des binären Suchbaums:**
- Linke Kinder sind immer kleiner als der Parent-Knoten
- Rechte Kinder sind immer größer als der Parent-Knoten
- Ermöglicht sehr effiziente Suche: O(log n)

---

## Exkurs: Komplexität und effiziente Algorithmen

::: {.flex style="display: flex; gap: 2rem;"}
::: {.flex-item style="flex: 1;"}
**Konzept der Komplexität:**

- Die eigentliche Berechnungszeit ergibt sich erst durch die genauen Eingabedaten und den genutzten Prozessor
- **Formal** ist Effizienz stattdessen eher eine Anstiegskurve, welche eine relative Schätzung abgibt wie viel länger ein Algorithmus bei mehr Eingabedaten rechnen muss
- **Notation**: O(x), wobei x die Menge der nötigen Rechenschritte angibt
:::

::: {.flex-item style="flex: 1;"}
**Komplexitäten verschiedener Algorithmen:**

Für Bäume und Listen hängt diese von der Anzahl an Elementen ab (Variable n):

- **Lineare Suche**: O(n)
- **Binäre Suche**: O(log(n))
- **Bubble Sort**: O(n²)  
- **Quick Sort**: O(n*log(n))
:::
:::

---

## Hörsaalfrage: Fragen? {background-image="https://via.placeholder.com/1200x800/6a4c93/ffffff?text=Psychedelic+DJ+Question+Mark"}

::: {style="background-color: rgba(255,255,255,0.9); padding: 20px; border-radius: 10px; text-align: center;"}
**DALL·E 2**: A psychedelic DJ with a question mark for a head

🎵 **Fragen zu Sortier- und Suchalgorithmen?** 🎵
:::