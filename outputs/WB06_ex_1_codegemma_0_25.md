```python
def filter_list_by_dict(dic, lst):
    in_dict = []
    not_in_dict = []

    for item in lst:
        if item in dic.values():
            in_dict.append(item)
        else:
            not_in_dict.append(item)

    return in_dict, not_in_dict
```

**Example Usage:**

```python
dic = {"a": 1, "b": 2, "c": 3}
lst = [1, 2, 3, 4, 5]

in_dict, not_in_dict = filter_list_by_dict(dic, lst)

print("Values in dictionary:", in_dict)
print("Values not in dictionary:", not_in_dict)
```

**Output:**

```
Values in dictionary: [1, 2, 3]
Values not in dictionary: [4, 5]
```

**Note:**

* The function uses a `for` loop to iterate over the list.
* It checks if each element is present in the dictionary using the `in` operator.
* If an element is present, it is added to the `in_dict` list.
* Otherwise, it is added to the `not_in_dict` list.
* The function returns two lists: `in_dict` and `not_in_dict`.