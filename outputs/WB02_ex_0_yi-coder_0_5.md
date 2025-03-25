Here is how you can implement this in Python:

```python
def force(mass, acceleration):
    """Return the force calculated by the formula: Force = Mass * Acceleration"""
    return mass * acceleration

# Testing our function with some test cases 
print(force(10,2)) # The output should be 20 as per given values.
print(force(50,4)) # The output should be 200 as per given values.
```

In this code, we first define a function called 'force' which calculates the force from the mass and acceleration provided to it as arguments. The calculation is simply done by multiplying these two quantities using `*` operator in Python.
Then for testing our function, we just need to call the function with test cases i.e. different masses and accelerations. We can print out the results returned by this function to verify if it's working as expected or not.