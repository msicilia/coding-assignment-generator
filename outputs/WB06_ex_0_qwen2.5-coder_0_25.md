Here is the Python code to solve the problem:

```python
def create_point(x, y):
    return {'x': x, 'y': y}

def add_points(p1, p2):
    new_x = p1['x'] + p2['x']
    new_y = p1['y'] + p2['y']
    return create_point(new_x, new_y)

def subtract_points(p1, p2):
    new_x = p1['x'] - p2['x']
    new_y = p1['y'] - p2['y']
    return create_point(new_x, new_y)

# Example usage:
p1 = create_point(1, 2)
p2 = create_point(3, 4)

result_add = add_points(p1, p2)
print(result_add)  # Output: {'x': 4, 'y': 6}

result_subtract = subtract_points(p1, p2)
print(result_subtract)  # Output: {'x': -2, 'y': -2}
```

This code defines functions to create a point with given `x` and `y` coordinates (`create_point`), add two points together (`add_points`), and subtract one point from another (`subtract_points`). The example usage demonstrates how to use these functions.