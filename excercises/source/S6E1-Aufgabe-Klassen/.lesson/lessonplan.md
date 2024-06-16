# Lesson plan
```python3
class Point:

  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y

  def as_tuple(self) -> Tuple[float]:
    return (self.x, self.y)

  def __str__(self) -> str:
    return "POINT (" + str(self.x) + " " + str(self.y) + ")"


class Line:

  def __init__(self, start: Point, end: Point):
    self.start = start
    self.end = end

  def __str__(self) -> str:
    return "LINE (" + str(self.start.x) + " " + str(self.end.y) + ", " + str(
      self.start.x) + " " + str(self.end.y) + ")"


class Polygon:

  def __init__(self, lines: List[Line]):
    self.lines = lines

  def intersects(self, polygon: Polygon) -> bool:
    #for each point of each polygon, check if it is in the other polygon
    for line in self.lines:
      if point_in_polygon(polygon, line.end):
        return True
    for line in polygon.lines:
      if point_in_polygon(self, line.end):
        return True
    return False


#Testdaten:
pt1 = Point(0, 0)
pt2 = Point(3, 3)
pt3 = Point(3, -3)
pt4 = Point(2, 0)
pt5 = Point(5, 3)
pt6 = Point(5, -3)
l1 = Line(pt1, pt2)
l2 = Line(pt2, pt3)
l3 = Line(pt3, pt1)
l4 = Line(pt4, pt5)
l5 = Line(pt5, pt6)
l6 = Line(pt6, pt4)
poly1 = Polygon([l1, l2, l3])
poly2 = Polygon([l4, l5, l6])
