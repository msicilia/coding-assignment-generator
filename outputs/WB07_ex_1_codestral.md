 Code:
   ```python
   def multiply(a, b):
       if b == 0:
           return 0
       else:
           return a + multiply(a, b - 1)

   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))

   result = multiply(num1, num2)
   print('The product of', num1, 'and', num2, 'is:', result)
   ```
   Thoughts: I've defined a function `multiply` that takes two parameters and recursively calls itself to add `a` to the sum of multiplication of `a` and `b - 1`. This is done until `b` becomes 0. Then, I prompted the user to enter numbers for `num1` and `num2`. The product of these two numbers is calculated by calling the `multiply` function with `num1` and `num2` as arguments. Finally, the result is printed on the console.