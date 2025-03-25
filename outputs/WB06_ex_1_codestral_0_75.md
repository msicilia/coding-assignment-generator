 I will define a Python function called 'split_list' that takes two parameters: a dictionary and a list. The function will iterate over each item in the input list. For each item, it will check if the item exists as a key in the dictionary. If it does, the corresponding value will be appended to the 'values_in_dict' list; otherwise, the item itself will be appended to the 'values_not_in_dict' list. Finally, the function will return both lists as a tuple.

Here is the code for the 'split_list' function:

```python
def split_list(dictionary, input_list):
    values_in_dict = []
    values_not_in_dict = []

    for item in input_list:
        if item in dictionary:
            values_in_dict.append(dictionary[item])
        else:
            values_not_in_dict.append(item)

    return values_in_dict, values_not_in_dict
```

Now, let's test the function with some example inputs:

```python
# Example dictionary
d = {'a': 1, 'b': 2, 'c': 3}

# Example list
l = ['a', 'b', 'e', 'f']

result = split_list(d, l)
print(result)
```

Output:
```
([1, 2], ['e', 'f'])
```

In this example, the input dictionary `d` contains keys 'a', 'b', and 'c'. The input list `l` contains elements 'a', 'b', 'e', and 'f'. The function returns two lists: one containing the values of the elements that are present in the dictionary ([1, 2]), and another containing the elements that are not present in the dictionary (['e', 'f']).