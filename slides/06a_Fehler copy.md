<style>
.flex-row{display:flex; gap:1rem; align-items:flex-start; justify-content:space-between;}
.flex-row .col1{flex:1; min-width:10px}
.flex-row .col2{flex:2; min-width:10px}
.flex-row .col3{flex:3; min-width:10px}
.flex-row .col4{flex:4; min-width:10px}
.flex-row .col5{flex:5; min-width:10px}
.flex-row .col6{flex:6; min-width:10px}
.vcent{display:flex; align-items:center; justify-content:center}
.flex-row .col7{flex:7; min-width:10px}
</style>

## Grundlagen - Warum machen wir Fehler?

<div class="flex-row">
<div class="col1">

*Gewollte Fehler passieren, wenn:*

- wir bewusst Fakten ignorieren und lieber unserem Bauch vertrauen
- wenn wir Tests durchführen, um zu prüfen ob ein Programm diese Fehler behandelt
- durch gezielte Sabotage (Insider Thread in der Datensicherheit)

</div>
<div class="col1">

*Ungewollte Fehler passieren u.a. durch:*

- falsche Annahmen da z.B. die Anforderungen nicht hinreichend analysiert worden oder man nicht alle Fehlerfälle durchdacht hat
- Unaufmerksamkeit (Flüchtigkeitsfehler) durch Müdigkeit, Zeitdruck oder Desinteresse
- weil wir an kognitive/körperliche Limits stoßen (z.B. optische Täuschungen)

</div>
</div>

## Grundlagen - Warum machen wir Fehler mit Computern?

- *Computer sind von Menschen gemacht*
- Die mentalen Modelle anderer Menschen haben (oft subtile) Unterschiede zu unseren eigenen, z.B. wegen:
  - Alter
  - Herkunft
  - Ausbildung
  - Erfahrung
  - Kultur
- Die meisten Fehler im Alltag passieren an der *Schnittstelle zwischen uns und den internen Vorgängen*: Nutzeroberflächen, Hardware, etc.

## Hörsaalfrage: Was bedeutet dieses Zeichen?

<div class="vcent" style="height: 300px;">
💾
</div>

*Think about it before we reveal the answer...*

## Grundlagen - Was bedeutet dieses Zeichen?

<div class="flex-row">
<div class="col1">

💾

*Das Diskettensymbol* wird häufig zum Abspeichern benutzt.

Es stammt ursprünglich aus den 90er wo Daten noch auf Disketten gespeichert wurden.

</div>
<div class="col1">

*Heutzutage* haben viele diesen Kontext nicht und können das Symbol nicht intuitiv deuten.

*Beispiel für unterschiedliche mentale Modelle zwischen Generationen*

</div>
</div>

## Grundlagen - Wann machen Computer Fehler?

- Computer machen nur *sehr selten* Fehler (z.B. Bitfehler durch kosmische Strahlung, Fehler bei Berechnungen mit Fließkommazahlen, Überläufe von Integer, Fehler bei der Datenübertragung oder Speicherung)

- *Meistens* ist es allerdings der Nutzer oder Programmierer der die Fehler erst ermöglicht hat (Falsche Datentypen, keine gute Ausnahmen- oder Fehlerbehandlung)

- Die eigentliche Frage ist: *Gibt es Fehler im System abseits von unserem eigenen Programmcode?*

## Grundlagen - Wie beugt man Fehlern vor?

- *Nutzen einer integrierten Entwicklungsumgebung (IDE)*
  - Automatische Fehlererkennung von Syntaxfehlern
  - Code-Vervollständigung
  - Code-Generierung (z.B. aus Diagrammen)

- *Umfangreiches Planen* der Software mit Anforderungsanalyse, Softwareentwurf, Testentwurf, etc.

- *TESTEN, TESTEN, TESTEN* mittels spezieller Testfälle (Unit-Tests)!
  - Nicht nur reiner Funktionstest (macht es was es soll?)

## Grundlagen - Klassen von Fehlern

<div class="flex-row">
<div class="col3">

*Entlang der Wissenspyramide:*

- *Lexikalisch* – Code enthält ungültige Zeichen oder Zeichenketten
- *Syntaktisch* – Code kombiniert lexikalisch gültige Wörter in ungültiger Weise  
- *Semantisch* – Code ist syntaktisch gültig, aber liefert keine Ergebnisse/stürzt ab
- *Logisch* – Code ist semantisch gültig, aber löst das gegebene Problem nicht

</div>
<div class="col2">

```
Wissen
   ↑
Informationen  
   ↑
Daten
   ↑
Zeichen
```

*Semantik ↔ Syntax*
*Verarbeitung*

</div>
</div>

## Grundlagen - Andere Klassifizierungen von Fehlern

<div class="flex-row">
<div class="col1">

*Nach Häufigkeit und Reproduzierbarkeit:*

- *Deterministische Fehler* - treten immer auf und lassen sich reproduzieren
- *Sporadische Fehler* - treten nur selten und in besonderen Zuständen auf. Sind schwer zu reproduzieren

</div>
<div class="col1">

*Nach Auftreten:*

- *Statische Fehler* - Direkt im geschriebenen Code erkennbar
- *Dynamische Fehler* - Treten erst beim Ausführen des Programms auf

</div>
</div>

## Lexikalische & Syntaktische Fehler

- Sind in den meisten Fällen *statisch* und *deterministisch*
- Erzeugen *immer* eine Fehlermeldung
  - Schon in IDE, beim Compilieren oder nach dem Ausführen
- *Diese Fehlermeldungen können allerdings trügerisch sein!*

## Lexikalische & Syntaktische Fehler - Beispiele

- Ein *Schlüsselwort* ist falsch geschrieben
- *Nicht geschlossene* Anführungszeichen oder Klammern
- Einen *Doppelpunkt* nach einer Bedingung oder Funktion vergessen
- *Falsche Einrückung* nach einer Bedingung, Schleife oder Funktion
- Ggf. auch falsches Einrücken durch *Tabs vs. Leerzeichen*

## Lexikalische & Syntaktische Fehler - Behandlung

- *Erster Blick:* In welcher Zeile ist der Fehler aufgetreten?
- Gibt der *Text der Fehlermeldung* einen Hinweis?
- Liegt der Fehler in der Zeile oder ist der Fehler nur ein *Symptom* und der Fehler liegt in einer Zeile davor?
- Normalerweise *einfach zu beheben* und von der Fehlerzeile den Code Zeile für Zeile rückwärts durchgehen
- Falls nicht: *Refactoring* - Code zur besseren Lesbarkeit umstrukturieren ohne das Verhalten zu verändern

## Semantische Fehler - Grundlagen

- Entstehen durch die *fehlerhafte Anwendung* von syntaktisch korrekten Programmstrukturen auf ein bestimmtes Problem

- Semantische Fehler können *erkennbar* oder *unerkennbar* sein. Sie sind immer deterministisch, aber können statisch oder dynamisch auftreten

- *Erkennbare Fehler* sind Fehler von denen man weiß, dass sie auftreten können (z.B. Division durch Null, keine Internetverbindung, etc.)
  - Sollten *immer* abgefangen und behandelt werden

- *Unerkannte Fehler* sind beim Erstellen des Programms unbekannt. Deutlich schwieriger abzufangen

## Semantische Fehler - Beispiele

- Eine *Variable wird als Funktion* aufgerufen  
  *(statisch, deterministisch)*

- Ein *Operator wird mit einem Wert des falschen Typs* genutzt  
  *(statisch oder dynamisch, deterministisch)*

- Ein *Wert des falschen Typs* wird in eine Funktion übergeben  
  *(statisch oder dynamisch, deterministisch)*

- Es geschieht eine *Division durch 0*  
  *(dynamisch, deterministisch)*

## Semantische Fehler - Behandlung

*Erster Schritt: Verstehen der Fehlermeldung*

- *Idealfall:* Gibt das exakte Problem an
- *Meistens:* Gibt Hinweise auf ein Problem
  - Ort
  - Art des Problems  
  - Die betroffene Variable/Operation
- *Oft:* Die Fehlermeldung ist nur ein Symptom des eigentlichen Problems

## Semantische Fehler - Behandlung (2)

*Falls die Fehlermeldung nicht genug Informationen gibt:*

- *Programmablauf loggen* und so besser nachvollziehen:
  - Weitere Ausgaben hinzufügen (z.B. über `print()`-Funktion)
  - Variablenzustände prüfen oder prüfen ob gewisse Zeilen erreicht werden

- *Debugging-Tools* nutzen:
  - Programmablauf an bestimmten Punkten (*Breakpoints*) pausieren
  - Programmablauf *Schritt für Schritt* nachvollziehen
  - *Variablen beobachten* in diesem Moment

## Logische Fehler - Grundlagen

*Entstehen durch:*
- Fehler in der *Programmlogik*
- Ein *falsches mentales Modell*
- Einen grundlegenden *Fehler im Programmentwurf*
- *Flüchtigkeitsfehler* bei der Übersetzung vom Entwurf zur Implementierung

*Charakteristika:*
- Erzeugen *nur selten Exceptions* sondern falsches Verhalten/Ergebnisse
- Bleiben oft *unentdeckt* und treten erst dynamisch auf
- Können *deterministisch* oder *sporadisch* sein

## Logische Fehler - Beispiele

<div class="flex-row">
<div class="col1">

*Deterministische Fehler:*

- Verwendung eines *falschen Faktors* in einer Einheitenkonvertierung
- Verwenden der *falschen Art von Schleife* oder falsche Schachtelung
- Verwenden einer *falschen Zeitzone* beim Schreiben von Sensor-Daten

</div>
<div class="col1">

*Sporadische Fehler:*

- Probleme mit *Sommer-/Winterzeitkonvertierung* bei Sensor-Daten
- Die Bedingung in einer Schleife hat Fälle in der sie *immer True* ist und so endlos wird

</div>
</div>

## Logische Fehler - Behandlung

<div class="flex-row">
<div class="col1">

*Deterministische Fehler:*

- *Testfälle erstellen* um zu reproduzieren wann und wie unerwartetes Verhalten stattfindet
- *Debugger nutzen* um die Ausführung nachzuvollziehen und Fehlerursache zu isolieren
- Werte *systematisch verfolgen* und Schritt-für-Schritt auf Korrektheit prüfen

</div>
<div class="col1">

*Sporadische Fehler:*

- Mittels *Logging* (`print()`) den Zustand des Fehlers identifizieren, so dass er reproduzierbar wird
- *Bedingte Breakpoints* im Debugging nutzen (Programm bleibt nur stehen, wenn eine Fehlerbedingung gegeben ist)

</div>
</div>

## Zusatz: Warnungen

- Weisen auf Code hin, der *syntaktisch und semantisch korrekt* scheint, seinen Zweck aber wahrscheinlich *nicht erfüllen* wird

- Basieren z.B. auf *Erfahrungswerten*

- Können dabei helfen *semantische und logische Fehler frühzeitig* zu erkennen