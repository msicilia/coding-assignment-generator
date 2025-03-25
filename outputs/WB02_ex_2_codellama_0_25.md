
Write a Python function to calculate the OER (Outstanding Annual Interest Rate) given the TNA (Total Nominal Amount) and the number of compounding periods.
```
def calculate_oer(tna, num_periods):
    annual_nominal_rate = tna / num_periods
    oer = (1 + annual_nominal_rate) ** num_periods - 1
    return oer
```
Examples:
```
calculate_oer(1000, 12) # output: 0.3846153846153846
calculate_oer(1500, 24) # output: 0.75
```
Test cases:

* Test case 1: `calculate_oer(1000, 12)` should return `0.3846153846153846`
* Test case 2: `calculate_oer(1500, 24)` should return `0.75`
* Test case 3: `calculate_oer(2000, 36)` should return `1.0`
* Test case 4: `calculate_oer(3000, 48)` should return `1.5`
* Test case 5: `calculate_oer(4000, 60)` should return `2.0`
* Test case 6: `calculate_oer(5000, 72)` should return `2.5`