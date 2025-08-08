---
title: "Bibliotheken und Pakete"
subtitle: "Einführung in Programmierung und Datenbanken"
author: "Joern Ploennigs"
format:
  revealjs:
    theme: default
    slide-number: true
    chalkboard: true
    preview-links: auto
    css: custom.css
---

## Bibliotheken und Pakete {.center}

::: {.flex}
::: {.flex-item}
![Library of Babel in hexagon shape - Midjourney](images/library_babel.jpg){fig-align="center" width="80%"}
:::
:::

---

## Organisieren von Projekten über mehrere Dateien

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Herausforderungen großer Programme:**

• Dutzende Klassen mit hunderten Funktionen
• Viele tausende Zeilen Code
• Schwer Überblick zu behalten
• Versionskonflikte bei mehreren Programmierern
:::

::: {.flex-item style="flex: 1;"}
**Lösung - Code aufteilen in .py Dateien:**

• **Pro Klasse** eine Datei (bei Klassendefinitionen)
• **Pro Thema** eine Datei (z.B. Mathematik-Funktionen)
• **Pro Aufgabenbereich** eine Datei (z.B. Laden vs. Verarbeitung)
:::
:::

---

## Die main()-Funktion als Standardfunktion

::: {.flex}
::: {.flex-item}
**Woher weiß Python was ausgeführt werden soll?**

• Eine bestimmte Datei als **Zentrum des Projektes** deklarieren
• Diese enthält eine spezielle Funktion namens `main()`
• Existiert in fast jeder Programmiersprache
• Gibt den **Startpunkt des Programms** an
• Kann keine oder dynamische Argumente erhalten (Kommandozeilenargumente)

**Beispiel:** Doppelklick auf Python-Datei ruft `main()` auf
:::
:::

---

## Die main()-Funktion in Python

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Verschiedene Ausführungsmöglichkeiten:**

1. Als Skript in Kommandozeile/Gesamtprogramm
2. Importiert in interaktive Python-Konsole  
3. Importiert in andere Python-Datei

**Problem:** In Fall 1 wollen wir das gesamte Skript, in Fall 2+3 nur Teile nutzen
:::

::: {.flex-item style="flex: 1;"}
**Die Lösung - Variable `__name__`:**

```python
def main():
    print("This is the main function")

if __name__ == "__main__":
    main()  # nur bei direktem Aufruf
```

`__name__` enthält `"__main__"` nur bei direkter Ausführung
:::
:::

---

## Best Practice für main()-Funktion

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Was gehört VOR die main()-Definition:**

✅ **Nur erlaubt:**
• Funktionsdefinitionen
• Klassendefinitionen

❌ **Vermeiden:**
• Variablenbelegungen (globale Variablen)
• Funktionsaufrufe (Nebeneffekte)
:::

::: {.flex-item style="flex: 1;"}
**Vorteile dieser Struktur:**

• **Programmfluss** wird übersichtlicher
• **Programm** einfach modifizierbar
• **Programm** besser weiterverwendbar

Alle Funktionalitäten in Klassen und Funktionen auslagern, dann in main() nutzen
:::
:::

---

## Programmfluss über mehrere Dateien

::: {.flex}
::: {.flex-item}
**Jetzt haben wir einen zentralen Startpunkt...**

**Wie rufen wir Code aus anderen Dateien auf?**

Jede Programmiersprache hat Befehle zum Laden externen Codes:
• `import` und `include`
• Spezielle "Header-Dateien"
• Definieren Zusammenhänge zwischen Dateien

**In Python:** Kombination aus Fall 1 und Fall 3 mit `import`-Statement
:::
:::

---

## Programmfluss in Python - import Statement

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Strategie:**
• Eine .py-Datei enthält `main()` (Fall 1)
• Alle anderen ohne `main()` oder mit `__name__` ignoriert (Fall 3)
• `import`-Statement lädt externe Dateien

**Achtung:** Kompletter Code wird ausgeführt, auch Variablen und Funktionsaufrufe!
:::

::: {.flex-item style="flex: 1;"}
**Beispiel:**

```python
import external_file

def main():
    print("This is the main function")
```

Variablen/Funktionen/Klassen aus `external_file.py` werden in Objekt `external_file` abgelegt
:::
:::

---

## Import externer Bibliotheken (Packages)

::: {.flex}
::: {.flex-item}
**Terminologie:**
• **Module:** Importierte Skripte
• **Namespace:** Das entstehende Objekt (Typ: module)
• **Package:** Modul mit weiteren Untermodulen

**Package-Struktur:**
Verhält sich wie Ordnerstruktur, aber für Sammlungen von Klassen und Funktionen anstatt Dateien
:::
:::

---

## Grundlagen der Projektstruktur

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Allgemeine Struktur:**

```
main.py [enthält main()]
├── module1.py
├── module2.py  
└── helpers.py
```

```python
import module1
import module2
import helpers
```
:::

::: {.flex-item style="flex: 1;"}
**Beispiel - Stadtprojekt:**

```
city.py
├── buildings.py
├── streets.py
└── geometry.py
```

```python
import buildings
import streets
import geometry
```
:::
:::

---

## Das import-Statement: Erweiterte Nutzungen

::: {.flex}
::: {.flex-item}
**Zusätzliche Import-Konstrukte:**

**from-import-Statement:**
Importiert Submodul/Teil direkt ohne übergeordneten Namespace

**from-import-as-Statement:**  
Arbeitet genauso, benennt aber das importierte Objekt um

```python
from external_file import external_function as ext_func
```

Die Import-Funktionen von Python sind komplex und vielschichtig - dies sind die wichtigsten Varianten im Alltag
:::
:::

---

## Import-Statements – Das Tor zur Welt

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Nicht nur eigene Pakete importieren!**

Auch Pakete von anderen Personen/Organisationen

**Zugriffsmöglichkeiten:**
• Paket in Python mitgeliefert
• Direkt als .py-Dateien herunterladen
• **Package-Manager benutzen** (Besser!)
:::

::: {.flex-item style="flex: 1;"}
**Python Package Index (PyPI):**
• Offizielle Anlaufstelle für Packages
• Derzeit über **418.000 frei verfügbare** Pakete
• Installation meist mit **einem einzigen Befehl/Klick**
:::
:::

---

## Packages - Die eigentliche Macht von Python

::: {.flex}
::: {.flex-item}
**Warum ist Python so populär?**

Python hat sich zur **Interface- und Pipeline-Sprache** entwickelt

**Fast jedes durch Computer lösbare Problem** kann durch geschicktes Verschalten der richtigen Python-Packages gelöst werden

**Pythons Erfolg basiert auf seinem Package-Ökosystem** - nicht nur auf der Sprache selbst
:::
:::

---

## Fragen? {.center}

::: {.flex}
::: {.flex-item}
![A psychedelic DJ with a question mark for a head - Midjourney](images/dj_question.jpg){fig-align="center" width="60%"}
:::
:::