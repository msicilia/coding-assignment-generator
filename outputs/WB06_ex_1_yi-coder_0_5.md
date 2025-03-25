Here is an implementation of this problem in Python:
```python
def split_list_into_two(input_dict, input_list):
    in_dict = []
    not_in_dict = []
    for item in input_list:
        if item in input_dict:
            in_dict.append(item)
        else:
            not_in_dict.append(item)
    return in_dict, not_in_dict
```
You can use the following test cases to check your function:
```python
# Test Case 1
print(split_list_into_two({'a':1, 'b':2, 'c':3}, ['a', 'b', 'd'])) # Expected output: (['a', 'b'], ['d'])

# Test Case 2
print(split_list_into_two({'x':10, 'y':20, 'z':30}, ['w', 'x', 'y', 'z', 'a'])) # Expected output: (['x', 'y', 'z'], ['w', 'a'])
```