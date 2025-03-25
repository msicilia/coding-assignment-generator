Here is a Python solution based on your requirements:

```python
def convert_time(hour):
    # Validate the hour is a number and within 24-hour notation limits
    try:
        int_hour = int(hour)
        if int_hour < 0 or int_hour > 23:
            raise ValueError()
    except ValueError:
        return "Invalid input"

    # Determine AM/PM and convert to 12-hour notation
    is_pm = True if int_hour >= 12 else False
    int_hour %= 12
    if int_hour == 0:
        int_hour = 12
    return str(int_hour) + " PM" if is_pm else str(int_hour) + " AM"

# Test the function with some examples.
print(convert_time('6')) # Outputs: '6 AM'
print(convert_time('15')) # Outputs: '3 PM'
print(convert_time('0')) # Outputs: '12 AM'
print(convert_time('12')) # Outputs: '12 PM'
```