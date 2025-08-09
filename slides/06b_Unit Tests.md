---
title: "Fehlerbehandlung"
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

## Fehlerbehandlung {.center}

::: {.flex}
::: {.flex-item}
![Dorian Gray shooting with a gun at his picture seeing an old monster - Midjourney](images/dorian_gray.jpg){fig-align="center" width="80%"}
:::
:::

---

## Umgang mit Programmfehlern - Strategien

::: {.flex}
::: {.flex-item}
**5 Hauptstrategien:**

1. **Fehlervermeidung**
2. **Fehlererkennung**
3. **Fehlerbehebung**
4. **Fehlerbehandlung**
5. **Fehlerausschluss**

Jede Strategie hat ihre eigenen Methoden und Werkzeuge
:::
:::

---

## 1. Fehlervermeidung

::: {.flex}
::: {.flex-item}
**Grundprinzip:** Beginnt mit Erfahrung darüber, wo Fehler entstehen können

**Strategien für sicheren Code:**
• **Code Reviews** → Jede Codezeile wird von einem anderen Programmierer geprüft
• **Test-Driven Development** → Man schreibt den Test vor dem eigentlichen Code
• **Full Test Coverage** → Jede Codezeile sollte mindestens einen Test haben

**Achtung:** Vorbeugung kann viel Vorarbeit bedeuten
:::
:::

---

## 2. Fehlererkennung

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Verschiedene Fehlertypen erfordern verschiedene Werkzeuge:**

**Syntaktische Fehler:**
• Automatisch in der IDE erkannt

**Statische Fehler:**
• Mittels **Lint-Tools** (statische Code-Analyse)
• Regelbasierte Verfahren
• Moderne IDEs nutzen intern Lint-Tools
:::

::: {.flex-item style="flex: 1;"}
**Dynamische Fehler:**
• Prüfen durch **automatisch ausgeführte Unit-Tests**
• Nach jeder Code-Änderung
• Testen Funktionen/Methoden systematisch

**→ Unit-Tests sind der Schlüssel für dynamische Fehlererkennung**
:::
:::

---

## 2. Fehlererkennung – Unit-Tests

::: {.flex}
::: {.flex-item}
**Definition:** Unit-Tests sind zusätzlich geschriebener Code, der nur zum Testen eines Moduls (Funktion, Klassen, Module) geschrieben wurde.

**Wichtige Eigenschaften:**
• Oft ist Test-Code umfangreicher als der zu testende Code
• **Ziel:** Prüfen ob Modul gewünschte Funktion korrekt ausführt
• **White-Box-Test:** Modul mit bestimmten Eingaben aufrufen
• Erwartete Ausgaben oder Exceptions prüfen
• **Automatisierte Ausführung** nach jeder Code-Änderung
:::
:::

---

## 2. Fehlererkennung – Unit-Test Typen

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Typische Unit-Tests:**

• **Funktionstests** – Korrekte Erfüllung der Funktion
• **Grenzwerttests** – Umgang mit Grenzwerten
• **Datentyptests** – Umgang mit unerwarteten Eingaben

**Beispiel: Division-Modul**
:::

::: {.flex-item style="flex: 1;"}
```
Modul: division

Test 1 - Funktionstest:
zaehler = 10, nenner = 2
→ ergebnis = 5

Test 2 - Grenzwerttest:
zaehler = 10, nenner = 0
→ ergebnis = None

Test 3 - Datentyptest:
zaehler = 'keine_zahl', nenner = 0
→ TypeError
```
:::
:::

---

## 3. Fehlerbehebung - Grundlagen

::: {.flex}
::: {.flex-item}
**Debugging - Das systematische Suchen und Beheben von Fehlern**

**Methoden:**
• **Logging-Nachrichten** zur Verfolgung des Programmflusses
• **Debugger** für detaillierte Analyse

**Debugger-Funktionen:**
• Schrittweise Ausführung von Codezeilen
• Überwachen von Variablenwerten
• Dynamisches Einfügen von Code
:::
:::

---

## 3. Fehlerbehebung – In Python

::: {.flex}
::: {.flex-item}
**Python Debugging-Tools:**

• **Standard-Debugger: pdb** (Python-Modul)
• **IDE-eigene Debugger** (oft benutzerfreundlicher)

**Mehr Details dazu in der Übung!**

Das systematische Debugging ist eine Kernkompetenz jeden Programmierers
:::
:::

---

## 4. Fehlerbehandlung - Auf alles vorbereitet sein

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Realität:** Allen Bemühungen zum Trotz werden in realen Programmen Fehler zur Laufzeit auftreten

**Ziel:** 
• Fehler abfangen und behandeln
• Programm läuft weiter oder beendet kontrolliert
:::

::: {.flex-item style="flex: 1;"}
**Mechanismus:** 
• Dynamischer Fehler → **Exception** wird erzeugt
• **Python-Werkzeuge:** `try`, `except`, `raise`

**Wichtige Blöcke:**
• `finally` - immer ausgeführt
• `else` - nur ohne Exception
:::
:::

---

## Semantische Fehler - Exceptions

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Exception-Mechanismus:**
• Unterbrechen normalen Programmverlauf
• Kommunizieren Fehler mit Fehlermeldung
• Verhindern unkontrolliertes Abstürzen
• Werden im **Stack nach oben weitergegeben**
• Bis sie abgefangen oder Programm abstürzt

**Ziel:** Programm in lauffähigen Zustand zurückbringen
:::

::: {.flex-item style="flex: 1;"}
```
Stack-Beispiel:
main()           ← Absturz hier
factorial(1)
factorial(2)
factorial(3)
factorial(4)
factorial(5)     ← Exception hier
```

Exception "wandert" nach oben bis abgefangen
:::
:::

---

## Semantische Fehler – Exceptions abfangen

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Grundprinzip:** Bekannte Exceptions sollten immer abgefangen werden

**Python try-except-Block:**
```python
try:
    # Block mit erwarteter Exception
    ergebnis = zaehler / nenner
except:
    # Fehlerbehandlung
    print("Division durch 0")
    ergebnis = None
```
:::

::: {.flex-item style="flex: 1;"}
```
Stack mit Abfangen:
main()           ← Abgefangen
factorial(1)
factorial(2)
factorial(3)
factorial(4)
factorial(5)     ← Exception hier
```

Exception wird abgefangen und behandelt
:::
:::

---

## Semantische Fehler - Exception-Ebenen

::: {.flex}
::: {.flex-item}
**Exceptions werden auf mehreren Ebenen genutzt:**

• **Betriebssystem** - Vordefinierte System-Exceptions
• **Programmiersprache** - Eingebaute Language-Exceptions  
• **Eigener Code** - Selbst definierte Exceptions

**Einsatzgebiete (wo Fehler wahrscheinlich sind):**
• Kommunikation mit externen Quellen
• Lesen von Dateien
• Nutzereingaben
• Netzwerkverbindungen
:::
:::

---

## 4. Fehlerbehandlung - Beispiel: Division durch 0

::: {.flex}
::: {.flex-item style="flex: 1;"}
```python
zaehler = 12
nenner = 0

try:
    ergebnis = zaehler / nenner
except:
    print("Exception")
```

**Frage:** Welche Exceptions können hier geworfen werden?
:::

::: {.flex-item style="flex: 1;"}
**Mögliche Exceptions:**
• `ZeroDivisionError` - Division durch 0
• `TypeError` - Falscher Datentyp
• `NameError` - Variable nicht definiert

**Bessere Praxis:** Spezifische Exceptions abfangen
:::
:::

---

## 4. Fehlerbehandlung - Exceptions propagieren

::: {.flex}
::: {.flex-item}
**Wichtiges Konzept in komplexerer Software:**

• Fehler lokal behandeln
• **Aber:** "Obere Ebenen" des Programms informieren
• **`raise`-Anweisung** "wirft" Exception aus `except`-Block weiter nach oben

**Warum?** 
• Lokale Behandlung für sofortige Maßnahmen
• Globale Information für übergeordnete Entscheidungen
:::
:::

---

## 4. Fehlerbehandlung - Beispiel: Exception weiterreichen

::: {.flex}
::: {.flex-item}
```python
def count_up_and_down(x):
    if x <= 0:
        raise ValueError("No negative values allowed")
    
    # Verknüpft vorwärts- und rückwärts-Liste
    return list(range(x)) + list(reversed(list(range(x-1))))

try:
    print(count_up_and_down(-6))
except ValueError:
    print("That value was invalid.")
```

**Funktion:** Erstellt Liste die hoch und runter zählt [0,1,2,1,0]
:::
:::

---

## 5. Fehlerausschluss - Mathematischer Beweis

::: {.flex}
::: {.flex-item}
**Die Korrektheit von Programmen beweisen:**

• Gewisser Programmcode kann mittels **mathematischen Beweises** validiert werden
• **Hoare-Kalkül:** Programm Zeile für Zeile mit mathematischer Logik formalisieren
• Von vorne nach hinten durch das gesamte Programm

**Problem:** Für die meisten Anwendungen zu zeitaufwendig und komplex

**Einsatz:** Nur bei kritischen Systemen (Medizintechnik, Luftfahrt, etc.)
:::
:::

---

## Fragen? {.center}

::: {.flex}
::: {.flex-item}
![A psychedelic DJ with a question mark for a head - Midjourney](images/dj_question.jpg){fig-align="center" width="60%"}
:::
:::