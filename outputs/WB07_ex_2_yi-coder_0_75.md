Here is one way to write this program using only recursion and without using match expressions or list comprehensions in Python:

```python
def count_digits(n):
    # Base case: if the number is less than 10, return 1
    if n < 10:
        return 1
    else: # Recursive case; reduce the problem size by one digit and recurse
        return 1 + count_digits(n // 10)

# Test cases
print(count_digits(56))   # Outputs: 2
print(count_digits(78934)) # Outputs: 5
```