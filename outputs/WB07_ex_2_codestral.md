 Thought: I will define a Python function called `count_digits` which takes an integer as input. This function will use recursion to count the number of digits in the integer. The base case for this recursion will be when the absolute value of the integer is less than 10, i.e., when it's a single digit number. In this case, the function will return 1 as there is only one digit. For all other cases, the function will call itself with the input divided by 10 and add 1 to the result. This way, we count each digit in the number individually. To handle negative integers, I'll convert them into positive before counting their digits.

   Code:
   ```py
   def count_digits(n):
       if n < 0: # Convert negative numbers to positive
           n = -n
       if n < 10: # Base case: single digit number
           return 1
       else:
           return 1 + count_digits(n // 10)

   print(count_digits(12345)) # Expected output: 5
   print(count_digits(0))     # Expected output: 1
   print(count_digits(-9876)) # Expected output: 4
   ```