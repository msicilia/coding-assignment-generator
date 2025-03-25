
Here is an example of how you can solve this problem without using any data structures or loops:
```python
def convert_time(time24):
    """
    Converts a time in 24-hour notation to 12-hour notation.
    :param time24: The time in 24-hour notation (HH:MM)
    :return: The time in 12-hour notation (HH:MM AM/PM)
    """
    try:
        hour, minute = time24.split(':')
        if int(hour) > 12:
            raise ValueError("Invalid time")
        am_pm = "AM"
        if int(hour) >= 12:
            am_pm = "PM"
        return f"{int(hour)}:{minute} {am_pm}"
    except ValueError as e:
        print(f"Invalid time: {e}")
```
This function takes a string in the format `HH:MM` (24-hour notation) and returns a string in the format `HH:MM AM/PM` (12-hour notation). It uses a try-except block to validate the input time, and raises a `ValueError` if the input is invalid.

You can test this function using values entered by the user like this:
```python
time24 = input("Enter a time in 24-hour notation (HH:MM): ")
print(convert_time(time24))
```
This code will prompt the user to enter a time in 24-hour notation, and then convert it to 12-hour notation using the `convert_time` function. It will print the converted time to the console.