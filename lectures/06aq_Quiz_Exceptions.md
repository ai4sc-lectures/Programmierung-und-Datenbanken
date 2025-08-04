## Exceptions

```{quizdown}
    ---
    shuffleQuestions: true
    shuffleAnswers: true
    ---

    ### Was ist eine Exception in Python?
    - [x] Eine Ausnahme, die den normalen Ablauf des Programms unterbricht
    - [ ] Ein Spezialfall bei Loops
    - [ ] Eine Warnung, die ignoriert werden kann
    - [ ] Eine globale Variable

    ### Warum verwendet man `try-except`-Blöcke?
    - [x] Um kontrolliert auf Fehler zu reagieren
    - [x] Um das Programm vor Abstürzen zu bewahren
    - [ ] Um Variablen zu initialisieren
    - [ ] Um Funktionen automatisch zu wiederholen

    ### Was passiert, wenn eine Exception im `try`-Block auftritt?
    - [x] Der Code im `except`-Block wird ausgeführt
    - [ ] Der `try`-Block wird ignoriert
    - [ ] Das Programm wird automatisch beendet
    - [ ] Der Fehler wird immer ignoriert

    ### Sortiere die folgenden Zeilen, um einen vollständigen `try-except`-Block korrekt aufzubauen:
    ```python
    # Annahme: Fehlerhafte Division
    ```
    1. `try:`
    2. `  ergebnis = 10 / 0`
    3. `  print("Ergebnis:", ergebnis)`
    4. `except:`
    5. `  print("Fehler bei der Division")`

    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    x = 10
    y = 0
    z = x / y
    print("Ergebnis:", z)
    ```
    - [x] Division durch null führt zu einer `ZeroDivisionError`-Exception
    - [ ] `print` darf nicht in try-Blöcken verwendet werden
    - [ ] `x` darf nicht 10 sein
    - [ ] `y` muss als String deklariert werden

    ### Was ist der Vorteil, wenn man `Exception as e` verwendet?
    - [x] Man kann Typ und Fehlermeldung der Exception gezielt ausgeben
    - [ ] Dadurch wird die Exception automatisch gelöst
    - [ ] Der Code wird kürzer
    - [ ] `as` ist Pflicht in jeder Fehlerbehandlung

    ### Warum sollte man bekannte Exception-Typen (wie `TypeError`) explizit abfangen?
    - [x] Um unterschiedliche Fehler gezielt zu behandeln
    - [ ] Weil Python sonst nicht funktioniert
    - [ ] Damit die Ausgabe schöner wird
    - [ ] Das ist nur bei `int`-Werten nötig

    ### Sortiere die folgenden Zeilen, um eine typisierte Fehlerbehandlung für Divisionen korrekt aufzubauen:
    ```python
    # Beispiel mit Division durch 0 und falschem Typ
    ```
    1. `try:`
    2. `  ergebnis = "zehn" / 0`
    3. `except TypeError:`
    4. `  print("Falscher Datentyp")`
    5. `except ZeroDivisionError:`
    6. `  print("Division durch 0")`

    ### Wann wird der `else`-Block bei `try-except-else` ausgeführt?
    - [x] Nur wenn im `try`-Block **keine** Exception auftritt
    - [ ] Wenn irgendein Fehler auftritt
    - [ ] Immer nach dem `except`
    - [ ] Wenn `print()` im `try` verwendet wird

    ### Was bewirkt ein `finally`-Block in Python?
    - [x] Der Code im `finally` wird **immer** ausgeführt – egal ob Fehler oder nicht
    - [ ] Der Code wird übersprungen bei Fehlern
    - [ ] Nur verwendet bei Netzwerken
    - [ ] Dient zur Initialisierung von Variablen

    ### Wann sollte man eigene Exceptions mit `raise` erzeugen?
    - [x] Wenn man Fehler gezielt kennzeichnen und weiterreichen will
    - [ ] Wenn man eine Schleife abbrechen will
    - [ ] Nur bei Syntaxfehlern
    - [ ] Nur für Debugging-Zwecke

    ### Warum ist es sinnvoll, spezifische Fehlertypen wie `ValueError` zu verwenden?
    - [x] Damit Fehler gezielter behandelt und unterschieden werden können
    - [ ] Damit `try`-Blöcke kürzer werden
    - [ ] Damit das Programm schneller läuft
    - [ ] Weil `Exception` in Python nicht erlaubt ist

    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    if not isinstance(x, int):
        raise "Fehler"
    ```
    - [x] `raise` erwartet ein Exception-Objekt, kein String
    - [ ] `raise` ist kein gültiges Python-Schlüsselwort
    - [ ] Strings dürfen nicht mit `if` verglichen werden
    - [ ] `int` ist kein gültiger Typ

    ### Sortiere die folgenden Zeilen, um eine sichere Divisionsfunktion mit Fehlern zu definieren:
    ```python
    # Annahme: Division mit Typprüfung und Division durch 0
    ```
    1. `def division(zaehler, nenner):`
    2. `  if not isinstance(zaehler, (int, float)):`
    3. `    raise ValueError("Zaehler ist ungültig")`
    4. `  if nenner == 0:`
    5. `    return None`
    6. `  return zaehler / nenner`

    ### Wie verhalten sich Exceptions in einem Funktionsaufruf-Stack?
    - [x] Sie steigen nach oben, bis sie behandelt oder zum Absturz führen
    - [ ] Sie verschwinden nach dem ersten Funktionsaufruf
    - [ ] Sie führen nur in der aktuellen Funktion zum Fehler
    - [ ] Sie werden automatisch ignoriert

    ### Was bewirkt folgende Zeile in einer rekursiven Funktion?
    ```python
    raise RecursionError("Recursion zu tief")
    ```
    - [x] Sie erzeugt gezielt einen Fehler, wenn die Rekursion zu tief wird
    - [ ] Sie verhindert eine Exception
    - [ ] Sie beendet die Rekursion erfolgreich
    - [ ] Sie wandelt den Rückgabewert in eine Exception um

    ### Was ist der Stack?
    - [x] Eine Datenstruktur, die Funktionsaufrufe speichert
    - [ ] Eine Liste aller Variablen im Programm
    - [ ] Ein spezieller Datentyp für Schleifen
    - [ ] Eine Art von Exception

    ### Was ist der Heap?
    - [x] Ein Speicherbereich für dynamisch erzeugte Objekte
    - [ ] Eine spezielle Art von Schleife
    - [ ] Ein Datentyp für Zahlen
    - [ ] Ein Bereich für globale Variablen

    ### Was ist der Unterschied zwischen Stack und Heap?
    - [x] Stack speichert Funktionsaufrufe, Heap dynamisch erzeugte Objekte
    - [ ] Stack ist schneller, Heap langsamer
    - [ ] Stack ist für Schleifen, Heap für Bedingungen
    - [ ] Stack ist für globale Variablen, Heap für lokale

    
```