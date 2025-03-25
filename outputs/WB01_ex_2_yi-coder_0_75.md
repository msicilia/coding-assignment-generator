Here's how you can solve this problem:
```python
# Define variables
annual_income = 20000  # You may replace this with input() if needed.
number_of_sons = 3   # You may replace this with input() if needed.

# Calculate taxable income
taxable_income = annual_income - 600 - (number_of_sons * 60)

# Calculate tax payable
tax_payable = taxable_income / 3

print("Tax Payable: ", tax_payable)
```