Certainly! Below is the Python code for the function `filter_by_dict` that meets the specified requirements. The function will take a dictionary and a list as input and return two lists: one containing values from the dictionary where keys exist in the list, and another containing the remaining elements of the list.

```python
def filter_by_dict(dictionary, lst):
    values_in_dict = []
    values_not_in_dict = []

    for item in lst:
        if item in dictionary:
            values_in_dict.append(dictionary[item])
        else:
            values_not_in_dict.append(item)

    return values_in_dict, values_not_in_dict

# Example test cases
dict_example = {'a': 1, 'b': 2, 'c': 3}
list_example = ['a', 'b', 'd', 'e']

values_in_dict, values_not_in_dict = filter_by_dict(dict_example, list_example)
print("Values in dictionary:", values_in_dict)  # Output: Values in dictionary: [1, 2]
print("Values not in dictionary:", values_not_in_dict)  # Output: Values not in dictionary: ['d', 'e']
```

### Explanation:
1. **Function Definition**: The function `filter_by_dict` takes two parameters: a dictionary (`dictionary`) and a list (`lst`).
2. **Initialization**: Two empty lists, `values_in_dict` and `values_not_in_dict`, are initialized to store the results.
3. **Loop Through List**: A `for` loop iterates through each element in the input list `lst`.
4. **Check Membership**: For each element in the list, it checks if the element is a key in the dictionary using the `in` keyword.
5. **Conditional Append**:
   - If the element is a key in the dictionary, its corresponding value is appended to `values_in_dict`.
   - If the element is not a key in the dictionary, the element itself is appended to `values_not_in_dict`.
6. **Return Result**: The function returns two lists: `values_in_dict` and `values_not_in_dict`.

### Example Test Cases:
- **dict_example** contains keys `'a'`, `'b'`, and `'c'` with corresponding values `1`, `2`, and `3`.
- **list_example** contains elements `'a'`, `'b'`, `'d'`, and `'e'`.
  - The function should return:
    - `values_in_dict` containing `[1, 2]` (corresponding to keys `'a'` and `'b'`).
    - `values_not_in_dict` containing `['d', 'e']`.

This solution adheres to the requirements by not using match expressions or list comprehensions, and it uses dictionaries as specified.