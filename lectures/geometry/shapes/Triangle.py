import Polygon

class Triangle(Polygon):
    def __init__(self, p1, p2, p3, name= "Triangle"):
        super().__init__(points=[p1, p2, p3], name=name)