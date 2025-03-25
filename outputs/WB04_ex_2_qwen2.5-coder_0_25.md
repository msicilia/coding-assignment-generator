Certainly! Below is the Python code to solve the problem as described. The program will read a positive integer \( n \) from the user and then generate a table with the first \( n \) powers of 2, 3, and 5. The solution strictly adheres to the constraints provided:

1. No data structures (other than basic sequences).
2. Only loops are allowed.
3. No match expressions.

```python
def get_positive_integer():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

n = get_positive_integer()

print(f"{'Power of 2':<15}{'Power of 3':<15}{'Power of 5':<15}")
for i in range(1, n + 1):
    power_2 = 2 ** i
    power_3 = 3 ** i
    power_5 = 5 ** i
    print(f"{power_2:<15}{power_3:<15}{power_5:<15}")
```

### Explanation:
1. **Function `get_positive_integer()`**:
   - This function continuously prompts the user to enter a positive integer.
   - It ensures that the input is an integer and greater than zero.

2. **Main Program Logic**:
   - The program reads \( n \) from the user using the `get_positive_integer` function.
   - It then prints a header for the table with column titles for powers of 2, 3, and 5.
   - A loop runs from 1 to \( n \), calculating the \( i \)-th power of 2, 3, and 5 for each iteration.
   - The results are formatted and printed in a tabular format.

This solution ensures that all constraints are met while providing a clear and functional program to generate the desired table.