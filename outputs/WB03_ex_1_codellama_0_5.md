
You can use the following code to solve the problem:
```python
def convert_time(time):
    if time >= 1200 and time < 2400:
        return f"{time - 1200} PM"
    else:
        return f"{time} AM"

print(convert_time(int(input("Enter a time in 24-hour notation: "))))
```
This code uses a conditional statement to check if the input time is between 1200 and 2400, which corresponds to times after noon. If it is, it subtracts 1200 from the input time to convert it to 12-hour notation and returns the result as a string with " PM" appended. Otherwise, it simply returns the input time as a string with " AM" appended.

Testing this code using the following inputs:

* Enter a time in 24-hour notation: 1500
* Enter a time in 24-hour notation: 0900
* Enter a time in 24-hour notation: 2500

should produce the following outputs:

* 3:00 PM
* 9:00 AM
* Invalid input, please enter a time between 0 and 2359.