# File: python/tp/tp6/ex5.py
import copy

class Shape:
    def __init__(self, color):
        self.color = color 
    
    def clone(self):
        return copy.deepcopy(self)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius  
    
    def __str__(self):
        return f"douwayra couleur t3ha {self.color}, nisf 9otr {self.radius}"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width  
        self.height = height 
    
    def __str__(self):
        return f"mostatil couleur t3ou {self.color}, 3ard {self.width} w toul {self.height}"


if __name__ == "__main__":

    
    # original
    c1 = Circle("rouge", 5)
    r1 = Rectangle("bleu", 10, 20)
    
    print("1. Original:")
    print("   ", c1)
    print("   ", r1)
    
    # 2. Copy
    c2 = c1.clone()
    c2.color = "5der"
    c2.radius = 10
    
    r2 = r1.clone()
    r2.width = 30
    r2.color = "safra"
    
    print("\n2. Copy:")
    print("   ", c2)
    print("   ", r2)
    
    # 3. Deep vs Shallow
    print("\n3. Deep vs Shallow clone:")
    obj = Circle("zra9", 7)
    obj.list = [1, 2, 3]
    
    deep = obj.clone()  # Deep copy
    shallow = copy.copy(obj)  # Shallow copy
    
    # Modify original
    obj.list.append(4)
    obj.color = "7mar"
    
    print("   Original list:", obj.list, "couleur:", obj.color)
    print("   Deep copy list:", deep.list, "couleur:", deep.color) 
    print("   Shallow copy list:", shallow.list, "couleur:", shallow.color) 