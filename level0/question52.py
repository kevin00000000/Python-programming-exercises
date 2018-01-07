class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def getArea(self):
        return self._length*self._width
rect = Rectangle(10,20)
print(rect.getArea())