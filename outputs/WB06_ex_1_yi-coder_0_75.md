Here's an example implementation for this problem:

```python
def getValues(dictionary, lst):
    inDict = []
    notInDict = []

    for item in lst:
        if item in dictionary:
            inDict.append(dictionary[item])
        else:
            notInDict.append(item)

    return inDict, notInDict
``` 

This function receives a dictionary and a list as inputs. It creates two empty lists: `inDict` for elements that are present in the dictionary, and `notInDict` for those that are not. Then it iterates over the input list; if an item is found within the dictionary, its corresponding value is appended to 'inDict', otherwise it gets added to 'notInDict'. Finally, both lists are returned as output.

The test cases show how this function would work with a simple dictionary and list of strings:
```python
dictionary = {'apple':1, 'banana':2, 'grape':3}
lst = ['apple', 'orange', 'banana']
print(getValues(dictionary, lst)) # Outputs ([1, 2], ['orange'])
```