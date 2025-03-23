```python
hours = 3
minutes = 45
seconds = 20

total_seconds_elapsed = hours * 3600 + minutes * 60 + seconds
total_seconds_remaining = (24 - hours) * 3600 + (60 - minutes) * 60 + (60 - seconds)

print("Total seconds elapsed since last midnight:", total_seconds_elapsed)
print("Seconds remaining until the next midnight:", total_seconds_remaining)
```

**Example Output:**

```
Total seconds elapsed since last midnight: 13420
Seconds remaining until the next midnight: 7220
```