```python
hours = 23
minutes = 59
seconds = 59

total_seconds_elapsed = (hours * 3600) + (minutes * 60) + seconds
seconds_remaining_until_next_midnight = (24 - hours) * 3600 + (60 - minutes) * 60 + (60 - seconds)

print("Total seconds elapsed since last midnight:", total_seconds_elapsed)
print("Seconds remaining until next midnight:", seconds_remaining_until_next_midnight)
```

**Explanation:**

* The code calculates the total seconds elapsed by multiplying the hours by 3600, the minutes by 60, and adding the seconds.
* The code calculates the seconds remaining until next midnight by subtracting the current time from 24 hours.
* The code prints the total seconds elapsed and seconds remaining until next midnight.

**Example Output:**

```
Total seconds elapsed since last midnight: 86399
Seconds remaining until next midnight: 3661
```

**Note:**

* The code does not use any functions or input from the keyboard.
* The code meets the specified Python elements and requirements.