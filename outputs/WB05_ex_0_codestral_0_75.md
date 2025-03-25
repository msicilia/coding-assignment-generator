 Thought:
I will define a function `sum_lists` that takes in two parameters, both are lists of equal length. Then I'll use a for loop to iterate through the indices of the lists and calculate the sum at each index. The result is stored in a new list which is returned as the output of the function.

   Code:
```python
def sum_lists(list1, list2):
    if len(list1) != len(list2):
        return 'Error: Lists are not of equal length'
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result
```
I will now test the function with two lists [1, 2, 3] and [4, 5, 6]. This should return a new list [5, 7, 9], which is the sum of each corresponding pair of elements in the input lists.

```python
print(sum_lists([1, 2, 3], [4, 5, 6]))
```
This code defines and tests a function that meets all the requirements stated by the user.