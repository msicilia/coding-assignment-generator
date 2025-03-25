 
Here is an example of how you can solve this problem using Python:
```
def get_values_not_in_dict(my_dict, my_list):
    values_in_dict = []
    values_not_in_dict = []
    for value in my_list:
        if value in my_dict:
            values_in_dict.append(value)
        else:
            values_not_in_dict.append(value)
    return (values_in_dict, values_not_in_dict)
```
You can then use this function to solve the problem by calling it with appropriate arguments, for example:
```
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = ['a', 'b', 'd']
values_in_dict, values_not_in_dict = get_values_not_in_dict(my_dict, my_list)
print(values_in_dict)  # Output: ['a', 'b']
print(values_not_in_dict)  # Output: ['d']
```
This code defines a function called `get_values_not_in_dict` that takes two arguments: a dictionary and a list. It then uses a for loop to iterate through the elements of the list, and checks if each element is in the dictionary using the `in` operator. If it is, it appends the value to the first list, otherwise it appends it to the second list. Finally, it returns both lists as the output of the function.
You can then use this function to solve the problem by calling it with appropriate arguments, for example:
```
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = ['a', 'b', 'd']
values_in_dict, values_not_in_dict = get_values_not_in_dict(my_dict, my_list)
print(values_in_dict)  # Output: ['a', 'b']
print(values_not_in_dict)  # Output: ['d']
```
This code creates a dictionary called `my_dict` with three key-value pairs. It then creates a list called `my_list` with three elements, where the first two elements are keys in the dictionary and the third element is not a key. Finally, it calls the `get_values_not_in_dict` function with the `my_dict` and `my_list` arguments, and prints out the output lists. The output lists contain the values that were found in the dictionary (i.e., ['a', 'b']) and those that were not found in the dictionary (i.e., ['d']).