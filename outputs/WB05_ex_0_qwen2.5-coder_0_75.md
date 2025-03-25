Certainly! Below is the Python code to solve the problem as described. The function `sum_lists` takes two lists of integers of equal length and returns a new list containing the element-wise sums. No match expressions or list comprehensions are used, and only basic lists or tuples are utilized.

```python
def sum_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    
    return result

# Example test cases
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = sum_lists(list1, list2)
print(result)  # Output: [5, 7, 9]

list1 = [10, 20, 30]
list2 = [1, 2, 3]
result = sum_lists(list1, list2)
print(result)  # Output: [11, 22, 33]
```

### Explanation:
1. **Function Definition**: The function `sum_lists` is defined to take two arguments, `list1` and `list2`.
2. **Length Check**: The function first checks if the lengths of `list1` and `list2` are equal. If not, it raises a `ValueError`.
3. **Result Initialization**: An empty list `result` is initialized to store the sums.
4. **Element-wise Summation**: A `for` loop iterates over the indices of the lists (using `range(len(list1))`). For each index `i`, it appends the sum of `list1[i]` and `list2[i]` to the `result` list.
5. **Return Statement**: Finally, the function returns the `result` list containing the element-wise sums.

### Example Test Cases:
- The first test case sums `[1, 2, 3]` and `[4, 5, 6]`, resulting in `[5, 7, 9]`.
- The second test case sums `[10, 20, 30]` and `[1, 2, 3]`, resulting in `[11, 22, 33]`.

This function meets all the requirements specified in the problem statement.