 Here is a Python solution that follows the provided constraints. The function `convert_time` takes a string in 24-hour notation as input and returns a string in 12-hour notation. We use try-except blocks to handle any ValueError that might occur when we attempt to split the time into hours and minutes, or convert them to integers. If either of these operations fails, it means that the input was not in the correct format, so we return "Invalid Time Format".

   After splitting the time into hours and minutes and converting them to integers, we check if they are within the valid range (hours between 0 and 23, minutes between 0 and 59). If they are not, we return "Invalid Time".

   If both steps pass, we convert the time to 12-hour notation by checking if the hours are less than or equal to 12. If they are, we keep them as is; otherwise, we subtract 12 from the hours. We then append "AM" or "PM" based on whether the original hours were less than or greater than 12, respectively.

```python
def convert_time(time):
    try:
        hours, minutes = map(int, time.split(':'))
    except ValueError:
        return "Invalid Time Format"

    if not (0 <= hours < 24 and 0 <= minutes < 60):
        return "Invalid Time"

    am_pm = "AM" if hours < 12 else "PM"
    if hours > 12:
        hours -= 12
    elif hours == 0:
        hours = 12
    return f"{hours}:{minutes} {am_pm}"

# Test cases
print(convert_time("6:30"))   # Expected output: "6:30 AM"
print(convert_time("18:45"))  # Expected output: "6:45 PM"
print(convert_time("25:30"))  # Expected output: "Invalid Time"
print(convert_time("10:70"))  # Expected output: "Invalid Time"
print(convert_time("10:ab"))  # Expected output: "Invalid Time Format"
```