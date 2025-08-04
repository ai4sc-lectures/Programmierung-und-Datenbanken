## Datenbanken

```{quizdown}
    ---
    shuffleQuestions: true
    shuffleAnswers: true
    ---

    ### Welche Python-Pakete werden zum Laden von CSV-Daten aus dem Internet verwendet?

    - [x] `urllib` und `pandas`
    - [ ] `requests` und `numpy`
    - [ ] `json` und `matplotlib`
    - [ ] `sqlite3` und `os`

    ### Was ist SQL?
    - [x] Eine Sprache zur Abfrage und Manipulation von Datenbanken
    - [ ] Ein Programm zur Datenvisualisierung
    - [ ] Eine Programmiersprache wie Python
    - [ ] Ein Datenformat wie JSON

    ### Was ist SQLite?

    - [x] Eine lokale relationale Datenbank ohne Server
    - [ ] Ein Cloud-Datenbank-Service
    - [ ] Ein NoSQL-Datenbanksystem
    - [ ] Ein Datenvisualisierungstool

    ### Sortiere die folgenden Zeilen für das Speichern einer Pandas-Tabelle in SQLite:

    ```python
    import sqlite3
    import pandas as pd
    ```
    1. `df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})`
    2. `con = sqlite3.connect("test.sqlite")`
    3. `df.to_sql("tabelle", con, if_exists="replace")`

    ### Welcher Fehler steckt in diesem Beispiel?

    ```python
    con = sqlite3.connect("test.sqlite")
    df.to_sql("tabelle", con, if_exists="append")
    ```

    - [ ] `sqlite3` ist nicht importiert
    - [ ] Der Datenbankname ist zu kurz
    - [x] Kein Fehler - der Code ist korrekt
    - [ ] `to_sql` existiert nicht

    ### Was macht der SQL-Befehl `SELECT * FROM baustellen;`?

    - [ ] Löscht alle Daten aus der Tabelle
    - [x] Gibt alle Spalten und Zeilen der Tabelle zurück
    - [ ] Erstellt eine neue Tabelle
    - [ ] Zählt die Zeilen in der Tabelle


    ### Wie führt man einen SQL-Befehl in Python aus?

    - [x] Mit `cur.execute(sql)` nach Erstellung eines Cursors
    - [ ] Mit `con.run(sql)`
    - [ ] Mit `sqlite3.query(sql)`
    - [ ] Mit `pd.sql(sql)`


    ### Sortiere die folgenden Zeilen für eine SQL-Abfrage:

    ```python
    con = sqlite3.connect("test.sqlite")
    ```

    1. `cur = con.cursor()`
    2. `sql = 'SELECT * FROM tabelle;'`
    3. `for row in cur.execute(sql):`
    4. `    print(row)`

    ### Welcher SQL-Befehl filtert Baustellen mit Baubeginn ab 2023?

    - [ ] `FILTER baubeginn >= '2023-01-01'`
    - [x] `WHERE baubeginn >= '2023-01-01 00:00:00+01'`
    - [ ] `IF baubeginn >= '2023-01-01'`
    - [ ] `SELECT baubeginn >= '2023-01-01'`

    ### Wie verknüpft man mehrere Bedingungen in SQL?

    - [x] Mit `AND`, `OR`, `NOT`
    - [ ] Mit `&&`, `||`, `!`
    - [ ] Mit `+`, `-`, `*`
    - [ ] Mit `COMBINE`, `MERGE`, `JOIN`


    ### Welcher Fehler steckt in diesem SQL-Beispiel?

    ```sql
    SELECT * FROM baustellen
    WHERE baubeginn = '2023-01-01' AND bauende = '2024-01-01'
    ```

    - [ ] `AND` ist nicht erlaubt
    - [ ] Datumsformat ist falsch
    - [x] Kein Fehler - der Code ist korrekt
    - [ ] `WHERE` muss am Ende stehen


    ### Was macht die SQL-Funktion `count(*)`?

    - [ ] Summiert alle Werte
    - [x] Zählt die Anzahl der Zeilen
    - [ ] Findet den Maximalwert
    - [ ] Berechnet den Durchschnitt


    ### Welche Aggregatfunktionen gibt es in SQL?

    - [x] `min()`, `max()`, `avg()`, `sum()`, `count()`
    - [ ] `first()`, `last()`, `middle()`
    - [ ] `add()`, `subtract()`, `multiply()`
    - [ ] `top()`, `bottom()`, `center()`


    ### Sortiere die folgenden Teile einer SQL-Aggregationsabfrage:

    1. `SELECT sparte, count(*), avg(baudauer)`
    2. `FROM baustellen`
    3. `GROUP BY sparte`


    ### Was macht `GROUP BY sparte` in einer SQL-Abfrage?

    - [ ] Sortiert nach Sparte
    - [x] Fasst Zeilen mit gleicher Sparte zusammen
    - [ ] Filtert nach Sparte
    - [ ] Löscht doppelte Sparten


    ### Wie sortiert man Ergebnisse in SQL absteigend?

    - [ ] `SORT BY spalte DOWN`
    - [x] `ORDER BY spalte DESC`
    - [ ] `ARRANGE BY spalte REVERSE`
    - [ ] `DESCEND BY spalte`


    ### Was bewirkt `LIMIT 3` in einer SQL-Abfrage?

    - [ ] Begrenzt auf 3 Spalten
    - [x] Gibt maximal 3 Ergebniszeilen zurück
    - [ ] Sortiert die ersten 3 Einträge
    - [ ] Filtert nach Werten kleiner 3


    ### Welcher Fehler steckt in diesem SQL-Beispiel?

    ```sql
    SELECT sparte, count(*)
    FROM baustellen
    ORDER BY count(*)
    GROUP BY sparte
    ```

    - [x] `ORDER BY` muss nach `GROUP BY` stehen
    - [ ] `count(*)` kann nicht sortiert werden
    - [ ] `GROUP BY` ist falsch positioniert
    - [ ] Es fehlt ein `WHERE`


    ### Was macht ein `JOIN` in SQL?

    - [ ] Kombiniert Spalten einer Tabelle
    - [x] Verknüpft Daten aus mehreren Tabellen
    - [ ] Sortiert Tabellendaten
    - [ ] Löscht doppelte Einträge


    ### Warum verwendet man Tabellenpräfixe wie `b.spalte` bei JOINs?

    - [ ] Zur Verschönerung des Codes
    - [x] Zur eindeutigen Identifikation bei gleichnamigen Spalten
    - [ ] Zur Beschleunigung der Abfrage
    - [ ] Zur Fehlerbehandlung


    ### Was macht `DISTINCT` in einer SQL-Abfrage?

    - [ ] Sortiert die Ergebnisse
    - [ ] Begrenzt die Anzahl der Ergebnisse
    - [x] Entfernt doppelte Zeilen aus den Ergebnissen
    - [ ] Verbindet mehrere Tabellen

    ### Was ist der Unterschied zwischen INNER JOIN und LEFT JOIN?
    - [x] INNER JOIN gibt nur übereinstimmende Zeilen zurück, LEFT JOIN alle Zeilen der linken Tabelle
    - [ ] LEFT JOIN gibt nur übereinstimmende Zeilen zurück, INNER JOIN alle Zeilen der linken Tabelle
    - [ ] Es gibt keinen Unterschied, beide sind gleich
    - [ ] INNER JOIN ist schneller als LEFT JOIN


    ### Sortiere die folgenden Teile einer JOIN-Abfrage:

    1. `SELECT b.spalte1, a.spalte2`
    2. `FROM baustellen AS b`
    3. `JOIN adressenliste AS a`
    4. `WHERE b.id = a.id`


    ### Was ist der Unterschied zwischen verschiedenen JOIN-Typen?

    - [x] Sie bestimmen, welche Zeilen bei fehlenden Übereinstimmungen zurückgegeben werden
    - [ ] Sie beeinflussen die Geschwindigkeit der Abfrage
    - [ ] Sie ändern die Sortierung der Ergebnisse
    - [ ] Sie bestimmen die Anzahl der verknüpften Tabellen


    ### Welcher Fehler steckt in diesem JOIN-Beispiel?

    ```sql
    SELECT * FROM baustellen
    NATURAL JOIN adressenliste, gemeinden
    ```

    - [ ] `NATURAL JOIN` existiert nicht
    - [ ] Zu viele Tabellen im JOIN
    - [x] Potentielle Kreuzverknüpfung durch mehrere Tabellen ohne explizite Bedingungen
    - [ ] Falsche Syntax bei `NATURAL JOIN`


```