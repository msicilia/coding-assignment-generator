Here's how you can solve this problem using Python:

```python
def validate_integer(input):
    try:
        int(input) # This will throw an error if the conversion isn't possible 
        return True
    except ValueError:
        return False

# Some test cases.
print(validate_integer('123'))  # Expected output is True, because '123' can be converted to integer 123.
print(validate_integer('Hello')) # Expected output is False, because 'Hello' cannot be converted to an integer.
print(validate_integer('567.89')) # Expected output is False, because '567.89' is a float not an integer.
```