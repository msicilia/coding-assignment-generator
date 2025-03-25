 The Python code to solve this problem has been successfully executed, returning the expected outputs for the test cases. Here is the function:

```python
def sum_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result
```

This function takes two lists of equal length as inputs and returns a new list containing the sum of the corresponding elements from each input list. This solution adheres to all given requirements, using only standard Python loops and lists or tuples. The test cases `print(sum_lists([1, 2, 3], [4, 5, 6]))` and `print(sum_lists([0, -1, -2], [-3, -4, -5]))` returned the expected outputs `[5, 7, 9]` and `[-3, -5, -7]`, respectively.