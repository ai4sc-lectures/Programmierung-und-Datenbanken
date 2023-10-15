from typing import List
from geometry.points.ImmutablePoint import ImmutablePoint


class Polygon:
    def __init__(self, points: List[ImmutablePoint], name="Polygon"):
        if not isinstance(points, list):
            raise TypeError("points not of type list")
        if not len(points) > 2:
            raise TypeError("points need to contain at least 2 Points")
        for point in points:
            if not isinstance(point, ImmutablePoint):
                raise TypeError("Point not of type ImmutablePoint")
        self.__points = points
        self.name = name

    def get_points(self):
        return self.__points

    # Fläche des Polygons entsprechend der Gaußsche Trapezformel
    def area(self):
        n = len(self.__points) # of corners
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.__points[i].get_x() * self.__points[j].get_y()
            area -= self.__points[j].get_x() * self.__points[i].get_y()
        area = abs(area) / 2.0
        return area

    # Überschriebene Standardmethode zur Erzeugung eines Strings
    def __str__(self):
        description = f"{self.name} has an area of {self.area()} and is defined by\n" # \n ist ein Zeilenumbruch
        for i,point in enumerate(self.__points):
            description += f"  Point {i} at x: {point.get_x()} {point.unit}; y: {point.get_y()} {point.unit}\n"
        return description