#1.​ Create a base class Shape with method area()
# 2.​ Create Rectangle, Circle, and Triangle subclasses overriding area().
# 3.​ Create a list of shapes and call area() on each → demonstrate polymorphism.
# 4.​ Bonus: Add a function that takes any “shape-like” object and calls area() (duck typing).
from math import pi 

class Shape:
    def __init__(self):
        pass

    def area(self):
        print("methode area de la classe Shape")

class Rectangle(Shape):
    __long: float
    __larg: float
    def __init__(self, long, larg):
        super().__init__()
        self.long = long
        self.larg = larg

    def area(self):
        return self.long * self.larg

class Circle(Shape):
    __rayon: float
    def __init__(self, rayon):
        super().__init__()
        self.rayon = rayon

    def area(self):
        return pi * (self.rayon ** 2)

class Triangle(Shape):
    __base: float
    __hauteur: float
    def __init__(self, base, hauteur):
        super().__init__()
        self.base = base
        self.hauteur = hauteur

    def area(self):
        return (self.base * self.hauteur) / 2   

shapes = [Rectangle(5, 10), Circle(7), Triangle(4, 8)]

for shape in shapes:
    print(f"Area: {shape.area()}")

def print_area(shape_like):
    print(f"Area from duck typing: {shape_like.area()}")

class Square:
    __side: float
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

square = Square(6)
print_area(square)