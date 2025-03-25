```py
def is_number_in_list(number, lst):
    if not lst:  # Base case: empty list
        return False
    elif lst[0] == number:  # Recursive case: first element matches the number
        return True
    else:  # Recursive case: continue searching the rest of the list
        return is_number_in_list(number, lst[1:])
```

This function can be used to search for a number in a list using recursion.