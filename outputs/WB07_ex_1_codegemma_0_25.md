```python
def product(a, b):
    if b == 0:
        return 0
    else:
        return a + product(a, b-1)

# Read numbers from keyboard
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate product recursively
product_result = product(a, b)

# Print product
print("The product of", a, "and", b, "is", product_result)
```

**Example Test Cases:**

```
Input:
a = 5
b = 3

Output:
The product of 5 and 3 is 15
```

```
Input:
a = 10
b = 2

Output:
The product of 10 and 2 is 20
```

**Explanation:**

* The `product()` function is a recursive function that calculates the product of two numbers.
* The function takes two arguments, `a` and `b`.
* If `b` is 0, the function returns 0.
* Otherwise, the function calculates the product by adding `a` to the result of the recursive call with `b-1`.
* The numbers `a` and `b` are read from the keyboard using the `input()` function.
* The `product()` function is called recursively to calculate the product.
* The product is printed using the `print()` function.