```python
def sum_lists(list1, list2):
    """
    Sums two lists of integers of equal length and returns another list containing the sum of the original ones element by element.

    Args:
        list1: The first list of integers.
        list2: The second list of integers.

    Returns:
        A list containing the sum of the original lists element by element.
    """

    if len(list1) != len(list2):
        raise ValueError("The two lists must be of equal length.")

    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list
```

**Example Test Cases:**

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum_list = sum_lists(list1, list2)

print(sum_list)  # Output: [5, 7, 9]
```