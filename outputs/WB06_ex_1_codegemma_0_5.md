```python
def filter_dict_elements(dict_values, list_elements):
    dict_elements = set(dict_values.values())
    in_dict = []
    not_in_dict = []

    for element in list_elements:
        if element in dict_elements:
            in_dict.append(element)
        else:
            not_in_dict.append(element)

    return in_dict, not_in_dict
```

**Example Usage:**

```python
dict_values = {"a": 1, "b": 2, "c": 3}
list_elements = [1, 2, 3, 4, 5]

in_dict, not_in_dict = filter_dict_elements(dict_values, list_elements)

print("Elements in dictionary:", in_dict)
print("Elements not in dictionary:", not_in_dict)
```

**Output:**

```
Elements in dictionary: [1, 2, 3]
Elements not in dictionary: [4, 5]
```

**Explanation:**

- The function `filter_dict_elements()` takes two arguments: `dict_values` (a dictionary) and `list_elements` (a list).
- It creates a set of dictionary values and initializes two empty lists, `in_dict` and `not_in_dict`.
- It iterates through the `list_elements`.
- If an element is in the dictionary set, it is added to the `in_dict` list.
- Otherwise, it is added to the `not_in_dict` list.
- Finally, the function returns both lists.

**Note:**

- The code does not use match expressions or list comprehensions as specified in the task.
- It uses dictionaries as specified in the task.