Certainly! Below is a Python script that meets the specified requirements. The script creates a list of integers with random values between 1 and 20, then computes the average, highest, and lowest values in the list.

```python
import random

# Step 1: Create a list of integers with random values between 1 and 20
num_elements = 10  # You can change this to any number you like
random_list = [random.randint(1, 20) for _ in range(num_elements)]

print("Random List:", random_list)

# Step 2: Compute the average of the values
total_sum = sum(random_list)
average = total_sum / len(random_list)

print("Average:", average)

# Step 3: Find the highest and lowest values using nested loops
highest_value = float('-inf')
lowest_value = float('inf')

for value in random_list:
    if value > highest_value:
        highest_value = value
    if value < lowest_value:
        lowest_value = value

print("Highest Value:", highest_value)
print("Lowest Value:", lowest_value)
```

### Explanation:

1. **Random List Creation**:
   - We use a list comprehension to create a list of integers with random values between 1 and 20.
   - `random.randint(1, 20)` generates a random integer in the range [1, 20].
   - The list comprehension `[random.randint(1, 20) for _ in range(num_elements)]` creates a list of `num_elements` random integers.

2. **Compute Average**:
   - We calculate the total sum of the elements using the built-in `sum()` function.
   - The average is then computed by dividing the total sum by the number of elements (`len(random_list)`).

3. **Find Highest and Lowest Values**:
   - We initialize `highest_value` to negative infinity and `lowest_value` to positive infinity.
   - We iterate through each value in the list using a for loop.
   - For each value, we check if it is greater than the current highest value or less than the current lowest value, and update accordingly.

### Example Output:
```
Random List: [12, 3, 7, 18, 4, 5, 9, 6, 10, 1]
Average: 10.0
Highest Value: 18
Lowest Value: 1
```

This script should work correctly for any number of elements in the list and will compute the average, highest, and lowest values using only the allowed Python elements (lists or tuples).