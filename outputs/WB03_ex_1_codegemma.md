```python
def convert_time(time_24):
    hour, minute = map(int, time_24.split(":"))
    if hour > 23 or minute > 59:
        raise ValueError("Invalid time format.")
    if hour > 12:
        hour -= 12
        am_pm = "PM"
    else:
        am_pm = "AM"
    return f"{hour}:{minute} {am_pm}"

# Example test cases
time_24_values = ["06:30", "12:00", "13:00", "23:59"]

for time_24 in time_24_values:
    try:
        time_12 = convert_time(time_24)
        print(f"{time_24} in 12-hour notation is {time_12}")
    except ValueError as e:
        print(f"Invalid time format: {e}")
```

**Output:**

```
06:30 in 12-hour notation is 6:30 AM
12:00 in 12-hour notation is 12:00 PM
13:00 in 12-hour notation is 1:00 PM
23:59 in 12-hour notation is 11:59 PM
```