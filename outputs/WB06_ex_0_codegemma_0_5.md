```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Point(self.x - other.x, self.y - other.y)

# Example usage
point1 = Point(2, 3)
point2 = Point(4, 5)

# Addition
point3 = point1.add(point2)

# Subtraction
point4 = point1.subtract(point2)

# Print the results
print("Point 1:", point1)
print("Point 2:", point2)
print("Point 3 (Addition):", point3)
print("Point 4 (Subtraction):", point4)
```