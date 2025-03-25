You can solve this problem with Python programming language. Below is a simple Python subprogram that accomplishes your task:

```python
def convert24to12(time):
    try: 
        # Check if the time has hour and minute parts only
        if len(time.split(':')) == 2: 
            h, m = map(int, time.split(':')) 

            # Validate that hours are between 0 to 23 inclusive & minutes are between 0 to 59 inclusive
            if (0 <= h < 24) and (0 <= m < 60): 
                converted = ""
                
                # If hour is more than 12 then subtract 12 from it
                if(h > 12): 
                    converted += str(h-12)+':'+str(m)+' PM'
                else: 
                    converted += str(h)+':'+str(m)+' AM'
            
                return converted
            else: 
                # Invalid hours or minutes, return the original time
                return time+ " is not a valid time."
        else: 
            # The input doesn't have an hour and minute part only, return the error message
            return time + " is not a valid format of time."
    except ValueError:
         # If the conversion to integer fails then some part of the time is not a number, return the error message
        return time + " is not a valid time."
``` 
Test this subprogram with the following values:

```python
print(convert24to12('6:30')) # Outputs '6:30 AM'
print(convert24to12('18:30')) # Outputs '6:30 PM'
print(convert24to12('25:30')) # Outputs '25:30 is not a valid time.'
print(convert24to12('6:60'))  # Outputs '6:60 is not a valid time.'
```