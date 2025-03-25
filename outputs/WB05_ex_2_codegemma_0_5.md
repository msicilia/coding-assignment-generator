```python
import random

# Create a list of integers
numbers = []

# Initialize the list with random values
for i in range(10):
    numbers.append(random.randint(1, 20))

# Compute the average of the values
average = sum(numbers) / len(numbers)

# Find the highest and lowest value
highest = max(numbers)
lowest = min(numbers)

# Print the results
print("Numbers:", numbers)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
```