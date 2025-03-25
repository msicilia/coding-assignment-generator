Thoughts: The task requires implementing a simple structure for 2D points using dictionaries and functions for adding and subtracting these points. We need to ensure that the code does not use match expressions or list comprehensions, as specified.

Here's the solution:

1. Define a function `create_point` to create a point dictionary.
2. Define a function `add_points` to add two points.
3. Define a function `subtract_points` to subtract one point from another.
4. Include example test cases to verify the correctness of the implementation.

### Code:
```py
def create_point(x, y):
    return {'x': x, 'y': y}

def add_points(point1, point2):
    return create_point(point1['x'] + point2['x'], point1['y'] + point2['y'])

def subtract_points(point1, point2):
    return create_point(point1['x'] - point2['x'], point1['y'] - point2['y'])

# Example test cases
pointA = create_point(3, 4)
pointB = create_point(5, 6)

result_add = add_points(pointA, pointB)
print(result_add)  # Output should be {'x': 8, 'y': 10}

result_subtract = subtract_points(pointA, pointB)
print(result_subtract)  # Output should be {'x': -2, 'y': -2}
```

### Explanation:
- The `create_point` function takes two parameters (`x` and `y`) and returns a dictionary representing the point.
- The `add_points` function takes two points as arguments and returns a new point that is the sum of the coordinates of the input points.
- The `subtract_points` function takes two points as arguments and returns a new point that is the difference between the coordinates of the input points.

The example test cases demonstrate creating points, adding them together, and subtracting one from another.