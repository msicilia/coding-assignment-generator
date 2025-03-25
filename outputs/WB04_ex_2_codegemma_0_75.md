```python
# Read the input
n = int(input("Enter a positive integer n: "))

# Print the header of the table
print("n\t2^n\t3^n\t5^n")

# Iterate through the range of 1 to n
for i in range(1, n + 1):
    # Calculate the powers of 2, 3, and 5
    power_2 = 2 ** i
    power_3 = 3 ** i
    power_5 = 5 ** i

    # Print the results in a tabular format
    print(f"{i}\t{power_2}\t{power_3}\t{power_5}")
```

**Example Usage:**

```
Enter a positive integer n: 5

n	2^n	3^n	5^n
1	2	3	5
2	4	9	25
3	8	27	125
4	16	81	625
5	32	243	3125
```

**Note:**

* The code does not use any data structures or match expressions.
* The code iterates through the range of 1 to n, calculates the powers of 2, 3, and 5 for each value of i, and prints the results in a tabular format.