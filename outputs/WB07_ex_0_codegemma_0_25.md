```python
def find_number(num, my_list):
    """
    Checks if a certain number is found in a list recursively.

    Args:
        num: The number to search for.
        my_list: The list to search in.

    Returns:
        True if the number is found, False otherwise.
    """

    if not my_list:
        return False

    if my_list[0] == num:
        return True

    return find_number(num, my_list[1:])


# Example test cases
my_list = [1, 2, 3, 4, 5]

print(find_number(3, my_list))  # Output: True
print(find_number(6, my_list))  # Output: False
```

**Explanation:**

* The code defines a recursive function called `find_number()` with two arguments: `num` and `my_list`.
* The function checks if the list is empty. If it is, it returns `False`.
* If the first element of the list matches the number, it returns `True`.
* Otherwise, it recursively calls itself with the remaining elements of the list.

**Example Test Cases:**

* `my_list = [1, 2, 3, 4, 5]`
* `print(find_number(3, my_list))` should print `True`.
* `print(find_number(6, my_list))` should print `False`.

**Note:**

* The code does not use match expressions, list comprehensions, or any other forbidden Python elements.
* It follows the requirements of the task, including using recursive function calls.