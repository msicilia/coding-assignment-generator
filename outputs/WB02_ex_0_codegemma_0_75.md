```python
def force(mass, acceleration):
    """
    Calculates the force from mass and acceleration.

    Args:
        mass: The mass of the object in kilograms.
        acceleration: The acceleration of the object in meters per second squared.

    Returns:
        The force in newtons.
    """

    return mass * acceleration

# Test cases
mass1 = 10  # kilograms
acceleration1 = 2  # meters per second squared

mass2 = 5  # kilograms
acceleration2 = 4  # meters per second squared

# Calculate the force for each test case
force1 = force(mass1, acceleration1)
force2 = force(mass2, acceleration2)

# Display the results
print("Force for mass", mass1, "and acceleration", acceleration1, "is", force1, "newtons.")
print("Force for mass", mass2, "and acceleration", acceleration2, "is", force2, "newtons.")
```

**Output:**

```
Force for mass 10 and acceleration 2 is 20 newtons.
Force for mass 5 and acceleration 4 is 20 newtons.
```

**Explanation:**

* The `force()` function calculates the force using the formula `mass * acceleration`.
* The tester program provides two test cases with the corresponding mass and acceleration values.
* The `force()` function is called to calculate the force for each test case.
* The results are displayed by printing the force values.

**Conclusion:**

This solution meets all the specified requirements, including the use of functions, modularity, and information hiding. It provides a working solution to the problem of calculating force based on mass and acceleration.