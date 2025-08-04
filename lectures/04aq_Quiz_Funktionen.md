## Funktionen

```{quizdown}
	---
	shuffleQuestions: true
	shuffleAnswers: true
	---

    ### Wozu dienen Funktionen in Python?
    - [x] Um wiederverwendbaren Code zu strukturieren  
    - [x] Um Programme übersichtlicher zu machen  
    - [ ] Um den Code schneller zu machen  
    - [ ] Um Datenbanken zu erstellen

    ### Wie beginnt eine Funktionsdefinition in Python?
    - [x] Mit dem Schlüsselwort `def`  
    - [ ] Mit `function`  
    - [ ] Mit `define()`  
    - [ ] Mit `func`

    ### Was passiert, wenn der Funktionskörper nicht richtig eingerückt ist?
    - [x] Es gibt einen Syntaxfehler  
    - [ ] Die Funktion wird ignoriert  
    - [ ] Die Funktion wird als globale Funktion gespeichert  
    - [ ] Python rückt den Code automatisch ein

    ### Was macht `return` in einer Funktion?
    - [x] Beendet die Funktion und gibt einen Wert zurück  
    - [ ] Gibt automatisch alle Argumente aus  
    - [ ] Wiederholt die Funktion  
    - [ ] Überspringt den Rest des Codes

    ### Was passiert, wenn mehrere Werte mit `return` zurückgegeben werden?
    - [x] Es wird ein Tuple zurückgegeben  
    - [ ] Nur der erste Wert wird zurückgegeben  
    - [ ] Es entsteht ein Fehler  
    - [ ] Alle Werte werden automatisch ausgedruckt

    ### Wo sind Variablen gültig, die innerhalb einer Funktion definiert wurden?
    - [x] Nur innerhalb der Funktion  
    - [ ] Im gesamten Programm  
    - [ ] Innerhalb von Schleifen  
    - [ ] Im gesamten Modul

    ### Was passiert mit einer Variable `x`, die in einer Funktion definiert ist?
    - [x] Sie existiert nur während der Funktionsausführung  
    - [ ] Sie überschreibt globale Variablen automatisch  
    - [ ] Sie wird zu einer globalen Konstante  
    - [ ] Sie bleibt im Speicher bis das Programm beendet ist

    ### Was passiert mit primitiven Datentypen, wenn sie einer Funktion übergeben und dort verändert werden?
    - [x] Die Änderung bleibt lokal innerhalb der Funktion  
    - [ ] Die ursprüngliche Variable wird immer überschrieben  
    - [ ] Python speichert die Änderung automatisch global  
    - [ ] Die Funktion gibt automatisch eine Kopie zurück

    ### Was passiert, wenn man eine Liste in einer Funktion **modifiziert**, aber nicht neu zuweist?
    - [x] Die Änderung wirkt sich auch außerhalb der Funktion aus  
    - [ ] Die Liste wird automatisch kopiert  
    - [ ] Die Funktion erzeugt eine neue Liste  
    - [ ] Es entsteht ein Fehler

    ### Wie verhält sich eine Liste, die in einer Funktion **neu zugewiesen** wird?
    - [x] Die globale Liste bleibt unverändert
    - [ ] Die globale Liste wird überschrieben
    - [ ] Sie kann nicht innerhalb einer Funktion verwendet werden  
    - [ ] Python blockiert diese Zuweisung

    ### Wie läuft ein Python-Programm grundsätzlich ab?
    - [x] Zeile für Zeile, von oben nach unten  
    - [ ] Zufällig, abhängig vom Interpreter  
    - [ ] Erst am Ende, dann rückwärts  
    - [ ] Von Funktionen zu Hauptprogramm

    ### Was passiert, wenn eine Funktion definiert, aber nicht aufgerufen wird?
    - [x] Der Code in der Funktion wird übersprungen  
    - [ ] Die Funktion wird trotzdem automatisch ausgeführt  
    - [ ] Der Code wird nur beim nächsten Neustart ausgeführt  
    - [ ] Python zeigt eine Warnung

    ### Was passiert beim Funktionsaufruf?
    - [x] Der Funktionscode wird an dieser Stelle ausgeführt  
    - [ ] Nur die Rückgabe wird berechnet  
    - [ ] Nur die letzte Zeile der Funktion wird ausgeführt  
    - [ ] Python pausiert das Hauptprogramm

    ### Was ist eine rekursive Funktion?
    - [x] Eine Funktion, die sich selbst aufruft
    - [ ] Eine Funktion, die nur einmal aufgerufen werden darf
    - [ ] Eine Funktion ohne Parameter
    - [ ] Eine spezielle Schleifenfunktion in Python

    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    def rekursive_funktion():
        rekursive_funktion()
    ```
    - [x] Es fehlt die Abbruchbedingung, dadurch entsteht eine Endlosschleife
    - [ ] Der Funktionsname ist ungültig
    - [ ] Python erlaubt keine Selbstaufrufe
    - [ ] Die Funktion muss einen Parameter haben

    ### Sortiere die folgenden Zeilen, um eine einfache rekursive Funktion korrekt zu implementieren:
    ```python
    n = 3
    ```
    1. `def count_down(n):`
    2. `  if n <= 0:`
    3. `    print("Fertig!")`
    4. `  else:`
    5. `    print(n)`
    6. `    count_down(n - 1)`

```