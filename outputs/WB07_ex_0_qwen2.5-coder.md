Certainly! Below is a Python code snippet for a recursive procedure that checks whether a certain number is found in a list. This implementation adheres to your specified constraints:

```python
def recursive_search(number, lst):
    # Base case: if the list is empty, the number is not found
    if not lst:
        return False
    
    # Check if the first element of the list matches the number
    if lst[0] == number:
        return True
    
    # Recursive call with the rest of the list
    return recursive_search(number, lst[1:])

# Example test cases:
print(recursive_search(3, [1, 2, 3, 4, 5]))  # Should return True
print(recursive_search(6, [1, 2, 3, 4, 5]))  # Should return False
print(recursive_search(0, []))               # Should return False
print(recursive_search(7, [7]))              # Should return True
```

### Explanation:

1. **Base Case**: The function first checks if the list `lst` is empty. If it is, it returns `False` because the number is not found in an empty list.

2. **Comparison**: It then checks if the first element of the list (`lst[0]`) matches the target number (`number`). If they match, it returns `True`.

3. **Recursive Call**: If the first element does not match the number, the function makes a recursive call to itself with the rest of the list (`lst[1:]`).

This procedure continues until it either finds the number (returns `True`) or exhausts the list (returns `False`). The example test cases demonstrate how the function works in different scenarios.