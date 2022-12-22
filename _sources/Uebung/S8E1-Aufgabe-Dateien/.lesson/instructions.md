# Aufgabe 8 - Dateien, Replit-Datenbank und Wegfindung

Wir wollen nun mit unserem in der letzten Übung erstellten Hafeneinfahrts-Graphen dafür sorgen, dass Schiffe effizient durch die Hafeneinfahrt manövriert werden können. Dafür benötigen wir einen Wegfindungs-Algorithmus wie er in komplexerer Form z.B. auch in Anwendungen wie Google Maps vorkommt. Statt die Kanten mittels einer Graph-Klasse im Arbeitsspeicher zu halten, haben wir sie für die heutige Übung jedoch in eine Datei ausgelagert.

## Schritt 1: Prozessierung der Dateien

Um den Graphen nicht andauernd neu aus unseren Dateien zu konstruieren, wollen wir den Inhalt einmal auslesen und dann direkt in eine effiziente Datenbank schreiben.

Mittels der ``process.py``-Datei sollen die Inhalte der beiden vorgegebenen Dateien folgendermaßen ausgelesen werden:

- ``waterways_reduced.json`` soll mittels des ``geojson``-Moduls als Dictionary ausgelesen werden. Sie enthält alle Polygone der Hafeneinfahrt mitsamt Attributwerten.
- ``edges`` soll zeilenweise ausgelesen werden. Sie enthält alle Pfade zwischen Polygonen, wobei die Polygone jeweils durch ihr ``OBJECTID``-Attribut repräsentiert sind.

Iteriere durch alle ``features`` im GeoJSON-Dictionary. Füge jedem Feature dabei ein neues Attribut hinzu, welches eine Liste mit allen ``OBJECTID``'s enthält mit denen es laut der ``edges``-Datei eine Verbindung hat (Bedenke dass Verbindungen in beide Richtungen funktionieren). Die Features sind nichts anderes als ineinander geschachtelte Dictionaries und Lists, daher können jederzeit dynamisch neue Einträge eingefügt werden. Schreibe jedes so angereicherte Feature einzeln mit seiner ``OBJECTID`` als Schlüssel in die Replit-Datenbank.


## Schritt 2: Wegfindungs-Algorithmus

Wir haben nun eine Datenbank welche mit den Polygonen des Hafen Rotterdamms gefüllt ist und sowohl Geometrie- als auch Topologie-Informationen für jedes Objekt enthält.

Implementiere nun eine Wegfindung mittels des Breitensuche-Algorithmus. (Es wird angenommen dass alle einzelnen Polygone ungefähr gleich weit voneinander entfernt sind, d.h. wir kümmern uns nur um topologische Nachbarschaft, nicht um genaue Distanzen zwischen Polygonen) 

Lese dafür z.B. die Erklärungen auf folgender Webseite und übernehme den vorgegebenen Programmcode (außer den Teil zur "Verification"): https://onestepcode.com/graph-shortest-path-python/

Am Ende soll der kürzeste Pfad zwischen zwei beliebigen Polygonen in der Hafeneinfahrt als Liste von ``id``'s (nicht ``OBJECTID``!) ausgegeben werden, damit die Schiffe effizient manövriert werden können.

Hier Hinweise zu den drei Änderungen die an dem durch die Webseite vorgegebenen Algorithmus vorgenommen werden müssen: 
- Da wir aus der Datenbank arbeiten brauchen wir keinen Eingabegraph. Die Funktion braucht also nur zwei Knoten-IDs als Eingabe.
- ``next_nodes`` wird im Beispielcode bei jedem Schleifendurchlauf mit einem Wert aus dem Graphen belegt. Der Graph ist in unserem Fall jedoch unsere Datenbank. Aus dieser muss also in jedem Schleifendurchlauf stattdessen die in Schritt 1 erzeugte Liste an Verbindungen ausgelesen werden. Die ``OBJECTID`` des aktuellen Features liegt immer in ``last_node``.
- Die Funktion gibt nun eine Liste mit ``OBJECTID``'s zurück. Da aber die ``id``'s zurück gegeben werden sollen, muss direkt vor dem erfolgreichen ``return``-Statement für jedes Feature mittels der ``OBJECTID`` die zugehörige ``id`` aus der Datenbank geholt werden.


## Hinweise

Die Indizes von Listen sind Zahlen, die Schlüssen von Dictionaries können auch Strings sein. In der Replit-Datenbank sind sowohl Keys als auch Values stets Strings. Achte also immer darauf wann wie konvertiert werden muss. Benutze print-Statements und den Debugger um sicherzugehen.

Wir definieren für diese Aufgabe keine explizite Graph-Klasse, sondern halten einen Graphen implizit in der Datenbank. Trotzdem nutzen wir im Endeffekt eine Vorgehensweise aus der Graphentheorie.

## Vorgegebener Code

main.py
```python3
from replit import db

# Angepasster Code hier

#

print(shortest_path(289, 473))
print(shortest_path(401, 104))
print(shortest_path(580, 740))

```

process.py
```python3
import geojson
from replit import db

db.clear()
```