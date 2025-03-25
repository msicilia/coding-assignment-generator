```python
# Get user input
n = int(input("Enter a positive integer n: "))

# Print table header
print("Table of Powers:")
print("-----------------")

# Power of 2
for i in range(1, n + 1):
    power_2 = 2**i
    print(f"2^{i} = {power_2}")

# Power of 3
for i in range(1, n + 1):
    power_3 = 3**i
    print(f"3^{i} = {power_3}")

# Power of 5
for i in range(1, n + 1):
    power_5 = 5**i
    print(f"5^{i} = {power_5}")
```