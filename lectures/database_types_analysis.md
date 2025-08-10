# Datenbanktypen - Ausführliche Analyse

## Grundlagen und Definitionen

### Was sind Datenbanken und Datenbanksysteme?

Eine **Datenbank (DB)** umfasst die logisch zusammengehörenden Daten, die von einem Datenbankmanagementsystem (DBMS) verwaltet werden. Das **Datenbanksystem** bezeichnet die Kombination aus Datenbank und DBMS.

Zur Datenbank gehören nicht nur die eigentlichen Nutzdaten, sondern auch alle verwaltungstechnischen Objekte wie Indizes für schnellere Suchen und Logdateien zur Nachverfolgung von Änderungen.

**Beispiel für Bauingenieure:** In einem Bauprojekt könnte eine Datenbank alle Projektdaten enthalten - von Materiallisten über Kostenschätzungen bis hin zu Zeitplänen. Das DBMS würde sicherstellen, dass verschiedene Teammitglieder gleichzeitig auf diese Daten zugreifen können, ohne dass Konflikte entstehen.

## Warum Datenbanken verwenden?

### Die Bank-Analogie

Genau wie wir unser Geld zur Bank bringen, bringen wir unsere Daten in Datenbanken - aus ähnlichen Gründen:

**Finanzielle Vorteile einer Bank:**
- Zentrale und langfristige Aufbewahrung
- Sicherung vor Verlusten
- Effizienz durch spezielles Dienstleistungsangebot
- Übersicht behalten
- Vernetzung mit dem globalen Finanznetzwerk

**Entsprechende Vorteile von Datenbanken:**
- **Effizienter Zugriff:** Verschiedene Clients (Webserver, mobile Apps, Desktop-Anwendungen) können gleichzeitig auf dieselben Daten zugreifen
- **Skalierbarkeit:** Verwaltung sehr großer Datenmengen wird möglich
- **Organisation:** Daten werden in vorgegebene Strukturen organisiert (Normalisierung)
- **Persistierung:** Langfristige, dauerhafte Speicherung der Daten
- **Schnelle Suche:** Indexierung ermöglicht rasches Auffinden spezifischer Daten
- **Transaktionssicherheit:** Abgesicherte Prozesse zum Ändern der Daten
- **Nachvollziehbarkeit:** Transaktions-Logs dokumentieren alle Änderungen
- **Automatische Analyse:** OLAP-Funktionen für Datenanalysen

**Beispiel für Umweltingenieure:** Bei der Überwachung von Gewässerqualität fallen kontinuierlich Messdaten von verschiedenen Sensoren an. Eine Datenbank ermöglicht es, diese Daten zentral zu sammeln, verschiedenen Behörden und Forschungseinrichtungen Zugriff zu gewähren und automatisch Trends oder kritische Werte zu erkennen.

## Konzeptvergleich: Dateien vs. Datenbanken

### Dateibasierte Ansätze
Bei traditionellen dateibasierten Systemen strukturiert jede Anwendung ihre Daten individuell entsprechend der jeweiligen Anforderungen. Jede Anwendung legt ihre Daten separat ab, was zu Redundanzen und Inkonsistenzen führen kann.

### Datenbankbasierte Ansätze  
Bei Datenbanken nutzen alle Anwendungen dieselbe, einheitlich modellierte Datenstruktur. Der Zugriff wird durch das DBMS koordiniert, Transaktionen werden synchronisiert und alle Operationen protokolliert.

**Beispiel für Bauingenieure:** In einem traditionellen System könnte die Buchhaltung ihre Kostendaten in Excel führen, während die Projektleitung ihre Zeitpläne in MS Project verwaltet. Bei einem datenbankbasierten Ansatz würden beide auf dieselbe zentrale Datenbank zugreifen, wodurch automatisch konsistente Berichte über Projektkosten und -fortschritt möglich werden.

## Die Codd'schen Regeln

Edgar Codd formulierte 1985 und 1990 grundlegende Prinzipien für Datenbanksysteme:

- **Integration:** Einheitliche, redundanzfreie Datenverwaltung
- **Operationen:** Grundfunktionen Speichern, Suchen und Ändern
- **Katalog:** Zugriffe auf Datenbankbeschreibungen im Data Dictionary
- **Benutzersichten:** Personalisierte Sichten auf die Daten je nach Berechtigung und Bedarf
- **Integritätssicherung:** Gewährleistung der Korrektheit des Datenbankinhalts
- **Datenschutz:** Schutz vor unauthorisierten Zugriffen
- **Transaktionen:** Zusammenfassung mehrerer Operationen als unteilbare Einheit
- **Synchronisation:** Koordination paralleler Transaktionen
- **Datensicherung:** Wiederherstellung nach Systemfehlern

## Übersicht der Datenbanktypen

Die Datenbanklandschaft wird dominiert von relationalen Datenbanken, aber NoSQL-Datenbanken gewinnen an Bedeutung für spezielle Anwendungsfälle.

## Relationale Datenbanken (RDBMS)

### Eigenschaften und Struktur
Relationale Datenbankmanagementsysteme werden seit den frühen 1980er Jahren eingesetzt und basieren auf dem tabellenorientierten Datenmodell. 

**Kernmerkmale:**
- **Tabellenschema:** Jede Tabelle hat einen Namen und eine fixe Anzahl von Attributen (Spalten) mit definierten Datentypen
- **Strukturierte Daten:** Starke Strukturierung durch Tabellendefinition und Normalisierung
- **SQL-Standard:** Structured Query Language für alle Datenbankoperationen

**Beliebte Systeme:** Oracle, MySQL, Microsoft SQL Server, PostgreSQL, IBM Db2

**Beispiel für Bauingenieure:** Eine Projektdatenbank könnte Tabellen für "Projekte", "Mitarbeiter", "Materialien" und "Kosten" enthalten. Jede Tabelle hat fest definierte Spalten (z.B. Projekt-ID, Projektname, Startdatum), und durch SQL können komplexe Abfragen erstellt werden wie "Zeige alle Projekte, die über Budget liegen und mehr als 6 Monate dauern".

## NoSQL-Datenbanken

### Entstehung und Motivation
NoSQL-Datenbankmanagementsysteme verzichten auf das relationale Datenmodell und unterstützen daher meist kein SQL. Seit etwa 2009 finden sie zunehmend Verbreitung.

**Hauptgründe für NoSQL:**
- **Skalierbarkeitsanforderungen:** Bewältigung sehr großer Datenmengen
- **Fehlertoleranz:** Robustheit für moderne Web-Applikationen
- **Big Data:** Verarbeitung riesiger, verteilter Datenmengen
- **Semi-strukturierte Daten:** Flexibilität für Daten ohne festes Schema

**Beliebte Systeme:** MongoDB, CouchDB, Cassandra, Redis, Neo4j, Amazon DynamoDB, HBase, OrientDB

## Dokumentenorientierte Datenbanken

### Schemafreie Organisation
Document Stores zeichnen sich durch maximale Flexibilität bei der Datenorganisation aus:

**Eigenschaften:**
- **Keine einheitliche Struktur:** Datensätze können völlig unterschiedlich aufgebaut sein
- **Variable Datentypen:** Spalten können in verschiedenen Datensätzen unterschiedliche Typen haben
- **Arrays:** Spalten können mehrere Werte enthalten
- **Verschachtelung:** Datensätze können hierarchische, verschachtelte Strukturen haben
- **JSON-Format:** Meist wird JSON zur Darstellung der Dokumente verwendet

**Beliebte Systeme:** MongoDB, Amazon DynamoDB, Databricks, Azure Cosmos DB, Couchbase

**Beispiel für Umweltingenieure:** Bei der Dokumentation von Umweltproben könnten verschiedene Standorte unterschiedliche Messparameter haben. Standort A misst pH-Wert, Temperatur und Sauerstoffgehalt, während Standort B zusätzlich noch Schwermetallkonzentrationen erfasst. In einer dokumentenorientierten Datenbank kann jeder Standort seine spezifische Datenstruktur haben.

## Key-Value Datenbanken

### Einfachheit als Stärke
Key-Value Stores sind die einfachste Form von Datenbankmanagementsystemen:

**Funktionsweise:**
- Speicherung von Schlüssel-Wert-Paaren
- Abruf von Werten anhand des Schlüssels
- Ähnlichkeit zu Python-Dictionaries

**Anwendungsgebiete:**
- **Ressourcenbegrenzte Systeme:** Embedded PCs und IoT-Geräte
- **Web-Entwicklung:** Schnelle Caching-Lösungen
- **Session-Management:** Speicherung von Benutzersitzungen

**Beliebte Systeme:** Redis, Amazon DynamoDB, Azure Cosmos DB, Memcached, Hazelcast

**Beispiel für Bauingenieure:** In einem Smart-Building-System könnten Sensordaten als Key-Value-Paare gespeichert werden: "Sensor_Raum_101_Temperatur" → 22.5°C, "Sensor_Raum_101_Luftfeuchtigkeit" → 45%. Dies ermöglicht schnellen Zugriff auf aktuelle Werte für die Gebäudesteuerung.

## Suchmaschinen-Datenbanken

### Spezialisierung auf Textsuche
Suchmaschinen-Datenbanken sind NoSQL-Systeme, die speziell für die Suche in Dateninhalten optimiert sind:

**Erweiterte Suchfunktionen:**
- **Komplexe Suchbegriffe:** Boolesche Operatoren, Wildcards
- **Volltextsuche:** Durchsuchung ganzer Dokumente
- **Stemming:** Reduzierung von Wörtern auf Stammformen
- **Relevanz-Ranking:** Bewertung und Sortierung der Suchergebnisse
- **Gruppierung:** Kategorisierung von Suchergebnissen
- **Verteilte Suche:** Skalierbarkeit durch Verteilung auf mehrere Server

**Beliebte Systeme:** Elasticsearch, Splunk, Solr, OpenSearch, MarkLogic

**Beispiel für Umweltingenieure:** In einer Umweltbehörde könnten tausende von Gutachten, Berichten und Studien durchsuchbar gemacht werden. Eine Suchanfrage nach "Grundwasser AND Kontamination AND Industriegebiet" würde alle relevanten Dokumente finden und nach Relevanz sortieren.

## Graphdatenbanken

### Modellierung von Beziehungen
Graph-DBMS stellen Daten als Netzwerk von Knoten (Nodes) und Verbindungen (Edges) dar:

**Anwendungsgebiete:**
- **Netzwerkanalysen:** Infrastrukturnetzwerke, Versorgungsnetze
- **Soziale Netzwerke:** Verbindungen zwischen Personen und Organisationen
- **Empfehlungssysteme:** Ähnlichkeitsanalysen und Vorschläge
- **Abhängigkeitsanalysen:** Projektabhängigkeiten, Lieferketten

**Beliebte Systeme:** Neo4j, Microsoft Azure Cosmos DB, Virtuoso, IBM KITT

**Beispiel für Bauingenieure:** Bei der Planung einer Stadtsanierung könnte eine Graphdatenbank die Abhängigkeiten zwischen verschiedenen Infrastrukturelementen modellieren. Knoten repräsentieren Straßen, Gebäude, Versorgungsleitungen, während Kanten die Abhängigkeiten darstellen (z.B. "Straße A muss vor Gebäude B saniert werden").

## Fokus in der Vorlesung

### Schwerpunkt auf relationalen Datenbanken
Der Kurs konzentriert sich hauptsächlich auf relationale Datenbanken (71.9% Marktanteil), da sie:
- Einfach zu erlernen und zu verwenden sind
- Die weiteste Verbreitung haben
- Eine solide Grundlage für das Verständnis von Datenbanken bilden

### Ergänzung durch Key-Value Datenbanken
Zusätzlich werden Key-Value Datenbanken behandelt, da sie:
- Einfache, leicht verständliche Konzepte bieten
- Sich gut für praktische Übungen eignen
- Eine wichtige Rolle in modernen Anwendungen spielen

## Praktische Implementierung in Python

### Datenbankzugriff über spezialisierte Bibliotheken
Für jede Datenbankart existieren entsprechende Python-Bibliotheken, die den Zugriff ermöglichen. Jede Datenbank (Oracle, Redis, MongoDB, etc.) hat ihre eigene, optimierte Schnittstelle.

**Einfaches Beispiel mit Key-Value Store:**
```python
from replit import db

# Daten speichern
db["entry"] = 5

# Daten abrufen
value = db["entry"]
print(value)  # Output: 5
```

**Praktisches Beispiel für Umweltingenieure:**
```python
# Speicherung von Messwerten
db["station_001_ph"] = 7.2
db["station_001_temperature"] = 18.5
db["station_002_ph"] = 6.8

# Abruf für Analyse
ph_wert = db["station_001_ph"]
if ph_wert < 6.5 or ph_wert > 8.5:
    print("pH-Wert außerhalb des Normalbereichs!")
```

## Zusammenfassung der Datenbanktypen

### Relationale Datenbanken
- **Stärken:** Strukturierte Daten, SQL-Standard, bewährte Technologie
- **Anwendung:** Klassische Geschäftsanwendungen, ERP-Systeme, Finanzdaten
- **Ingenieur-Beispiel:** Projektmanagement, Kostenverfolgung, Ressourcenplanung

### NoSQL-Datenbanken
- **Dokumentenorientiert:** Flexible Schemas für unterschiedliche Datenstrukturen
- **Key-Value:** Einfache, schnelle Zugriffe für Caching und Session-Management
- **Suchmaschinen:** Spezialisiert auf Textsuche und Content-Discovery
- **Graph:** Optimiert für Beziehungsanalysen und Netzwerkstrukturen

### Auswahlkriterien
Die Wahl des Datenbanktyps hängt ab von:
- **Datenstruktur:** Strukturiert vs. semi-strukturiert vs. unstrukturiert
- **Skalierungsanforderungen:** Lokale Anwendung vs. globale Verteilung
- **Abfragekomplexität:** Einfache Lookups vs. komplexe Analysen
- **Konsistenzanforderungen:** Sofortige vs. eventual Consistency

**Beispiel für Bauingenieure:** Ein Infrastrukturprojekt könnte verschiedene Datenbanktypen kombinieren: Relationale DB für Projektdaten und Kosten, Graph-DB für Abhängigkeitsanalysen, Key-Value Store für Sensor-Caching und Elasticsearch für die Dokumentensuche in technischen Spezifikationen.