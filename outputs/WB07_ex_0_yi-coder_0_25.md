Here's how it can be implemented in Python:

```python
def findNumberInList(lst, num): 
    if len(lst) == 0: # Base case for recursion when list is empty
        return False
    elif lst[0] == num: # Base case where the first element of the list matches our target number
        return True
    else: # Recursive step where we call function on rest of the list
        return findNumberInList(lst[1:],num)
  
# Test the function with some test cases.
print(findNumberInList([1,2,3,4,5], 3)) # It will return True because 3 is in the list.
print(findNumberInList(['a', 'b', 'c', 'd'], 'e')) # It will return False as 'e' is not in the list.
```