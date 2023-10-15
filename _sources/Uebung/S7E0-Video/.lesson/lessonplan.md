# Lesson plan

main.py

```python3
import geojson
import geopandas
from printer import print_intersections

def main():
  f = open("polygons.json")
  gj = geojson.load(f)
  data = geopandas.GeoDataFrame(gj.features, crs="EPSG:4326")
  intersections = []
  for id, geom in data.geometry.items():
    other_id = 0
    for intersection in data.geometry.intersects(geom):
      if intersection and id != other_id:
        intersections.append((id, other_id))
      other_id = other_id + 1
  print_intersections(intersections)

if __name__ == "__main__":
  main()
```

printer.py

```python3
def print_intersections(intersections):
  for i in intersections:
    print(i[0], "->", i[1])
```