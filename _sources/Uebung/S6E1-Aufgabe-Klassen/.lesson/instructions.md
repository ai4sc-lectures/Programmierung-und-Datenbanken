# Aufgabe 6 - Klassendefinitionen

In dieser Aufgabe wollen wir den ersten Teil eines größeren Systems definieren: eine Sammlung von Geometrie-Klassen, welche später die Grundlage für komplexere Analysen bilden.

Die benötigten Klassen sind folgende:

* Die ``Point``-Klasse aus dem Übungsvideo (kann direkt übernommen werden)
* Die ``Line``-Klasse, welche aus zwei Punkten namens ``start`` und ``end`` besteht (Eingabeparameter: ``start:Point, end:Point``)
* Die ``Polygon``-Klasse, welche aus einer Liste aus aufeinander folgenden Linien namens ``lines`` besteht (Eingabeparameter: ``lines:List[Line]``)

Die Klassen sollen in der **main.py**-Datei definiert werden. Die **exercise4.py** muss nicht verändert werden. Jede Klasse soll einen Konstruktor ``__init__()`` haben. ``Point`` und ``Line`` sollen außerdem eine ``__str__()``-Methode enthalten, welche Ausgaben der folgenden Form erzeugt:
* ``"POINT (x y)"``
* ``"LINE (x1 y1, x2 y2)"``

Zur Polygon-Klasse soll eine erweiterte Methode hinzugefügt werden, welche wir in späteren Übungen benötigen: die ``intersects()``-Methode, welche prüft ob das vorliegende Polygon sich mit einem anderen Polygon schneidet. Als Hilfe vorgegeben ist hierfür eine leicht angepasste Version der Punkt-in-Polygon-Methode aus Übung 4 (``point_in_polygon()``). Prüfe mit Hilfe dieser für jeden Punkt des einen Polygons ob dieser sich im anderen Polygon befindet. Wiederhole den selben Vorgang für das andere Polygon. Das Prinzip ist folgendes: Zwei Polygone überschneiden sich wenn irgend ein Punkt eines Polygons sich innerhalb des anderen Polygons befindet.

## Hinweise

Die Tests sind wieder Unit-Tests, d.h. die von dir definierten Funktionen werden direkt aufgerufen. Eigene Testdaten können außerhalb der Klassendefinitionen also problemlos definiert und mittels Print-Befehlen ausgegeben werden.

Die Polygone sind über aneinanderhängende Linien definiert, ein Punkt kommt also immer zweimal in einem Polygon vor. Überlege welche Schritte du gehen musst um von der Liste von Linien zu den Punkten zu kommen.

Bei der hier mitgelieferten Point-in-Polygon-Methode handelt es sich um eine Heuristik - sie erkennt nur eindeutig enthaltene Punkte, Fälle wie Punkte die auf dem Rand oder einer Ecke eines Polygons liegen werden nicht exakt behandelt.

## Vorgegebener Code

main.py
```python3
from __future__ import annotations
from exercise4 import point_in_polygon
from typing import List, Tuple
```

exercise4.py
```python3
from sympy.geometry import Segment, Ray
from random import random

def line_ray_intersection(line, ray):
  l = Segment(line.start.as_tuple(), line.end.as_tuple())
  r = Ray(ray[0], angle=ray[1])
  if r.intersection(l):
    return 1
  else:
    return 0

def construct_ray(point):
  random_ray = (point.as_tuple(), random() * 360)
  return random_ray

def point_in_polygon(poly, point):
  ray = construct_ray(point)
  intersections = 0
  for line in poly.lines:
    intersections += line_ray_intersection(line, ray)
  if (intersections % 2) == 0:
    return False
  else:
    return True

```