 Thoughts: The problem requires iterating over the input list and checking if each element exists in the dictionary. If it does, add the corresponding value to one output list; otherwise, add it to another output list. Since we cannot use match expressions or list comprehensions, I will write a Python function using dictionaries and control flow statements to solve the problem as required.

   Code:
```python
def separate_dict(input_dict, input_list):
    values_in_dict = []
    values_not_in_dict = []

    for element in input_list:
        if element in input_dict:
            values_in_dict.append(input_dict[element])
        else:
            values_not_in_dict.append(element)

    return values_in_dict, values_not_in_dict
```
<end_code>

This function takes a dictionary and a list as input arguments. It initializes two empty lists to store the elements found in the dictionary and those not found in the dictionary. The function then iterates over each element of the input list, checks if it exists in the dictionary, and appends the corresponding value or the element itself to the appropriate output list based on the result. Finally, the function returns both output lists as a tuple.

Now let's test this function with some example test cases:
```python
# Test case 1
dictionary1 = {'a': 10, 'b': 20, 'c': 30}
list1 = ['a', 'd', 'c', 'e']
result1 = separate_dict(dictionary1, list1)
print("Values in dictionary:", result1[0])  # Expected output: [10, 30]
print("Values not in dictionary:", result1[1])  # Expected output: ['d', 'e']

# Test case 2
dictionary2 = {1: "one", 2: "two", 3: "three"}
list2 = [1, 4, 5, 3]
result2 = separate_dict(dictionary2, list2)
print("Values in dictionary:", result2[0])  # Expected output: ["one", "three"]
print("Values not in dictionary:", result2[1])  # Expected output: [4, 5]
```
<end_code>