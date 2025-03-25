Below is a simple solution using Python programming language that uses dictionary to represent points in 2D space:

```python
class Point2D:
    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.coords = {'x': x, 'y': y}
        else:
            raise TypeError('Point2D coordinates should be numbers')

    def __str__(self):
        return f'({self.coords["x"]}, {self.coords["y"]})'


def add_points(p1, p2):
    if not isinstance(p1, Point2D) or not isinstance(p2, Point2D):
        raise TypeError('Both arguments should be of Point2D type')
    return Point2D(p1.coords['x'] + p2.coords['x'], p1.coords['y'] + p2.coords['y'])

def sub_points(p1, p2):
    if not isinstance(p1, Point2D) or not isinstance(p2, Point2D):
        raise TypeError('Both arguments should be of Point2D type')
    return Point2D(p1.coords['x'] - p2.coords['x'], p1.coords['y'] - p2.coords['y'])
```
You can test this code using the following example:

```python
# Testing our functions with some example points
point1 = Point2D(3, 4)
point2 = Point2D(7, 8)
print('Point1:', point1) # Should print (3, 4)
print('Point2:', point2) # Should print (7, 8)
point3 = add_points(point1, point2)
print('Point1 + Point2:', point3) # Should print (10, 12)
point4 = sub_points(point1, point2)
print('Point1 - Point2:', point4) # Should print (-4, -4)
```