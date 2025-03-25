```python
def sum_lists(list1, list2):
    """
    Sums two lists of integers of equal length and returns another list containing the sum of the original ones element by element.

    Args:
        list1: The first list of integers.
        list2: The second list of integers.

    Returns:
        A list containing the sum of the original elements element by element.
    """

    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length.")

    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result
```

**Example Usage:**

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = sum_lists(list1, list2)

print(result)  # Output: [5, 7, 9]
```

**Additional Notes:**

* The code uses a `for` loop to iterate over the elements of both lists.
* It checks if the lists are of equal length using `len()` and raises a `ValueError` if they are not.
* It appends the sum of each pair of elements to the `result` list.
* The `result` list is returned as the result of the function.