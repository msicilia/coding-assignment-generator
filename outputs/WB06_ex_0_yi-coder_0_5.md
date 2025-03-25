Here is an implementation that uses dictionaries as requested while also taking into account the restrictions specified:

```python
def create_point(x=0, y=0):
    return {'x': x, 'y': y}

def add_points(p1, p2):
    return {'x': p1['x'] + p2['x'], 'y': p1['y'] + p2['y']}

def subtract_points(p1, p2):
    return {'x': p1['x'] - p2['x'], 'y': p1['y'] - p2['y']}

# Test cases:
p1 = create_point(3, 4)
p2 = create_point(-1, 2)
print(add_points(p1, p2))  # Expected output is {'x': 2, 'y': 6} because of p1 + p2.
print(subtract_points(p1, p2)) # Expected output is {'x': 4, 'y': 2} because of p1 - p2.
```