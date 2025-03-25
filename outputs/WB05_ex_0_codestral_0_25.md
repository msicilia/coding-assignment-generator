 Here is the Python code to solve the problem, according to your instructions:

```python
def sum_lists(list1, list2):
    if len(list1) != len(list2):
        return "Error: Input lists must have equal length."

    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result
```

   This function takes two lists as input, checks if they have equal lengths, and then iterates through each element of the lists, adding them together and appending the sum to a new result list. If the input lists do not have equal length, the function returns an error message.

   Here are some example test cases you might use with this function:

```python
print(sum_lists([1, 2, 3], [4, 5, 6]))  # Outputs: [5, 7, 9]
print(sum_lists([10, 20, 30], [5, -5, -10]))  # Outputs: [15, 15, 20]
print(sum_lists([1, 2, 3], [4, 5]))  # Outputs: Error message
```