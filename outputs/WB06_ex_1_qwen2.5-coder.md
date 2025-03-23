Certainly! Below is the Python code for the function `split_values_by_dict` that meets the specified requirements:

```python
def split_values_by_dict(dictionary, input_list):
    in_dict = []
    not_in_dict = []

    for item in input_list:
        if item in dictionary:
            in_dict.append(dictionary[item])
        else:
            not_in_dict.append(item)

    return in_dict, not_in_dict

# Example test cases
print(split_values_by_dict({'a': 1, 'b': 2, 'c': 3}, ['a', 'd', 'b']))  # ([1, 2], ['d'])
print(split_values_by_dict({'x': 'hello', 'y': 'world'}, ['x', 'z', 'y']))  # (['hello', 'world'], ['z'])
print(split_values_by_dict({}, [1, 2, 3]))  # ([], [1, 2, 3])
print(split_values_by_dict({'a': True}, []))  # ([], [])
```

### Explanation:
- The function `split_values_by_dict` takes two parameters: a dictionary and a list.
- Two empty lists, `in_dict` and `not_in_dict`, are initialized to store the results.
- A `for` loop iterates through each item in the input list.
- For each item, it checks if the item exists as a key in the dictionary.
  - If it does, the corresponding value is appended to `in_dict`.
  - If it doesn't, the item itself is appended to `not_in_dict`.
- Finally, the function returns the two lists.

### Example Test Cases:
1. `split_values_by_dict({'a': 1, 'b': 2, 'c': 3}, ['a', 'd', 'b'])` should return `([1, 2], ['d'])`.
2. `split_values_by_dict({'x': 'hello', 'y': 'world'}, ['x', 'z', 'y'])` should return `(['hello', 'world'], ['z'])`.
3. `split_values_by_dict({}, [1, 2, 3])` should return `([], [1, 2, 3])`.
4. `split_values_by_dict({'a': True}, [])` should return `([], [])`.

This implementation ensures that the function works as required without using match expressions or list comprehensions, adhering to the given constraints.