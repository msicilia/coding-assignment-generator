Here is a simple recursive Python code which performs multiplication by using addition operation.

```python
def multiply(n, m):
    # Base case for recursion termination
    if m == 0 or n == 0:
        return 0
    else:
        # Recursive function call
        return n + multiply(n, m-1)

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print('The product is:', multiply(num1, num2))
```
This program will take two numbers from the user and calculate their product recursively by adding the first number to itself a certain number of times specified by the second number. If either of the inputs are zero then this function returns 0 because multiplication with zero results in zero.