Here's how you can define such a function, which we will call "is_in_list":

```python
def is_in_list(n, lst):
    # Base case: if the list is empty and n hasn't been found yet, it isn't in the list.
    if not lst: 
        return False

    # Recursive case: if the first element of the list matches n, then n is in the list.
    elif lst[0] == n: 
        return True
    else:  # Otherwise continue searching the rest of the list.
        return is_in_list(n, lst[1:]) # This is a slice operation that gives you all elements from index 1 onwards.
```
You can test this function with these examples:

```python
print(is_in_list(42, [13, 42, 89]))  # Should print True as 42 is in the list.
print(is_in_list('a', ['b', 'c']))    # Should print False as 'a' isn't in this list.
```