## Function to validate user input as an integer

```python
def validate_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False
```

**Explanation:**

* The function uses a `try-except` block to convert the input `text` to an integer.
* If the conversion is successful, it returns `True`.
* If the conversion fails due to a `ValueError`, it returns `False`.

**Example Usage:**

```python
text1 = "123"
text2 = "hello"
text3 = "3.14"

print(validate_integer(text1))  # Output: True
print(validate_integer(text2))  # Output: False
print(validate_integer(text3))  # Output: False
```

**Additional Notes:**

* The function only accepts strings as input.
* It does not perform any additional validation, such as checking for negative numbers or overflow.
* The example test cases provide a basic demonstration of the function's functionality. Additional tests can be added to cover various edge cases.

**Conclusion:**

This function fulfills the requirements of the task by validating user input as an integer using `try-except` blocks. It is a concise and efficient way to ensure that user input meets the expected criteria.