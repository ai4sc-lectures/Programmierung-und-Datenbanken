import Polygon

class Pentagon(Polygon):
    def __init__(self, p1, p2, p3, p4, p5, name="Pentagon"):
        super().__init__(points=[p1, p2, p3, p4, p5], name=name)