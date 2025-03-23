
Here is an answer to the user task:
```py
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
```
Example test cases:
```py
p1 = Point(3, 4)
p2 = Point(5, 6)
print(p1 + p2) # should print (8, 10)
print(p1 - p2) # should print (-2, -2)
```