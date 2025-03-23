Here is how you can solve the problem:
```python
import random

def create_random_list(size):
    return [random.randint(1, 20) for _ in range(size)]

def compute_average(lst):
    return sum(lst) / len(lst)

def find_max_min(lst):
    return max(lst), min(lst)

# Test the functions with a list of 10 integers.
random_list = create_random_list(10)
average, (maximum, minimum) = compute_average(random_list), find_max_min(random_list)
print('Randomly Generated List:', random_list)
print('Average Value:', average)
print('Highest Value in the list:', maximum)
print('Lowest Value in the list:', minimum)
```