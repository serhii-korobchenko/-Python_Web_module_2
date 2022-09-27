from enum import Enum


class SideType(Enum):
    TYPE_WIDTH = 'width'
    TYPE_HEIGHT = 'height'


class Shape:
    def set_side(self, size, side):
        pass

    def area_of(self):
        pass


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_side(self, size, side):
        if SideType.TYPE_WIDTH == side:
            self.width = size
        if SideType.TYPE_HEIGHT == side:
            self.height = size

    def set_width(self, width):
        self.set_side(width, SideType.TYPE_WIDTH)

    def set_height(self, height):
        self.set_side(height, SideType.TYPE_HEIGHT)

    def area_of(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.edge = size

    def set_side(self, size, side=None):
        self.edge = size

    def set_width(self, width):
        self.set_side(width)

    def area_of(self):
        return self.edge ** 2

square = Square(10)
print("square", square.area_of())
rect = Rect(5, 10)
print("rect", rect.area_of())