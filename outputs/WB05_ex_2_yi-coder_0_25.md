Here is an example solution for your problem:

```python
import random

def calculate_stats():
    random_list = []
  
    # Initialize list with random values between 1 and 20
    for i in range(5):
        random_list.append(random.randint(1,20))

    print('List: ' + str(random_list))

    # Compute the average value of the elements in the list
    average = sum(random_list) / len(random_list)
    print('Average: ' + str(average))

    # Find the highest and lowest values in the list
    highest = max(random_list)
    lowest = min(random_list)

    print('Lowest Value: ' + str(lowest))
    print('Highest Value: ' + str(highest))

calculate_stats()
```
This program initializes a list of five random integers between 1 and 20. It calculates the average, finds the highest and lowest values in the list and prints them out. Please note that you cannot use match expressions or list comprehensions according to your problem's constraints. Hence we used simple loops for generating our lists.