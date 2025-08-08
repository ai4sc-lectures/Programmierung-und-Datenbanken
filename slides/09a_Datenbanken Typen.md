---
title: "Einführung in Programmierung und Datenbanken"
subtitle: "Datenbanken Typen"
author: "joern ploennigs"
format: 
  revealjs:
    theme: default
    transition: slide
    background-transition: fade
    incremental: false
---

# Datenbanken {background-image="https://via.placeholder.com/800x600/2C3E50/FFFFFF?text=Data+Bank"}

## Zielstellung {.smaller}

::: {.flex}
::: {.flex-item}
### Lernziele
- Was sind Datenbanken?
- Warum relationale Datenbanken?
- Wie werden Daten strukturiert in diesen gespeichert?
- Wie greifen wir auf diese zu?
:::
:::

## Datenbanken Definition {.smaller}

- Unter einer **Datenbank (DB)** versteht man die logisch zusammengehörenden Daten, die von einem **DBMS (Datenbankmanagementsystem)** verwaltet werden
- Datenbank und Datenbankmanagementsystem zusammen bezeichnet man als **Datenbanksystem**
- Zur Datenbank gehören neben den reinen 'Nutzdaten' auch die für die Verwaltung vom Datenbankmanagementsystem angelegten Objekte (beispielsweise Indizes und Logdateien)

::: {.notes}
Definition nach DB Engines: https://db-engines.com/de/article/Datenbank
:::

## Warum bringen wir Geld „auf die Bank"? {background-image="https://via.placeholder.com/400x300/34495E/FFFFFF?text=Bank+Safe"}

::: {.flex}
::: {.flex-item}
- Zentrale und langfristige Aufbewahrung
- Sicherung vor Verlusten
- Effizienz durch spezielles Dienstleistungsangebot (Daueraufträge, Portfolio, …)
- Übersicht behalten
- Vernetzung mit dem globalen Finanznetzwerk
:::
:::

## Warum bringen wir Daten auf die „Bank"? {.smaller}

- **Effizienter** speichern und laden von Daten durch verschiedenen Clients (Webserver, Geräte, etc.)
- **Verwaltung** von sehr (sehr) großen Datenmengen (Skalierbarkeit)
- **Organisation** der Daten in vorgegebene Datenstrukturen (Normalisierung)
- **Langfristiges** speichern der Daten (Persistierung)
- **Schnelles** suchen der Daten durch Indexierung
- **Abgesicherte** Prozesse zum Ändern der Daten (Transaktionen)
- **Nachvollziehbares** Verändern von Daten durch Transaktions-Logs
- **Automatische** Datenanalyse (OLAP)

## Grundkonzepte Dateien

::: {.flex}
::: {.flex-item style="flex: 1;"}
### Struktur
Jede Anwendung strukturiert die Daten entsprechend der darin vorkommenden Datenarten (Format, Struktur …).

### Dateisystem
Jede Anwendung legt die Daten entsprechend seiner Anforderungen (Zugriff, Endung, Ort …) ab.
:::

::: {.flex-item style="flex: 1;"}
```
Datensatz 1    Datensatz 2    Datensatz 3
     ↓              ↓              ↓
Anwendung 1    Anwendung 2    Anwendung 3
```
:::
:::

## Grundkonzepte Datenbanken

::: {.flex}
::: {.flex-item style="flex: 1;"}
### Struktur
Alle Anwendung nutzen die gleiche Struktur die in der Datenbank modelliert wurde

### Dateisystem
Alle Anwendungen greifen auf die gleichen Daten zu. Zugriffe werden durch Transaktionen synchronisiert und protokolliert.
:::

::: {.flex-item style="flex: 1;"}
```
    Anwendung 1
         ↓
    Anwendung 2  →  DBMS  →  Datenbank
         ↓              ↘
    Anwendung 3         Datenbanksystem (DBS)
```
:::
:::

## Die Codd'schen Regeln (Codd, 1985, 1990) {.smaller}

- **Integration**: einheitliche, nichtredundante Datenverwaltung
- **Operationen**: Speichern, Suchen, Ändern
- **Katalog**: Zugriffe auf Datenbankbeschreibungen im Data Dictionary
- **Benutzersichten**: Jeder Nutzer sieht die Daten die er sehen darf in der Art wie er sie sehen möchte
- **Integritätssicherung**: Korrektheit des Datenbankinhalts
- **Datenschutz**: Ausschluss unauthorisierter Zugriffe, nur berechtigte Nutzer
- **Transaktionen**: mehrere DB-Operationen als Funktionseinheit (ganz oder gar nicht)
- **Synchronisation**: parallele Transaktionen koordinieren
- **Datensicherung**: Wiederherstellung von Daten nach Systemfehlern

::: {.notes}
Details: https://www.w3resource.com/sql/sql-basic/codd-12-rule-relation.php
:::

## Datenbanken Typen - Übersicht

::: {.flex}
::: {.flex-item style="flex: 1;"}
### Datenbanken
- **Relationale DB**: 71.9 %
- **NoSQL DB**: 25.2 %
  - Dokument DB: 10.4 %
  - Key-Value & Wide Column: 8.6 %
  - Suchmaschinen: 4.4 %
  - Graph DB: 1.8 %
- **Andere**: 2.9 %
:::

::: {.flex-item style="flex: 1;"}
![Verteilung der Datenbanktypen](https://via.placeholder.com/400x300/3498DB/FFFFFF?text=DB+Types+Chart)
:::
:::

::: {.notes}
Verbreitung nach DB Engines: https://db-engines.com/de/ranking_categories
:::

## Relationale Datenbanken {.smaller}

- **RDBMS** werden bereits seit Anfang der 1980er Jahre verwendet und basieren auf dem relationalen (=tabellenorientierten) Datenmodell
- Das Schema einer Tabelle (=Relationenschema) ist definiert durch den Tabellennamen und eine fixe Anzahl von Attributen (=Spalten) mit entsprechenden Datentypen
- Da Daten in Tabellen organisiert werden, sind sie stark strukturiert mit einer durch die Tabelle definierten Struktur (Normalisierung)
- Die Standardsprache zum Aufbau/Änderung/Löschen ist **SQL**

### Populärste Systeme
Oracle | MySQL | Microsoft SQL Server | PostgreSQL | IBM Db2

::: {.notes}
Definition nach DB Engines: https://db-engines.com/de/article/relationale+Datenbanken
:::

## NoSQL Datenbanken {.smaller}

- **NoSQL** Datenbankmanagementsysteme sind Datenbanken die kein relationales (=tabellenorientierten) Datenmodell verwenden und damit in der Regel auch kein SQL unterstützen
- Sie finden seit etwa **2009** zunehmend Verbreitung
- **Hauptgründe**:
  - Hohe Anforderungen an Skalierbarkeit
  - Fehlertoleranz moderner Web-Applikationen
  - Big Data Szenarien
  - Daten sind oft nur semi-strukturiert (lassen sich nicht in ein Schema pressen)

::: {.notes}
Definition nach DB Engines: https://db-engines.com/de/article/NoSQL
:::

## Dokumentenorientierte Datenbanken {.smaller}

**Document Stores** zeichnen sich durch eine **schemafreie** Organisation der Daten aus:

- Datensätze haben keine einheitliche Struktur
- Die Typen der Werte einzelner Spalten können pro Datensatz unterschiedlich sein
- Spalten können mehr als einen Wert haben (Arrays)
- Datensätze können eine verschachtelte Struktur haben
- Zur Darstellung der „Dokumente" wird meist **JSON** verwendet

### Populärste Systeme
MongoDB | Amazon DynamoDB | Databricks | Azure Cosmos DB | Couchbase

::: {.notes}
Definition nach DB Engines: https://db-engines.com/de/article/Document+Stores
:::

## Key-Value Datenbanken {.smaller}

- **Key-Value Stores** sind die wohl einfachste Form von Datenbankmanagementsystemen
- Sie können lediglich Paare von Schlüsseln und Werten abspeichern, sowie die Werte anhand des Schlüssels wieder zurückliefern
- Damit ähneln sie dem **dict** in Python
- Diese Einfachheit macht sie attraktiv für:
  - Ressourcenbegrenzte Systeme wie embedded PCs
  - Entwicklung von Web-Interfaces

### Populärste Systeme
Redis | Amazon DynamoDB | Azure Cosmos DB | Memcached | Hazelcast

::: {.notes}
Definition nach DB Engines: https://db-engines.com/de/article/Key-Value+Stores
:::

## Suchmaschinen Datenbanken {.smaller}

**Suchmaschinen** sind NoSQL DBMS spezialisiert auf die Suche nach Dateninhalten wie Text:

### Features
- Unterstützung komplexer Suchbegriffe
- Volltextsuche
- Stemming (Stammformreduktion eines Wortes)
- Ergebnisreihung
- Gruppierung von Suchergebnissen
- Verteilte Suche für hohe Skalierbarkeit

### Populärste Systeme
Elasticsearch | Splunk | Solr | OpenSearch | MarkLogic

::: {.notes}
Definition nach DB Engines: https://db-engines.com/de/article/Suchmaschinen
:::

## Graphdatenbanken {.smaller}

- **Graph DBMS** stellen Datensätze in Form von **Knoten (Nodes)** und **Beziehungen (Edges)** zueinander dar
- Sie ermöglichen insbesondere die **Modellierung von Verbindungen**
- Ideal für Netzwerkanalysen, soziale Netzwerke, Empfehlungssysteme

### Populärste Systeme
Neo4j | Microsoft Azure Cosmos DB | Virtuoso | IBM KITT

::: {.notes}
Definition nach DB Engines: https://db-engines.com/de/article/Graph+DBMS
:::

## Datenbanken Typen in der Vorlesung {.smaller}

::: {.flex}
::: {.flex-item style="flex: 1;"}
### Fokus auf:
**Relationale DB** (71.9%)
- Einfach zu benutzen
- Meist verbreitet
- Solide Grundlage

**Key-Value DB** 
- Einfache Konzepte
- Praktische Übungen
:::

::: {.flex-item style="flex: 1;"}
### Warum diese Auswahl?
- **Lernfreundlich**: Klare Strukturen
- **Praxisrelevant**: Weiteste Verbreitung
- **Fundament**: Basis für Verständnis anderer Typen
:::
:::

::: {.notes}
Verbreitung nach DB Engines: https://db-engines.com/de/ranking_categories
:::

## Datenbanken in Python {.smaller}

::: {.flex}
::: {.flex-item style="flex: 1;"}
### Allgemein
- Zugriff über jeweils passende Bibliothek der Datenbank
- Oracle, Redis, MongoDB, etc.

### In Replit
- Mitgeliefert: Key-Value Store
- Datenzugriff wie Python Dictionary
:::

::: {.flex-item style="flex: 1;"}
### Code Beispiel
```python
from replit import db

# Daten speichern
db["entry"] = 5

# Daten abrufen
value = db["entry"]
print(value)  # Output: 5
```
:::
:::

## Fragen? {background-image="https://via.placeholder.com/800x600/E74C3C/FFFFFF?text=Questions?"}

::: {.r-fit-text}
**Hörsaalfrage**
:::

---

## Ende

Vielen Dank für Ihre Aufmerksamkeit!