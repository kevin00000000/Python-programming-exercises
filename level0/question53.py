class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self._length = length
    def area(self):
        return self._length**2
shape = Shape()
square = Square(100)

print(square.area())