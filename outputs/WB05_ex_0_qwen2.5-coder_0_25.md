Sure, I can help with that. Below is the Python code for a function that sums two lists of integers of equal length and returns another list containing the sum of the original ones element by element. This solution adheres to the constraints provided:

```python
def sum_lists(list1, list2):
    # Initialize an empty list to store the sums
    result_list = []
    
    # Iterate over the indices of the input lists
    for i in range(len(list1)):
        # Calculate the sum of the elements at index i and append it to result_list
        result_list.append(list1[i] + list2[i])
    
    # Return the resulting list containing the sums
    return result_list

# Example test cases
print(sum_lists([1, 2, 3], [4, 5, 6]))  # Output: [5, 7, 9]
print(sum_lists([0, -1, 2], [-3, 4, -5]))  # Output: [-3, 3, -3]
```

### Explanation:
1. **Initialization**: We start by initializing an empty list `result_list` to store the sums of corresponding elements from the two input lists.
2. **Iteration**: We use a `for` loop to iterate over the indices of the input lists. The `range(len(list1))` ensures that we go through each element in both lists up to their length.
3. **Summation and Appending**: Inside the loop, we calculate the sum of the corresponding elements from `list1` and `list2` using `list1[i] + list2[i]`, and append this sum to `result_list`.
4. **Return**: Finally, we return the `result_list` containing all the sums.

### Example Test Cases:
- The first test case sums `[1, 2, 3]` and `[4, 5, 6]`, resulting in `[5, 7, 9]`.
- The second test case sums `[0, -1, 2]` and `[-3, 4, -5]`, resulting in `[-3, 3, -3]`.

This function should work correctly for any two lists of integers of equal length, adhering to the constraints provided.