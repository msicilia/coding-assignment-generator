Here is an example solution in Python:

```python
def force(mass, acceleration):
    """Compute force based on Newtown-Splace's law (F = m*a) """
    return mass * acceleration

# Test Cases
print(force(10, 5)) # Expected Output: 50
print(force(20, 3)) # Expected Output: 60
```

In the above code, we have implemented a function `force` which takes in mass and acceleration as parameters. The function returns the product of these two values, which is equivalent to the force according to Newton-Splace's law. This implementation follows good practice principles like modularity (separation of concerns), and adheres to Pythonic principles like keeping the code simple and easily understood.

We have also written some test cases at the end where we call this function with different input values to ensure its correctness.