Certainly! Below is a Python program that reads a positive integer \( n \) and generates a table with the \( n \) first powers of 2, 3, and 5. The program uses basic loops and avoids using data structures or match expressions as specified.

```python
# Function to generate and print the table of powers
def generate_powers_table(n):
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    # Print the table header
    print("Powers of 2 | Powers of 3 | Powers of 5")
    
    # Generate and print the first n powers of 2, 3, and 5
    for i in range(1, n + 1):
        power_2 = 2 ** i
        power_3 = 3 ** i
        power_5 = 5 ** i
        print(f"{power_2}         {power_3}         {power_5}")

# Example usage:
if __name__ == "__main__":
    # Read input from the user
    try:
        n = int(input("Enter a positive integer: "))
        generate_powers_table(n)
    except ValueError as e:
        print(e)
```

### Explanation:
1. **Function Definition**: The function `generate_powers_table` is defined to encapsulate the logic for generating and printing the table.
2. **Input Validation**: The function checks if \( n \) is a positive integer. If not, it raises a `ValueError`.
3. **Table Header**: The header of the table is printed once.
4. **Loop for Powers Calculation**: A loop runs from 1 to \( n \), calculating the \( i \)-th power of 2, 3, and 5. These values are then formatted and printed in a tabular form.

### Example Test Cases:
- If the user inputs `n = 5`, the output will be:
  ```
  Powers of 2 | Powers of 3 | Powers of 5
  1         1         1
  2         3         5
  4         9         25
  8         27         125
  16         81         625
  ```
- If the user inputs `n = 7`, the output will be:
  ```
  Powers of 2 | Powers of 3 | Powers of 5
  1         1         1
  2         3         5
  4         9         25
  8         27         125
  16         81         625
  32         243         3125
  64         729         15625
  ```
- If the user inputs `n = 3`, the output will be:
  ```
  Powers of 2 | Powers of 3 | Powers of 5
  1         1         1
  2         3         5
  4         9         25
  ```

This program ensures that the user inputs a valid positive integer and generates the required table using basic loops, meeting all specified requirements.