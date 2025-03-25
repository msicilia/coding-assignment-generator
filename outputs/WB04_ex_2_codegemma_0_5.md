```python
n = int(input("Enter a positive integer n: "))

print("Table of Powers:")
print("Number\tPower of 2\tPower of 3\tPower of 5")

for i in range(1, n + 1):
    power_2 = 2 ** i
    power_3 = 3 ** i
    power_5 = 5 ** i
    print(f"{i}\t\t{power_2}\t\t{power_3}\t\t{power_5}")
```

**Example Output:**

```
Enter a positive integer n: 5

Table of Powers:
Number	Power of 2	Power of 3	Power of 5
1		2		3		5
2		4		9		25
3		8		27		125
4		16		81		625
5		32		243		3125
```

**Note:**

* The code meets all the specified requirements.
* The code uses only loops for iterations.
* The code does not use any data structures or match expressions.