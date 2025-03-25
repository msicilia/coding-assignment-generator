
Here is an example solution that uses only lists and tuples:
```python
import random

# Initialize a list with random integers in the range 1..20
numbers = [random.randint(1, 20) for _ in range(5)]

# Compute the average of the values
average = sum(numbers) / len(numbers)

# Find the highest and lowest value
highest = max(numbers)
lowest = min(numbers)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
```
This code creates a list of 5 random integers in the range 1..20 using the `random.randint()` function, and then computes the average of those values using the `sum()` and `len()` functions. It then finds the highest and lowest value in the list using the `max()` and `min()` functions, and prints them to the console.