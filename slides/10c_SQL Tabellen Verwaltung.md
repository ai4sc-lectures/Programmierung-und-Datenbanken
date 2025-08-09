---
title: "Einführung in Programmierung und Datenbanken"
subtitle: "SQL Tabellen Verwaltung"
author: "Joern Ploennigs"
format:
  revealjs:
    theme: default
    transition: slide
    background-transition: fade
    highlight-style: github
    code-block-background: true
    incremental: false
---

## Überblick {background-color="#f0f0f0"}

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Fehler und Debugging**

**Funktionen und Rekursion**
:::

::: {.flex-item style="flex: 1;"}
**Objektorientierung u. Softwareentwurf**

**Datenhaltung**
:::

::: {.flex-item style="flex: 1;"}
**Datenbanken**

**Datenbankentwurf**

**Trends und KI**
:::
:::

**Modellierung Datenbanken**

---

## Tabellen mit SQL anlegen {background-image="url(https://via.placeholder.com/1920x1080/4a90e2/ffffff?text=Construction+plan+of+the+tower+of+babel)" background-size="cover"}

### Midjourney: Construction plan of the tower of babel

---

## Letzter Schritt: Implementierung des ER-Diagrammes {.smaller}

**Abbilden des ER-Modells auf SQL-Befehle zum Erzeugen der Tabellen**

- Erstellen der Tabellen
- Für jedes Attribut jeder Relation einen sinnvollen Datentyp finden
- Festlegen ob Attribute Nullbar oder Nicht Null sind
- Festlegen des Primärschlüssel
- Festlegen von Fremdschlüssel
- Deklarieren zusätzlicher Suchindexe zur Performanceoptimierung
- Definition von Zugriffsrechten

**Um die Tabelle zu erstellen, benötigt man den CREATE TABLE SQL-Befehl.**

*Dieser fügt noch keine Daten ein, sondern erstellt nur ein leeres Grundgerüst.*

---

## DDL - Data Definition Language

**Erlaubt Operationen auf den Definitionen von Datenstrukturen:**

::: {.flex}
::: {.flex-item style="flex: 1;"}
- **CREATE** – Tabellen erzeugen
- **ALTER** – Tabellen verändern
- **DROP** – Tabellen löschen
- **TRUNC** – Daten aber nicht die Tabelle löschen
:::

::: {.flex-item style="flex: 1;"}
**Die möglichen Datenstrukturen sind dabei:**

- **TABLE** – Tabellen zum speichern von Daten
- **VIEW** – Dynamisch generierte Ansichten auf Tabellen
- **MATERIALIZED VIEW** – Tabellen die sich aus anderen Tabellen ableiten
:::
:::

---

## Tabellen erstellen in SQL

**Grundsyntax:**

```sql
CREATE TABLE table_name (
    attribute1_name attribute1_type attribute1_constraints,
    attribute2_name attribute2_type attribute2_constraints,
    …,
    table_constraints
)
```

---

## Datentypen in SQLite vs. Python

| SQLite | Python | Beschreibung |
|--------|--------|--------------|
| Boolean (INTEGER) | bool | Wahrheitswerte |
| INTEGER | int | Ganzzahl |
| REAL | float | Gleitkommazahl |
| NUMERIC | - | Interpretiert beliebige Dateneingaben als Zahl |
| TEXT | str | Text-String, gespeichert in UTF-8 oder UTF-16 |
| BLOB | bytes | Beliebiger Block an Binärdaten |
| NULL | None | Keine Daten |

---

## Beispiel: Tabellen erstellen in SQLite

**Für unser Geometriebeispiel ergeben sich folgende CREATE TABLE Statements:**

```sql
CREATE TABLE Points (
    point_id INTEGER,
    x REAL,
    y REAL
);

CREATE TABLE Lines (
    lines_id INTEGER,
    start INTEGER,
    end INTEGER
);
```

---

## Schlüssel und Constraints in SQL

**Primär- und Sekundärschlüssel werden meistens durch INTEGER-Spalten abgebildet.**

**Der Primärschlüssel jeder Relation muss speziell markiert werden durch den PRIMARY KEY Constraint.**

**Weitere Constraints die beim Einfügen neuer Daten eingehalten werden:**

- **NOT NULL** – Werte dürfen nicht null sein
- **AUTOINCREMENT** – Numerische Primärschlüssel werden automatisch berechnet
- **UNIQUE** – Werte müssen eindeutig sein, keine Dopplungen erlaubt
- **CHECKED** – Zusätzliche logische Bedingung für neue Werte
- **FOREIGN KEY** – Wert eines existierenden Fremdschlüssels

---

## Beispiel: Primärschlüssel, Fremdschlüssel und Constraints

```sql
CREATE TABLE Points (
    point_id INTEGER PRIMARY KEY AUTOINCREMENT,
    x REAL NOT NULL,
    y REAL NOT NULL
);

CREATE TABLE Lines (
    lines_id INTEGER PRIMARY KEY AUTOINCREMENT,
    start INTEGER NOT NULL,
    end INTEGER NOT NULL,
    FOREIGN KEY(start) REFERENCES Points(point_id),
    FOREIGN KEY(end) REFERENCES Points(point_id)
);
```

---

## CREATE TABLE erweiterte Funktionen

**Zusätzliche Optionen:**

- **DEFAULT**: Standardwert für neue Elemente festlegen
- **WITHOUT ROWID**: Tabellen die nicht durchnummeriert werden
- **STRICT**: Tabelle forciert Datentypen strikt

---

## Daten zu Tabellen hinzufügen

**Daten werden in Tabellen mit dem SQL-Befehl INSERT hinzugefügt**

::: {.flex}
::: {.flex-item style="flex: 1;"}
**Daten hinzufügen in der Reihenfolge der Spaltennamen:**

```sql
INSERT INTO Points VALUES(1, 54.083336, 12.108811);
INSERT INTO Points VALUES(2, 12.094167, 54.075211);
INSERT INTO Lines VALUES(1, 1, 2);
```
:::

::: {.flex-item style="flex: 1;"}
**oder mit expliziten Spaltennamen:**

```sql
INSERT INTO Points(x, y) VALUES(54.083336, 12.108811);
INSERT INTO Points(x, y) VALUES(12.094167, 54.075211);
INSERT INTO Lines(start, end) VALUES(1, 2);
```
:::
:::

---

## Tabelle aus bestehenden Daten erstellen

```sql
CREATE TABLE tablename AS
SELECT … FROM … WHERE …
```

**Hat keinen Primärschlüssel, kann nur nachträglich definiert werden**

---

## ALTER TABLE - Statement

**Ändern von Tabellen und Spaltennamen, Hinzufügen und Löschen von Spalten**

```sql
ALTER TABLE tablename TO newtablename
```

**Beispiel:**
```sql
ALTER TABLE Points RENAME TO Punkte
```

---

## ALTER TABLE - Beispiel

**Besitzer zu Kunde umbenennen, Spalte für Kontonummer hinzufügen**

```sql
ALTER TABLE tablename ADD COLUMN column_name column_type
```

**Beispiel:**
```sql
ALTER TABLE PolygonType ADD COLUMN maxPoints INTEGER
```

---

## DROP TABLE - Statement

**Das Löschen von kompletten Tabellen.**

```sql
DROP TABLE tablename
```

**Beispiel:**
```sql
DROP TABLE Points
```

---

## Hörsaalfrage {background-image="url(https://via.placeholder.com/1920x1080/ff6b6b/ffffff?text=A+psychedelic+DJ+with+a+question+mark+for+a+head)" background-size="cover"}

### FRAGEN?

**Midjourney: A psychedelic DJ with a question mark for a head**