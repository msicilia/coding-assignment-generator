To solve this problem, we need to write a recursive function in Python that counts the number of digits in a given integer without using `match expressions` or `list comprehensions`. Here’s how you can do it:

### Step-by-Step Approach

1. **Base Case**: If the absolute value of the number is less than 10, return 1 because there's only one digit.
2. **Recursive Case**: Otherwise, recursively call the function with the integer divided by 10 and add 1 to the result.

### Example Code

```python
def count_digits(n):
    # Base case: if n has one digit, return 1
    if abs(n) < 10:
        return 1
    # Recursive case: count digits of n // 10 and add 1 for this digit
    else:
        return 1 + count_digits(n // 10)

# Example test cases
print(count_digits(123))  # Output should be 3
print(count_digits(-456)) # Output should be 3
print(count_digits(1))    # Output should be 1
print(count_digits(-1))   # Output should be 1
print(count_digits(9999)) # Output should be 4
```

### Explanation

- **Base Case**: The condition `abs(n) < 10` checks if the absolute value of `n` is less than 10. If true, it means that `n` has only one digit.
- **Recursive Case**: The function calls itself with `n // 10`, which effectively removes the last digit from `n`. It then adds 1 to account for the digit just removed.

### Additional Test Cases

To further validate the function, we can add more test cases that include edge scenarios:

```python
# Additional test cases
print(count_digits(1000)) # Output should be 4
print(count_digits(-12345)) # Output should be 5
print(count_digits(0))    # Output should be 1 (edge case)
```

### Full Code with All Test Cases

```python
def count_digits(n):
    # Base case: if n has one digit, return 1
    if abs(n) < 10:
        return 1
    # Recursive case: count digits of n // 10 and add 1 for this digit
    else:
        return 1 + count_digits(n // 10)

# Example test cases
print(count_digits(123))  # Output should be 3
print(count_digits(-456)) # Output should be 3
print(count_digits(1))    # Output should be 1
print(count_digits(-1))   # Output should be 1
print(count_digits(9999)) # Output should be 4

# Additional test cases
print(count_digits(1000)) # Output should be 4
print(count_digits(-12345)) # Output should be 5
print(count_digits(0))    # Output should be 1 (edge case)
```

This code should meet the requirements and handle various edge cases effectively.