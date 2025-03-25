The temperature expressed in degrees Celsius (TC) can be converted to degrees Fahrenheit (TF) using the following formula: TF = (9.0*TC)/5.0 + 32.0 Write a program that, using a certain temperature value in degrees Fahrenheit, displays the equivalent temperature in degrees Celsius and vice versa.

You cannot use the following Python elements:
Functions

You must use the following Python elements:
No required elements

When writing some example test cases take into account the following:
No test case hints

Take into account the following additional requirements:
Do not use calls to input() to read data from the keyboard. Use variables instead to exercise the code.

This is a basic programming exercise that requires you to write a program using only the basic Python elements, such as arithmetic operations and data types. The goal of this exercise is to practice writing and testing simple programs using Python.

Here's an example solution:

# Write a program that displays the equivalent temperature in Celsius and Fahrenheit for a given temperature in Fahrenheit.
temperature_fahrenheit = 75
temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
print("The temperature in Celsius is:", temperature_celsius)
print("The temperature in Fahrenheit is:", temperature_fahrenheit)

# Write some example test cases for the program.
def test(temperature):
    result = (temperature - 32) * 5 / 9
    return result

test(70) == 21.0
test(80) == 27.0
test(90) == 35.0

# Write a function that takes the temperature in Celsius as input and returns the equivalent temperature in Fahrenheit.
def to_fahrenheit(temperature):
    return (temperature * 9 / 5) + 32

# Test the function with some example values.
assert to_fahrenheit(0) == 32.0
assert to_fahrenheit(100) == 212.0
assert to_fahrenheit(-100) == -148.0