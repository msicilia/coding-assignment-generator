Here is your Python code to solve this problem using recursion:

```python
def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(int(n/10))

# Test cases
print(count_digits(54321))  # Outputs: 5
print(count_digits(9876))   # Outputs: 4
```

This task can be solved by writing a recursive function in Python. The base case for the recursion is when the number n is 0, where we just return 0 as there are no more digits left to count. If this isn't the base case then we add one to our recursive call on `count_digits(n // 10)`, effectively removing the last digit from the number and continuing the recursion until we reach the base case.