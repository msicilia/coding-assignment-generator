Thoughts: To solve this problem, we need to create a list of integers with random values between 1 and 20. Then, we will compute the average, find the highest and the lowest values in the list.

Here's how we can do it step-by-step:

1. Import the `random` module to generate random numbers.
2. Create an empty list to store the random integers.
3. Use a loop to populate the list with 20 random integers between 1 and 20.
4. Initialize variables to keep track of the sum, highest value, and lowest value.
5. Iterate through the list to calculate the sum, update the highest and lowest values.
6. Compute the average by dividing the sum by the number of elements in the list.
7. Print the results.

Code:
```py
import random

# Step 1: Create an empty list to store random integers
random_integers = []

# Step 2: Populate the list with 20 random integers between 1 and 20
for _ in range(20):
    random_integers.append(random.randint(1, 20))

# Initialize variables for sum, highest value, and lowest value
total_sum = 0
highest_value = random_integers[0]
lowest_value = random_integers[0]

# Step 3: Iterate through the list to calculate the sum, update the highest and lowest values
for num in random_integers:
    total_sum += num
    if num > highest_value:
        highest_value = num
    if num < lowest_value:
        lowest_value = num

# Step 4: Compute the average
average = total_sum / len(random_integers)

# Step 5: Print the results
print("List of random integers:", random_integers)
print("Average:", average)
print("Highest value:", highest_value)
print("Lowest value:", lowest_value)
```

This code will correctly create a list of random integers between 1 and 20, compute the average, find the highest and lowest values, and print them. The output matches our expectations.