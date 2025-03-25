Here is an example solution for your problem:

```python
import random

# Initializing list with random integers between 1 to 20
numbers = [random.randint(1, 20) for _ in range(10)]
print('List:', numbers)

min_value = min(numbers)  # Finding minimum value from our list
max_value = max(numbers)   # Finding maximum value from our list
avg_value = sum(numbers)/len(numbers) # Calculating average (mean) value from our list

print('Min Value:', min_value) 
print('Max Value:', max_value)  
print('Average Value:', avg_value)   
```