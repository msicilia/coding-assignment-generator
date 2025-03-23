 
```py
def dict_list(my_dict, my_list):
    in_dict = []
    not_in_dict = []
    for element in my_list:
        if element in my_dict:
            in_dict.append(my_dict[element])
        else:
            not_in_dict.append(element)
    return in_dict, not_in_dict
```
Example test cases:
```
test1 = dict({"a": 1, "b": 2, "c": 3})
test2 = ["a", "b", "d"]
print(dict_list(test1, test2)) # Output: ([1, 2], ["d"])

test3 = dict({"a": 1, "b": 2, "c": 3})
test4 = ["a", "b", "c"]
print(dict_list(test3, test4)) # Output: ([1, 2, 3], [])
```