Here's an example Python solution that meets all requirements:

```python
def sortLists(original):
    even = [] 
    odd = []  
    for num in original: # traverse the list
        if num % 2 == 0: # check if number is even
            even.append(num)
            even.sort() # keep it sorted ascendingly
        else: # else, the number is odd
            odd.append(num)
            odd.sort(reverse=True) # keep it sorted descendingly
    return (even, odd) # return the lists 
```  
Here's a test case to verify the function works as expected:
```python
print(sortLists([10,5,2,8,1])) # The even list should be [2, 8, 10] and the odd one [5, 1]
```  
This function starts by initializing two empty lists for the even numbers (`even`) and the odd ones (`odd`). Then it traverses the original list and checks if each number is even or not. If it's an even number, it appends to the `even` list and keeps it sorted in ascending order; otherwise, it appends to the `odd` list maintaining its descending sort. Finally, it returns both lists as a tuple.

Please note that this solution assumes that we are dealing with integers only and doesn't handle float or other types of numbers.