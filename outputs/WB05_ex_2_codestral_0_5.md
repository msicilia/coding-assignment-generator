 I will write Python code to create a list of 10 random integers between 1 and 20. To do this, I'll use the `random` module's `randint()` function within a loop that appends each new integer to our list. The length of the list is not specified, so I will assume it to be 10 for demonstration purposes.

   After creating the list, I will compute its average by summing all elements and dividing by the total number of elements (which in this case is 10). To find the highest value, I'll use the `max()` function, while to get the lowest value, I'll use the `min()` function.

Here's how you can do it:
```python
import random

# Initialize an empty list
numbers = []

# Populate the list with 10 random integers between 1 and 20
for _ in range(10):
    numbers.append(random.randint(1, 20))

# Compute the average of the values
average = sum(numbers) / len(numbers)

# Find the highest value
highest_value = max(numbers)

# Find the lowest value
lowest_value = min(numbers)

# Print the results
print("List of numbers:", numbers)
print("Average of the values:", average)
print("Highest value:", highest_value)
print("Lowest value:", lowest_value)
```

Remember that since we're using random numbers, each time you run this code, you may get a different list and thus a different average, highest value, and lowest value.