import unittest

class Rectangle:
    def __init__(self):
        self._width = 0
        self._height = 0
    
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def get_area(self):
        return self._width * self._height
    
    def get_perimeter(self):
        return 2 * (self._width + self._height)

class Square(Rectangle):
    def set_width(self, width):
        self._width = width
        self._height = width  # VIOLATION: changes both dimensions
    
    def set_height(self, height):
        self._width = height
        self._height = height  # VIOLATION: changes both dimensions

# Test demonstrating LSP violation
class TestLSPViolation(unittest.TestCase):
    def test_rectangle_area_consistency(self):
        """Test that demonstrates the LSP violation"""
        
        def modify_rectangle(rect: Rectangle):
            """Function that expects Rectangle behavior"""
            rect.set_width(5)
            rect.set_height(4)
            return rect.get_area()
        
        # Test with actual Rectangle
        rectangle = Rectangle()
        area1 = modify_rectangle(rectangle)
        self.assertEqual(area1, 20)  # 5 * 4 = 20 ✓
        
        # Test with Square (should behave like Rectangle)
        square = Square()
        area2 = modify_rectangle(square)
        # This SHOULD be 20 if Square truly substitutes Rectangle
        # But it's actually 4 * 4 = 16 due to the violation
        self.assertEqual(area2, 20)  # This will FAIL!
        
    def test_rectangle_perimeter(self):
        """Another example of violation"""
        
        def double_width(rect: Rectangle):
            """Double the width of a rectangle"""
            current_width = rect._width
            rect.set_width(current_width * 2)
        
        rectangle = Rectangle()
        rectangle.set_width(3)
        rectangle.set_height(4)
        original_area = rectangle.get_area()  # 12
        original_perimeter = rectangle.get_perimeter()  # 14
        
        double_width(rectangle)
        new_area = rectangle.get_area()  # 24 (3*2 * 4 = 24)
        new_perimeter = rectangle.get_perimeter()  # 20 ((6+4)*2=20)
        
        # With Square
        square = Square()
        square.set_width(3)  # width=3, height=3
        original_sq_area = square.get_area()  # 9
        original_sq_perimeter = square.get_perimeter()  # 12
        
        double_width(square)  # width=6, height also becomes 6!
        new_sq_area = square.get_area()  # 36 (6*6)
        new_sq_perimeter = square.get_perimeter()  # 24
        
        # Inconsistent behavior: Rectangle doubles width only
        # Square doubles both width and height
        print(f"Rectangle area change: {original_area} -> {new_area} (2x)")
        print(f"Square area change: {original_sq_area} -> {new_sq_area} (4x!)")

# Why it breaks LSP:
# 1. Square cannot substitute Rectangle in functions expecting independent width/height
# 2. Preconditions are violated: set_width() should only change width, not height
# 3. Postconditions are violated: area calculations give unexpected results
# 4. Invariants are broken: Square doesn't maintain Rectangle's behavioral contracts