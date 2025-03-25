 I will provide a Python code snippet for a recursive function named `check_number` to solve the problem described. This function will take a target number and a list as inputs, then it will check if that target number exists within the given list using recursion.

Here is my plan:
- Define a recursive function `check_number(num, lst)`.
- The base case of this recursive function would be when the input list is empty. In such case, we return False as the number has not been found in an empty list.
- If the first element of the list matches with our target number, then we return True.
- If neither base case is met, the function will call itself recursively with the rest of the list (all elements except the first one). This approach will shrink the problem size until it finds the target number or exhausts all possibilities in the list.
- Finally, I'll include some test cases to demonstrate that the function works as expected.

Let's write and execute this Python code:

```python
def check_number(num, lst):
    if len(lst) == 0:
        return False
    elif lst[0] == num:
        return True
    else:
        return check_number(num, lst[1:])

# Test cases
print(check_number(5, [1, 2, 3, 4, 5]))  # Expected output: True
print(check_number(6, [1, 2, 3, 4, 5]))  # Expected output: False
```
```python
def check_number(num, lst):
    if len(lst) == 0:
        return False
    elif lst[0] == num:
        return True
    else:
        return check_number(num, lst[1:])

# Test cases
print(check_number(5, [1, 2, 3, 4, 5]))  # Expected output: True
print(check_number(6, [1, 2, 3, 4, 5]))  # Expected output: False
```