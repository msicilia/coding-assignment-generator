Here is the Python code that meets the requirements of the problem:

```py
# Variables for the temperature values
temperature_fahrenheit = 98.6
temperature_celsius = (5.0/9.0) * (temperature_fahrenheit - 32)

# Display the temperatures
print("Temperature in Fahrenheit:", temperature_fahrenheit)
print("Temperature in Celsius:", temperature_celsius)

# Convert and display another set of temperatures
temperature_fahrenheit_2 = 32.0
temperature_celsius_2 = (5.0/9.0) * (temperature_fahrenheit_2 - 32)
print("Temperature in Fahrenheit:", temperature_fahrenheit_2)
print("Temperature in Celsius:", temperature_celsius_2)

temperature_fahrenheit_3 = 212.0
temperature_celsius_3 = (5.0/9.0) * (temperature_fahrenheit_3 - 32)
print("Temperature in Fahrenheit:", temperature_fahrenheit_3)
print("Temperature in Celsius:", temperature_celsius_3)
```

This code defines three different temperature values, converts each to the other unit using the given formula, and prints the results. It meets all the requirements specified in the task:

1. It does not use functions.
2. It uses variables instead of input() to read data from the keyboard.
3. It displays both temperatures (Fahrenheit and Celsius) for different values.

The test cases cover a range of common temperatures, ensuring that the conversion formula is accurate.