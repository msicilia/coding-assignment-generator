 Thoughts: I will write and execute a Python function using recursion that calculates the product of two numbers without using the multiplication operator, as per your instructions.

Code:
```python
def multiply_recursively(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    else:
        return num2 + multiply_recursively(num1 - 1, num2)

# Assuming input numbers for demonstration
num1 = 5
num2 = 4

result = multiply_recursively(num1, num2)
result
```