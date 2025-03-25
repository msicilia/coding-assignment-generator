```python
def find_elements_in_dict(dictionary, lst):
    """
    Receives a dictionary and a list and generates as output two lists: one with all the values of those elements of the list that are in the dictionary, and another one with those that are NOT in the dictionary.

    Args:
        dictionary: The dictionary to search in.
        lst: The list of elements to search for.

    Returns:
        A tuple containing two lists: one with elements in the dictionary, and another with elements not in the dictionary.
    """

    elements_in_dict = []
    elements_not_in_dict = []

    for element in lst:
        if element in dictionary:
            elements_in_dict.append(element)
        else:
            elements_not_in_dict.append(element)

    return elements_in_dict, elements_not_in_dict
```

**Example usage:**

```python
dictionary = {"a": 1, "b": 2, "c": 3}
lst = [1, 2, 3, 4, 5]

elements_in_dict, elements_not_in_dict = find_elements_in_dict(dictionary, lst)

print("Elements in dictionary:", elements_in_dict)
print("Elements not in dictionary:", elements_not_in_dict)
```

**Output:**

```
Elements in dictionary: [1, 2, 3]
Elements not in dictionary: [4, 5]
```