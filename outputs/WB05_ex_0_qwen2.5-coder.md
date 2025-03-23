Certainly! Below is a Python function that sums two lists of integers of equal length and returns another list containing the sum of the original ones element by element. This function adheres to the constraints provided, avoiding match expressions, list comprehensions, and using only lists or tuples.

```python
def sum_lists(list1, list2):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the indices of the input lists
    for i in range(len(list1)):
        # Append the sum of corresponding elements from both lists to the result list
        result.append(list1[i] + list2[i])
    
    return result

# Example test cases
print(sum_lists([], []))  # Output: []
print(sum_lists([1, 2, 3], [4, 5, 6]))  # Output: [5, 7, 9]
print(sum_lists([-1, -2, -3], [-4, -5, -6]))  # Output: [-5, -7, -9]
```

Explanation:
1. The function `sum_lists` takes two lists, `list1` and `list2`, as input.
2. It initializes an empty list called `result` to store the sums of corresponding elements.
3. It iterates over the indices of the input lists using a `for` loop.
4. For each index `i`, it appends the sum of `list1[i]` and `list2[i]` to the `result` list.
5. Finally, it returns the `result` list containing the sums.

This function adheres to the constraints provided and demonstrates how to achieve the desired functionality using only lists or tuples and basic loops.