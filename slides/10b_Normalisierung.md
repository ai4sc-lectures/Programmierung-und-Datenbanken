---
title: "Einführung in Programmierung und Datenbanken"
subtitle: "Normalisierung"
author: "Jörn Plönnigs"
format:
  revealjs:
    theme: default
    slide-number: true
    chalkboard: true
    preview-links: auto
    css: styles.css
---

## Programmierung und Datenbanken {.center}

::: {.flex}
::: {.flex-item}
- Fehler und Debugging
- Objektorientierung u. Softwareentwurf
- Datenhaltung
:::
::: {.flex-item}
- Datenbanken
- Datenbankentwurf
- Trends und KI
:::
:::

::: {.flex}
::: {.flex-item}
- Funktionen und Rekursion
- Modellierung
:::
::: {.flex-item}
- Datenbanken
:::
:::

## Normalisierung {.center}

![Construction plan of the tower of babel](https://via.placeholder.com/600x400/4A90E2/FFFFFF?text=Construction+Plan+of+Tower+of+Babel)

*Midjourney: Construction plan of the tower of babel*

## Hörsaalfrage {.center}

### Wie modellieren wir einen Punkt, eine Linie und ein Polygon?

## Konzeptionelles Modell

Es gibt drei Entitätstypen:

- **Punkt:** Besitzt die Attribute x,y-Koordinate, Datentyp float
- **Linie:** Startet und endet an jeweils genau einem Punkt
- **Polygon:** Umfasst mehrere (mind. 3) Punkte und hat einen Untertyp (Dreieck, Viereck, etc.)
- **Für alle drei Entitäten** brauchen wir einen Primärschlüssel. Numerische Indexe sind mit am effizientesten

## Vom Konzeptionellem Modell zum Logischen Modell

- Unterschiedliche DBMS bieten unterschiedliche Datentypen
- Komplexe Attribute (Listen, Dictionary) können nicht direkt abgespeichert werden
- Relationen mit Multiplizitäten >1 können nicht in einer Tabelle mit der Entität abgespeichert werden
- Redundante Daten (z.B. Polygontyp oder Adressen) mit immer den gleichen Werten kosten unnötig Speicher und sind schlecht zu pflegen (Aktualisierung an vielen Stellen)
- Diese Beschränkungen führen dazu dass Konzeptionelle Datenmodelle oft nicht direkt in einer Datenbank abbildbar sind

::: {.notes}
Unterstützte Datenbanken in Dbeaver: https://dbeaver.io/
:::

## Normalisierung

Die Normalisierung ist ein wichtiger Schritt im Prozess der Abbildung eines Konzeptionellen Datenmodells auf ein Logisches und Physikalisches Datenmodell. Sie hat den Zweck, Redundanzen (mehrfaches Festhalten des gleichen Sachverhalts) zu minimieren, indem:

- komplexe Attribute in neue Tabellen ausgelagert werden
- Relationen mit hoher Kardinalität in neue Tabellen ausgelagert werden
- Redundante Daten (z.B. Polygontyp) in neue Tabellen ausgelagert werden

## Normalformen

Verschiedene Normalformen mit fortschreitend strengeren Bedingungen an das Datenbankschema:

- **1. Normalform:** Alle Attributwerte sind atomar (nicht komplex)
- **2. Normalform:** Nicht-Schlüssel Attribute sind von allen Primärschlüsseln voll abhängig
- **3. Normalform:** Nicht-Schlüssel Attribute sind nur von Primärschlüssel abhängig
- **Boyce-Codd-Normalform:** Alle Attribute von denen Attribute abhängen sind Schlüssel
- **4. Normalform:** Es gibt nur noch triviale mehrwertige Abhängigkeiten
- **5. Normalform:** Es gibt keine mehrwertigen Abhängigkeiten, die voneinander abhängig sind

Dies sorgt für sehr viele, sehr stark vereinfachten Tabellen, die wieder zu größeren Relationen zusammengesetzt werden können.

**Meistens sind nur die ersten drei Normalformen im Datenbank-Alltag relevant.**

## Erste Normalform

- **Beispiel:** Erste Normalform verletzt
- **Fehler:** List<Punkt> als Attribut statt Relation

```sql
-- Falsch: Komplexe Attribute
CREATE TABLE Polygon (
    id INT PRIMARY KEY,
    punkte LIST<Punkt>  -- Verletzt 1NF
);

-- Richtig: Atomare Attribute
CREATE TABLE Polygon (
    id INT PRIMARY KEY
);

CREATE TABLE PolygonPunkte (
    polygon_id INT,
    punkt_id INT,
    FOREIGN KEY (polygon_id) REFERENCES Polygon(id),
    FOREIGN KEY (punkt_id) REFERENCES Punkt(id)
);
```

## Zweite Normalform

- **Beispiel:** Zweite Normalform verletzt
- **Fehler:** Punkt nicht ausgelagert

```sql
-- Falsch: Nicht voll abhängig vom Primärschlüssel
CREATE TABLE Linie (
    id INT PRIMARY KEY,
    start_x FLOAT,
    start_y FLOAT,
    end_x FLOAT,
    end_y FLOAT
);

-- Richtig: Punkte ausgelagert
CREATE TABLE Punkt (
    id INT PRIMARY KEY,
    x FLOAT,
    y FLOAT
);

CREATE TABLE Linie (
    id INT PRIMARY KEY,
    start_punkt_id INT NOT NULL,
    end_punkt_id INT NOT NULL,
    FOREIGN KEY (start_punkt_id) REFERENCES Punkt(id),
    FOREIGN KEY (end_punkt_id) REFERENCES Punkt(id)
);
```

## Dritte Normalform

- **Beispiel:** Dritte Normalform verletzt
- **Fehler:** PolygonTyp von Polygon abhängig

```sql
-- Falsch: Transitive Abhängigkeit
CREATE TABLE Polygon (
    id INT PRIMARY KEY,
    typ_name VARCHAR(50),
    typ_beschreibung VARCHAR(200)
);

-- Richtig: PolygonTyp ausgelagert
CREATE TABLE PolygonTyp (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    beschreibung VARCHAR(200)
);

CREATE TABLE Polygon (
    id INT PRIMARY KEY,
    typ_id INT,
    FOREIGN KEY (typ_id) REFERENCES PolygonTyp(id)
);
```

## Kardinalitäten (Multiplizitäten)

::: {.flex}
::: {.flex-item}
Kardinalitäten werden unterschiedlich abgebildet:

- **1 zu 1:** Relation wird mit Fremdschlüssel in der Entität abgebildet. Der Fremdschlüssel darf NICHT NULL
- **1 zu 0..1:** Relation wird mit Fremdschlüssel in der Entität abgebildet. Der Fremdschlüssel darf NULL
:::
::: {.flex-item}
- **1 zu 0...*:** Relation wird als neue Entität mit Fremdschlüssels abgebildet
- **1 zu 1...*:** Relation wird als neue Entität mit Fremdschlüssels abgebildet. Mindestens ein Eintrag sollte vorhanden sein
:::
:::

## Hörsaalfrage {.center}

### Welche Tabellen brauchen wir für unser Geometriebeispiel?

## Konzeptionelles Modell - Lösung

Durch Normalisierung erhalten wir **fünf Tabellen:**

- **Punkt:** Besitzt die Attribute x,y-Koordinate, Datentyp float
- **Linie:** Start- und End-Punkt sind Fremdschlüssel die NichtNull sind da eine 1-1-Relation vorliegt
- **Polygon:** Eine Tabelle mit PK und FK auf den PolynomTypen, die Punkte sind extern
- **PolygonTyp:** Eine Tabelle der redundanten Polygontypen mit Name (Dreieck, Viereck, etc.) und PK
- **PolygonPunkte:** Eine Tabelle die für jeden Polygon FK, die zugehörigen Punkte FK listet, da eine 3..* Relation vorlag
- **Für alle fünf** brauchen wir einen Primärschlüssel (Immer Not Null)

## Fragen? {.center}

![A psychedelic DJ with a question mark for a head](https://via.placeholder.com/400x400/FF6B6B/FFFFFF?text=DJ+?)

*Midjourney: A psychedelic DJ with a question mark for a head*

---

## CSS Styling

```css
/* styles.css */
.flex {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 2rem;
}

.flex-item {
  flex: 1;
}

.center {
  text-align: center;
}

.reveal .slides section .fragment.highlight-current-blue {
  opacity: 1;
  visibility: inherit;
}

.reveal .slides section .fragment.highlight-current-blue.current-fragment {
  background: #4A90E2;
  color: white;
  padding: 0.2em 0.4em;
  border-radius: 0.2em;
}
```