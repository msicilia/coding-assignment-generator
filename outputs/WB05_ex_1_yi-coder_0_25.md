Here's how you can solve this problem using Python:

```python
class Solution(object):
    def generateLists(self, originalList):
        evenList = []
        oddList  = []
        for i in range(len(originalList)):
            if originalList[i] % 2 == 0 : # Check if number is even.
                # Insert the new value into correct position to maintain sorted order.
                for j in range(len(evenList)):
                    if evenList[j] > originalList[i]:
                        evenList.insert(j,originalList[i])
                        break
                else:
                    evenList.append(originalList[i])
            else : # The number is odd.
                # Insert the new value into correct position to maintain sorted order.
                for j in range(len(oddList)):
                    if oddList[j] < originalList[i]:
                        oddList.insert(j,originalList[i])
                        break
                else:
                    oddList.append(originalList[i])
        return evenList , oddList
```

You can test the code with a simple test case like this :

```python
# Test Case
s = Solution()
print(s.generateLists([10,7,8,5,2,14])) # It should return ([2, 8, 10, 14], [7, 5])
```