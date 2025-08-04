
## Schleifen

```{quizdown}
	---
	shuffleQuestions: true
	shuffleAnswers: true
	---

    ### Warum werden Schleifen in Programmen verwendet?

    - [x] Um Anweisungen mehrfach auszuführen  
    - [ ] Um Programme zu beenden  
    - [ ] Um Fehler im Code zu suchen  
    - [ ] Um Funktionen zu definieren

    ### Was ist typisch für eine `for`-Schleife?

    - [x] Sie wiederholt Anweisungen für eine Sequenz oder Anzahl  
    - [ ] Sie führt Anweisungen nur einmal aus  
    - [ ] Sie erzeugt automatisch Variablen  
    - [ ] Sie wird immer mit `if` kombiniert

    ### Wie funktioniert ein For-Each-Loop in Python?

    - [x] Er iteriert direkt über die Elemente einer Sequenz  
    - [ ] Er zählt von 1 bis 100  
    - [ ] Er verändert automatisch alle Elemente  
    - [ ] Er wird nur für Zahlen verwendet

    ### Was enthält die Schleifenvariable bei einem For-Each-Loop?

    - [x] Das aktuelle Element aus der Sequenz  
    - [ ] Die Länge der Sequenz  
    - [ ] Den Index des vorherigen Elements  
    - [ ] Immer eine Zahl

    ### Wozu wird `range(n)` in Python verwendet?

    - [x] Um eine Sequenz von Zahlen von 0 bis n-1 zu erzeugen
    - [ ] Um eine Sequenz von Zahlen von 0 bis n zu erzeugen
    - [ ] Um eine Liste mit n Nullen zu erstellen  
    - [ ] Um Strings zu vergleichen  
    - [ ] Um Bedingungen auszuwerten

    ### Was macht `enumerate()` in Python?
    - [x] Erzeugt eine Sequenz mit Index und Element  
    - [ ] Sortiert eine Liste alphabetisch  
    - [ ] Entfernt Duplikate aus einem Dictionary  
    - [ ] Wandelt Strings in Zahlen um

    ### Wie kann man durch ein Dictionary iterieren?
    - [x] Mit einer Schleife über die Schlüssel  
    - [x] Mit einer Schleife über Schlüssel-Wert-Paare mit `items()`
    - [ ] Nur mit einer While-Schleife  
    - [ ] Nur durch Umwandlung in eine Liste

    ### Sortiere die folgenden Zeilen, um eine gültige `for`-Schleife zu schreiben, die alle geraden Zahlen von 0 bis 10 (inklusive) ausgibt:
    1. `for i in range(0, 11, 2):`
    2. `  print(i)`

    ### Sortiere die folgenden Zeilen, um alle Elemente einer Liste mit `for` und einer Bedingung auszugeben. Gegeben ist:
    ```python
    zahlen = [3, 6, 9, 12, 15]
    ```
    1. `for z in zahlen:`
    2. `  if z > 8:`
    3. `    print(z)`

    ### Sortiere die folgenden Zeilen, um die Schlüssel und Werte eines Dictionary korrekt auszugeben und dabei nur Werte größer als 20 zu drucken. Gegeben ist:
    ```python
    person = {"name": "Anna", "alter": 30, "punkte": 18}
    ```
    1. `for key, value in person.items():`
    2. `  if isinstance(value, int) and value > 20:`
    3. `    print(f"{key}: {value}")`

    ### Sortiere die folgenden Zeilen, um `enumerate()` korrekt zu nutzen und das Element mit Index auszugeben, wenn der Index ungerade ist. Gegeben ist:
    ```python
    tiere = ["Katze", "Hund", "Maus", "Vogel"]
    ```
    1. `for i, tier in enumerate(tiere):`
    2. `  if i % 2 == 1:`
    3. `    print(f"{i}: {tier}")`

```