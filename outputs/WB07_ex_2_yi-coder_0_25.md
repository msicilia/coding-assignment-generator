Here is your solution in Python programming language: 

```python
def count_digits(n):
    if n == 0:  # base case when the number becomes zero
        return 0
    else:   # recursive call when the number is non-zero
        return 1 + count_digits(n // 10)
```

This function works by recursively dividing the input number 'n' by 10 (which effectively removes the last digit of the number in each iteration) and counting one for every division operation. The recursion ends when the number becomes zero, at which point it returns a count of zero (since there are no more digits to be removed).

You can test this function with some example values as follows: 
```python
print(count_digits(0))  # prints: 0
print(count_digits(5))  # prints: 1
print(count_digits(34)) # prints: 2
print(count_digits(789)) # prints: 3
```