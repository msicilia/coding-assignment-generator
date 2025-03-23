Here is an example solution based on your problem description:

```python
def calculate_AER(ANN, m):
    """Calculate Annual Effective Rate (AER) given nominal rate (ANN) and number of compounding periods (m)"""
  
    if ANN > 1:
        # If the input annual nominal rate is greater than 1, consider it as a percentage.
        ANN = ANN / 100

    AER = (1 + ANN/m) ** m - 1

    return AER
  
def test_calculate_AER():
    """Test the function calculate_AER with some example test cases """
   
    assert abs(calculate_AER(5, 12) - 0.0513497693866658 ) < 1e-9, "Test case 1 failed"
    assert abs(calculate_AER(1,  4) - 0.0102653833317955 ) < 1e-9, "Test case 2 failed"
    assert abs(calculate_AER(2,  2) - 0.0203469175817366 ) < 1e-9, "Test case 3 failed"

test_calculate_AER()
```

In the solution above, `calculate_AER` is a function that takes two arguments: ANN (Annual Nominal Rate) and m (Number of compounding periods per year). The function first checks if ANN is larger than 1; if it is, the function considers ANN as a percentage and divides ANN by 100. Then it calculates AER using the formula provided in your problem description. The function finally returns the calculated value for AER.
The `test_calculate_AER` is used to check whether the implementation of the `calculate_AER` works properly with some example test cases. If any assertion in this function fails, an error message will be displayed indicating which test case has failed.