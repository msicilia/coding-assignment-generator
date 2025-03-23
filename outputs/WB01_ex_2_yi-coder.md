```python
def calculate_tax(annual_income, num_sons):
    """Calculate tax payable by a taxpayer based on his annual income and number of sons. The tax payable is one third of the taxable income, the latter being equal to the total income minus a personal deduction of €600 and a further deduction of €60 per son. """
    taxable_income = annual_income - 600 - (60 * num_sons)
    tax_payable = taxable_income / 3.0  # use 3.0 instead of 3 to get a floating point result
    return tax_payable

# Test cases:
print("Tax for an income of €15000 and 2 sons:", calculate_tax(15000, 2)) # Expected output 4000.0
```