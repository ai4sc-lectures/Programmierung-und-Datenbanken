---
title: "Programmieren und Datenbanken - Programmablauf"
author: "Joern Ploennigs"
format: revealjs
---

## Programmierung und Datenbanken - Entwurfsvorgehen

::: {style="text-align: center; margin-top: 2em;"}
*PROGRAMMIERUNG UND DATENBANKEN*

Motivation Computer und Architekturen • Programmierung und Datentypen • Fehler und Debugging • Objektorientierung u. Softwareentwurf • Verzweigungen und Schleifen • Funktionen und Rekursion

*grundlagen* • *modellierung*
:::



## Entwurfsvorgehen

::: {style="text-align: center; margin-top: 3em;"}
![Midjourney: Software Waterfall](waterfall-image-placeholder.jpg){fig-alt="Software Waterfall visualization"}
:::



## Softwareentwurf

Software wird selten allein entwickelt, sondern oft im Team über eine längere Zeit. Hierfür braucht man einen Projektplan wie die Software auszusehen hat und arbeitsteilig entwickelt werden kann. Dieser Projektplan umfasst den Bauplan (Klassenentwurf) als auch die Bauablaufplanung (Programmiervorgehen) für die zu konstruierende Software.

Das Erstellen dieses Projektplan wird als *Softwareentwurf* bezeichnet. Sie gleicht im Vorgehen stark dem Entwurfsvorgehen im Umwelt- und Bauingenieurwesen.



## Softwareentwurf - Phasen

Es gibt ähnliche Phasen wie:

- *die Anforderungsdefinition* – Definition was die Software etwas realisieren soll (vgl. dokumentieren welche Funktionen und Randbedingungen das Bauwerk erfüllt)

- *den Entwurf*
  - Modul- und Klassenentwurf – Definition wie die Software umgesetzt wird und (Grobplanung im Bau)
  - Ausführungsplanung – Was wird wann, durch wen, und wie implementiert (Gewerkplanung im Bau)



## Softwareentwurf - Phasen (Fortsetzung)

- *die Ausführung*
  - Implementation – Programmieren der einzelnen Klassen & Module (vgl. Gewerke im Bau umsetzen)
  - Integration – Zusammenführen der Module zur fertigen Lösung (vgl. Gewerke im Bau verbinden, wie Energie, Klima, Wasser, etc.)

- *die Abnahme* – Test des fertigen Softwareprogramms
  - Modultest – Unit-Test von Modulen (vgl. einzelne Gewerke abnehmen)
  - Integrationstest – Kombination von Module testen (vgl. mehrere Gewerke gemeinsam testen)
  - Systemtest – Gesamtheit der Module testen (vgl. Gesamtbauwerk abnehmen)



## Vergleich: Software- vs. Bauingenieurwesen

::: {style="display: flex; gap: 2em;"}
::: {style="flex: 1;"}
*Äquivalente Schritte im Bauingeneurwesen*

- *Ausschreibung:* Dokumentieren welche Funktionen und Randbedingungen das Bauwerk erfüllen
- *Entwurf*
  - Architektur und Grobentwurf – Definition wir das Bauwerk grob strukturiert ist
  - Fein- und Gewerkplanung - Definition wie Teile und die Gewerke umgesetzt werden
  - Ausführungsplanung – Was wird wann, durch wen, und wie gebaut
:::

::: {style="flex: 1;"}
*Schritte im Softwareentwurf*

- *Anforderungsdefinition* – Definition welche Funktionen und Randbedingungen die Software realisieren soll
- *Entwurf*
  - Modulentwurf – Definition welche Teile die Software hat
  - Klassenentwurf – Definition in welche Klassen die Software strukturiert ist
  - Ausführungsplanung – Was wird wann, durch wen, und wie implementiert
:::
:::



## Vergleich: Software- vs. Bauingenieurwesen (Fortsetzung)

::: {style="display: flex; gap: 2em;"}
::: {style="flex: 1;"}
*Bauingenieurwesen (Fortsetzung)*

- *Ausführung*
  - Einzelne Gewerke werden umgesetzt
  - Gewerke im Bau integrieren, wie Energie und Wasser mit Klima integrieren
- *Abnahme*
  - Abnahme einzelner Gewerke
  - Test mehrerer Gewerke gemeinsam
  - Gesamtbauwerk abnehmen
:::

::: {style="flex: 1;"}
*Softwareentwurf (Fortsetzung)*

- *Ausführung*
  - Implementation – Programmieren der einzelnen Klassen & Module
  - Integration – Zusammenführen der Module zur fertigen Lösung
- *Abnahme*
  - Modultest – Unit-Test von Modulen
  - Integrationstest – Kombination von Module testen
  - Systemtest – Gesamtheit der Module testen
:::
:::



## Lineare Methode - Wasserfallmethode

- Traditionelles Modell das häufig noch in der Ausschreibung großer Systeme gefordert wird

- Entwicklung ist in mehrere sequenzielle Schritte aufgeteilt und jeder Schritt muss vor dem nächsten beendet werden

- Benutzerbeteiligung nur in der Anforderungsdefinition

- Jeder Aktivität wird dokumentiert → Gut geeignet für Ausschreibungen (nach der Anforderungsdefinition oder dem Entwurf, ISO 9000)



## V-Methode

- Primär verwendet bei der Entwicklung sicherheitskritischer Software (Auto, Flugzeug, etc.)

- Separiert Entwicklungs- (linke Seite) und Testaktivitäten (rechte Seite)

- Tests werden schon im Entwicklungsarm definiert

- Ziel einer hohen Testabdeckung

- Benutzerbeteiligung in der Anforderungsdefinition und im Abnahmetest



## Agile Methode

- Moderne Methode um mit sich an ständig ändernden Anforderungen anpassen

- Ziel der schrittweisen Entwicklung der Lösung, um Aufwand und Komplexität einzelner Schritte in Grenzen zu halten

- Startet mit einer einfachen und ausbaufähigen Implementierung (MVP – Minimal Viable Produkt)

- Schrittweise Erweiterung und Verbesserung des Produktes mit regelmäßigen Releases (meist alle 3 Monate)

- Entwurfsfehler der ersten Iterationen können zu kompletten Neuentwurf führen



## Hörsaalfrage

::: {style="text-align: center; margin-top: 3em;"}
*FRAGEN?*

![Midjourney: A psychedelic DJ with a question mark for a head](dj-question-placeholder.jpg){fig-alt="Psychedelic DJ with question mark head"}
:::
