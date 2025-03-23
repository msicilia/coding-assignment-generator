Here is how you can write this function in Python using only tuples for input:
```python
def add_lists(list1, list2):
    result = []
    for i in range(len(list1)): 
        result.append(list1[i] + list2[i]) 
    return tuple(result)
```
You can then test the function with:
```python
print(add_lists((1,2,3), (4,5,6))) # should print (5,7,9)
```
If you want to use this in a context where lists are expected instead of tuples, replace tuple(result) at the end with result.