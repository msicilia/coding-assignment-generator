```python
def count_digits(n):
    """
    Counts the number of digits in an integer recursively.

    Args:
        n (int): The integer to count the digits of.

    Returns:
        int: The number of digits in n.
    """

    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)


# Example test cases
print(count_digits(12345))  # Output: 5
print(count_digits(0))     # Output: 1
print(count_digits(100))   # Output: 3
```