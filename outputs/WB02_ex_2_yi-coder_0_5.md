Here is an implementation in Python:
```python
def calculate_AER(ANN, m):
    """Function to calculate Annual Effective Interest Rate (AER)"""
    return round((1 + ANN/m)**m - 1,4)  # The AER formula rounded to four decimal places

# Test cases:
print(calculate_AER(0.05, 2))   # Expected output: 0.0509
print(calculate_AER(0.1, 4))    # Expected output: 0.1026
print(calculate_AER(0.03, 12))  # Expected output: 0.0308
```