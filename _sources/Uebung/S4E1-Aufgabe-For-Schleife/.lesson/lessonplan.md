# Musterlösung
  

```python
import math

lines = [[[25, 30],[85, 55]], [[85, 55],[105, 115]], [[105, 115],[155, 135]], [[155, 135],[180, 110]]]

def distance(p1, p2):
  a = p1[0] - p2[0]
  b = p1[1] - p2[1]
  result = math.sqrt((a**2)+(b**2))
  return result

def calculate_cost():
  length = 0
  for line in lines:
    p1 = line[0]
    p2 = line[1]
    dist = distance (p1, p2)
    length = length + dist
  cost = length * 100
  return cost
```

  
  