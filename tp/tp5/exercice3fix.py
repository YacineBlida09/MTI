# File: python/tp/tp5/exercice3fix.py
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height

class Square(Shape):
    def __init__(self, side):
        self._side = side
    
    def area(self):
        return self._side ** 2
    
    def perimeter(self):
        return 4 * self._side
    
    def set_side(self, side):
        self._side = side
    
    def get_side(self):
        return self._side



class ShapeUtilities:
    @staticmethod
    def total_area(shapes: list[Shape]):
        return sum(shape.area() for shape in shapes)
    
    
    @staticmethod
    def find_largest(shapes: list[Shape]) -> Shape:
        return max(shapes, key=lambda s: s.area())



shapes = [
        Rectangle(5, 4),
        Square(3),
        Rectangle(2, 8),
        Square(5)
        ]
    
total = ShapeUtilities.total_area(shapes)
print(f"surface totale: {total}")
    
largest = ShapeUtilities.find_largest(shapes)
print(f"plus grande surface: {largest.area()}")