Thought: Since direct input usage within functions is restricted, we can provide a function `read_number()` outside the main logic that handles user input and passes it to the recursive multiplication function.

Code:
```python
def read_number(prompt):
    return int(input(prompt))

def multiply_recursive(a, b):
    # Base case: if either number is 0, the product is 0
    if a == 0 or b == 0:
        return 0
    
    # If b is negative, convert the problem to multiplication of positive numbers
    elif b < 0:
        return -multiply_recursive(a, -b)
    
    # Recursive case: add 'a' to the product of 'a' and 'b-1'
    else:
        return a + multiply_recursive(a, b - 1)

# Example usage:
num1 = read_number("Enter the first number: ")
num2 = read_number("Enter the second number: ")

product = multiply_recursive(num1, num2)
print(f"The product of {num1} and {num2} is: {product}")
```

### Example Test Cases:

1. **Test Case 1**:
   - Input:
     ```
     Enter the first number: 5
     Enter the second number: 3
     ```
   - Expected Output:
     ```
     The product of 5 and 3 is: 15
     ```

2. **Test Case 2**:
   - Input:
     ```
     Enter the first number: -4
     Enter the second number: 6
     ```
   - Expected Output:
     ```
     The product of -4 and 6 is: -24
     ```

3. **Test Case 3**:
   - Input:
     ```
     Enter the first number: 0
     Enter the second number: 7
     ```
   - Expected Output:
     ```
     The product of 0 and 7 is: 0
     ```

4. **Test Case 4**:
   - Input:
     ```
     Enter the first number: 8
     Enter the second number: -5
     ```
   - Expected Output:
     ```
     The product of 8 and -5 is: -40
     ```

This solution ensures that input handling is done in a separate function, adhering to the restrictions provided.