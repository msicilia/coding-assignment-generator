```python
# Define the annual income
annual_income = 100000

# Define the number of sons
num_sons = 2

# Calculate the personal deduction
personal_deduction = 600

# Calculate the deduction per son
son_deduction = num_sons * 60

# Calculate the taxable income
taxable_income = annual_income - personal_deduction - son_deduction

# Calculate the tax payable
tax_payable = float(taxable_income) / 3

# Print the tax payable
print("Tax payable:", tax_payable)
```