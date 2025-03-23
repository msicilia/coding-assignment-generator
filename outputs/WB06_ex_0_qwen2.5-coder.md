Thoughts:

The task requires implementing a simple structure to represent points in a 2D space and functions to add and subtract these points using dictionaries.

To achieve this, we need:
1. A dictionary to represent a point with 'x' and 'y' coordinates.
2. Functions `add_points` and `subtract_points` that take two points as input and return the result of adding or subtracting them.

The functions should use dictionary operations directly without using match expressions or list comprehensions.

Example test cases can be provided to demonstrate the functionality of the implemented functions.

Implementation steps:
1. Define a function `make_point(x, y)` to create a point dictionary.
2. Implement the `add_points(p1, p2)` function that adds two points.
3. Implement the `subtract_points(p1, p2)` function that subtracts one point from another.
4. Write example test cases to demonstrate the functionality of the implemented functions.

Example test case:
```python
pointA = make_point(3, 5)
pointB = make_point(1, 7)
sum_point = add_points(pointA, pointB)  # Should return {'x': 4, 'y': 12}
diff_point = subtract_points(pointA, pointB)  # Should return {'x': 2, 'y': -2}
```

This implementation follows the requirements by using dictionaries and providing example test cases without using match expressions or list comprehensions.