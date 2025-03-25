Here is an example solution based on the problem description:
```python
def compute_force(mass, acceleration): 
    """Return the force given by F = m*a where m is mass and a is acceleration. """
    return mass * acceleration
  
# Define a function for testing our 'compute_force' function.
def test_compute_force():
    """Test the 'compute_force' function with some example cases."""
    # Test case 1: A body of mass 5 kg is accelerating at 2 m/s^2, what is the force applied to it?
    assert compute_force(5, 2) == 10  
    # Test case 2: A body of mass 7 kg is accelerating at 3 m/s^2, what is the force applied to it?
    assert compute_force(7, 3) == 21  
    # Test case 3: A body of mass 9 kg is accelerating at 4 m/s^2, what is the force applied to it?
    assert compute_force(9, 4) == 36  
    print("All test cases passed.")

test_compute_force()
```
This code first defines a function `compute_force` that calculates and returns the force given by the formula F = m*a (where 'm' is mass and 'a' is acceleration). 
Then, another function named `test_compute_force` is defined to test our previous function using some example cases. 
Finally, we call this testing function to check if the implementation of the main function is correct or not.