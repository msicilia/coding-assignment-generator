Thought: The Python code executed successfully and provided the expected output. The list of integers was initialized with random values between 1 and 20, and the average, highest, and lowest values were computed correctly.

The code used lists to store the random numbers and performed basic operations such as appending to a list, iterating through a list, and calculating the sum and length of a list. It also utilized built-in functions like `max()` and `min()` to find the highest and lowest values in the list.

Here is the final Python code that solves the problem:

```python
# Import the random module to generate random numbers
import random

# Initialize an empty list to store the random integers
my_list = []

# Populate the list with 10 random integers between 1 and 20
for _ in range(10):
    my_list.append(random.randint(1, 20))

# Compute the average of the values in the list
total_sum = 0
for num in my_list:
    total_sum += num

average = total_sum / len(my_list)

# Find the highest and lowest values in the list
highest_value = max(my_list)
lowest_value = min(my_list)

# Print the results
print("List:", my_list)
print("Average:", average)
print("Highest Value:", highest_value)
print("Lowest Value:", lowest_value)
```

This code meets all the requirements specified in the task, including using only lists or tuples and avoiding match expressions and list comprehensions.