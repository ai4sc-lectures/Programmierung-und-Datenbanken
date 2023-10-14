# Lesson plan

```python3
from typing import Tuple

class Point:
  def __init__(self, x:float, y:float):
    self.x = x
    self.y = y

  def as_tuple(self) -> Tuple[float]:
    return (self.x, self.y)

  def __str__(self) -> str:
    return "POINT (" + str(self.x) + " " + str(self.y) + ")"


pt = Point(4, 5)
print(pt.x, pt.y)
print(pt.as_tuple())
print(pt)
```