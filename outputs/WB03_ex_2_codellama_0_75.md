
To solve this problem, you can use a try-except block to check whether the input is an integer. If it is not an integer, the except block will be executed and the function will return False. Here's an example of how you could implement this function:
```
def validate_integer(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
```
This function takes in a string as input and tries to convert it to an integer using the `int()` function. If the conversion is successful, the function returns True. If it fails (i.e., if the input is not an integer), the except block will be executed and the function will return False.

You can test this function by calling it with different inputs:
```
print(validate_integer("123")) # Output: True
print(validate_integer("abc")) # Output: False
```
In this example, we call the `validate_integer()` function with two different inputs: "123" and "abc". The output shows that the function returns True for an integer input and False for a non-integer input.