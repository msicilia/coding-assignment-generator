Certainly! Below is the Python code for the `split_values` function that meets the specified requirements:

```python
def split_values(dictionary, key_list):
    # Initialize two empty lists to store values
    values_in_dict = []
    values_not_in_dict = []

    # Iterate over each element in the key_list
    for key in key_list:
        if key in dictionary:
            # If the key is in the dictionary, add its value to values_in_dict
            values_in_dict.append(dictionary[key])
        else:
            # If the key is not in the dictionary, add it to values_not_in_dict
            values_not_in_dict.append(key)

    return values_in_dict, values_not_in_dict

# Example test cases
def example_test_cases():
    # Test case 1: Empty dictionary and list
    dict1 = {}
    keys1 = []
    result1 = split_values(dict1, keys1)
    print(f"Test Case 1: {result1}")  # Output: ([], [])

    # Test case 2: Dictionary with some present and missing keys
    dict2 = {'a': 1, 'b': 2, 'c': 3}
    keys2 = ['a', 'd', 'c']
    result2 = split_values(dict2, keys2)
    print(f"Test Case 2: {result2}")  # Output: ([1, 3], ['d'])

    # Test case 3: Dictionary with all missing keys
    dict3 = {'x': 5, 'y': 6}
    keys3 = ['a', 'b', 'c']
    result3 = split_values(dict3, keys3)
    print(f"Test Case 3: {result3}")  # Output: ([], ['a', 'b', 'c'])

# Run example test cases
example_test_cases()
```

### Explanation:
1. **Function Definition**:
   - `split_values(dictionary, key_list)`: This function takes a dictionary and a list as input.

2. **Initialization**:
   - Two empty lists, `values_in_dict` and `values_not_in_dict`, are initialized to store the values of keys present and not present in the dictionary, respectively.

3. **Iteration**:
   - The function iterates over each key in the `key_list`.
   - If the key exists in the dictionary (`if key in dictionary:`), its corresponding value is added to `values_in_dict`.
   - If the key does not exist in the dictionary, the key itself is added to `values_not_in_dict`.

4. **Return**:
   - The function returns two lists: one with values from keys present in the dictionary and another with keys not present.

5. **Example Test Cases**:
   - Several test cases are provided to demonstrate the functionality of the function.
   - Each test case is run, and the results are printed.

This code adheres to the requirements by using dictionaries and a basic loop without employing match expressions or list comprehensions.