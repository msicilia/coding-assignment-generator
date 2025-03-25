```python
def product(a, b):
    if b == 0:
        return 0
    else:
        return a + product(a, b-1)

# Read two numbers from the keyboard
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate the product of the two numbers recursively
product_result = product(a, b)

# Print the product of the two numbers
print("The product of", a, "and", b, "is", product_result)
```

**Explanation:**

* The `product()` function is a recursive function that takes two arguments, `a` and `b`.
* The base case is when `b` is equal to 0. In this case, the function returns 0.
* The recursive case is when `b` is greater than 0. In this case, the function calculates the product by adding `a` to the result of the recursive call `product(a, b-1)`.
* The rest of the code remains the same.

**Example Test Cases:**

```
Test Case 1:
Input:
5
3
Output:
15

Test Case 2:
Input:
10
4
Output:
40
```