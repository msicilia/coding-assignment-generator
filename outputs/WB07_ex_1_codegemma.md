```python
def product(x, y):
    if y == 0:
        return 0
    else:
        return x + product(x, y-1)

# Read numbers from the keyboard
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Calculate the product
product_result = product(x, y)

# Print the product
print("The product is:", product_result)
```

**Explanation:**

- The `product()` function recursively calculates the product of two numbers.
- The base case is when `y` is 0, in which case the function returns 0.
- The recursive case is when `y` is greater than 0, in which case the function returns `x` plus the product of `x` and `y-1`.
- The user is prompted to enter the two numbers.
- The `product()` function is called to calculate the product.
- The product is printed to the console.

**Output:**

```
Enter the first number: 5
Enter the second number: 3
The product is: 15
```

**Note:**

- The code does not use the multiplication operator.
- It uses recursive function calls to calculate the product.
- It does not use match expressions or list comprehensions.