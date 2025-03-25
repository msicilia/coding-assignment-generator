Sure! Here's how you can implement the `force` function and a tester program following the provided requirements:

1. **Force Function**: This function will take two parameters: `mass` and `acceleration`. It will return the calculated force using the formula \( F = m \times a \).

2. **Tester Program**: This program will call the `force` function with different test cases and print the results.

Here's the code:

```python
def force(mass, acceleration):
    # Calculate force using the formula F = m * a
    return mass * acceleration

def test_force():
    # Test case 1: Mass = 5 kg, Acceleration = 3 m/s^2
    mass1 = 5
    acceleration1 = 3
    result1 = force(mass1, acceleration1)
    print(f"Test Case 1:")
    print(f"Mass: {mass1} kg, Acceleration: {acceleration1} m/s^2")
    print(f"Force: {result1} N")

    # Test case 2: Mass = 2 kg, Acceleration = 4 m/s^2
    mass2 = 2
    acceleration2 = 4
    result2 = force(mass2, acceleration2)
    print("\nTest Case 2:")
    print(f"Mass: {mass2} kg, Acceleration: {acceleration2} m/s^2")
    print(f"Force: {result2} N")

# Run the tester program
test_force()
```

### Explanation:

1. **force Function**:
   - The `force` function takes two parameters: `mass` and `acceleration`.
   - It calculates the force using the formula \( F = m \times a \) and returns the result.

2. **test_force Function**:
   - This function defines two test cases.
   - For each test case, it calls the `force` function with the specified mass and acceleration values.
   - It prints the results for each test case in a formatted manner.

### Good Practices of Modularity:

- **Information Hiding**: The `force` function encapsulates the calculation logic, hiding the details from the user. The user only needs to call this function with the required parameters.
- **Use of Functions**: Both the `force` and `test_force` functions are modular. They perform specific tasks independently and can be reused in different parts of a program or even in different programs.

### Example Test Cases:

- **Test Case 1**: Mass = 5 kg, Acceleration = 3 m/s^2
  - Expected Force: \( 5 \times 3 = 15 \) N

- **Test Case 2**: Mass = 2 kg, Acceleration = 4 m/s^2
  - Expected Force: \( 2 \times 4 = 8 \) N

When you run the `test_force` function, it will display the calculated force for each test case, following the good practices of modularity.