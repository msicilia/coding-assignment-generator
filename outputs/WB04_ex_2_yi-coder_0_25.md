The task is to create a program that takes an input 'n' (a positive integer) and generate a table with the first 'n' powers of 2, 3 and 5. Here is how we can do it:

```python
def power_table(n):
    print('Number\tPowerOfTwo\tPowerOfThree\tPowerOfFive')
    for i in range(1, n+1):
        print(f'{i}\t{2**i}\t\t{3**i}\t\t{5**i}')

# Test the function with some example test cases.
power_table(10)  
```

In this Python program, we first print out a formatted table header then use a loop to iterate over each number from 1 to n (inclusive). For every iteration, it prints that number and its power to the console. 
The '\t' represents a tab space for formatting purposes.

The function 'power_table(n)' can be tested by calling it with different positive integer values as argument.