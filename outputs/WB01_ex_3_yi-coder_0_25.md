Here is how you can solve this problem:
```python
def time_to_midnight(hours, minutes, seconds):
    # Convert hours to seconds
    hours_in_seconds = hours * 3600

    # Convert minutes to seconds
    minutes_in_seconds = minutes * 60

    # Total elapsed seconds since midnight
    elapsed_seconds = hours_in_seconds + minutes_in_seconds + seconds

    # Calculate the number of seconds until midnight (24 hours * 3600 seconds/hour)
    remaining_seconds = 86400 - elapsed_seconds

    return f'Elapsed since last midnight: {elapsed_seconds} seconds, remaining till next midnight: {remaining_seconds} seconds.'

# Example usage
print(time_to_midnight(12, 34, 56))  # Should print 'Elapsed since last midnight: 45296 seconds, remaining till next midnight: 38904 seconds.'
```
In this solution, we first convert the hours to seconds by multiplying them by 3600 (the number of seconds in an hour). We do the same for minutes but multiply them by 60 instead. Then we add all these together to get elapsed seconds since midnight. To calculate remaining seconds until midnight, we subtract the elapsed seconds from total seconds in a day which is 24*60*60 = 86400.