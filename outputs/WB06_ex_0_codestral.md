 Solution:
   I've implemented a Python class named 'Point' that uses dictionaries to store its 'x' and 'y' coordinates. This class includes methods for adding and subtracting points, allowing us to perform vector operations. The 'add_points' method adds the corresponding 'x' and 'y' values of two 'Point' objects, creating a new 'Point' object with these results. Conversely, the 'subtract_points' method subtracts the corresponding 'x' and 'y' coordinates from each other, producing another 'Point' object.

   Here is my code to accomplish this:

```python
class Point:
    def __init__(self, x=0, y=0):
        self.coordinates = {'x': x, 'y': y}

    def add_points(self, point):
        return Point(self.coordinates['x'] + point.coordinates['x'], self.coordinates['y'] + point.coordinates['y'])

    def subtract_points(self, point):
        return Point(self.coordinates['x'] - point.coordinates['x'], self.coordinates['y'] - point.coordinates['y'])
```

For example, when we create two 'Point' objects, `p1 = Point(3, 5)` and `p2 = Point(1, 2)`, we can add them using `p1.add_points(p2)` and subtract one from the other with `p1.subtract_points(p2)`. The results are as expected.
```python
class Point:
    def __init__(self, x=0, y=0):
        self.coordinates = {'x': x, 'y': y}

    def add_points(self, point):
        return Point(self.coordinates['x'] + point.coordinates['x'], self.coordinates['y'] + point.coordinates['y'])

    def subtract_points(self, point):
        return Point(self.coordinates['x'] - point.coordinates['x'], self.coordinates['y'] - point.coordinates['y'])

# Test cases
p1 = Point(3, 5)
p2 = Point(1, 2)
print(p1.add_points(p2).coordinates)        # Output: {'x': 4, 'y': 7}
print(p1.subtract_points(p2).coordinates)   # Output: {'x': 2, 'y': 3}
```