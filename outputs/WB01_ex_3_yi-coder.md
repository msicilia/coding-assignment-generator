Here is an example of how you could write this program without using any Python functions:

```python
# Define variables for current time
current_hour = 10  # Replace with actual hour
current_minute = 23  # Replace with actual minute
current_second = 45  # Replace with actual second

# Calculate total seconds elapsed since last midnight
total_seconds_since_last_midnight = current_hour * 3600 + current_minute * 60 + current_second

# Calculate total seconds remaining until next midnight
total_seconds_until_next_midnight = 24*3600 - total_seconds_since_last_midnight

print("Total seconds elapsed since last midnight:", total_seconds_since_last_midnight)
print("Total seconds remaining until next midnight:", total_seconds_until_next_midnight)
```

In this code we first calculate the total number of seconds from the current time by multiplying the hour with 3600 (the number of seconds in an hour), the minute with 60 and adding them to the second. Then we calculate the remaining seconds until next midnight which is simply 24*3600 (the number of seconds in a day) subtracted from total_seconds_since_last_midnight.