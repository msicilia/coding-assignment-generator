Here is how you can solve this problem using Python programming language:
```python
n = int(input('Enter a positive number: '))  # Reading input from user
powers_of_nums = [(2**i, 3**i, 5**i) for i in range(1, n+1)]  # Generating the powers of numbers
print('Powers of (2, 3 and 5):\n', powers_of_nums) # Printing the generated table
```
This program first reads a positive integer from the user. Then it generates a list containing tuples, where each tuple contains the corresponding power of 2, 3 and 5 using a loop for `i` ranging from 1 to n (inclusive on both ends). The result is printed out as the generated table.