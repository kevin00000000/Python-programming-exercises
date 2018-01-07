import math
class Circle:
    def __init__(self, radius):
        self._radius = radius
    def getArea(self):
        return math.pi * self._radius**2
print(Circle(3).getArea())