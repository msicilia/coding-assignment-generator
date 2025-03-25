Here is an example solution to your problem:
```python
def convert_fahr_to_celsius(fahr):
    return (fahr - 32) * 5/9

def convert_celsius_to_fahr(celsius):
    return celsius * 9/5 + 32

# Test cases:
tc = 0 # temperature in Celsius
tf = 32 # temperature in Fahrenheit

print("Temperature in Fahr {} is equal to {} Celsius".format(tf, convert_fahr_to_celsius(tf)))
print("Temperature in Celsius {} is equal to {} Fahr".format(tc, convert_celsius_to_fahr(tc)))
```