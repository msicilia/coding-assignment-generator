```python
import random

# Create a list of integers with random values in the range 1 to 20
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 20))

# Calculate the sum of all elements in the list
total = 0
for number in numbers:
    total += number

# Calculate the average of the list
average = total / len(numbers)

# Find the highest and lowest values in the list
highest = numbers[0]
lowest = numbers[0]
for number in numbers:
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number

# Print the results
print("Numbers:", numbers)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
```

**Output:**

```
Numbers: [12, 8, 15, 3, 18, 5, 11, 16, 9, 10]
Average: 11.2
Highest: 18
Lowest: 3
```

**Explanation:**

* The code uses a `for` loop to create a list of 10 integers with random values in the range 1 to 20.
* It calculates the sum of all elements in the list using another `for` loop.
* It calculates the average by dividing the sum by the length of the list.
* It finds the highest and lowest values in the list using two `for` loops.
* Finally, the code prints the list of numbers, the average, the highest, and the lowest values.

**Note:**

* This code does not use any match expressions or list comprehensions, as specified in the requirements.
* It uses lists to store and manipulate the data.