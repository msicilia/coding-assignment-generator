Sure! Below is the Python code for a recursive procedure that checks whether a certain number is found in a list. The code does not use match expressions, list comprehensions, and adheres to the requirement of using only recursive function calls:

```python
def is_number_in_list(lst, num):
    # Base case: if the list is empty, return False
    if len(lst) == 0:
        return False
    
    # Check if the first element is equal to the number
    if lst[0] == num:
        return True
    
    # Recursive call with the rest of the list
    return is_number_in_list(lst[1:], num)

# Example test cases
print(is_number_in_list([1, 2, 3, 4, 5], 3))  # Output: True
print(is_number_in_list([10, 20, 30], 25))      # Output: False
print(is_number_in_list([], 7))                 # Output: False
```

### Explanation:
1. **Base Case**: If the list is empty (`len(lst) == 0`), return `False` because the number cannot be in an empty list.
2. **Check Element**: Check if the first element of the list (`lst[0]`) is equal to the number we are looking for (`num`). If it is, return `True`.
3. **Recursive Call**: If the first element is not the number, recursively call the function with the rest of the list (`lst[1:]`).

### Example Test Cases:
- `is_number_in_list([1, 2, 3, 4, 5], 3)` returns `True` because `3` is in the list.
- `is_number_in_list([10, 20, 30], 25)` returns `False` because `25` is not in the list.
- `is_number_in_list([], 7)` returns `False` because the list is empty.

This code adheres to all the provided requirements and demonstrates a clear recursive approach to solving the problem.