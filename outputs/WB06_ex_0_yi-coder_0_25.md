```python
class Point2D():
    def __init__(self,x,y):
        self.coords = {'x': x, 'y': y}

    def add(self, other_point):
        return Point2D(self.coords['x'] + other_point.coords['x'], 
                         self.coords['y'] + other_point.coords['y'])

    def subtract(self, other_point):
        return Point2D(self.coords['x'] - other_point.coords['x'], 
                          self.coords['y'] - other_point.coords['y'])

# Test cases
p1 = Point2D(3,4)
p2 = Point2D(1,2)
p3 = p1.add(p2)
print((p3.coords['x'], p3.coords['y'])) # Should print (4,6)

p4 = p1.subtract(p2)
print((p4.coords['x'], p4.coords['y'])) # Should print (2,2)
```
The above program first creates a class `Point2D` with methods for addition and subtraction of two points in 2-dimensional space. Then it tests these methods using example test cases where two points are added or subtracted together.