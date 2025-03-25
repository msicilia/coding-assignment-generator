```python
# Given time
hours = 15
minutes = 30
seconds = 45

# Total seconds elapsed since midnight
total_seconds_since_midnight = hours * 3600 + minutes * 60 + seconds

# Remaining seconds until the next midnight
remaining_seconds_until_next_midnight = 86400 - total_seconds_since_midnight

# Display results
print("Total seconds since midnight:", total_seconds_since_midnight)
print("Seconds remaining until next midnight:", remaining_seconds_until_next_midnight)
```