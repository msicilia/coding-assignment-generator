The provided Python code already meets all the requirements specified in the user task. Here's the code again for reference:

```python
def m2_to_barns(m2):
    return m2 / 10**-28

def barns_to_m2(barns):
    return barns * 10**-28

# Example test cases
print("1 m² is equal to", m2_to_barns(1), "Barns")
print("1 Barn is equal to", barns_to_m2(1), "m²")

# Additional test cases
print("1e-4 m² is equal to", m2_to_barns(1e-4), "Barns")
print("1e+30 Barns is equal to", barns_to_m2(1e+30), "m²")
```

### Explanation:
1. **Function Definitions**:
   - `m2_to_barns(m2)`: Converts square meters (m²) to Barns.
   - `barns_to_m2(barns)`: Converts Barns to square meters (m²).

2. **Example Test Cases**:
   - The code prints the conversions for 1 m², 1 Barn, 1e-4 m², and 1e+30 Barns.

### Additional Notes:
- The function definitions use basic data types (`float`).
- There are no loops or conditional statements.
- The functions are modular and reusable, following good programming practices.

This code correctly implements the conversion between square meters and Barns as specified in the problem statement.