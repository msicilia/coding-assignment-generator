The task is to implement a data structure that can represent points in 2D space and perform basic arithmetic operations on those points. The following is a possible solution:
```
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
```
This implementation uses a dictionary to store the x and y coordinates of the point. The `__add__` and `__sub__` methods are used to perform addition and subtraction operations on two points, respectively. The `__repr__` method is used to display the point in a human-readable format.

Here are some example test cases that demonstrate the functionality of the `Point2D` class:
```
pt1 = Point2D(3, 4)
pt2 = Point2D(5, 6)
print(pt1 + pt2) # Output: Point2D(8, 10)
print(pt1 - pt2) # Output: Point2D(-2, -2)
```
The above test cases demonstrate that the `Point2D` class can be used to perform basic arithmetic operations on points in 2D space.