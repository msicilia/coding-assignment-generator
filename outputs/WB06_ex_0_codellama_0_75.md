  Write Python code to solve the following problem:
Implement a structure to support the points in 2D, i.e. with two x and y coordinates. Program then functions for their addition and subtraction

You cannot use the following Python elements:
match expressions, list comprehensions

You must use the following Python elements:
Dictionaries

When writing some example test cases take into account the following:
No test case hints

Take into account the following additional requirements:
No additional requirements.

# Solution

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)
    
    def sub(self, other_point):
        return Point(self.x - other_point.x, self.y - other_point.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

# Test cases
p1 = Point(3, 4)
p2 = Point(5, 6)

assert str(p1.add(p2)) == "(8, 10)"
assert str(p1.sub(p2)) == "(-2, -2)"