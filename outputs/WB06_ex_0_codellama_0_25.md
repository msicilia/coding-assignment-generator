To implement a structure to support points in 2D using dictionaries, you can use the following code:
```python
class Point(dict):
    def __init__(self, x=0, y=0):
        super().__init__()
        self['x'] = x
        self['y'] = y

    @property
    def x(self):
        return self['x']

    @property
    def y(self):
        return self['y']

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
```
This code defines a `Point` class that inherits from the built-in `dict` class. The `__init__()` method is used to initialize the point with default values of 0 for both coordinates. The `x` and `y` properties are defined as read-only properties, which return the corresponding values from the dictionary.

The `__add__()` and `__sub__()` methods implement the addition and subtraction operations between points, respectively. These methods simply add or subtract the corresponding values of the two points together and create a new point with those values.

Here are some example test cases:
```python
point1 = Point(3, 4)
point2 = Point(5, 6)

# Test addition operation
result = point1 + point2
print(result.x, result.y)  # Output: 8 10

# Test subtraction operation
result = point1 - point2
print(result.x, result.y)  # Output: -2 -2
```
Note that the `Point` class is defined using dictionaries, which are a built-in Python data structure for storing key-value pairs. Using dictionaries to implement the `Point` class allows us to access the point coordinates as properties (e.g., `point.x`) and also allows us to perform mathematical operations between points (e.g., `point1 + point2`).