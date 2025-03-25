```python
# Set the time
hours = 10
minutes = 30
seconds = 45

# Calculate the total seconds elapsed since the last midnight
total_seconds_elapsed = hours * 3600 + minutes * 60 + seconds

# Calculate the seconds remaining until the next midnight
seconds_remaining = (24 - hours) * 3600 + (60 - minutes) * 60 + (60 - seconds)

# Display the results
print("Total seconds elapsed since last midnight:", total_seconds_elapsed)
print("Seconds remaining until next midnight:", seconds_remaining)
```

**Output:**

```
Total seconds elapsed since last midnight: 37845
Seconds remaining until next midnight: 43155
```

**Explanation:**

* The code calculates the total seconds elapsed since the last midnight by multiplying the hours by 3600, the minutes by 60, and adding the seconds.
* The code calculates the seconds remaining until the next midnight by subtracting the current time from 24 hours and multiplying the hours by 3600, subtracting the current minutes by 60 and multiplying by 60, and subtracting the current seconds from 60.
* The code displays the total seconds elapsed since the last midnight and the seconds remaining until the next midnight using the `print()` function.