# Conversion from Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    c = (5.0/9.0)*(f - 32)
    return c

# Conversion from Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    f = (9.0/5.0)*c + 32
    return f

# Test data
test_temperatures = [100, -459.67, 212] # Replace this with your input temperatures

for temp in test_temperatures:
    print("Fahrenheit to Celsius:",fahrenheit_to_celsius(temp)))
    print("Celsius to Fahrenheit:",celsius_to_fahrenheit(temp)))")

# Replace 'test_temperatures' with your input temperatures.