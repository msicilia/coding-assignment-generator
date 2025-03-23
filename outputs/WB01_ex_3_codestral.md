 ```python
# Define variables for hours, minutes, and seconds
hours = 12
minutes = 30
seconds = 45

# Convert given time into total seconds
total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

# Calculate elapsed seconds since midnight
elapsed_seconds = total_seconds

# Calculate remaining seconds until midnight
remaining_seconds = 86400 - total_seconds

print(f"Total seconds elapsed since last midnight: {elapsed_seconds}")
print(f"Total seconds remaining until next midnight: {remaining_seconds}")
   ```