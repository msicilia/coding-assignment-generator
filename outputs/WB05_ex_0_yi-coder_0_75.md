Sure, here's how you can solve this problem in Python:

```python
def sum_lists(list1, list2):
    result = [] 
    for i in range(len(list1)):                               
        result.append(list1[i] + list2[i])
    return result

print(sum_lists([1,2,3], [4,5,6])) # Output should be [5,7,9]
print(sum_lists([0,-1,1], [1,2,-3])) # Output should be [1,1,-2]
```
This function takes two lists as input and returns a new list where each element is the sum of the corresponding elements from the input lists. The function uses a for loop to iterate through each pair of elements in the input lists, adds them together using the '+' operator, and appends the result to the output list using the 'append' method.