## Datenbankentwurf

```{quizdown}
    ---
    shuffleQuestions: true
    shuffleAnswers: true
    ---


    ### Welche Schritte gehören zum klassischen Datenbankentwurf?

    - [x] Anforderungsanalyse, Konzeptioneller Entwurf, Logischer Entwurf
    - [ ] Nur Konzeptioneller und Physikalischer Entwurf
    - [x] Physikalischer Entwurf, Implementation und Test
    - [ ] Nur Implementation und Wartung


    ### Was ist der Hauptunterschied zwischen konzeptionellem und logischem Entwurf?

    - [x] Konzeptioneller Entwurf ist ein Grobentwurf, logischer ein Detailentwurf
    - [ ] Konzeptioneller Entwurf verwendet SQL, logischer nicht
    - [ ] Es gibt keinen Unterschied
    - [ ] Logischer Entwurf kommt vor dem konzeptionellen


    ### Sortiere die Schritte des Datenbankentwurfs in der richtigen Reihenfolge:

    1. Anforderungsanalyse
    2. Konzeptioneller Entwurf
    3. Logischer Entwurf
    4. Physikalischer Entwurf
    5. Implementation und Test


    ### Was kennzeichnet eine Entität in der UML-Notation für ER-Diagramme?

    - [x] Die Anmerkung `<<Entity>>`
    - [ ] Der Name `Entity`
    - [ ] Die Anmerkung `<Table>`
    - [ ] Das spezielles Symbol `ER`
    - [ ] Keine besondere Kennzeichnung


    ### Welche UML-Elemente werden in ER-Diagrammen NICHT verwendet?

    - [x] Methoden und Vererbung
    - [ ] Attribute und Klassen
    - [x] Polymorphismus und Kapselung
    - [ ] Assoziationen


    ### Was bedeutet das Zeichen `>>` in einer Relation?

    - [x] Die Relation wird von links nach rechts gelesen
    - [ ] Die Relation ist bidirektional
    - [ ] Es ist ein Fehler in der Notation
    - [ ] Die Relation wird von rechts nach links gelesen


    ### Was bedeutet die Kardinalität "1 zu 0..*"?

    - [x] Eine Entität kann mit null bis vielen anderen verknüpft sein
    - [ ] Eine Entität muss mit mindestens einer anderen verknüpft sein
    - [ ] Genau eine Verknüpfung ist erlaubt
    - [ ] Die Kardinalität ist ungültig


    ### Bei welcher Kardinalität werden neue Tabellen für Relationen benötigt?

    - [ ] 1 zu 1
    - [ ] 1 zu 0..1
    - [x] 1 zu 0..*
    - [x] 1 zu 1..*


    ### Welcher Fehler steckt in diesem ER-Diagramm-Fragment?
    ```
    Person >>wohnt in>> Ort
    1                    1..*
    ```

    - [x] Die Leserichtung macht bei dieser Kardinalität keinen Sinn
    - [ ] Personen können nicht in Orten wohnen
    - [ ] Die Notation ist völlig falsch
    - [ ] Es fehlen Attribute


    ### Was ist das Ziel der Normalisierung?

    - [x] Redundanzen minimieren
    - [x] Datenintegrität sicherstellen
    - [ ] Abfragen verlangsamen
    - [ ] Mehr Tabellen erstellen


    ### Was verlangt die 1. Normalform (1NF)?

    - [x] Alle Attributwerte sind atomar
    - [ ] Alle Attribute sind Primärschlüssel
    - [x] Keine komplexen Attribute wie Listen
    - [ ] Mindestens drei Tabellen


    ### Welche Normalform wird verletzt, wenn Kundendaten direkt in der Rechnungstabelle gespeichert werden?

    - [ ] 1NF
    - [x] 2NF
    - [ ] 3NF
    - [ ] Keine Verletzung


    ### Sortiere die Normalformen nach ihrer Strenge (von weniger zu mehr streng):

    1. 1NF (Erste Normalform)
    2. 2NF (Zweite Normalform) 
    3. 3NF (Dritte Normalform)
    4. BCNF (Boyce-Codd-Normalform)


    ### Welcher Fehler steckt in diesem Tabellenentwurf?
    ```sql
    CREATE TABLE Kunden (
      id INTEGER,
      name TEXT,
      adressen LIST<TEXT>
    )
    ```

    - [x] Das Attribut `adressen` verletzt die 1NF (nicht atomar)
    - [ ] Der Datentyp INTEGER ist falsch
    - [ ] Es fehlt ein Primärschlüssel
    - [ ] Der Tabellenname ist ungültig


    ### Wie wird eine 1:1-Relation in Tabellen abgebildet?

    - [x] Durch Fremdschlüssel in einer der Tabellen
    - [ ] Durch eine separate Relationstabelle
    - [ ] Durch Duplizierung aller Attribute
    - [ ] Gar nicht, da ungültig


    ### Wann ist ein Fremdschlüssel "Nullable"?

    - [x] Bei Kardinalität 1 zu 0..1
    - [ ] Bei Kardinalität 1 zu 1
    - [x] Wenn die Beziehung optional ist
    - [ ] Niemals


    ### Sortiere diese Schritte zur Normalisierung einer 1:n-Relation:

    1. Neue Relationstabelle erstellen
    2. Fremdschlüssel zu beiden ursprünglichen Tabellen hinzufügen
    3. Primärschlüssel für die Relationstabelle definieren
    4. Kardinalität überprüfen


    ### Welcher SQL-Befehl erstellt eine neue Tabelle?

    - [x] CREATE TABLE
    - [ ] INSERT TABLE
    - [ ] NEW TABLE
    - [ ] MAKE TABLE


    ### Was bewirkt AUTOINCREMENT bei einem Primärschlüssel?

    - [x] Automatische Zuweisung eindeutiger Werte
    - [ ] Automatisches Löschen alter Einträge
    - [x] Erleichtert das Einfügen neuer Datensätze
    - [ ] Verhindert Datenänderungen


    ### Welcher Fehler steckt in diesem SQL-Code?
    ```sql
    CREATE TABLE Points (
      point_id INTEGER PRIMARY KEY,
      x REAL NOT NULL,
      y REAL NOT NULL,
      FOREIGN KEY(x) REFERENCES Lines(line_id)
    )
    ```

    - [x] Ein Attribut (x) kann nicht gleichzeitig Koordinate und Fremdschlüssel sein
    - [ ] REAL ist kein gültiger Datentyp
    - [ ] PRIMARY KEY ist falsch geschrieben
    - [ ] NOT NULL ist überflüssig


    ### Sortiere diese SQL-Befehle in der logischen Reihenfolge für das Erstellen einer Datenbank:

    1. CREATE TABLE für Hauptentitäten
    2. CREATE TABLE für Fremdschlüssel-abhängige Tabellen  
    3. INSERT Grunddaten
    4. INSERT verknüpfte Daten


    ### Mit welchem SQL-Befehl fügt man Daten hinzu?

    - [x] INSERT INTO
    - [ ] ADD DATA
    - [ ] CREATE DATA
    - [ ] PUT INTO


    ### Was passiert bei diesem SQL-Befehl?
    ```sql
    DELETE FROM Points WHERE x > 50;
    ```

    - [x] Alle Punkte mit x-Koordinate > 50 werden gelöscht
    - [ ] Die Tabelle Points wird gelöscht
    - [ ] Nur der erste gefundene Punkt wird gelöscht
    - [ ] Es ist ein Syntaxfehler


    ### Welcher Fehler steckt in diesem INSERT-Statement?
    ```sql
    INSERT INTO Lines VALUES(1, 99, 100);
    ```
    *Angenommen, die Punkte mit ID 99 und 100 existieren nicht*

    - [x] Fremdschlüssel-Constraint wird verletzt
    - [ ] Zu viele Werte angegeben
    - [ ] INTEGER ist kein gültiger Datentyp
    - [ ] INSERT ist falsch geschrieben

    ### Sortiere diese Schritte zum sicheren Löschen von Daten:

    1. Backup der Tabelle erstellen
    2. DELETE-Statement mit WHERE-Bedingung testen
    3. Tatsächliches Löschen durchführen  
    4. Ergebnis überprüfen

    ### Mit welchem Befehl benennt man eine Tabelle um?

    - [x] ALTER TABLE ... RENAME TO
    - [ ] CHANGE TABLE NAME
    - [ ] RENAME TABLE
    - [ ] UPDATE TABLE NAME

    ### Was ist der Unterschied zwischen DELETE FROM table und DROP TABLE?

    - [x] DELETE löscht nur Daten, DROP löscht die ganze Tabelle
    - [ ] Es gibt keinen Unterschied
    - [x] DROP entfernt auch die Tabellenstruktur
    - [ ] DELETE ist schneller

    ### Welcher Fehler steckt in diesem ALTER-Statement?
    ```sql
    ALTER TABLE Points ADD COLUMN z REAL;
    ```
    *Angenommen, es gibt bereits Daten in der Tabelle*

    - [ ] ADD COLUMN ist falsch
    - [ ] REAL ist kein gültiger Datentyp  
    - [x] Es fehlt ein DEFAULT-Wert für bestehende Zeilen
    - [ ] Der Spaltenname z ist zu kurz

    ### Sortiere diese Schritte zur sicheren Tabellenmodifikation:

    1. Backup der Tabelle erstellen
    2. ALTER-Statement planen
    3. Änderung durchführen
    4. Datenintegrität prüfen
```