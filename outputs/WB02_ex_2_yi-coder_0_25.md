Here is how you can solve this problem using Python:
```python
def calculate_aer(ann, m):
    """
    This function calculates the Annual Effective Interest Rate (AER) from the Annual Nominal Rate (ANN) and the number of compounding periods.

    Parameters:
        ann (float): The annual nominal rate
        m (int): The number of compounding periods per year 

    Returns:
       The calculated AER as a float.
    """
    return (1 + ann/m) ** m - 1
```
This function can be used to calculate the effective annual interest rate for any given nominal annual interest rate and number of compounding periods per year.

Please note that this is a Python function, which needs to be called with appropriate parameters in order to execute:

Example test cases could look like this:
```python
# Testing the function 
annual_nominal_rate = 0.1  # or 10%
compounding_periods = 4   # quarterly compounding
aer = calculate_aer(annual_nominal_rate, compounding_periods)
print(f"The Annual Effective Rate for the given inputs is: {aer*100}%")  # The *100 here is to convert it into percentage form.
```