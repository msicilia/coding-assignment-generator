```python
def validate_integer(input):
    try:
        int_value = int(input)
        return True
    except ValueError:
        return False

# Test cases
print(validate_integer('123')) # Returns: True
print(validate_integer('456.78')) # Returns: False
print(validate_integer('True')) # Returns: False
print(validate_integer('Hello')) # Returns: False
```