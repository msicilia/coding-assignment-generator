Certainly! Below is a Python program that meets your requirements:

```python
def recursive_product(a, b):
    # Base case: if b is 0, return 0 (multiplication of any number with 0 is 0)
    if b == 0:
        return 0
    # If b is negative, make it positive and use the property that a * (-b) = -(a * b)
    elif b < 0:
        return -recursive_product(a, -b)
    # Recursive case: add 'a' to the product of 'a' and (b-1)
    else:
        return a + recursive_product(a, b - 1)

def read_numbers():
    # Read two numbers from the keyboard
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a, b

def main():
    # Read numbers from the keyboard
    a, b = read_numbers()
    
    # Calculate the product recursively
    product = recursive_product(a, b)
    
    # Print the result
    print(f"The product of {a} and {b} is {product}")

# Run the main function
if __name__ == "__main__":
    main()
```

### Explanation:
1. **recursive_product(a, b)**: This function calculates the product of two numbers using recursion.
   - If `b` is 0, it returns 0 because any number multiplied by 0 is 0.
   - If `b` is negative, it converts it to positive and uses the property that \(a * (-b) = -(a * b)\).
   - For a positive `b`, it adds `a` to the result of multiplying `a` with `(b-1)`.

2. **read_numbers()**: This function reads two integers from the keyboard and returns them as a tuple.

3. **main()**: This is the main function that orchestrates the flow:
   - Reads two numbers using `read_numbers()`.
   - Calculates their product using `recursive_product(a, b)`.
   - Prints the result.

4. **if __name__ == "__main__":** This ensures that the `main()` function runs only when the script is executed directly, not when imported as a module.

### Example Test Cases:
- Input: 3 and 4
  Output: The product of 3 and 4 is 12

- Input: -2 and 5
  Output: The product of -2 and 5 is -10

- Input: 6 and -3
  Output: The product of 6 and -3 is -18

- Input: 0 and 7
  Output: The product of 0 and 7 is 0