You can solve this problem by converting the number to string and then getting length of it. Here is a simple Python code snippet that implements such solution: 

```python
def count_digits(n):
    if n < 0:
        # Handle negative numbers by counting digits in its positive form
        return count_digits(-n)
    elif n == 0 or n//10==0: 
        # Base case where the number is a single digit, return 1.
        return 1
    else: 
        # Recursive case where the number has more than one digits.
        return count_digits(n//10) + 1
  
print(count_digits(2345)) # Output will be 4 as there are four digits in this number.
```