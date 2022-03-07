from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

class Specification:
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


