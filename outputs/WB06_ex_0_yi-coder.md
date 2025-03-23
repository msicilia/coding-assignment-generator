Here is an implementation using Python dictionaries according to your problem's constraints:

```python
class Point2D:
    def __init__(self, x=0, y=0):
        self.coords = {'x': x, 'y': y} 

    def add(self, other_point):
        return Point2D(self.coords['x'] + other_point.coords['x'], self.coords['y'] + other_point.coords['y'])

    def sub(self, other_point):
        return Point2D(self.coords['x'] - other_point.coords['x'], self.coords['y'] - other_point.coords['y'])

    def __str__(self):
        return f"Point({self.coords['x']}, {self.coords['y']})"

# Test cases:
p1 = Point2D(3, 4)
p2 = Point2D(5, 6)
print('Point 1:', p1)  # prints: Point 1: Point(3, 4)
print('Point 2:', p2)  # prints: Point 2: Point(5, 6)

p3 = p1.add(p2)
print('Addition result:', p3) # prints: Addition result: Point(8, 10)

p4 = p2.sub(p1)
print('Subtraction result:', p4)  # prints: Subtraction result: Point(2, 2)
```