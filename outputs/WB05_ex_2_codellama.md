
Here is an example of how you can solve this problem without using list comprehensions:
```python
import random

# Initialize a list with random integers between 1 and 20
my_list = []
for i in range(5):
    my_list.append(random.randint(1, 20))

# Compute the average of the values
average = sum(my_list) / len(my_list)
print(f"Average: {average}")

# Find the highest and lowest value in the list
highest = my_list[0]
lowest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > highest:
        highest = my_list[i]
    elif my_list[i] < lowest:
        lowest = my_list[i]
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
```
This code will generate a list of 5 random integers between 1 and 20, compute the average of the values, find the highest and lowest value in the list.