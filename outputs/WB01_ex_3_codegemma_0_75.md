```python
hours = 23
minutes = 59
seconds = 59

total_seconds_elapsed = (hours * 3600) + (minutes * 60) + seconds
total_seconds_remaining = (24 - hours) * 3600 + (60 - minutes) * 60 + (60 - seconds)

print("Total seconds elapsed since last midnight:", total_seconds_elapsed)
print("Seconds remaining until next midnight:", total_seconds_remaining)
```

**Output:**

```
Total seconds elapsed since last midnight: 86399
Seconds remaining until next midnight: 3661
```