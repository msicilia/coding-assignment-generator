 I'm going to write a Python function that creates two lists: one for even numbers and another for odd numbers. The function will iterate through each number in the original list. If the number is even, it will be inserted into the even list at the appropriate position to maintain ascending order. If the number is odd, it will be inserted into the odd list at the appropriate position to maintain descending order. Let's write and run this code now.
```python
def separate_and_sort(original):
    evens = []
    odds = []
    for num in original:
        if num % 2 == 0:
            # Insert into the evens list at the appropriate position to maintain ascending order
            for i, even_num in enumerate(evens):
                if num < even_num:
                    evens.insert(i, num)
                    break
            else:
                evens.append(num)
        else:
            # Insert into the odds list at the appropriate position to maintain descending order
            for i, odd_num in enumerate(odds):
                if num > odd_num:
                    odds.insert(i, num)
                    break
            else:
                odds.append(num)
    return evens, odds

# Test the function with some examples
original1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
evens1, odds1 = separate_and_sort(original1)
print('Original list:', original1)
print('Even numbers sorted ascendingly:', evens1)
print('Odd numbers sorted descendingly:', odds1)

original2 = [0, -1, -2, -3, -4, -5, -6]
evens2, odds2 = separate_and_sort(original2)
print('\nOriginal list:', original2)
print('Even numbers sorted ascendingly:', evens2)
print('Odd numbers sorted descendingly:', odds2)
```