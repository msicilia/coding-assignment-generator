```python
import random

# Create a list of integers with random values in the range 1 to 20
random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(1, 20))

# Calculate the average of the values
total = 0
for number in random_numbers:
    total += number
average = total / len(random_numbers)

# Find the highest and lowest values
highest = random_numbers[0]
lowest = random_numbers[0]
for number in random_numbers:
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number

# Print the results
print("Random numbers:", random_numbers)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
```

**Example Output:**

```
Random numbers: [14, 7, 18, 3, 19, 1, 15, 8, 4, 10]
Average: 10.2
Highest: 19
Lowest: 1
```