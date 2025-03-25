Here's a solution using recursion without match expressions, list comprehensions, and any other Python features that would make this easier (aside from standard list methods):

```python
def check_number_in_list(lst, num):
    # Base case: if the list is empty, return False
    if len(lst) == 0:
        return False
    else:
        # If the first element of the list matches the number, return True
        if lst[0] == num:
            return True
        else:
            # Otherwise, remove the first item from the list and continue checking
            return check_number_in_list(lst[1:], num)

def test():
    assert check_number_in_list([1,2,3,4,5], 5) == True
    assert check_number_in_list([1,2,3,4,5], 6) == False
    assert check_number_in_list([], 1) == False
    print("All tests passed.")

test()
```

This program will print "All tests passed." if the `check_number_in_list` function works as expected.