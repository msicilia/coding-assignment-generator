Here's a simple Python code that fits your requirements:

```python
def validate_integer(user_input):
    try:
        int(user_input)  # Try converting to an integer
        return True   # If it is possible, the input is valid (integer).
    except ValueError:
        return False  # If not possible, the input isn't a valid (not an integer).

```
You can use this function with different test cases like so:
```python
print(validate_integer('123'))  # Expected output: True (it is an integer)
print(validate_integer('456.789'))  # Expected output: False (not an integer)
print(validate_integer('Hello'))  # Expected output: False (not an integer)
```
Remember, this function will only validate if a given text can be transformed into an integer or not. It won't validate if the text represents an integer that is actually used in your program or not.