```python
def product(a, b):
    """
    Calculates the product of two numbers recursively.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of the two numbers.
    """

    if b == 0:
        return 0
    else:
        return a + product(a, b - 1)


# Read two numbers from the keyboard
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate the product recursively
product_result = product(a, b)

# Print the result
print("The product of", a, "and", b, "is", product_result)
```

**Example Test Cases:**

```
Input:
5
3

Output:
The product of 5 and 3 is 15

Input:
10
4

Output:
The product of 10 and 4 is 40
```

**Explanation:**

* The `product()` function recursively calculates the product of two numbers.
* If `b` is 0, the function returns 0.
* Otherwise, the function calculates `a` plus the product of `a` and `b-1`.
* The program reads two numbers from the keyboard and calls the `product()` function recursively.
* The result is then printed to the console.

**Note:**

* The program does not use the multiplication operator.
* The program uses recursive function calls.
* The program does not use match expressions or list comprehensions.