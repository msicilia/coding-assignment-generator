
You are correct that the best way to print the powers of 2, 3, and 5 using Python is by using loops and the `range()` function. Here's an example code snippet that does this:
```
for i in range(1, n + 1):
    print(f"{i}: {2**i}, {3**i}, {5**i}")
```
This code will print the powers of 2, 3, and 5 up to a maximum value of `n`. The `range()` function is used to generate a sequence of numbers from 1 to `n + 1`, which are then used as arguments for the `**` operator to calculate the powers. The `print()` function is used to print the resulting values in a formatted manner.

Note that this code does not use any data structures, other than the basic iteration of sequences in loops. It uses only loops and the `range()` function to generate the powers of 2, 3, and 5.