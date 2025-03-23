```python
def separate_values(dictionary, my_list):
    values_in_dict = []
    values_not_in_dict = []

    for value in my_list:
        if value in dictionary.values():
            values_in_dict.append(value)
        else:
            values_not_in_dict.append(value)

    return values_in_dict, values_not_in_dict
```

**Example Usage:**

```python
dictionary = {"a": 1, "b": 2, "c": 3}
my_list = [1, 2, 3, 4, 5]

values_in_dict, values_not_in_dict = separate_values(dictionary, my_list)

print("Values in dictionary:", values_in_dict)
print("Values not in dictionary:", values_not_in_dict)
```

**Output:**

```
Values in dictionary: [1, 2, 3]
Values not in dictionary: [4, 5]
```