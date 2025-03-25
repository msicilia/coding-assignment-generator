```python
def validate_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

# Example test cases
text1 = "123"
text2 = "hello"
text3 = "3.14"

print(validate_integer(text1))  # Output: True
print(validate_integer(text2))  # Output: False
print(validate_integer(text3))  # Output: False
```