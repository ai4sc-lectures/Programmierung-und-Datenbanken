import Polygon

class Tetragon(Polygon):
    def __init__(self, p1, p2, p3, p4, name= "Tetragon"):
        super().__init__(points=[p1, p2, p3, p4], name=name)