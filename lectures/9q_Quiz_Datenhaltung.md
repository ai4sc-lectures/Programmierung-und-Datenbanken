## Datenhaltung

```{quizdown}
    ---
    shuffleQuestions: true
    shuffleAnswers: true
    ---

    ### Warum werden in Programmen häufig Dateien verwendet?
    - [x] Um Daten dauerhaft zu speichern
    - [ ] Um den Code schneller auszuführen
    - [ ] Um Variablen automatisch zu initialisieren
    - [ ] Um grafische Oberflächen zu erstellen

    ### Wo befinden sich Dateien in einem Computer?
    - [x] In Verzeichnissen (Ordnern)
    - [ ] Im RAM
    - [ ] In der CPU
    - [ ] Nur in der Cloud

    ### Welche der folgenden Aussagen zum Umgang mit Dateien in Python ist korrekt?
    - [x] Man sollte Dateien nach dem Öffnen immer schließen oder `with` verwenden.
    - [ ] Dateien können ohne Pfadangabe nur aus dem Internet geladen werden.
    - [ ] Es gibt keine Möglichkeit, Dateien zeilenweise zu lesen.
    - [ ] Python unterstützt keinen Schreibmodus.

    ### Was macht der folgende Code?
    ```python
    with open("notizen.txt", "r") as f:
        zeilen = f.readlines()
    ```
    - [x] Er liest alle Zeilen der Datei `notizen.txt` in eine Liste ein.
    - [ ] Er schreibt alle Zeilen in die Datei.
    - [ ] Er löscht die Datei.
    - [ ] Er gibt jede Zeile sofort auf dem Bildschirm aus.

    ### Was bewirkt die Funktion `open("datei.txt", "r")` in Python?
    - [x] Sie öffnet die Datei `datei.txt` zum Lesen.
    - [ ] Sie erstellt eine neue Datei mit dem Namen `datei.txt`.
    - [ ] Sie öffnet die Datei `datei.txt` zum Schreiben.
    - [ ] Sie löscht den Inhalt der Datei `datei.txt`.

    ### Was passiert, wenn die Datei nicht existiert und `open("nichtda.txt", "r")` ausgeführt wird?
    - [x] Es wird eine Fehlermeldung `FileNotFoundError` ausgelöst.
    - [ ] Eine leere Datei wird erstellt.
    - [ ] Das Programm läuft normal weiter.
    - [ ] Die Datei wird automatisch im Schreibmodus geöffnet.

    ### Welcher Fehler steckt in diesem Beispiel?
    ```python
    file = open("daten.txt", "r"
    data = file.read()
    ```
    - [x] Eine schließende Klammer fehlt in der `open`-Funktion.
    - [ ] Der Dateiname ist ungültig.
    - [ ] `read()` kann nur auf binäre Dateien angewendet werden.
    - [ ] `open` ist kein gültiger Befehl.


    ### Welcher Modus öffnet eine Datei zum Schreiben und überschreibt den Inhalt?
    - [x] "w"
    - [ ] "r"
    - [ ] "a"
    - [ ] "x"

    ### Was passiert bei folgendem Code, wenn die Datei bereits existiert?
    ```python
    with open("ausgabe.txt", "w") as f:
        f.write("Hallo Welt")
    ```
    - [x] Der alte Inhalt der Datei wird gelöscht und überschrieben.
    - [ ] Es wird ein Fehler ausgelöst.
    - [ ] Der neue Text wird an das Ende der Datei angehängt.
    - [ ] Die Datei wird nicht verändert.

    ### Wie prüft man in Python, ob eine Datei existiert?
    - [x] Mit `os.path.exists("datei.txt")`
    - [ ] Mit `open("datei.txt")`
    - [ ] Mit `exists("datei.txt")`
    - [ ] Mit `os.exist("datei.txt")`

    ### Was ist notwendig, um `os.path.exists` nutzen zu können?
    - [x] Das Modul `os` muss importiert werden.
    - [ ] Das Modul `datetime` muss importiert werden.
    - [ ] Es braucht keine Imports.
    - [ ] `os.path.exists` ist eine eingebaute Funktion.

    ### Welche Funktion listet alle Dateien in einem Verzeichnis auf?
    - [x] `os.listdir()`
    - [ ] `os.showfiles()`
    - [ ] `os.files()`
    - [ ] `list.files()`

    ### Wie kann man mit Python nur `.txt`-Dateien aus einem Ordner auflisten?
    - [x] Mit einer Kombination aus `os.listdir()` und einer Filterung per Schleife
    - [ ] Nur mit `os.gettxtfiles()`
    - [ ] Automatisch mit `open("*.txt")`
    - [ ] Mit `file.list("*.txt")`

    ### Wie löscht man eine Datei in Python?
    - [x] Mit `os.remove("datei.txt")`
    - [ ] Mit `os.delete("datei.txt")`
    - [ ] Mit `os.clear("datei.txt")`
    - [ ] Mit `os.erase("datei.txt")`

    ### Wie lädt man eine JSON-Datei in Python?
    - [x] Mit `json.load(open("datei.json"))`
    - [ ] Mit `json.read("datei.json")`
    - [ ] Mit `json.load("datei.json")`
    - [ ] Mit `json.open("datei.json")`

    ### Was ist der Zweck von `json.dump()`?
    - [x] Um Python-Objekte in eine JSON-Datei zu schreiben.
    - [ ] Um JSON-Daten zu lesen.
    - [ ] Um JSON-Daten zu löschen.
    - [ ] Um JSON-Daten zu formatieren.

    ### Was ist JSON?
    - [x] Ein textbasiertes Format zum Austausch von Daten.
    - [ ] Ein binäres Dateiformat.
    - [ ] Ein Bildformat

    ### Was sind textbasierte Dateien?
    - [ ] *.png
    - [x] *.csv
    - [x] *.xml
    - [x] *.json
    - [ ] *.jpg

    ### Was ist der Unterschied zwischen JSON und XML?
    - [x] JSON ist einfacher und kompakter, XML ist umfangreicher und flexibler.
    - [ ] JSON ist älter als XML.
    - [ ] XML ist einfacher zu lesen als JSON.
    - [ ] JSON kann keine verschachtelten Strukturen darstellen.

```