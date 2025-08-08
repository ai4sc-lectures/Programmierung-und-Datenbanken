---
title: "Einführung in Programmierung und Datenbanken"
subtitle: "Modellierung"
author: "joern ploennigs"
format: 
  revealjs:
    theme: default
    slide-number: true
    chalkboard: true
    preview-links: auto
    css: styles.css
---

## Modellierung mit Objekten

:::: {.columns}

::: {.column width="60%"}
- Unsere Wahrnehmung und unser Denken besteht darauf Objekte zu erkennen. Das setzt voraus, dass wir das Objekt von anderen Objekten trennen können (z. B. Stuhl und Tisch)

- Das Nachbilden dieser Wahrnehmung und dieses Weltverständnisses im Computer, nennt man **Modellierung**. Ein Modell ist eine abstrakte, vereinfachte Abbildung eines Systems (meist aus der Realität).
:::

::: {.column width="40%"}
- Da unsere Wahrnehmung auf Objekten basiert, ist es naheliegend für die Modellierung auch Objekte zu nutzen.

- Die echte Welt hat Systeme die interagieren, die Verhaltensweisen müssen wir auch modellieren!

- Das Verhalten wird in Programmen meist durch Funktionen abgebildet, welche Variablen verarbeiten und ändern.
:::

::::

## Hörsaalfrage

::: {.r-fit-text}
**WAS HABEN DIESE ELEMENTE GEMEIN?**
:::

## Hörsaalfrage

::: {.r-fit-text}
**WORAUS BESTEHEN DIESE ELEMENTE?**
:::

## Woraus bestehen diese Elemente?

:::: {.columns}

::: {.column width="50%"}
- Das sind alles **geometrische Objekte**

- Sie bestehen alle aus **Punkten**, die mit **Linien** verbunden sind
:::

::: {.column width="50%"}
- Das können wir bei der Modellierung ausnutzen und die Klassen so definieren, dass wir die **Gemeinsamkeit** in der Konstruktion ausnutzen
:::

::::

## Objektorientierter Softwareentwurf

Im objektorientierten Softwareentwurf, wird ein Programm so entworfen, dass es nur aus **Objekten** besteht. Man modelliert im Entwurf wie:

- diese Objekte in Form von **Klassen** definiert sind,
- welche **Attribute und Methoden** sie besitzen,
- wie diese Klassen aufeinander aufbauen (**Vererbung**),
- als auch wie sie miteinander in statischer Beziehung stehen (**Referenzen**)
- und wie sie dynamisch interagieren (**Verhalten**)

Der Softwareentwurf gleicht dabei stark dem Vorgehen von Ingenieuren beim Erstellen von Plänen, z. B. von Bauplänen.

Die übliche Modellierungssprache sind **UML Diagramme**.

## Objektorientierter Softwareentwurf - Referenzen

:::: {.columns}

::: {.column width="60%"}
- In Programmen stehen Objekte meist im Zusammenhang. Z. B. besteht eine Linie aus zwei Punkten.

- Diesen Zusammenhang zweier Objekt-Klassen bezeichnet man als **Referenz**.

- Um Referenzen in Python zu erstellen, erstellt man einfach ein Attribut vom Datentyp des anderen Objektes.
:::

::: {.column width="40%"}
```python
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def length(self):
        return self.start.distance(self.end)
```
:::

::::

## Objektorientierter Softwareentwurf - Vererbung

- Gleiche Objekte teilen oft auch ähnliche Eigenschaften und Methoden. Z. B. bestehen alle geometrischen Elemente aus Punkten die mit Linien verbunden sind

- Um diese Attribute und Methoden nicht jedes mal neu definieren zu müssen dabei ggf. Fehler zu machen, gibt es die **Vererbung** in der OOP

- OOP erlaubt das Definieren von spezialisierten **Unterklassen**, bzw. von generalisierten **Oberklassen**.

- Die Unterklasse (Spezialklasse) besitzt die Methoden und Attribute der generalisierten Oberklasse (Basisklasse).

- Angelehnt an die Genetik auch **„Vererbung"** genannt

## Beispiel Vererbung

::: {.r-fit-text style="text-align: center;"}
```
    Polygon
   /   |   \
Linie Dreieck Viereck
```
:::

## Objektorientierter Softwareentwurf - Polymorphie

- Ein Objekt einer **Spezialklasse** kann stets auch als Mitglied der **Basisklasse** betrachtet werden.

- Die Spezialklasse kann die geerbten Methoden/Attribute der Basisklasse **überschreiben** und somit umdefinieren.

- In statisch typisierten Sprachen gilt außerdem: In einer Variablen die ein Objekt der Basisklasse aufnehmen kann, kann auch ein Objekt einer abgeleiteten Klasse gespeichert werden.

## Paradigmen der Objektorientierung - Datenkapselung

:::: {.columns}

::: {.column width="60%"}
**Ziel der Datenkapselung** ist es Kontrolle darüber zu haben, welche Attribute lesbar oder beschreibbar sind und wie dies geschehen kann

Hierfür deklariert man Attribute oder Methoden als:
- **privat** – Nur die Instanz der gleichen Klasse kann zugreifen
- **protected** – Nur die Instanz der gleichen Klasse oder Unterklasse kann zugreifen
- **public** – Alle können zugreifen
:::

::: {.column width="40%"}
Ferner kontrolliert man ob Attribute nur **lesbar** oder auch **schreibbar** sind. 

Dafür werden Attribute als privat deklariert und sind dann nur durch **Get-Funktionen** lesbar und durch **Set-Funktionen** veränderbar.
:::

::::

## Dynamik in Klassen

- In der OOP wird angenommen, dass Klassen **statisch** sind und es keine anderen als die in der Klasse definierten Attribute und Methoden gibt.

- **Python** bietet ein höheres Maß an Dynamik als andere Programmiersprachen:
  - Dynamische Typisierung von Variablen
  - Dynamisches Binden von Methoden und Attributen
  - Wir können sogar Attribute und Methoden selbst hinzufügen, wenn diese nicht in der Klasse definiert sind.

- So können wir z. B. zur Laufzeit Referenzen zwischen Objekten schaffen die im vordefinierten Datenmodell keinen Bezug haben.

## Unified Modelling Language - Grundlagen

**UML (Unified Modelling Language)** ist ein ISO-Standard mit dem Softwareentwürfe dokumentiert werden.

:::: {.columns}

::: {.column width="50%"}
**Genutzt für den Entwurf, die Ausschreibung, Implementation und Dokumentation von:**
- Funktionalitäten
- Strukturen
- Prozessen und Interaktionen
:::

::: {.column width="50%"}
**Der Standard umfasst 13 Diagrammtypen, die typischsten:**
- **Klassendiagramme** (Für die Klassen- und Datenstruktur)
- **Programmablaufplan** (Für allgemeine Abläufe und Algorithmen)
- **Sequenzdiagramme** (Für Interaktionen)
- **Use-Case Diagramme** (Für Nutzer und Nutzfälle)
:::

::::

## Unified Modelling Language - Klassendiagramm

Das am **häufigsten verwendete Diagramm** im objektorientierten Modellieren

**Im Klassendiagramm modelliert werden:**
- Klassen mit
  - Attributen
  - Methoden
- Beziehungen
- Hierarchien & Vererbungen
- ...

## Klassendiagramm – Vererbung

**Vererbung** wird in UML durch ein Referenz mit einem **gefüllten Dreieck "▲"** bei der Oberklasse gezeichnet.

Um zum Beispiel auszudrücken, dass `Triangle`, `Tetragon` und `Pentagon` Unterklassen des Polygons sind, können wir zeichnen.

*Quelle: de.wikipedia.org/wiki/Klassendiagramm*

## Klassendiagramm - Referenzen

- **Referenzen** werden in UML mit Linien zwischen Objekten gekennzeichnet. Die Art der Linie und des Pfeils geben den Typ der Referenz an.

- Man unterscheidet in UML die Referenzen in der Art der **Besitzverhältnisse**:
  - **Aggregated** - ein Objekt ist Teil eines anderen und kann ohne ihn existieren
  - **Composition** - kann nicht ohne diesen existieren  
  - **Assoziation** - komplett unabhängig

- **Zahlen** an den Referenzen geben die **Multiplizität** an, also wie viele Objekte in dieser Relation im Zusammenhang stehen.

*Quelle: de.wikipedia.org/wiki/Klassendiagramm*

## Klassendiagramm - Gesamtbeispiel

- **Klassendiagramme** können recht schnell groß werden

- Sie eignen sich sehr gut um das **(Daten-) Modell** darzustellen

## Anwendungsbeispiel – BIM (Building Information Models)

:::: {.columns}

::: {.column width="60%"}
- **Bauzeichnungen** werden heutzutage als **BIM (Building Information Model)** gespeichert

- **IFC** ist ein objektorientiertes Model, mit Vererbung, Spezialisierung, Generalisierung und Polymorphismus

- Es wird u.a. in **UML** dokumentiert
:::

::: {.column width="40%"}
*[Hier würde normalerweise ein BIM-Diagramm oder Beispiel stehen]*
:::

::::

## Literaturhinweise

**Technische Einführung:**
[https://docs.python.org/3/reference/datamodel.html](https://docs.python.org/3/reference/datamodel.html)

**Einsteigerfreundliche Erklärung:**
[https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)

## Hörsaalfrage

::: {.r-fit-text}
**FRAGEN?**
:::

::: {style="font-size: 0.7em; text-align: center; margin-top: 2em;"}
*Midjourney: A psychedelic DJ with a question mark for a head*
:::