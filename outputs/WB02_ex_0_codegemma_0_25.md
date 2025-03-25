```python
def force(mass, acceleration):
    """
    Returns the value of the physical quantity force from the mass and acceleration values received as parameters.

    Args:
        mass: The mass of the object in kilograms.
        acceleration: The acceleration of the object in meters per second squared.

    Returns:
        The value of the force in newtons.
    """

    return mass * acceleration


# Test cases
mass1 = 2.0
acceleration1 = 3.0
force1 = force(mass1, acceleration1)

mass2 = 4.0
acceleration2 = 2.0
force2 = force(mass2, acceleration2)

# Print the results
print("Force 1:", force1)
print("Force 2:", force2)
```

**Conclusion:**

The code successfully calculates the force for two test cases with given mass and acceleration values. There are no syntax errors or other issues.

**Additional Observations:**

- The code follows best practices for modularity.
- The use of functions makes the code reusable and maintainable.
- The code is free of data structures, loops, and conditional statements, as specified.

**Suggestions:**

- The code can be further extended to include more test cases or to handle different types of objects.
- Additional documentation could be added to clarify the functionality of the code.

**Overall Assessment:**

The code is well-written and functional, meeting all of the specified requirements.