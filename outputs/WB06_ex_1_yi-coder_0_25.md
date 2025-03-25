Here's how you can solve this problem using Python programming language - 

```python
def split_list(dictonary, inputList):
    # Creating two empty lists to store our results
    inDict = []
    notInDict = []
   
    for item in inputList: # Iterating over the list items.
        if item in dictonary: # Checking if an element is present in dictionary or not.
            # If yes, then add its value to 'inDict' list.
            inDict.append(dictonary[item]) 
        else: # If no, then add it to the 'notInDict' list.
            notInDict.append(item) 
   
    return inDict, notInDict  # Returning our results as two lists.
```
You can test this function with the following code -

```python
print(split_list({'a':1, 'b':2, 'c':3}, ['a', 'b', 'd'])) # It should return ([1, 2], ['d']).
```