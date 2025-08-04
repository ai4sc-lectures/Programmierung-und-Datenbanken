
## Verzweigung

```{quizdown}
	---
	shuffleQuestions: true
	shuffleAnswers: true
	---

    ### Was macht eine `if`-Anweisung in Python?
    - [x] Führt einen Block aus, wenn die Bedingung wahr ist  
    - [ ] Wiederholt Code mehrfach  
    - [ ] Beendet das Programm  
    - [ ] Fragt den Nutzer nach einer Eingabe

    ### Welche Syntax ist korrekt für eine `if`-Bedingung in Python?
    - [x] if x > 5:  
    - [ ] if (x > 5)  
    - [ ] if x > 5 then  
    - [ ] if x > 5 {}

    ### Was passiert bei der Bedingung `if not x:` in Python?
    - [x] Der Codeblock wird ausgeführt, wenn `x` als False interpretiert wird  
    - [ ] Der Codeblock wird bei `x == True` ausgeführt  
    - [ ] Die Variable `x` wird gelöscht  
    - [ ] Python erzeugt einen Fehler

    ### Welche dieser Werte gelten in Python als `False`?
    - [x] Leere Liste `[]`  
    - [x] Der Wert `None`  
    - [x] Leerer String `""`  
    - [ ] Die Zahl `1`

    ### Wann wird ein `else`-Block in Python ausgeführt?
    - [x] Wenn die `if`-Bedingung nicht zutrifft  
    - [ ] Wenn die `if`-Bedingung wahr ist  
    - [ ] Immer, wenn ein Fehler auftritt  
    - [ ] Direkt nach dem Start des Programms

    ### Wofür wird `else` häufig verwendet?
    - [x] Um einen alternativen Code auszuführen  
    - [ ] Um Funktionen zu definieren  
    - [ ] Um Variablen zu löschen  
    - [ ] Um Einrückungen zu prüfen

    ### Was ist `elif` in Python?
    - [x] Kurzform für „else if“  
    - [ ] Eine Methode zur String-Verarbeitung  
    - [ ] Ein logischer Operator  
    - [ ] Ein alternativer Schleifentyp

    ### Warum ist `elif` nützlich?
    - [x] Es macht den Code kürzer und übersichtlicher  
    - [ ] Es ersetzt die `while`-Schleife  
    - [ ] Es deaktiviert `else`  
    - [ ] Es zwingt Python zum Neustart

    ### Was macht `isinstance(x, int)`?
    - [x] Prüft, ob `x` vom Typ `int` ist  
    - [ ] Wandelt `x` in einen `int` um  
    - [ ] Löscht die Variable `x`  
    - [ ] Erzeugt eine neue Instanz

    ### Warum ist Typprüfung in Python nützlich?
    - [x] Um Fehler zu vermeiden, z. B. bei Division durch 0  
    - [ ] Weil Python stark typisiert ist  
    - [ ] Um Variablen in Funktionen zu kopieren  
    - [ ] Um Schleifen zu beenden

    ### Sortiere die folgenden Zeilen, um ein korrekt eingerücktes `if-else`-Statement zu erhalten. Geben ist:
    ```python
    a = 3
    b = 5
    ```
    1. `if a < b:`
    2. `  print("a ist kleiner als b")`
    3. `else:`
    4. `  print("a ist größer oder gleich b")`

    ### Sortiere die Zeilen korrekt für eine Funktion mit `if` und `return`:
    1. `  if x > 0:`
    2. `    return "positiv"`
    3. `  else:`
    4. `    return "nicht positiv"`


    ### Bringe die `if-elif-else`-Struktur in korrekte Reihenfolge:
    1. `if note == 1:`
    2. `  print("sehr gut")`
    3. `elif note >= 4:`
    4. `  print("bestanden")`
    5. `else:`
    6. `  print("nicht bestanden")`


    ### Welcher Fehler ist in folgendem Code enthalten?
    ```python
    if x > 5
        print("x ist größer als 5")
    ```
    - [x] Der Doppelpunkt `:` nach der Bedingung fehlt
    - [ ] Die Einrückung ist zu groß
    - [ ] `if` darf nicht mit `>` kombiniert werden
    - [ ] `print` darf nicht in einer `if`-Anweisung stehen


    ### Was stimmt bei diesem Code nicht?
    ```python
    if y == 10:
    print("y ist gleich 10")
    ```
    - [x] Die Zeile mit `print` ist nicht eingerückt
    - [ ] Der Vergleichsoperator `==` ist ungültig
    - [ ] Die `if`-Bedingung darf kein `:` enthalten
    - [ ] Strings müssen in Hochkommas stehen


    ### Wo ist der Fehler in diesem Code?
    ```python
    if x > 5:
        return True
    else
        return False
    ```
    - [x] Nach `else` fehlt ein Doppelpunkt `:`
    - [ ] `return` darf nicht in `if` stehen
    - [ ] Funktionen dürfen kein `if` enthalten
    - [ ] Die Klammern bei `test` sind falsch


    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    if x = 5:
        print("x ist 5")
    ```
    - [x] Es wird `=` (Zuweisung) statt `==` (Vergleich) verwendet
    - [ ] `x` ist kein gültiger Variablenname
    - [ ] Der `print`-Befehl ist veraltet
    - [ ] Zahlen dürfen nicht verglichen werden


```
