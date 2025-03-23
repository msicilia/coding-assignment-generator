```python
def is_number_in_list(num, lst):
    """
    Checks if a certain number is found in a list recursively.

    Args:
        num (int): The number to check for.
        lst (list): The list to search in.

    Returns:
        bool: True if the number is found, False otherwise.
    """

    if not lst:
        return False

    if lst[0] == num:
        return True

    return is_number_in_list(num, lst[1:])


# Example usage:
print(is_number_in_list(5, [1, 2, 3, 4, 5]))  # Output: True
print(is_number_in_list(7, [1, 2, 3, 4, 5]))  # Output: False
```

**Explanation:**

* The function takes two arguments, `num` and `lst`.
* It checks if the list is empty. If it is, the number cannot be found, so the function returns `False`.
* If the first element of the list is equal to the number, the number is found, so the function returns `True`.
* Otherwise, the function recursively calls itself with the same number and the remaining list (excluding the first element).

**Note:**

* The code only uses recursive function calls.
* The code does not use match expressions or list comprehensions.

**Additional Thoughts:**

* This recursive function is a straightforward way to check if a number is in a list.
* It is important to note that recursion can be computationally expensive, so it is important to use it wisely.