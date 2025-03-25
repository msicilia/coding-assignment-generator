Here is an example Python script which does exactly this:

```python
# Define current time (hours, minutes and seconds)
hour = 15
minute = 30
second = 45

# Calculate total seconds elapsed since last midnight
total_seconds_since_midnight = hour * 3600 + minute * 60 + second
print('Total seconds elapsed since the last midnight:', total_seconds_since_midnight)

# Calculate total seconds remaining until next midnight
total_seconds_until_next_midnight = 24*3600 - total_seconds_since_midnight
print('Total seconds remaining until next midnight:', total_seconds_until_next_midnight)
```
You can replace the "hour", "minute" and "second" variables with actual current time. This code will print both the number of seconds that have passed since last midnight (0:00 o'clock) as well as the number of seconds remaining until next midnight.