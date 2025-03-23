
To solve this problem, you can use variables to store the values of the temperature in both Celsius and Fahrenheit systems. Here is an example of how you can do this:
```
# Define the temperature value in Fahrenheit
fahrenheit = 212

# Convert the temperature from Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the equivalent temperature in Celsius
print("The temperature in Celsius is:", celsius)

# Convert the temperature from Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Print the equivalent temperature in Fahrenheit
print("The temperature in Fahrenheit is:", fahrenheit)
```
This code defines a variable `fahrenheit` and assigns it a value of 212. It then uses an arithmetic expression to convert the temperature from Fahrenheit to Celsius and stores the result in the variable `celsius`. The code then prints the equivalent temperature in Celsius using the `print()` function. Finally, it converts the temperature back from Celsius to Fahrenheit using the same formula and stores the result in the variable `fahrenheit`. The code then prints the equivalent temperature in Fahrenheit using the `print()` function again.

You can use this approach to solve the problem for any temperature value you want, simply by changing the value assigned to the variable `fahrenheit`.