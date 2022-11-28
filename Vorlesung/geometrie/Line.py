from ImmutablePoint import ImmutablePoint

class Line:
    def __init__(self, start: ImmutablePoint, end: ImmutablePoint):
        self.start = start
        self.end = end

    def length(self):
        return self.start.distance(self.end)