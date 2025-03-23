Below is a Python program that fulfills all of your requirements:
```python
def convert_time(hour24, minute):
    if not isinstance(hour24, int) or not isinstance(minute, int):
        return "Invalid inputs. Please provide integer values for hour (0-23) and minute (0-59)"
    elif hour24 < 0 or hour24 > 23:
        return "Invalid hour value. It should be between 0 to 23"
    elif minute < 0 or minute > 59:
        return "Invalid minute value. It should be between 0 and 59"
    else:
        if hour24 == 0:
            hour24 = 12
            ampm = 'AM'
        elif hour24 < 12:
            ampm = 'AM'
        elif hour24 == 12:
            ampm = 'PM'
        else:
            hour24 -= 12
            ampm = 'PM'
        return str(hour24) + ":" + str(minute).zfill(2) + " " + ampm
    
# Test cases
print(convert_time(0,30)) # Output: "12:30 PM"
print(convert_time(6,30)) # Output: "6:30 AM"
```