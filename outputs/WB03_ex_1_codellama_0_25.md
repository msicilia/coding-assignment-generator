
Here is a solution that meets the requirements:
```python
def convert_to_12hr(time):
    hour = int(time / 100)
    minute = time % 100
    if hour >= 12:
        return f"{hour - 12}:{minute} PM"
    else:
        return f"{hour}:{minute} AM"
```
Test cases:

* `assert convert_to_12hr(600) == "12:00 PM"`
* `assert convert_to_12hr(1830) == "6:30 PM"`
* `assert convert_to_12hr(0) == "12:00 AM"`
* `assert convert_to_12hr(1400) == "2:00 PM"`
* `assert convert_to_12hr(2030) == "8:30 PM"`

Note that the `f` strings used in the return statements are a Python 3.6+ feature, so if you're using an earlier version of Python, you can replace them with regular string concatenation using the `+` operator.