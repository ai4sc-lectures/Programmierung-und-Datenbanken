# Lesson plan

main.py

```python3
from graph import Graph
from geometry import get_intersections

def main():
  intersections = get_intersections("polygone.json")
  g = Graph([])
  for i in intersections:
    g.add_edge(i[0], i[1])
  return(str(g))

if __name__ == "__main__":
  main()
```

geometry.py

```python3
import geojson
import geopandas

def get_intersections(file):
  f = open(file)
  gj = geojson.load(f)
  data = geopandas.GeoDataFrame(gj.features, crs="EPSG:4326")
  intersections = []
  for id, geom in data.geometry.items():
    other_id = 0
    for intersection in data.geometry.intersects(geom):
      if intersection and id != other_id:
        intersections.append((id, other_id))
      other_id = other_id + 1
  return intersections
```

graph.py

```python3
class Graph:

  def __init__(self, edges):
    self.edges = edges

  def add_edge(self, node1: int, node2: int):
    edge = {node1, node2}
    if edge not in self.edges:
      self.edges.append(edge)

  def __str__(self):
    output = ""
    for e in self.edges:
      ordered = sorted(list(e))
      output += str(ordered[0]) + " -- " + str(ordered[1]) + "\n"
    return output
```