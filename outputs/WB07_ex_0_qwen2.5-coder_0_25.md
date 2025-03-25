Certainly! Below is a Python code snippet for a recursive procedure that checks whether or not a certain number is found in a list. This function adheres to the constraints provided, such as using only recursive function calls and avoiding match expressions and list comprehensions.

```python
def recursive_search(target, lst):
    # Base case: if the list is empty, the number is not in the list
    if len(lst) == 0:
        return False
    
    # Check if the first element matches the target
    if lst[0] == target:
        return True
    
    # Recursively search in the rest of the list
    return recursive_search(target, lst[1:])

# Test case 1: Number is in the list
print(recursive_search(3, [1, 2, 3, 4, 5]))  # Expected output: True

# Test case 2: Number is not in the list
print(recursive_search(6, [1, 2, 3, 4, 5]))  # Expected output: False

# Test case 3: Empty list
print(recursive_search(0, []))  # Expected output: False

# Test case 4: Single element list where the number is present
print(recursive_search(7, [7]))  # Expected output: True

# Test case 5: Single element list where the number is not present
print(recursive_search(8, [9]))  # Expected output: False
```

### Explanation:
1. **Base Case**: If the list (`lst`) is empty, it means we have checked all elements and the target is not found. Therefore, return `False`.
2. **Recursive Case**:
   - Check if the first element of the list (`lst[0]`) matches the target.
   - If it does, return `True` because we have found the target.
   - If it does not, recursively call `recursive_search` with the rest of the list (`lst[1:]`).

### Example Test Cases:
- **Test Case 1**: The number `3` is in the list `[1, 2, 3, 4, 5]`, so the output should be `True`.
- **Test Case 2**: The number `6` is not in the list `[1, 2, 3, 4, 5]`, so the output should be `False`.
- **Test Case 3**: The list is empty, so the output should be `False`.
- **Test Case 4**: The list contains only one element which is the target `7`, so the output should be `True`.
- **Test Case 5**: The list contains only one element which is not the target `8`, so the output should be `False`.

This function efficiently checks for the presence of a target number in a list using recursion, as per the provided constraints.