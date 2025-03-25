Understood! I will provide Python code that solves the problem of converting temperatures between Celsius and Fahrenheit without using functions. The code will include example test cases to demonstrate its functionality.

Here is the Python code:

```python
# Example test case 1: Convert 32°F to Celsius
temp_fahrenheit = 32.0
temp_celsius = (5.0 * temp_fahrenheit - 9.0 * 32) / 9.0
print(f"Temperature in Celsius: {temp_celsius}°C")

# Example test case 2: Convert 100°F to Celsius
temp_fahrenheit = 100.0
temp_celsius = (5.0 * temp_fahrenheit - 9.0 * 32) / 9.0
print(f"Temperature in Celsius: {temp_celsius}°C")

# Example test case 3: Convert -40°F to Celsius
temp_fahrenheit = -40.0
temp_celsius = (5.0 * temp_fahrenheit - 9.0 * 32) / 9.0
print(f"Temperature in Celsius: {temp_celsius}°C")

# Example test case 4: Convert 68°F to Celsius
temp_fahrenheit = 68.0
temp_celsius = (5.0 * temp_fahrenheit - 9.0 * 32) / 9.0
print(f"Temperature in Celsius: {temp_celsius}°C")

# Example test case 5: Convert 212°F to Celsius
temp_fahrenheit = 212.0
temp_celsius = (5.0 * temp_fahrenheit - 9.0 * 32) / 9.0
print(f"Temperature in Celsius: {temp_celsius}°C")

# Example test case 6: Convert 0°C to Fahrenheit
temp_celsius = 0.0
temp_fahrenheit = (9.0 * temp_celsius) / 5.0 + 32.0
print(f"Temperature in Fahrenheit: {temp_fahrenheit}°F")

# Example test case 7: Convert 100°C to Fahrenheit
temp_celsius = 100.0
temp_fahrenheit = (9.0 * temp_celsius) / 5.0 + 32.0
print(f"Temperature in Fahrenheit: {temp_fahrenheit}°F")

# Example test case 8: Convert -40°C to Fahrenheit
temp_celsius = -40.0
temp_fahrenheit = (9.0 * temp_celsius) / 5.0 + 32.0
print(f"Temperature in Fahrenheit: {temp_fahrenheit}°F")
```

### Explanation:
1. **Conversion from Fahrenheit to Celsius**:
   - The formula for converting Fahrenheit to Celsius is \( \text{TC} = \frac{5.0 \times \text{TF} - 9.0 \times 32}{9.0} \).
   - In each test case, we substitute the given Fahrenheit temperature into this formula and print the result.

2. **Conversion from Celsius to Fahrenheit**:
   - The formula for converting Celsius to Fahrenheit is \( \text{TF} = \frac{9.0 \times \text{TC}}{5.0} + 32.0 \).
   - In each test case, we substitute the given Celsius temperature into this formula and print the result.

These example test cases demonstrate both conversions and show how the code works without using functions.