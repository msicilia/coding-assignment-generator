```python
def force(mass, acceleration):
    """
    Returns the force from the mass and acceleration.

    Args:
        mass: The mass of the object.
        acceleration: The acceleration of the object.

    Returns:
        The force of the object.
    """
    return mass * acceleration


# Test cases
mass1 = 10
acceleration1 = 5
force1 = force(mass1, acceleration1)

mass2 = 20
acceleration2 = 10
force2 = force(mass2, acceleration2)

print("Force 1:", force1)
print("Force 2:", force2)
```