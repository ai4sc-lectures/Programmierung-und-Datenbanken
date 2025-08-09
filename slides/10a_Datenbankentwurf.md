---
title: "Einführung in Programmierung und Datenbanken"
subtitle: "Relationale Datenbanken"
author: "Jörn Plönnigs"
format: 
  revealjs:
    theme: default
    slide-number: true
    chalkboard: true
    preview-links: auto
    css: custom.css
---

## Übersicht {.smaller}

:::: {.flex}
::: {.flex-item}
**Programmierung und Datenbanken**
- Fehler und Debugging
- Funktionen und Rekursion
- Objektorientierung u. Softwareentwurf
:::

::: {.flex-item}
**Datenhaltung**
- Datenbanken
- Datenbankentwurf  
- Trends und KI
- Modellierung
:::
::::

---

## Relationale Datenbanken

![Midjourney: Relational Database](images/relational-database.jpg){.center}

---

## Relationale Datenbanken - Grundkonzepte

- **Daten sind in Tabellenstrukturen (Schemata) organisiert**
- **Relation** ist hierbei der Begriff für eine Tabelle
- Eine **relationale Datenbank** ist eine Menge von Tabellen

| Spalte 1 | Spalte 2 | Spalte 3 |
|----------|----------|----------|
| Zeile 1  | ...      | ...      |
| Zeile 2  | ...      | ...      |

---

## Relationale Datenbanken - Grundbegriffe

:::: {.flex}
::: {.flex-item}
- Jede Tabelle hat einen **Relationennamen** (Tabellennamen)
- **Relation** steht für die Gesamtheit der Datentupel
- Jedes **Tupel** an Daten besteht aus einer Abfolge von Attributwerten
- Reihenfolge festgelegt durch **Relationenschema**
:::

::: {.flex-item}
| Attribut 1 | Attribut 2 | Attribut 3 |
|------------|------------|------------|
| Attributwert | ... | ... |
| Attributwert | ... | ... |

*Relation = {Tupel}*  
*Relationenschema = (Attribut 1, Attribut 2, Attribut 3)*
:::
::::

---

## Beispiel: OpenData Hanse-Stadt Rostock

**Informationen sind meist über verschiedene Tabellen verteilt** und müssen oft zusammengeführt verarbeitet werden, um daraus anwendbares Wissen abzuleiten.

**Beispiel:** [https://www.opendata-hro.de](https://www.opendata-hro.de)

- Bebauungspläne
- Gemeinden  
- Baustellen
- Bodenrichtwerte
- Adressenliste

---

## Schlüsselattribute

:::: {.flex}
::: {.flex-item}
- Gewisse **Attribute (Spalten)** können als **Schlüssel** markiert werden
- Schlüssel sind meist **eindeutig (unique)** zuordenbar
- Sie existieren in der Tabelle nur **einmal**
- Man kann damit die **Zeile (Tupel) identifizieren**
- Zeilennummern eignen sich nicht (können gelöscht werden)
:::

::: {.flex-item}
**Schlüsseltypen:**
- **Einzelnes Attribut** oder **Menge von Attributen**
- **Unique ID (UID)** - einzelnes Attribut
- **Globally Unique IDs (GUID)** - global eindeutig
- **UUID** (universally unique identifier) - ISO Standard
:::
::::

---

## Schlüsselattribute - Beispiel

| GemeindeID | Name | Einwohner |
|------------|------|-----------|
| 1 | Dummerstorf | 7.329 |
| 2 | Graal-Müritz | 4.278 |
| 3 | Sanitz | 5.831 |

*GemeindeID ist hier der Schlüssel*

---

## Verweise über Schlüssel

:::: {.flex}
::: {.flex-item}
**Gemeinden Tabelle**

| GemeindeID | Name | Einwohner |
|------------|------|-----------|
| 1 | Dummerstorf | 7.329 |
| 2 | Graal-Müritz | 4.278 |
| 3 | Sanitz | 5.831 |

*Primärschlüssel*
:::

::: {.flex-item}
**Bauwerke Tabelle**

| BauwerksID | Bauwerkstyp | GemeindeID |
|------------|-------------|------------|
| 5000 | Tankstelle | 2 |
| 5001 | Hotel | 1 |
| 5002 | Kirche | 2 |

*Primärschlüssel* → *Fremdschlüssel*
:::
::::

---

## Schlüsselkonzepte

- Die **Schlüssel anderer Tabellen** kann man nutzen um auf Tupel in diesen zu verweisen
- Die **eigenen Schlüssel** einer Tabelle heißen **Primärschlüssel** (Primary Key)
- Die **Schlüssel anderer Tabellen** heißen **Fremdschlüssel** (Foreign Key)
- Die **Tabellen werden über Schlüssel in Beziehung gesetzt**

> Der Fremdschlüssel verweist auf den Primärschlüssel in der anderen Tabelle

---

## Die Rolle von Schlüsseln

**Schlüssel definieren sogenannte Integritätsbedingungen:**

:::: {.flex}
::: {.flex-item}
### Primärschlüssel
- Stehen für die **Integrität der einzelnen Tabelle**
- **Lokale Integrität**
:::

::: {.flex-item}
### Fremdschlüssel
- Stehen für die **Integrität des gesamten Datenbanksystems**
- **Globale Integrität**
:::
::::

---

## Hörsaalfrage

:::: {.flex .center}
::: {.flex-item}
![Midjourney: A psychedelic DJ with a question mark for a head](images/question-dj.jpg)
:::

::: {.flex-item}
# FRAGEN?
:::
::::

---

## Custom CSS

```css
/* Custom CSS für bessere Darstellung */
.flex {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
}

.flex-item {
  flex: 1;
}

.center {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.smaller {
  font-size: 0.8em;
}

table {
  font-size: 0.9em;
  margin: 0 auto;
}

blockquote {
  background-color: #f5f5f5;
  border-left: 4px solid #ddd;
  margin: 1rem 0;
  padding: 0.5rem 1rem;
  font-style: italic;
}
```