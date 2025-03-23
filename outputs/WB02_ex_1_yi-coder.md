Here's how you can implement this problem using Python functions:
```python
def convert_to_barns(area_in_sq_m):
    return area_in_sq_m * 1e28

def convert_from_barns(area_in_barns):
    return area_in_barns / 1e28

# Test cases:
print(convert_to_barns(1))  # should print 1e+28, which is the conversion of 1 m² to barns.
print(convert_from_barns(1e-28)) # should print 1, which is the conversion of 1 barn back to m².
```