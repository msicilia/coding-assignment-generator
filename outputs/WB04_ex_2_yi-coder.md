Here is an example of how you might solve this problem in Python:
```python
def generate_powers(n):
    for i in range(1, n+1):
        print(f"{i}: {2**i} {3**i} {5**i}")

# Read a positive integer from the user
try:
    n = int(input('Please enter a positive integer: '))
    if n <= 0:
        raise ValueError  # We explicitly raise an error if the input is not positive.
except ValueError:
    print('Invalid input! Please enter a positive integer.')
else:
    generate_powers(n)
```
In this code, we are defining a function `generate_powers` that takes in a single argument `n`. This function runs a loop from 1 to n (inclusive) and prints the power of 2,3 and 5 for each number in the range.

We then ask the user to enter a positive integer value using Python's built-in `input()` function. We ensure that this input is valid by wrapping it with a try/except block. If the entered value is not a positive integer, an error will be thrown and a message informing about the incorrect format of entry is displayed to the user.

If the user enters a valid positive integer, then we call our function `generate_powers` passing in the user's input `n` as the argument. This function prints out a series of lines where each line contains the power of 2,3 and 5 for the corresponding number from 1 to n (inclusive).