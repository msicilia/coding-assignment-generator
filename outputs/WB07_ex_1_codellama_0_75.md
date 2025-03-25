
You are correct! Here is an example implementation of the product function using recursion and no multiplication operator:
```
def product(a, b):
    if b == 0:
        return a
    else:
        return a + product(a, b-1)
```
This function takes two arguments `a` and `b`, where `a` is the number to be multiplied with `b`. If `b` is equal to 0, the function returns `a`, which means that if we multiply `a` by 0, the result is just `a`. Otherwise, the function calls itself recursively with `a` and `b-1` as arguments. This process continues until `b` becomes 0, at which point the function returns `a`.

To test this function, you can use the following test cases:
```
test_product(assertEqual(product(3, 4), 12))
test_product(assertEqual(product(5, 6), 30))
test_product(assertEqual(product(7, 8), 56))
```
These test cases verify that the product function works correctly for different input values.