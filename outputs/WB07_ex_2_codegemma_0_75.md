```python
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

# Test cases
print(count_digits(12345))  # Output: 5
print(count_digits(0))  # Output: 1
print(count_digits(1000))  # Output: 4
```