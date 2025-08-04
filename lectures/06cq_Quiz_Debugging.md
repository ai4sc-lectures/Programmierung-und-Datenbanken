## Debugging

```{quizdown}
    ---
    shuffleQuestions: true
    shuffleAnswers: true
    ---

    ### Was versteht man unter Debugging?
    - [x] Das Finden und Beheben von Fehlern im Programmcode
    - [ ] Die Optimierung des Programmcodes
    - [ ] Das Schreiben von Dokumentation
    - [ ] Das Formatieren von Quellcode

    ### Warum reicht statische Code-Analyse allein nicht aus?
    - [x] Weil logische Fehler zur Laufzeit auftreten können
    - [ ] Weil sie keine Sicherheitslücken erkennt
    - [ ] Weil sie den Code langsamer macht
    - [ ] Weil sie nicht mit Python funktioniert

    ### Was ist `print`-Debugging?
    - [x] Das Einfügen von `print()`-Befehlen zur Laufzeitanalyse
    - [ ] Das Entfernen aller `print()`-Befehle
    - [ ] Ein automatisiertes Debugging-Verfahren
    - [ ] Ein grafischer Debugger

    ### Was ist der Zweck von `logging` in Python?
    - [x] Protokollierung von Ereignissen und Fehlern
    - [ ] Optimierung der Programmausführung
    - [ ] Erstellen von Benutzeroberflächen
    - [ ] Automatisches Testen von Funktionen

    ### Sortiere die folgenden Zeilen, um einen vollständigen `try-except`-Block korrekt aufzubauen

    1. `def division(zaehler, nenner):`
    2. `    print(f"Debug: Eingabe Zaehler: {zaehler}")`
    3. `    print(f"Debug: Eingabe Nenner: {nenner}")`
    4. `    if not isinstance(nenner, (int, float)):`
    5. `        print(f"Error: Nenner nicht vom Datentyp `int` oder `float`, sondern vom Typ {type(nenner)}")`
    6. `        raise ValueError(f"Nenner nicht vom Datentyp `int` oder `float`, sondern vom Typ {type(nenner)}")`
    7. `    elif not isinstance(zaehler, (int, float)):`
    8. `        print(f"Error: Zaehler nicht vom Datentyp `int` oder `float`, sondern vom Typ {type(zaehler)}")`
    9. `        raise ValueError(f"Zaehler nicht vom Datentyp `int` oder `float`, sondern vom Typ {type(zaehler)}")`
    10. `    elif not nenner:`
    11. `        print("Warning: Division durch 0")`
    12. `        return None`
    13. `    else:`
    14. `        ergebnis = zaehler / nenner`
    15. `        print(f"Info: Das Ergebnis von {zaehler}/{nenner} = {ergebnis}")`
    16. `        return ergebnis`


    ### Was passiert bei einer Division durch Null im folgenden Code?
    ```python
    def division(zaehler, nenner):
        print(f"Debug: Eingabe Zaehler: {zaehler}")
        print(f"Debug: Eingabe Nenner: {nenner}")
        if not isinstance(nenner, (int, float)):
            ...
        elif not nenner:
            print("Warning: Division durch 0")
            return None
    ```
    - [x] Eine Warnung wird ausgegeben und `None` zurückgegeben.
    - [ ] Es erfolgt ein Abbruch durch `ZeroDivisionError`.
    - [ ] Es wird 0 zurückgegeben.
    - [ ] Der Nenner wird automatisch auf 1 gesetzt.

```