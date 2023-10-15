import math

class Point:
    # Attribut aller Instanzen
    unit = "m"
    
    # Konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Eigene Methode
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)