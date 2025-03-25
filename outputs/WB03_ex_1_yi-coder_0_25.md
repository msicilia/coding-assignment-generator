Here is a python solution for your problem:

```python
def convert_time(time):
    try:  # try-except block to validate time format and hour value
        hr, _ = map(int, time.split(':')))
        if not (0 <= hr < 24):  # if hour is not in the correct range raise an exception
            raise ValueError()
    except ValueError: # if any error occurs return this message
        return "Invalid input"

    am_pm = 'AM' if hr < 12 else 'PM'  # determine am or pm
    hr = hr % 12  # convert to 12-hour format and handle midnight and noon special cases
    if hr == 0:   # set hour for midnight and noon
        hr = 12
    return f'{hr}:{_} {am_pm}' # return time in 12-hour notation

times = ["6:30", "24:00", "15:00", "12:00"]  # test cases
for t in times: print(f'Input - {t} | Output - {convert_time(t)}') # apply the function and print results
```