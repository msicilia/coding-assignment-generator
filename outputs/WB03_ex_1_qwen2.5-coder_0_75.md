To solve this problem within the constraints provided, we need to ensure that our code adheres to the following rules:
1. Use only basic data types and conditional statements.
2. Avoid loops and match expressions.
3. Handle user input using variables instead of `input()`.

Given these constraints, here's a possible solution:

```python
def convert_time(time_str):
    # Extract hour and minute from the input string
    parts = time_str.split(':')
    if len(parts) != 2:
        return "Invalid input format"
    
    try:
        hour = int(parts[0])
        minute = int(parts[1])
        
        # Validate hour and minute ranges
        if hour < 0 or hour > 23:
            return "Invalid time"
        if minute < 0 or minute > 59:
            return "Invalid time"
        
        # Convert to 12-hour format
        period = "AM" if hour < 12 else "PM"
        if hour == 0:
            hour = 12
        elif hour == 12:
            pass
        elif hour > 12:
            hour -= 12
        
        return f"{hour}:{minute:02d} {period}"
    
    except ValueError:
        return "Invalid input format"

# Test cases with variables instead of user input
time_test1 = "07:45"
time_test2 = "12:30"
time_test3 = "19:45"
time_test4 = "25:00"
time_test5 = "13:60"
time_test6 = "hello world"

print(convert_time(time_test1))  # Expected output: 7:45 AM
print(convert_time(time_test2))  # Expected output: 12:30 PM
print(convert_time(time_test3))  # Expected output: 7:45 PM
print(convert_time(time_test4))  # Expected output: Invalid time
print(convert_time(time_test5))  # Expected output: Invalid time
print(convert_time(time_test6))  # Expected output: Invalid input format
```

### Explanation:
1. **Extracting and Validating Input**: The function `convert_time` takes a string representing time in 24-hour notation. It splits the string into hours and minutes and checks if the split was successful.
   
2. **Validation**: It then attempts to convert the extracted parts into integers. If this conversion fails, it returns "Invalid input format". It also checks if the hour is within the valid range (0-23) and the minute is within the valid range (0-59).

3. **Converting to 12-hour Format**: If all validations pass, it determines whether the time falls in AM or PM based on the hour. It adjusts the hour to be between 1 and 12 as needed.

4. **Formatting Output**: The function returns the time in 12-hour format with a colon separator for minutes and an AM/PM indicator.

This solution ensures that all constraints are met, including using only basic data types, conditional statements, and try-except blocks while avoiding loops and match expressions.