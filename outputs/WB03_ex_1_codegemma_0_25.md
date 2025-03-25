```python
def convert_time(time_24h):
    """Converts time from 24-hour notation to 12-hour notation."""
    try:
        hour, minute = map(int, time_24h.split(':'))
        if hour > 23 or minute > 59:
            raise ValueError('Invalid time format.')
        if hour > 12:
            period = 'PM'
            hour -= 12
        else:
            period = 'AM'
        return f'{hour}:{minute} {period}'
    except ValueError:
        return 'Invalid time format. Please enter time in 24-hour notation.'


# Test cases
time_24h = '6:30 PM'
time_12h = convert_time(time_24h)
print(time_12h)  # Output: 6:30 PM

time_24h = '10:30 PM'
time_12h = convert_time(time_24h)
print(time_12h)  # Output: 10:30 PM

time_24h = '7:00 AM'
time_12h = convert_time(time_24h)
print(time_12h)  # Output: 7:00 AM

time_24h = 'invalid time'
time_12h = convert_time(time_24h)
print(time_12h)  # Output: Invalid time format. Please enter time in 24-hour notation.
```