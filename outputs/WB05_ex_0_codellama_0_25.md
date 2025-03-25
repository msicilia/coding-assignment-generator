
To solve this problem, you can use a nested loop to iterate over both lists simultaneously and add their elements together. Here is an example code snippet:
```
def sum_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result
```
This code first checks if the lengths of the two lists are equal using the `len()` function. If they are not equal, it raises a `ValueError` with a helpful message. Otherwise, it initializes an empty list called `result`, which will contain the sum of the original lists element by element. It then uses a nested loop to iterate over both lists simultaneously and add their elements together. The resulting sums are appended to the `result` list using the `append()` method. Finally, the function returns the `result` list.

Here is an example usage of this code:
```
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(sum_lists(list1, list2)) # Output: [5, 7, 9]
```
In this example, the `sum_lists()` function is called with two lists as arguments, and it returns a new list containing the sum of their elements element by element. The resulting list `[5, 7, 9]` is then printed to the console.