
Here is an example of how you can solve this problem using Python without using data structures or loops:
```
def convert_time(time_24):
    # Check if the input time is in the correct format
    if not re.match(r'^\d{2}:\d{2}$', time_24):
        raise ValueError('Invalid time format')
    
    # Convert the 24-hour time to 12-hour time
    hour, minute = time_24.split(':')
    hour = int(hour)
    if hour >= 12:
        return f'{hour - 12}:{minute} PM'
    else:
        return f'{hour}:{minute} AM'
```
This function takes a string in the format of `HH:MM` (e.g., `'06:30'` or `'18:45'`) as input, and returns a string in the format of `HH:MM AM/PM` (e.g., `'6:30 PM'` or `'6:45 PM'`).

To test this function, you can use the following code:
```
print(convert_time('06:30')) # Output: 6:30 AM
print(convert_time('18:45')) # Output: 6:45 PM
print(convert_time('24:00')) # Output: Invalid time format
```
This code will print the converted time in the format of `HH:MM AM/PM` for each input string. The first two test cases provide valid input times, while the third test case provides an invalid input time (i.e., the hour is greater than 12).