Here is an example of Python code which solves your problem:

```python
# Here's a simple version using integer inputs directly in our function
def time_calculations(hour, minute, second):
    # calculating total seconds elapsed since last midnight (00:00:00)
    total_seconds_elapsed = hour*3600 + minute*60 + second
    print('Total Seconds Elapsed:', total_seconds_elapsed)

    # calculating total seconds remaining until next midnight
    total_seconds_remaining = 24*3600 - total_seconds_elapsed
    print('Total Seconds Remaining Until Next Midnight:', total_seconds_remaining)

time_calculations(15, 37, 28)  # Example test case.
```

This program will output the total seconds elapsed and remaining until midnight for a given time (hour, minute, second).