Here are the requested Python functions:

```python
def m2_to_barns(area_in_m2):
    """Converts surface area from square meters to barns."""
    # A Barn is equivalent to 1e-28 square meters, hence the conversion factor.
    conversion_factor = 1e28
    return area_in_m2 * conversion_factor

def barns_to_m2(area_in_barns):
    """Converts surface area from barns to square meters."""
    # A Barn is equivalent to 1e-28 square meters, hence the conversion factor.
    conversion_factor = 1e-28
    return area_in_barns * conversion_factor
```
These functions can be used in the following way:

```python
print(m2_to_barns(1))  # Outputs 1e+28
print(barns_to_m2(1))  # Outputs 1e-28
```
The first function, `m2_to_barns()`, converts an area from square meters to barns and the second one, `barns_to_m2()` does the opposite.