```python
def barns_to_m2(barns):
    """Converts units in barns to m²."""
    return barns * 1e-28

def m2_to_barns(m2):
    """Converts units in m² to barns."""
    return m2 / 1e-28
```

**Example Usage:**

```python
# Convert 1 barn to m²
barns_to_m2(1)  # Output: 1e-28

# Convert 1 m² to barns
m2_to_barns(1)  # Output: 1e+28
```

**Explanation:**

* The `barns_to_m2()` function multiplies the input value `barns` by `1e-28` to convert it to m².
* The `m2_to_barns()` function divides the input value `m2` by `1e-28` to convert it to barns.

**Note:**

* The code uses the `e` notation to represent powers of 10.
* The functions are modular and efficient, following good coding practices.