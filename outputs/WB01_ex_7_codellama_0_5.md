Sure! Here is an example of how you could solve this problem using only basic Python elements:
```
# Get the user's input for the temperature in degrees Fahrenheit
fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))

# Calculate the equivalent temperature in Celsius
celsius = (9.0 * fahrenheit) / 5.0 + 32.0

print("The temperature in Celsius is:", celsius)

# Calculate the equivalent temperature in Fahrenheit
fahrenheit = (celsius - 32.0) * 5.0 / 9.0

print("The temperature in Fahrenheit is:", fahrenheit)
```
This code will ask the user to input a temperature value in degrees Fahrenheit, and then it will calculate the equivalent temperature in Celsius and vice versa using the formula provided. The output will be displayed using the `print()` function.