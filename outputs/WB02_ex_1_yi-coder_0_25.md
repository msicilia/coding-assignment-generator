Here's how you can define those function: 

```python
def m2_to_barns(area_in_m2):
    '''Convert area from square meters to barns.'''
  
    # A Barn is equivalent to 1e-28 m²
    return area_in_m2 / 1e-28

def barns_to_m2(area_in_barns):
    '''Convert area from barns to square meters.'''
  
    # A Barn is equivalent to 1e-28 m²
    return area_in_barns * 1e-28
```
You can test these functions with the following code:

```python
print(m2_to_barns(1))       # Will print 10000000000000000.
print(barns_to_m2(10000000000000000))  # Will print 1.
```