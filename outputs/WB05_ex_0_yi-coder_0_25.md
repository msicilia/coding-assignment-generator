Here's an example solution in Python code for the problem you presented above. This program uses loops to iterate through each index in the lists, adds corresponding elements together and appends it to a new list:

```python
def sum_lists(l1, l2):
    sum_list = []
    for i in range(len(l1)):
        sum_list.append(l1[i] + l2[i])
    return sum_list
```
This function takes two lists as inputs: `l1` and `l2`. It then creates an empty list named `sum_list` which will be used to store the sums of corresponding elements from both input lists. The loop iterates over a range equal to the length of one list (since it's specified that these two lists have equal lengths), for each iteration it adds together elements at current index in both lists and appends this sum value into `sum_list`. After all iterations are done, it returns `sum_list` with sums from both input lists.

You can test the function with: 
```python
print(sum_lists([1, 2, 3], [4, 5, 6]))  # Outputs: "[5, 7, 9]"
```