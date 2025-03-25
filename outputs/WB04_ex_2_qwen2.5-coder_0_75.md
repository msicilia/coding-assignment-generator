Certainly! Let's write a Python program to solve the problem as described. The program will read a positive integer \( n \) from the user and generate a table with the first \( n \) powers of 2, 3, and 5 using loops only. Here is the code:

```python
def generate_power_table(n):
    # Initialize the headers for the table
    print("n\t2^n\t3^n\t5^n")
    
    # Loop through from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Calculate the powers of 2, 3, and 5
        power_2 = 2 ** i
        power_3 = 3 ** i
        power_5 = 5 ** i
        
        # Print the values in a formatted table row
        print(f"{i}\t{power_2}\t{power_3}\t{power_5}")

# Read the positive integer n from the user
n = int(input("Enter a positive integer: "))

# Generate and display the power table
generate_power_table(n)
```

### Explanation:

1. **Function Definition**: The function `generate_power_table` takes one argument `n`, which is the number of rows in the table to generate.

2. **Table Header**: The first line prints the headers for the table using `\t` (tab) to separate the columns.

3. **Loop and Calculation**:
   - A `for` loop runs from 1 to \( n \) (inclusive).
   - Inside the loop, it calculates the powers of 2, 3, and 5 for the current value of \( i \).

4. **Printing the Table**: For each iteration, it prints a row in the table format using an f-string, which is formatted as `{i}\t{power_2}\t{power_3}\t{power_5}`.

5. **User Input**: The program prompts the user to enter a positive integer \( n \) and then calls the `generate_power_table` function with this input.

### Example Test Cases:

- If the user enters `n = 1`, the output will be:
  ```
  n    2^n   3^n   5^n
  1    2     3     5
  ```

- If the user enters `n = 5`, the output will be:
  ```
  n    2^n   3^n   5^n
  1    2     3     5
  2    4     9     25
  3    8     27    125
  4    16    81    625
  5    32    243   3125
  ```

This code adheres to the constraints of using only loops and does not utilize any data structures or match expressions.