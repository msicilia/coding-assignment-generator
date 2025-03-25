Sure! Let's write a Python subprogram that reads a time in 24-hour notation and returns it in 12-hour notation. We will use conditional statements and try-except blocks to handle validation and conversion.

Here is the code:

```python
def convert_to_12_hour(time_str):
    # Split the input time string into hours and minutes
    parts = time_str.split(':')
    
    if len(parts) != 2:
        return "Invalid time format. Please use HH:MM."
    
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            return "Invalid time range. Hours should be between 0-23, and minutes between 0-59."
        
        # Determine AM or PM
        period = "AM" if hours < 12 else "PM"
        
        # Convert hour to 12-hour format
        if hours == 0:
            hours_12hr = 12
        elif hours > 12:
            hours_12hr = hours - 12
        else:
            hours_12hr = hours
        
        # Format the time string
        return f"{hours_12hr}:{minutes:02d} {period}"
    
    except ValueError:
        return "Invalid time format. Please use HH:MM."

# Example test cases using variables instead of input()
time_1 = "14:30"
time_2 = "09:05"
time_3 = "23:59"
time_4 = "12:00"
time_5 = "25:00"
time_6 = "08:60"

# Test the function
print(convert_to_12_hour(time_1))  # Output: 2:30 PM
print(convert_to_12_hour(time_2))  # Output: 9:05 AM
print(convert_to_12_hour(time_3))  # Output: 11:59 PM
print(convert_to_12_hour(time_4))  # Output: 12:00 PM
print(convert_to_12_hour(time_5))  # Output: Invalid time range. Hours should be between 0-23, and minutes between 0-59.
print(convert_to_12_hour(time_6))  # Output: Invalid time format. Please use HH:MM.
```

### Explanation:
1. **Splitting the Input**: The input string is split into hours and minutes using `split(':')`.
2. **Validation**:
   - Check if the input has exactly two parts (hours and minutes).
   - Validate that both parts are integers and within their respective ranges.
3. **Conversion to 12-Hour Format**:
   - Determine whether it is AM or PM based on the hour.
   - Convert hours greater than 12 to the 12-hour format.
   - Format the output string in the desired 12-hour notation.

This code ensures that the input time is validated and converted correctly, adhering to the constraints provided.