```python
def is_number_in_list(num, lst):
    if not lst:
        return False

    if lst[0] == num:
        return True

    return is_number_in_list(num, lst[1:])


print(is_number_in_list(5, [1, 2, 3, 4, 5]))  # True
print(is_number_in_list(6, [1, 2, 3, 4, 5]))  # False
```

**Explanation:**

* The function `is_number_in_list` takes two arguments: `num` (the number to search for) and `lst` (the list to search in).
* If the list is empty, the function returns `False`.
* If the first element of the list is equal to `num`, the function returns `True`.
* Otherwise, the function recursively calls itself with the same `num` and the remaining elements of the list.

**Example Usage:**

```python
print(is_number_in_list(5, [1, 2, 3, 4, 5]))  # True
print(is_number_in_list(6, [1, 2, 3, 4, 5]))  # False
```

**Output:**

```
True
False
```

**Note:**

* The function does not use match expressions or list comprehensions.
* The function is recursive and calls itself until it finds the number or exhausts the list.