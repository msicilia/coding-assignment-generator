```python
def sum_lists(list1, list2):
    """
    Sums two lists of integers of equal length and returns a new list containing the sum of the original ones element by element.

    Args:
        list1: The first list of integers.
        list2: The second list of integers.

    Returns:
        A new list containing the sum of the original ones element by element.
    """

    if len(list1) != len(list2):
        raise ValueError("Input lists must be of equal length.")

    summed_list = []

    for i in range(len(list1)):
        summed_list.append(list1[i] + list2[i])

    return summed_list


# Test case 1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = sum_lists(list1, list2)
print(result)  # Output: [5, 7, 9]

# Test case 2
list1 = [10, 20, 30]
list2 = [40, 50, 60]
result = sum_lists(list1, list2)
print(result)  # Output: [50, 70, 90]
```