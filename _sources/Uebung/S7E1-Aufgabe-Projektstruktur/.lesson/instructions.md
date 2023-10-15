# Aufgabe 7 - Projektstruktur  

Wir wollen nun die Intersection-Methode aus dem Übungsvideo nutzen um einen Graphen zu erzeugen. Dieser Graph wird uns helfen Wegfindungs-Analysen zur Hafeneinfahrt durchzuführen. 

Erstelle eine Projektstruktur mit drei Dateien:

``geometry.py``
- Kopiere den Inhalt der main-Methode (und die nötigen Imports von geojson und geopandas) aus dem Übungsvideo in eine Funktion ```get_intersections(file)``` und verändere den Code so, dass das Funktionsargument bestimmt welche Datei geöffnet wird. Die Funktion soll diesmal die ``intersections``-Liste direkt zurückgeben anstatt zu drucken.

``graph.py``
- Erstelle eine Klasse ```Graph``` welche die Topologie der Polygone speichern soll. Dafür wird in der Klasse eine Liste von Kanten abgespeichert. Jede Kante ist ein Python-Set mit zwei Integer-Werten (Indizes). Knoten werden nicht separat geführt, sondern sind durch die Integer-Werte in den Kanten implizit.
  - Die ``__init__``-Methode soll die Liste von Kanten erhalten und speichern. Diese Liste kann dabei leer sein.
  - Es gibt eine Methode ``add_edge``, welche zwei Integer-Zahlen erhält und diese als neue Kante hinzufügt. Beim Hinzufügen einer neuen Kante soll zuerst geprüft werden ob sie schon in der Liste existiert.
  - Die ``__str__``-Methode des Graphen soll alle Kanten Zeile-für-Zeile in einen String schreiben. Jede Kante soll dabei vom kleineren Index ``x`` zum größeren Index ``y`` ausgegeben werden, nach folgendem Muster: ``"x -- y"``. Zeilenumbrüche in Strings erzeugt man durch das Hinzufügen der Zeichenfolge ``"\n"``.

``main.py``
- Importiere die ``Graph``-Klasse aus der ``graph.py`` und die ``get_intersections``-Funktion aus der ``geometry.py``.
- Schreibe eine main-Funktion welche die get_intersections-Funktion aufruft und dann jede einzelne Intersection als Kante in einem Graphen abspeichert. Dann soll mittels ```return``` und ``str()`` der Graph als String ausgeben werden.

## Hinweise

Um die Ausgabe der Graph-Klasse korrekt zu formatieren, kann ein Python-Set durch die ``list()`` Funktion in eine Liste überführt und dann mittels ``sorted()`` sortiert werden.