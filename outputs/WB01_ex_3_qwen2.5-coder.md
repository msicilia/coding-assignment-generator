```py
# Define variables for hours, minutes, and seconds
hours = 15  # Replace with actual variable if needed
minutes = 30  # Replace with actual variable if needed
seconds = 45  # Replace with actual variable if needed

# Calculate total seconds elapsed since midnight
total_seconds_elapsed = (hours * 3600) + (minutes * 60) + seconds

# Calculate remaining seconds until the next midnight
seconds_remaining = 24 * 3600 - total_seconds_elapsed

# Display results
print("Total seconds elapsed since last midnight:", total_seconds_elapsed)
print("Seconds remaining until next midnight:", seconds_remaining)
```