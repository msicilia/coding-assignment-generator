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

    # Check if the lists are of equal length.
    if len(list1) != len(list2):
        raise ValueError("The lists must be of equal length.")

    # Create a new list to store the sums.
    sum_list = []

    # Iterate over the lists and add the corresponding elements.
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    # Return the new list.
    return sum_list
```

**Example Test Cases:**

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum_list = sum_lists(list1, list2)

assert sum_list == [5, 7, 9]
```