## Algorithmen

```{quizdown}
    ---
    shuffleQuestions: true
    shuffleAnswers: true
    ---

    ### Was ist ein Algorithmus?
    - [x] Eine Schritt-für-Schritt-Anleitung zur Lösung eines Problems
    - [ ] Ein zufälliger Code ohne Struktur
    - [ ] Eine Art von Datenbank
    - [ ] Ein grafisches Design-Tool

    ### Welche der folgenden Eigenschaften hat ein guter Algorithmus?
    - [x] Er ist effizient und löst das Problem in akzeptabler Zeit
    - [ ] Er ist immer kompliziert und schwer zu verstehen
    - [ ] Er benötigt keine Eingaben
    - [ ] Er kann nur auf Zahlen angewendet werden

    ### Was ist ein typischer Anwendungsbereich von Bäumen in der Informatik?
    - [x] Effizientes Suchen
    - [ ] Textformatierung
    - [ ] Dateikompression
    - [ ] Netzwerkanalyse

    ### Was ist ein Baum in der Informatik?
    - [x] Eine hierarchische Datenstruktur mit Knoten
    - [ ] Eine Schleife mit mehreren Bedingungen
    - [ ] Eine spezielle Liste mit fester Länge
    - [ ] Ein Zahlenarray mit zufälliger Reihenfolge

    ### Sortiere die folgenden Zeilen, um eine rekursive Funktion zur Traversierung eines binären Baums korrekt aufzubauen:
    ```python
    # Gegeben ist: tree = {"wert": 5, "links": {"wert": 3}, "rechts": {"wert": 7}}
    ```
    1. `def traverse(tree):`
    2. `  print(tree["wert"])`
    3. `  if "links" in tree:`
    4. `    traverse(tree["links"])`
    5. `  if "rechts" in tree:`
    6. `    traverse(tree["rechts"])`

    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    def traverse(tree):
        print(tree["wert"])
        traverse(tree["links"])
        traverse(tree["rechts"])
    ```
    - [x] Es fehlt die Prüfung, ob "links" oder "rechts" überhaupt vorhanden sind
    - [ ] Die Funktion darf nicht rekursiv aufgerufen werden
    - [ ] Der `print`-Befehl ist falsch eingerückt
    - [ ] Python kennt keine Dictionaries

    ### Wie funktioniert Bubble Sort?
    - [x] Elemente werden paarweise verglichen und bei Bedarf getauscht
    - [x] Die Liste wird mehrfach durchlaufen, bis keine Vertauschung mehr nötig ist
    - [ ] Alle Elemente werden sofort sortiert
    - [ ] Nur gerade Zahlen werden betrachtet

    ### Warum ist Bubble Sort ineffizient für große Datenmengen?
    - [x] Weil viele Vergleiche und Tauschvorgänge nötig sind
    - [ ] Weil Python keine Listen verarbeiten kann
    - [ ] Weil es keine `for`-Schleifen verwendet
    - [ ] Weil die Elemente gelöscht werden

    ### Wie funktioniert QuickSort?
    - [x] Wählt ein Pivot-Element, teilt in kleinere und größere Teilmengen und sortiert rekursiv
    - [x] Nutzt das Divide-and-Conquer-Prinzip
    - [ ] Tauscht benachbarte Elemente mehrfach aus
    - [ ] Sortiert nur durch Anhängen an eine Liste

    ### Sortiere die folgenden Zeilen, um eine vereinfachte QuickSort-Funktion korrekt zu bauen:
    ```python
    # Annahme: Liste besteht nur aus Zahlen
    ```
    1. `def quicksort(arr):`
    2. `  if len(arr) <= 1:`
    3. `    return arr`
    4. `  pivot = arr[0]`
    5. `  less = [x for x in arr[1:] if x <= pivot]`
    6. `  greater = [x for x in arr[1:] if x > pivot]`
    7. `  return quicksort(less) + [pivot] + quicksort(greater)`

    ### Wie funktioniert Insertion Sort?
    - [x] Elemente werden an der richtigen Stelle in eine bereits sortierte Teilliste eingefügt
    - [ ] Jedes Element wird mit einem zufälligen verglichen
    - [ ] Alle Elemente werden gleichzeitig verschoben
    - [ ] Die Liste wird rückwärts durchlaufen und sortiert

    ### Was ist der Hauptunterschied zwischen Insertion Sort und Bubble Sort?
    - [x] Insertion Sort fügt Elemente korrekt ein, Bubble Sort vertauscht sie wiederholt
    - [ ] Insertion Sort verwendet keine Schleifen
    - [ ] Bubble Sort nutzt keinen Vergleich
    - [ ] Insertion Sort kann nur auf Zeichenketten angewendet werden

    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    zahlenfolge = [4, 2, 1]
    zahlenfolge = zahlenfolge.sort()
    ```
    - [x] `sort()` verändert die Liste in-place und gibt `None` zurück – `zahlenfolge` wird `None`
    - [ ] `sort()` ist nicht erlaubt auf Listen
    - [ ] Listen dürfen nicht sortiert werden
    - [ ] `sorted()` wäre hier schneller

    ### Warum ist `sorted()` schneller als Bubble Sort oder Insertion Sort?
    - [x] Es ist in C implementiert und verwendet eine optimierte Variante von `insert_sort`
    - [ ] Es nutzt Zufallszahlen zum Sortieren
    - [ ] Es verwendet keine Vergleiche
    - [ ] Es sortiert nur die Hälfte der Liste

```