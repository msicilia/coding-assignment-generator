 ```python
def count_digits(n):
    if n < 0:
        return count_digits(-n)
    elif n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

# Test cases
print(count_digits(3))         # Expected output: 1
print(count_digits(12345))      # Expected output: 5
print(count_digits(0))          # Expected output: 1
print(count_digits(-9876))     # Expected output: 4
   ```