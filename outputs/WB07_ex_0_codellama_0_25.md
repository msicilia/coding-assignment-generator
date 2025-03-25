 
 Here's an example of how to write a recursive function in Python to check if a certain number is found in a list:
```
def contains(my_list, num):
    if len(my_list) == 0:
        return False
    elif my_list[0] == num:
        return True
    else:
        return contains(my_list[1:], num)
```
This function takes two arguments: `my_list`, which is the list to search, and `num`, which is the number to find. It uses a recursive approach by checking if the first element of the list is equal to the number we're looking for. If it is, it returns `True`. If not, it recursively calls itself with the rest of the list as an argument until it finds the number or reaches the end of the list. If it reaches the end of the list without finding the number, it returns `False`.

To test this function, we can use the following example:
```
print(contains([1, 2, 3, 4, 5], 3)) # True
print(contains([1, 2, 3, 4, 5], 6)) # False
print(contains([], 3)) # False
```
This will print `True`, `False`, and `False` respectively.