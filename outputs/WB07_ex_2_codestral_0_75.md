 Thought: I will define a Python function called `count_digits` which takes an integer as input and returns the count of its digits using recursion. The base case for the recursion is when the absolute value of the input is less than 10, in which case the function returns 1. For all other cases, the function divides the input by 10 (removing a digit) and calls itself with the result, adding 1 to the count for each call made. This allows the function to count the number of digits in any integer input without using match expressions or list comprehensions, as required.

   Code:
   ```python
   def count_digits(n):
       n = abs(int(n))
       if n < 10:
           return 1
       else:
           return 1 + count_digits(n // 10)

   # Test cases
   print(count_digits(0))    # Expected output: 1
   print(count_digits(123))  # Expected output: 3
   print(count_digits(-456789))  # Expected output: 6
   ```