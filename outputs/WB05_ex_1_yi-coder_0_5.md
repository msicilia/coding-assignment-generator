Here's a Python code that meets all your requirements:

```python
def sort_odd_even(numbers):
    evens = []  
    odds = []   

    for number in numbers: 
        if number % 2 == 0:  
            evens.append(number)  
            evens.sort()  
        else: 
            odds.append(number)  
            odds.sort(reverse=True)  
    return evens, odds   

# test the function with a list of numbers
print(sort_odd_even([10, 9, 8, 7, 6])) # This should return ([6, 8, 10], [9, 7]).
```