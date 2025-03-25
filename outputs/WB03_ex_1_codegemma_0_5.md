```python
def convert_time(time_24h):
    """Converts a time in 24-hour notation to 12-hour notation.

    Args:
        time_24h: A string in 24-hour notation.

    Returns:
        A string in 12-hour notation.
    """

    try:
        hours, minutes = map(int, time_24h.split(':'))
        if hours > 23 or hours < 0 or minutes > 59 or minutes < 0:
            raise ValueError("Invalid time format.")

        if hours > 12:
            hours -= 12
            period = "PM"
        else:
            period = "AM"

        return f"{hours}:{minutes} {period}"
    except ValueError as e:
        print(e)

# Example test cases
test_cases = [
    "6:30",
    "12:00",
    "03:45",
    "24:00",
]

for test_case in test_cases:
    print(convert_time(test_case))
```