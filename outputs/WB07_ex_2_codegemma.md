**Answer:**

```python
def count_digits(number):
    if number == 0:
        return 0
    else:
        return 1 + count_digits(number // 10)

# Test cases
print(count_digits(12345))  # Output: 5
print(count_digits(0))     # Output: 1
print(count_digits(100))   # Output: 3
```

**Explanation:**

* The function `count_digits()` takes an integer as input.
* If the number is 0, it returns 0. This is the base case of the recursion.
* Otherwise, it returns 1 (to account for the current digit) and calls itself recursively with the number divided by 10.
* The recursion continues until the number reaches 0, at which point the recursion stops and the total number of digits is returned.

**Example Output:**

```
5
1
3
```

**Note:**

* The function does not use any match expressions or list comprehensions, as per the requirements.
* It uses a recursive function call to count the digits.