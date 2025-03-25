  Here is an example of how to write such a function using only dictionaries:
```py
def get_in_and_out(my_dict, my_list):
    in_dict = []
    out_dict = []
    for item in my_list:
        if item in my_dict:
            in_dict.append(item)
        else:
            out_dict.append(item)
    return in_dict, out_dict
```
This function takes two inputs: a dictionary and a list. It iterates through the list and checks if each element is in the dictionary using the `in` operator. If it is, it appends that element to the first output list (`in_dict`). If not, it appends that element to the second output list (`out_dict`). Finally, it returns both output lists as a tuple.

Here are some test cases:
```py
test_dict = {'a': 1, 'b': 2, 'c': 3}
test_list = ['a', 'b', 'd']
in_out = get_in_and_out(test_dict, test_list)
print(in_out) # Output: (['a', 'b'], ['d'])
```
In this example, the input dictionary is `{'a': 1, 'b': 2, 'c': 3}`, and the input list is `['a', 'b', 'd']`. The function returns two lists as output: `['a', 'b']` and `['d']`.

Note that this function uses only dictionaries, so it does not use any regular expressions or other advanced Python features.