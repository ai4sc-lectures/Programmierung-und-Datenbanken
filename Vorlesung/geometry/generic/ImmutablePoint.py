import math

class ImmutablePoint:
    unit = "m"
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y