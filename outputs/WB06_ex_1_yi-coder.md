Here is a Python solution to this problem using dictionaries and loops/conditions:

```python
def solve_problem(dictionary, input_list):
    in_dict = []
    not_in_dict = []
  
    for element in input_list: 
        if element in dictionary: 
            in_dict.append(dictionary[element]) 
        else: 
            not_in_dict.append(element) 

    return in_dict, not_in_dict
```
This function takes a dictionary and a list as input and returns two lists - one with all the values of those elements from the given list that are keys in the provided dictionary, and another one with the rest. It uses an if-else condition structure to check whether or not each element of the list is a key in the dictionary.
  
You can test this function with different inputs:
```python 
print(solve_problem({'a':1, 'b':2, 'c':3}, ['a','d','b','e','c']))
# Output will be ([1, 2, 3], ['d', 'e'])
```