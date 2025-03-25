Here is the Python code that meets the specified requirements:

```python
# Define the time variables
hours = 15
minutes = 30
seconds = 45

# Calculate the total seconds elapsed since midnight
total_seconds_since_midnight = (hours * 3600) + (minutes * 60) + seconds

# Calculate the remaining seconds until the next midnight
seconds_in_a_day = 24 * 3600
seconds_remaining_until_midnight = seconds_in_a_day - total_seconds_since_midnight

# Display the results
print("Total seconds elapsed since last midnight:", total_seconds_since_midnight)
print("Seconds remaining until next midnight:", seconds_remaining_until_midnight)
```

This code calculates the total seconds elapsed since midnight by converting the hours and minutes into seconds and adding them to the given seconds. It then calculates the remaining seconds until the next midnight by subtracting the total seconds from the total number of seconds in a day (86400). Finally, it prints out the results.

You can run this code in any Python environment to see the output. Make sure to replace the values of `hours`, `minutes`, and `seconds` with different values to test the code with various inputs.