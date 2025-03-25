**Answer:**

```python
import random

# Create a list of integers
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 20))

# Calculate the average
total = 0
for number in numbers:
    total += number
average = total / len(numbers)

# Find the highest and lowest values
highest = numbers[0]
lowest = numbers[0]
for number in numbers:
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number

# Print the results
print("List of numbers:", numbers)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
```

**Explanation:**

- The code satisfies all the requirements, including the use of lists, random number generation, and calculations of average, highest, and lowest values.
- The observations and assessments in the user messages are consistent with the code's functionality.

**Example Output:**

```
List of numbers: [5, 1, 15, 9, 2, 10, 3, 3, 13, 20]
Average: 8.1
Highest: 20
Lowest: 1
```

**Note:**

- The specific values in the output may vary due to the randomness of the generated numbers.
- The code can be run and tested to verify its functionality.