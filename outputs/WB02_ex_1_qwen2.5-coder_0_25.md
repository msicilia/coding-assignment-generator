```python
def meters_to_barns(meters_squared):
    return meters_squared * 1e28

def barns_to_meters(barns):
    return barns * 1e-28

# Example test cases
meters_value = 1e-26  # 1 barn in m^2
barns_value = 1

# Convert meters squared to barns
converted_barns = meters_to_barns(meters_value)
print(f"{meters_value} m^2 is equal to {converted_barns} barns")

# Convert barns back to meters squared
converted_meters = barns_to_meters(barns_value)
print(f"{barns_value} barns is equal to {converted_meters} m^2")
```

This code defines two functions, `meters_to_barns` and `barns_to_meters`, which convert between meters squared and barns, respectively. The example test cases demonstrate the usage of these functions, confirming that 1 barn is approximately \(1 \times 10^{-26}\) meters squared.