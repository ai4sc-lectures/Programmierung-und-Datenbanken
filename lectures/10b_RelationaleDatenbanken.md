
# Relationale Datenbanken

![](images/10b_RelationaleDatenbanken/mj_title.png)

> If you think you understand SQL, you’re probably wrong.
>
> - C. J. Date

## <a href="/lec_slides/10b_RelationaleDatenbanken.slides.html">Folien</a>
<iframe src="/lec_slides/10b_RelationaleDatenbanken.slides.html" width="750" height="500"></iframe>

## Ablauf

![](images/partB_2.svg)

## Relationale Datenbanken

<script>setSectionBackground('#E2F0D9');</script>
<div class="flex-row">
  <div class="col4 vcent">

  </div>
  <div class="col6"> 
    <figure class="mj-fig">
        <img src="images/10_Datenbanken/mj_databank2.png" class="mj-fig-img">
        <figcaption class="mj-fig-cap">
            Midjourney: Relational Database
        </figcaption>
    </figure>
  </div>
</div>

## Relationale Datenbanken - Grundkonzepte

<div class="alert alert-block alert-success">
<b>📘 Definition: Relationale Datenbank</b>

Eine relationale Datenbank ist ein *Datenbanksystem*, das Informationen in *Tabellen* (Relationen) speichert, wobei die Daten als *Tupel* (Zeilen) organisiert sind und jede Spalte (Attribut) einen definierten Datentyp besitzt.
</div>

<div class="flex-row">
  <div class="col1">

- Daten sind in Tabellenstrukturen (Schemata) organisiert
- *Relation* ist hierbei der Begriff für eine Tabelle
- Eine *relationale Datenbank* ist eine Menge von Tabellen

  </div>
  <div class="col1"> 

| Spalte 1 | Spalte 2 | Spalte 3 |
|----------|----------|----------|
| Zeile 1  | ...      | ...      |
| Zeile 2  | ...      | ...      |

  </div>
</div>

## Relationale Datenbanken - Grundbegriffe

<div class="flex-row">
  <div class="col1">

- Jede Tabelle hat einen *Relationennamen* (Tabellennamen)
- *Relation* steht für die Gesamtheit der Datentupel (Alle Zeilen)
- Jedes *Tupel* an Daten besteht aus einer Abfolge von Attributwerten (Einzelne Zeile)
- Reihenfolge festgelegt durch *Relationenschema* (Spaltennamen)

  </div>
  <div class="col1"> 

| Attribut 1   | Attribut 2 | Attribut 3 |
|--------------|------------|------------|
| Attributwert |     ...    |     ...    |
| Attributwert |     ...    |     ...    |

  </div>
</div>

## Beispiel: OpenData Hanse-Stadt Rostock

Informationen sind meist über verschiedene Tabellen verteilt und müssen oft zusammengeführt verarbeitet werden, um daraus anwendbares Wissen abzuleiten.

- Beispiel: https://www.opendata-hro.de
    - Bebauungspläne
    - Gemeinden  
    - Baustellen
    - Bodenrichtwerte
    - Adressenliste

## Schlüsselattribute

<div class="flex-row">
  <div class="col1">

- Gewisse *Attribute (Spalten)* können als *Schlüssel* markiert werden
- Schlüssel sind meist *eindeutig (unique)* zuordenbar
- Sie existieren in der Tabelle nur *einmal*
- Man kann damit die *Zeile (Tupel) identifizieren*
- Zeilennummern eignen sich nicht (können gelöscht werden)

  </div>
  <div class="col1"> 

Schlüsseltypen:
- *Einzelnes Attribut* oder *Menge von Attributen*
- *Unique ID (UID)* - einzelnes Attribut
- *Globally Unique IDs (GUID)* - global eindeutig
- *UUID* (universally unique identifier) - ISO Standard

  </div>
</div>

## Schlüsselattribute - Beispiel

**Gemeinden Tabelle**

| GemeindeID | Name | Einwohner |
|------------|------|-----------|
| 1 | Dummerstorf | 7.329 |
| 2 | Graal-Müritz | 4.278 |
| 3 | Sanitz | 5.831 |

<br/> Schlüssel: GemeindeID

## Verweise über Schlüssel

<div class="flex-row">
  <div class="col1">

**Gemeinden Tabelle**

| GemeindeID | Name | Einwohner |
|---|--------------|-------|
| 1 | Dummerstorf  | 7.329 |
| 2 | Graal-Müritz | 4.278 |
| 3 | Sanitz       | 5.831 |

<br/> Primärschlüssel: GemeindeID

  </div>
  <div class="col1"> 

**Bauwerke Tabelle**

| BauwerksID | Bauwerkstyp | GemeindeID |
|------------|-------------|------------|
| 5000       | Tankstelle  | 2 |
| 5001       | Hotel       | 1 |
| 5002       | Kirche      | 2 |


<br/> Fremdschlüssel: GemeindeID

  </div>
</div>

## Schlüsselkonzepte

- Die *Schlüssel anderer Tabellen* kann man nutzen um auf Tupel in diesen zu verweisen
- Die *eigenen Schlüssel* einer Tabelle heißen *Primärschlüssel* (Primary Key)
- Die *Schlüssel anderer Tabellen* heißen *Fremdschlüssel* (Foreign Key)
- Die *Tabellen werden über Schlüssel in Beziehung gesetzt*

> Der Fremdschlüssel verweist auf den Primärschlüssel in der anderen Tabelle

## Die Rolle von Schlüsseln

Schlüssel definieren sogenannte Integritätsbedingungen:

<div class="flex-row">
  <div class="col1">

**Primärschlüssel**

- Stehen für die *Integrität der einzelnen Tabelle*
- *Lokale Integrität*

  </div>
  <div class="col1"> 

**Fremdschlüssel**

- Stehen für die *Integrität des gesamten Datenbanksystems*
- *Globale Integrität*

  </div>
</div>
