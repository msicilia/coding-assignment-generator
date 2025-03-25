 ```python
def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

# Read numbers from keyboard
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

product = multiply(num1, num2)
print("The product is:", product)
```