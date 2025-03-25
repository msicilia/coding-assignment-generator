To solve the problem of checking whether a certain number is present in a list using recursion, you can use the following approach:

1. Define a function `contains` that takes two arguments: the list to search and the number to search for.
2. If the list is empty, return False.
3. Check if the first element of the list is equal to the number we are searching for. If it is, return True.
4. Recursively call the function `contains` with the rest of the list and the same number.
5. Return the result of the recursive call.

Here's an example implementation in Python:
```
def contains(my_list, num):
    if len(my_list) == 0:
        return False
    elif my_list[0] == num:
        return True
    else:
        return contains(my_list[1:], num)
```
You can test this function with the following example inputs and expected outputs:

* `contains([1, 2, 3], 4)` should return False.
* `contains([1, 2, 3], 3)` should return True.
* `contains([1, 2, 3, 4], 5)` should return False.
* `contains([1, 2, 3, 4], 4)` should return True.

I hope this helps! Let me know if you have any questions or need further clarification.