from geometry.points.ImmutablePoint import ImmutablePoint

class Line:
    def __init__(self, start: ImmutablePoint, end: ImmutablePoint):
        if not isinstance(start, ImmutablePoint):
            raise TypeError("start not of type ImmutablePoint")
        if not isinstance(end, ImmutablePoint):
            raise TypeError("end not of type ImmutablePoint")
        self.start = start
        self.end = end

    def length(self):
        return self.start.distance(self.end)